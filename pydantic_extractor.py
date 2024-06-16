import nest_asyncio
from app_secrets import api_key, azure_enpoint, api_version
nest_asyncio.apply()
import os
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core import Settings
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from pydantic import BaseModel, Field
from typing import List
from llama_index.program.openai import OpenAIPydanticProgram
from llama_index.core.extractors import PydanticProgramExtractor
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core import load_index_from_storage, StorageContext, ServiceContext
from llama_index.core import GPTVectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever



llm = AzureOpenAI(
    model="gpt-35-turbo-16k",
    deployment_name="DanielChatGPT16k",
    api_key=api_key,
    azure_endpoint=azure_enpoint,
    api_version=api_version,
    max_tokens=5000
)
embed_model = AzureOpenAIEmbedding(
    model="text-embedding-ada-002",
    deployment_name="text-embedding-ada-002",
    api_key=api_key,
    azure_endpoint=azure_enpoint,
    api_version=api_version,
)


Settings.llm = llm
Settings.embed_model = embed_model



class NodeMetadata(BaseModel):  
    """  
    A data model to capture the unique keywords from various sections of a job description document.  
    """  
    job_summary_keywords: List[str] = Field(  
        ...,  
        description="List of unique keywords extracted from the JOB SUMMARY section."  
    )  
    principal_duties_and_responsibilities_keywords: List[str] = Field(  
        ...,  
        description="List of unique keywords extracted from the PRINCIPAL DUTIES AND RESPONSIBILITIES section."  
    )  
    qualifications_knowledge_skills_abilities: List[str] = Field(  
        ...,  
        description="List of unique keywords related to required knowledge, skills, and abilities from the MINIMUM QUALIFICATIONS section."  
    )  
    qualifications_education: List[str] = Field(  
        ...,  
        description="List of unique keywords related to required education from the MINIMUM QUALIFICATIONS section."  
    )  
    qualifications_experience: List[str] = Field(  
        ...,  
        description="List of unique keywords related to required experience from the MINIMUM QUALIFICATIONS section."  
    )  
    working_conditions_keywords: List[str] = Field(  
        ...,  
        description="List of unique keywords extracted from the WORKING CONDITIONS section."  
    )  



EXTRACT_TEMPLATE_STR = """\
Here is the content of the section:
----------------
{context_str}
----------------
Given the contextual information, extract out a {class_name} object.\
"""

openai_program = OpenAIPydanticProgram.from_defaults(
    output_cls=NodeMetadata,
    prompt_template_str="{input}",
    # extract_template_str=EXTRACT_TEMPLATE_STR
)

program_extractor = PydanticProgramExtractor(
    program=openai_program, input_key="input", show_progress=True
)



def update_metadata(nodes):
    keys_to_keep = ['job_summary_keywords', 'principal_duties_and_responsibilities_keywords','qualifications_knowledge_skills_abilities','qualifications_education','qualifications_experience','working_conditions_keywords']

    for node in nodes:
        metadata = node.metadata
        keys_to_remove = [key for key in metadata if key not in keys_to_keep]
        
        for key in keys_to_remove:
            del metadata[key]
        
        node.metadata = metadata


# Creating a vector store for the metadata

service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

persist_dir = './storage'

is_local_vector_store = os.path.exists(persist_dir) and os.listdir(persist_dir)

if is_local_vector_store:
    print("loading index from storage")
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    print(storage_context)
    index = load_index_from_storage(storage_context, service_context=service_context)
    # index = load_index_from_storage(storage_context)

else:
    docs = SimpleDirectoryReader("./JD_Data").load_data()
    pipeline = IngestionPipeline(transformations=[program_extractor])
    orig_nodes = pipeline.run(documents=docs)
    update_metadata(orig_nodes)
    for node in orig_nodes:
        print(node.metadata)
        print()

    # # Open the file in write mode
    # with open("metadata.txt", 'w', encoding='utf-8') as file:
    #     for item in orig_nodes:
    #         # Write each dictionary as a line in the text file
    #         file.write(str(item.metadata) + '\n\n\n')

    index = GPTVectorStoreIndex(orig_nodes, service_context=service_context, show_progress=True)
    index.storage_context.persist()


# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=1,
)


def retrieve_data(doc_title):
    response = retriever.retrieve(doc_title)
    job_summary = response[0].metadata['job_summary_keywords']
    responsibility = response[0].metadata['principal_duties_and_responsibilities_keywords']
    skills = response[0].metadata['qualifications_knowledge_skills_abilities']
    education = response[0].metadata['qualifications_education']
    experience = response[0].metadata['qualifications_experience']
    working_conditions = response[0].metadata['working_conditions_keywords']

    return job_summary, responsibility, skills, education, experience, working_conditions
