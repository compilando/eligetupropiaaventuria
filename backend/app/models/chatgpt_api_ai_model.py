from openai import OpenAI

import os
import json
import logging
import traceback
from dotenv import load_dotenv
from .llm_interface import LLMInterface

logger = logging.getLogger(__name__)
load_dotenv()

class ChatGPTApiModel(LLMInterface):
    # Deprecated: We will use LiteLLM from now on

    """
    Model for direct integration with OpenAI ChatGPT.
    """

    def __init__(self, model_name="gpt-3.5-turbo", temperature=0.7, max_tokens=2048):
        """
        Initializes the ChatGPT model using the official OpenAI API.

        Args:
            model_name (str): Model name, such as "gpt-4".
            temperature (float): Randomness level in generation.
            max_tokens (int): Maximum tokens generated.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        OpenAI.api_key = self.api_key  # Set the API key globally
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

        self.client = OpenAI(
            api_key=self.api_key  # This is the default and can be omitted
        )

    @staticmethod
    def clean_json_string(json_string):
        """
        Cleans a JSON string by removing unnecessary characters.

        Args:
            json_string (str): Raw JSON string.

        Returns:
            str: Cleaned JSON string.
        """
        return json_string.strip("```json").strip("```").strip()

    def generate_fragment(self, prompt):
        """
        Generates a fragment and options based on the theme, story, and user's choice.

        Args:
            prompt (str): LLM Prompt.

        Returns:
            tuple: Contains a text fragment (str) and a list of options (list).
        """

        logger.debug(f"prompt: {prompt}")
        try:            
            # Sends the request to the OpenAI API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            # Extracts the model's response
            clean_content = self.clean_json_string(response.choices[0].message.content)
            result = json.loads(clean_content)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from ChatGPT response: {clean_content}", exc_info=e)
            logger.error(traceback.format_exc())
            raise ValueError("The model's response is not valid JSON.") from e

        title = result.get("title", "The model did not return a title.")
        fragment = result.get("fragment", "The model did not return a valid fragment.")
        options = result.get("options", [])

        return title, fragment, options
