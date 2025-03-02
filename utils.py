import logging
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from config import OPENAI_API_KEY

def load_data(directory_path):
    """Load documents from the specified directory"""
    try:
        documents = SimpleDirectoryReader(directory_path).load_data()
        print(f"Loaded {len(documents)} documents from {directory_path}")
        return documents
    except Exception as e:
        print(f"Error loading documents: {e}")
        return None

def create_index(documents):
    """Create an index from the documents"""
    # Initialize OpenAI settings with API key from config
    Settings.llm = OpenAI(
        api_key=OPENAI_API_KEY,
        temperature=0, 
        model="gpt-3.5-turbo"
    )
    Settings.embed_model = OpenAIEmbedding(
        api_key=OPENAI_API_KEY,
        model="text-embedding-ada-002"
    )
    
    # Create index
    return VectorStoreIndex.from_documents(documents)

def ask_question(index, question):
    """Query the index with a question"""
    query_engine = index.as_query_engine()
    return query_engine.query(question)