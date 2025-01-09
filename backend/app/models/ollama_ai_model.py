import logging
from ollama import chat, ChatResponse
import json

logger = logging.getLogger(__name__)

class OllamaAiModel:
    # Deprecated: We will use LiteLLM from now on

    """
    Model for integration with Ollama LLM using the `ollama` library.

    This class interacts with Ollama to generate interactive narrative fragments and choice options.
    """

    def __init__(self, model_name="gemma2", temperature=0.7, max_tokens=8192):
        """
        Initializes the Ollama model.

        Args:
            model_name (str, optional): Name of the model in Ollama. Default: "gemma2".
            temperature (float, optional): Randomness level in generation. Default: 0.7.
            max_tokens (int, optional): Maximum tokens generated. Default: 8192.
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate_fragment(self, prompt):
        """
        Generates a fragment and options based on the theme, story, and a user's choice.

        Args:
            prompt (str): LLM Prompt.

        Returns:
            tuple: Contains a text fragment (str) and a list of options (list).

        Raises:
            ValueError: If the model's response is invalid.
        """
        try:
            # Calls the Ollama model using the `ollama` library
            response: ChatResponse = chat(model=self.model_name, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            # Extracts and processes the model's response
            content = response.message.content
            logger.debug(f"Response content: {content}")

            # Assuming the response is a JSON with `title`, `fragment`, and `options`
            result = json.loads(content)
            title = result.get("title", "The model did not return a title.")
            fragment = result.get("fragment", "The model did not return a valid fragment.")
            options = result.get("options", [])

            return title, fragment, options
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from Ollama response: {response.message.content}", exc_info=e)
            raise ValueError("The model's response is not valid JSON.") from e
        except Exception as e:
            logger.error("Error generating the fragment", exc_info=e)
            raise RuntimeError("Unexpected error in generate_fragment.") from e
