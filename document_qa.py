import os
import sys
import logging
from config import OPENAI_API_KEY
from utils import load_data, create_index, ask_question

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def main():
    # Set OpenAI API key from config
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    
    # Specify the directory containing your documents
    directory_path = "documents/"
    
    # Load documents
    documents = load_data(directory_path)
    if not documents:
        return
    
    # Create index
    index = create_index(documents)
    
    # Interactive Q&A loop
    print("\nWelcome to Document Q&A!")
    print("Type 'quit' to exit")
    
    while True:
        question = input("\nEnter your question: ")

        response = ask_question(index, question)
        print("\nAnswer:", response.response)

if __name__ == "__main__":
    main() 