from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def create_embedding(text: str):
    """
    Generates embeddings for the given text.
    Useful if you want to build a vector database later.
    """
    try:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"⚠️ Error creating embedding: {str(e)}")
        return None
