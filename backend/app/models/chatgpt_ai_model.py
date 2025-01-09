import logging
import json
import traceback
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from .llm_interface import LLMInterface
import os

load_dotenv()
logger = logging.getLogger(__name__)

class ChatGPTModel(LLMInterface):
    # Deprecated: We will use LiteLLm from now on

    """
    Model for integration with OpenAI ChatGPT via LangChain Core.

    This class uses LangChain Core to interact with the OpenAI API and
    generate interactive narrative fragments and choice options.
    """

    def __init__(self, model_name="gpt-3.5-turbo", temperature=0.7, max_tokens=2048):
        """
        Initializes the ChatGPT model.

        Args:
            api_key (str): OpenAI API key.
            model_name (str, optional): Model name. Default: "gpt-3.5-turbo".
            temperature (float, optional): Randomness level in generation. Default: 0.7.
            max_tokens (int, optional): Maximum tokens generated. Default: 8192.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(
            api_key=api_key,
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
        )

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
        
        logger.debug(f"prompt: {prompt}")
        message = HumanMessage(content=prompt)
        try:
            response = self.llm([message])
            clean_content = response[0].content.strip()
            clean_content = self.clean_json_string(clean_content)
            result = json.loads(clean_content)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from ChatGPT response: {clean_content}", exc_info=e)
            logger.error(traceback.format_exc())
            raise ValueError("The model's response is not valid JSON.") from e

        title = result.get("title", "The model did not return a title.")
        fragment = result.get("fragment", "The model did not return a valid fragment.")
        options = result.get("options", [])

        return title, fragment, options
