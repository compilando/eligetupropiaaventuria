# Model-Specific Instructions

Below are instructions for using each type of LLM. **LiteLLM** is the recommended option, and all others are deprecated.

---

## **1. LiteLLM (Recommended)**

LiteLLM provides a streamlined way to interact with LLMs using modern APIs and improved performance. Learn more and set up LiteLLM through these links:  
- [LiteLLM GitHub Repository](https://github.com/litellm)  
- [LiteLLM Documentation](https://docs.litellm.com)

### **Setup Instructions:**
1. Set the `LLM` environment variable in your `.env` file to `litellm`.
2. Obtain an API key from your LLM provider (e.g., OpenAI) and set the `OPENAI_API_KEY` environment variable.
3. Configure additional LiteLLM-specific settings as described in the [LiteLLM Documentation](https://docs.litellm.com).

---

## **Deprecated Options**

### **2. Ollama (Local)**

> *Note: Deprecated in favor of LiteLLM.*

#### **Linux/macOS:**
- Install Ollama by following the instructions on the [Ollama website](https://ollama.ai).
- Set the `LLM` environment variable in your `.env` file to `ollama`.
- Set the `MODEL_NAME` environment variable to the name of the Ollama model (e.g., `gemma2`).

#### **Windows:**
- Ollama's native installation is not officially supported on Windows. Check the Ollama documentation for workarounds using WSL or similar methods.

---

### **3. ChatGPT (API)**

> *Note: Deprecated in favor of LiteLLM.*

- Set the `LLM` environment variable in your `.env` file to `chatgpt`.
- Obtain an API key from OpenAI and set the `OPENAI_API_KEY` environment variable.

---

### **4. Vertex AI (API)**

> *Note: Deprecated in favor of LiteLLM.*

- Set the `LLM` environment variable in your `.env` file to `vertexai`.
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your Google Cloud credentials JSON file.
- Set the `GCP_PROJECT` and `GCP_LOCATION` environment variables to your Google Cloud project ID and region.

---

### **5. Claude (Local - Hugging Face)**

> *Note: Deprecated in favor of LiteLLM.*

#### **Linux/macOS/Windows:**
- Install the necessary Hugging Face Transformers library and any Claude-specific dependencies. See the Hugging Face documentation for installation instructions.
- Set the `LLM` environment variable in your `.env` file to `claude`.
- Set the `MODEL_NAME` environment variable to the specific Claude model name.
- Ensure you have the necessary resources (e.g., sufficient RAM and VRAM) for running the model locally.
