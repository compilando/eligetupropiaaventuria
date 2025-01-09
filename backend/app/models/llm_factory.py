import logging

from .litellm_ai_model import LiteLLMModel
from .chatgpt_ai_model import ChatGPTModel
from .chatgpt_api_ai_model import ChatGPTApiModel
from .ollama_ai_model import OllamaAiModel
from .vertex_ai_model import VertexAIModel
from .claude_local_model import ClaudeLocalModel

logger = logging.getLogger(__name__)

class LLMFactory:
    # DEPRECATED
    # This factory made sense before incorporating LiteLLM; I'll keep it for future experiments.

    MODEL_TYPE_LITELLM = "litellm"
    MODEL_TYPE_OLLAMA = "ollama"
    MODEL_TYPE_VERTEX_AI = "vertexai"
    MODEL_TYPE_CHATGPT = "chatgpt"
    MODEL_TYPE_CHATGPT_API = "chatgpt_api"
    MODEL_TYPE_CLAUDE_LOCAL = "claude_local"

    @staticmethod
    def create_llm(model_type, **kwargs):
        logger.debug(f"Creating LLM of type: {model_type} with kwargs: {kwargs}")
        if model_type == LLMFactory.MODEL_TYPE_OLLAMA:
            kwargs.pop("project", None)
            kwargs.pop("location", None)
            return OllamaAiModel(**kwargs)
        if model_type == LLMFactory.MODEL_TYPE_LITELLM:
            kwargs.pop("project", None)
            kwargs.pop("location", None)
            return LiteLLMModel(**kwargs)
        if model_type == LLMFactory.MODEL_TYPE_VERTEX_AI:
            return VertexAIModel(**kwargs)
        elif model_type == LLMFactory.MODEL_TYPE_CHATGPT:
            kwargs.pop("project", None)
            kwargs.pop("location", None)
            return ChatGPTModel(**kwargs)
        elif model_type == LLMFactory.MODEL_TYPE_CHATGPT_API:
            kwargs.pop("project", None)
            kwargs.pop("location", None)
            return ChatGPTApiModel(**kwargs)
        elif model_type == LLMFactory.MODEL_TYPE_CLAUDE_LOCAL:
            kwargs.pop("project", None)
            kwargs.pop("location", None)
            return ClaudeLocalModel(**kwargs)
        else:
            logger.error(f"Unknown model type requested: {model_type}")  # Log the error
            raise ValueError(f"Unknown model type: {model_type}")
