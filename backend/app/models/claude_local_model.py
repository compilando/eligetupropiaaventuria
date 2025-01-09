import logging
import json
import os
from transformers import pipeline
from .llm_interface import LLMInterface

logger = logging.getLogger(__name__)

class ClaudeLocalModel(LLMInterface):
    # Deprecated: We will use LiteLLM from now on

    """
    Local model for fragment generation using a pre-trained large language model.
    Utilizes Hugging Face Transformers to run the model locally.
    """

    def __init__(self, model_name="EleutherAI/gpt-neo-1.3B", temperature=0.7, max_tokens=8192):
        """
        Initializes the local model using Hugging Face Transformers.

        Args:
            model_name (str): Name of the Hugging Face model. Default: "EleutherAI/gpt-neo-1.3B".
        """
        logger.info(f"Loading local LLM model: {model_name}")
        #self.generator = pipeline("text-generation", model=model_name, device=0)torch.backends.cuda.matmul.allow_tf32 = True  # Accelerate mixed precision operations
        generator = pipeline("text-generation", model="EleutherAI/gpt-j-6B", device=0)

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
        Generates a fragment and options based on the theme, story, and user's choice.

        Args:
            prompt (str): LLM Prompt.

        Returns:
            tuple: Contains a text fragment (str) and a list of options (list).

        Raises:
            ValueError: If the model's response is not valid JSON.
        """
        logger.debug(f"prompt: {prompt}")

        # Prepare the content of the prompt
        # Generate text with the local model
        #logger.debug(f"Generated prompt for local LLM: {prompt}")
        response = self.generator(prompt, max_length=1024, num_return_sequences=1, temperature=0.7)
        logger.debug(f"Raw response: {response}")

        if not isinstance(response, list) or "generated_text" not in response[0]:
            import traceback; traceback.print_exc();
            logger.error(f"Unexpected response format: {response}")
            raise ValueError("The model did not return a valid response.")
        
        generated_text = response[0]
        logger.debug(f"Raw response from local LLM: {generated_text}")

        # Clean and load the JSON
        try:
            clean_content = self.clean_json_string(generated_text)
            result = json.loads(clean_content)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from local LLM response: {generated_text}", exc_info=e)
            raise ValueError("The model's response is not valid JSON.") from e

        # Extract fragment and options
        title = result.get("title", "The model did not return a title.")
        fragment = result.get("fragment", "The model did not return a valid fragment.")
        options = result.get("options", [])
        
        #logger.info(f"Generated fragment: {fragment}, options: {options} (ClaudeLocal)")
        return title, fragment, options
