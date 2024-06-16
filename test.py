from llama_index.legacy import VectorStoreIndex
from llama_index.legacy import GPTVectorStoreIndex, SimpleDirectoryReader,  ServiceContext, StorageContext, load_index_from_storage
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings


from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core import PromptHelper
from llama_index.core.callbacks import CallbackManager, LlamaDebugHandler

# pip install llama-index-llms-azure-openai
from llama_index.llms.azure_openai import AzureOpenAI


# pip install llama-index-embeddings-azure-openai
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding



# from llama_index.llm_predictor import LLMPredictor
# from llama_index.tools import QueryEngineTool, ToolMetadata
# from llama_index.query_engine import SubQuestionQueryEngine
# from llama_index.indices.prompt_helper import PromptHelper
# from llama_index.callbacks import CallbackManager, LlamaDebugHandler
# from llama_index.llms.azure_openai import AzureOpenAI
# from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding

# ImportError: cannot import name 'ChatMessage' from 'llama_index.core.llms' (unknown location)



"""
# **_JOB DESCRIPTION_**  
   
|                                  |                                   |  
|----------------------------------|-----------------------------------|  
| **JOB TITLE:** {} | **DATE:** {} |  
| **DEPARTMENT:** {} | **FLSA CLASSIFICATION:** {}|  
| **REPORTS TO:** {} | **EEO CLASSIFICATION:** {} |  
   
## **JOB SUMMARY**  
   
JOB SUMMARY keywords to use: {}
   
## **ESSENTIAL DUTIES AND RESPONSIBILITIES**  
   
ESSENTIAL DUTIES AND RESPONSIBILITIES keywords to use: 
   
## **OTHER DUTIES AND RESPONSIBILITIES**  
   
OTHER DUTIES AND RESPONSIBILITIES keywords to use: {}
   
## **MINIMUM QUALIFICATIONS**  
### Knowledge/Skills/Abilities:  
Knowledge/Skills/Abilities keywords to use: {}
   
### Education:  
Education keywords to use: {}
   
### Experience:  
Experience keywords to use: {}
   
## **WORKING CONDITIONS**  
   
N/A = 0-10%, Occasionally = 11-33%, Frequently = 34 - 66%, Constantly = 67 - 100%  
   
| Requirement | Frequency |  
|-------------|-----------|  
| Travel |  |  
| Sitting |  |  
| Standing |  |  
| Walking |  |  
| Reading |  |  
| Typing |  |  
| Concentration |  |  
| Oral and Written Communication |  |  
| Horizontal Reaching |  |  
| Vertical Reaching |  |  
| Twisting |  |  
| Repetitive Arm/Hand/Finger Movements |  |  
| Weight |  |  

WORKING CONDITIONS keywords to use: {}

"""