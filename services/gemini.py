import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()


# Get Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not configured. "
        "Please add it to your .env file."
    )


# Create Gemini client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


# Gemini model
MODEL_NAME = "gemini-3.5-flash"

def generate_response(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the response text.

    Raises:
        RuntimeError: If the Gemini API request fails.
    """

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as error:

        raise RuntimeError(
            "Gemini API request failed. "
            "Please check your API key, network connection, "
            "or API usage limits."
        ) from error