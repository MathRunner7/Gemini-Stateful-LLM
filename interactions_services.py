from google.genai import Client, types
from dotenv import load_dotenv
import os
# Ignore UserWarning warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load environment variables from .env file
load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")

# Initialize the Gemini API client
gemini_client = Client()

def create_interaction(message: str, previous_interaction_id: str = None) -> dict:
    """
    Create an interaction with the Gemini API.

    Args:
        message (str): The message to send to the Gemini API.
        previous_interaction_id (str, optional): The ID of the previous interaction for context. Defaults to None.
    Returns:
        dict: The response from the Gemini API.
    """
    try:
        # Create an interaction
        if previous_interaction_id is not None:
            print(f"Creating interaction with previous interaction ID: {previous_interaction_id}")
            response = gemini_client.interactions.create(
                model=GEMINI_MODEL,
                input=message,
                previous_interaction_id=previous_interaction_id
            )
        else:
            print("Creating interaction without previous interaction ID")
            response = gemini_client.interactions.create(
                model=GEMINI_MODEL,
                input=message
            )
        return response
    except Exception as e:
        print(f"An error occurred while creating interaction: {e}")
        return None