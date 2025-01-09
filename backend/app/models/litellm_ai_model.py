import logging
import json
import traceback
from dotenv import load_dotenv
from litellm import completion
from .llm_interface import LLMInterface
import os

load_dotenv()
logger = logging.getLogger(__name__)

class LiteLLMModel(LLMInterface):
    """
    Model for integration with OpenAI ChatGPT using LiteLLM.

    This class uses LiteLLM to interact with the OpenAI API and
    generate interactive narrative fragments and choice options.
    """

    def __init__(self, model_name="openai/gpt-4o", temperature=0.7, max_tokens=2048):
        """
        Initializes the ChatGPT model with LiteLLM.

        Args:
            model_name (str, optional): Model name. Default: "openai/gpt-4o".
            temperature (float, optional): Randomness level in generation. Default: 0.7.
            max_tokens (int, optional): Maximum tokens generated. Default: 2048.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def clean_json_string(json_string):
        """
        Cleans a JSON string to remove unnecessary characters.

        Args:
            json_string (str): Raw JSON string.

        Returns:
            str: Clean JSON string.
        """
        return json_string.strip("```json").strip("```").strip()

    def generate_fragment(self, prompt):
        """
        Generates a fragment and options based on the theme, story, and a user's choice.

        Args:
            prompt (str): LLM Prompt.

        Returns:
            tuple: Contains a text fragment (str) and a list of options (list).

        Raises:
            ValueError: If the model's response is not valid JSON.
        """

        #logger.debug(f"prompt: {prompt}")
        try:
            messages = [{ "content": prompt, "role": "user" }]
            response = completion(model="openai/gpt-4o", messages=messages)
            plain_text = response["choices"][0]["message"]["content"]
            clean_content = self.clean_json_string(plain_text)
            logger.debug(f"clean_content: {clean_content}")
            result = json.loads(clean_content)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from LiteLLM response: {response}", exc_info=e)
            logger.error(traceback.format_exc())
            raise ValueError("The model's response is not valid JSON.") from e

        title = result.get("title", "The model did not return a title.")
        fragment = result.get("fragment", "The model did not return a valid fragment.")
        options = result.get("options", [])

        return title, fragment, options
