import logging
from app import create_app

# Configure logging
logging.basicConfig(level=logging.INFO,  # Set to desired level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

app = create_app()

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

if __name__ == "__main__":
    app.run(debug=True)
