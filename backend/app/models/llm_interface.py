import logging  # Import logging module

logger = logging.getLogger(__name__)

class LLMInterface:
    def generate_fragment(self, prompt):
        logger.warning("LLMInterface.generate_fragment() called. This should be overridden.") # A warning is appropriate here.
        raise NotImplementedError("This method should be overridden by subclasses")
