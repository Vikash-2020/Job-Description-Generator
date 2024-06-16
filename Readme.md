# Job Description Generator App Documentation  
   
## Table of Contents:  
1. Overview  
2. Getting Started  
   - Prerequisites  
   - Installation  
   - Configuration  
3. Resources Info  
   - Files and Modules  
   - Dependencies  
4. Working & Usage (App)  
   - Workflow Overview  
   - Extracting Metadata  
   - Generating Job Descriptions  
5. UI (User Interface)  
   - Interface Components  
   - User Interaction Flow  
6. Code (App)  
   - Core Components  
   
---  
   
## 1. Overview  
The Job Description Generator App is an advanced tool designed to automate the creation of job descriptions. It utilizes natural language processing and machine learning to extract relevant keywords from job description documents and generate comprehensive job descriptions that include essential duties, qualifications, and working conditions.  
   
## 2. Getting Started  
   
### Prerequisites  
- Python 3.7 or higher  
- Pydantic  
- Azure account with access to Azure OpenAI services  
   
### Installation  
1. Clone the repository or download the source code.  
2. Install the required Python packages using `pip install -r requirements.txt`.  
   
### Configuration  
- Set up `app_secrets.py` with your Azure API key, endpoint, and API version.  
- Configure `pydantic_extractor.py` with the appropriate model names and deployment names for the Azure OpenAI services.  
   
## 3. Resources Info  
   
### Files and Modules  
- `pydantic_extractor.py`: Contains logic for initializing the OpenAI models, extracting metadata from documents, and creating a vector store for metadata.  
- `tot_prompt.py`: Defines the system and user prompts for generating job descriptions.  
- `jd_generator.py`: Combines the extracted metadata with the system and user prompts to generate the final job description.  
   
### Dependencies  
- `nest_asyncio`: Ensures compatibility of asyncio with Jupyter Notebooks or other environments that run event loops.  
- `llama_index`: A set of modules for working with language models, including embeddings, retrievers, and storage.  
- `pydantic`: A data validation library that uses Python type annotations.  
   
## 4. Working & Usage (App)  
   
The Job Description Generator App is a sophisticated application designed to automate the process of creating detailed job descriptions. The app interfaces with Azure's OpenAI services to leverage the power of GPT models for natural language understanding and generation. The following section elaborates on the key functions and their roles within the app.  
   
### Workflow Overview  
   
The core workflow of the application involves several steps that are executed in sequence to produce the final job description:  
   
1. **Initialization of Language Models**: The app starts by setting up the language models provided by Azure OpenAI services. These models are used for both extracting relevant information from existing job descriptions and generating new ones.  
   
2. **Document Reading and Metadata Extraction**: Using the `SimpleDirectoryReader`, the app reads job description documents from a specified directory. It then utilizes a `PydanticProgramExtractor` to extract metadata from these documents based on predefined schema.  
   
3. **Metadata Vector Store Creation**: The extracted metadata is stored in a vector store, which allows for efficient retrieval based on similarity queries. This is crucial for the app's ability to find and use relevant information quickly.  
   
4. **Job Description Generation**: With the metadata ready, the app combines it with user input to craft a structured job description. The user provides specific details and guidelines, which are integrated into the template to generate the final document.  
   
### Extracting Metadata  
   
#### NodeMetadata Class  
The `NodeMetadata` class is a Pydantic model that defines the structure of metadata to be extracted from job description documents. It includes fields for keywords related to job summary, principal duties, qualifications, education, experience, and working conditions.  
   
#### PydanticProgramExtractor  
`PydanticProgramExtractor` is responsible for processing documents and extracting structured metadata using the `NodeMetadata` schema. It does so by running an OpenAI program defined by the `OpenAIPydanticProgram` class, which uses a template to guide the extraction.  
   
#### update_metadata Function  
This function cleans up the extracted metadata by removing any unnecessary keys and ensuring that only the relevant ones are kept, as specified by the `keys_to_keep` list.  
   
### Generating Job Descriptions  
   
#### get_contract_prompt Function  
The `get_contract_prompt` function in both `tot_prompt.py` and `jd_generator.py` is a critical component that constructs the final job description. It uses the system and user prompts to structure the document according to the provided format and guidelines. The function takes several parameters, including job title, department, and various keyword lists extracted from the metadata, to generate a comprehensive job description.  
   
#### retrieve_data Function  
This function is part of the retrieval process. It uses the `VectorIndexRetriever` to find the most relevant metadata from the vector store based on a query (in this case, the document title). It then extracts and returns the specific parts of the metadata needed for the job description.  
   
### Integration of Components  
   
The various components of the app work together to create a seamless process for generating job descriptions. The `IngestionPipeline` runs the extraction program across all documents, the `update_metadata` function ensures the metadata is clean, and the `GPTVectorStoreIndex` creates an efficient index for retrieval. Finally, the `retrieve_data` function and the `get_contract_prompt` function are used in tandem to produce the final job description document that meets the specific needs of the user.
## 5. UI (User Interface)  
   
### Interface Components  
The app's interface allows users to input the job title, department, and other details, as well as select the desired format and guidelines for the job description.  
   
### User Interaction Flow  
Users interact with the app by providing necessary details and selecting options for the job description. The app processes the input and returns a well-structured job description document.  
   
## 6. Code (App)  
   
### Core Components  
The core components include the language model initialization, metadata extraction, vector store index creation, and the retrieval and generation of job descriptions.  