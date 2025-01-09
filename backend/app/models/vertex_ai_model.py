import logging
import json
import traceback
from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI
from .llm_interface import LLMInterface
import os

logger = logging.getLogger(__name__)

class VertexAIModel(LLMInterface):
    # Deprecated: We will use LiteLLM from now on

    """
    Model for integration with Vertex AI via LangChain.

    This class uses the Vertex AI language model to generate interactive narrative fragments and choice options.
    """

    def __init__(self, model_name, project, location, temperature=0.7, max_tokens=8192):
        """
        Initializes the Vertex AI model.

        Args:
            model_name (str): Name of the model in Vertex AI.
            project (str): Google Cloud project ID.
            location (str): Location of the model in Vertex AI.
            temperature (float, optional): Randomness level in generation. Default: 0.7.
            max_tokens (int, optional): Maximum tokens generated. Default: 8192.
        """
        self.llm = ChatVertexAI(
            model_name=model_name,
            max_output_tokens=max_tokens,
            project=project,
            location=location,
            temperature=temperature,
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
        response = self.llm([message])

        try:
            clean_content = response.content.strip()
            clean_content = self.clean_json_string(clean_content)
            result = json.loads(clean_content)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from Vertex AI response: {clean_content}", exc_info=e)
            logger.error(traceback.format_exc())
            raise ValueError("The model's response is not valid JSON.") from e

        title = result.get("title", "The model did not return a title.")
        fragment = result.get("fragment", "The model did not return a valid fragment.")
        options = result.get("options", [])
        
        return title, fragment, options
