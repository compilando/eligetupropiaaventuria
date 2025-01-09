# EligeTuPropiaAventurIA Backend

This project provides a backend service using Flask and potentially integrates with Google Cloud Platform (GCP) and others LLM based on the provided `.env` file.

## Setup

### 1. Create a Virtual Environment

It's highly recommended to use a virtual environment to isolate project dependencies.  Here's how to create one using `venv`:

```bash
python3 -m venv .venv  # Create the virtual environment
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
.venv\Scripts\activate  # Activate the virtual environment (Windows)

2. Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

3. Set Environment Variables
Copy the .env.example file (you should create this file, see example below) to .env and fill in the required values

```bash
FLASK_ENV=development
LLM=litellm
MODEL_NAME=openai/gpt-4o
OPENAI_API_KEY=your-openai-api-key # if using OpenAI
```

4. Models
This application supports various Large Language Models (LLMs). For detailed information on each model and specific instructions, see [MODELS.md](MODELS.md).

## General Instructions for Using LLMs
This application uses a `.env` file to store sensitive information such as API keys and other credentials. Make sure you have a `.env` file in the backend directory and populate it according to the examples below.

**Using the .env file:**
The application relies on environment variables stored within the `.env` file.  Here's a breakdown of the common variables and how to set them:

```bash
FLASK_ENV=development
LLM=[litellm|ollama|chatgpt|vertexai|claude]
MODEL_NAME= # Specific model name (e.g., gemma2, gpt-3.5-turbo, etc.)
OPENAI_API_KEY=sk-... # For ChatGPT and other OpenAI models

GOOGLE_APPLICATION_CREDENTIALS=./gcp_credentials.json # Only for Vertex AI
GCP_PROJECT=your-gcp-project # For Vertex
GCP_LOCATION=your-gcp-location # For Vertex AI
```

Remember to consult [MODELS.md](MODELS.md) for specific setup instructions and troubleshooting tips for each LLM.

4. Run the Application
You can run the Flask development server for testing:

flask run
Or using gunicorn for production with a WSGI entry point (assuming your main application file is app.py and the WSGI variable is app):

gunicorn --bind 0.0.0.0:8080 app:app
(Ensure gunicorn is added to your requirements.txt file)


## License
This project is licensed under the CC0-1.0 Universal (CC0 1.0) Public Domain Dedication. Feel free to use, modify, and distribute this project as you see fit!

