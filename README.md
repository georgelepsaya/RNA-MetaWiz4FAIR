# RNA-MetaWiz4FAIR

> [!NOTE]  
> This project is in the prototyping stage.
> Application is not ready for practical use.

## Notes for Development

### Run container

1. Create an `.env` file with the following contents:

    ```
    LANGSMITH_TRACING=true
    LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
    LANGSMITH_API_KEY=<your_key>
    LANGSMITH_PROJECT=<your_project>
    OPENAI_API_KEY=<your_openai_api_key>
    NCBI_API_KEY=<your_ncbi_api_key>
    ```

2. You can run the container directly: `docker run -p 8501:8501 --env-file .env georgelepsaya/msw4fair:latest`
3. Or you can pull the image to your local machine. First, make sure Docker is installed on your machine
4. Pull this image: `docker pull georgelepsaya/msw4fair`
5. Run the container: `docker run -p 8501:8501 --env-file .env msw4fair`
6. Finally, access the application at `http://localhost:8501`

### Start the Python project

#### Using `uv`

1. Install uv if it isn't installed already, e.g. `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Install dependencies:
    - All dependencies: `uv sync`
    - Excluding dev dependencies: `uv sync --no-dev`
3. Run the app: `streamlit run app.py`

#### Using `requirements.txt`

1. Create a virtual environment: `python3 -m venv .venv`
2. Activate the virtual environment: `. .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`
