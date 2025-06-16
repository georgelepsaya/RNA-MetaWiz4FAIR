# RNA-MetaWiz4FAIR

## Start the project

### Using `uv`

1. Install uv if it isn't installed already, e.g. curl -LsSf https://astral.sh/uv/install.sh | sh
2. Install dependencies:
    - All dependencies: `uv sync`
    - Excluding dev dependencies: `uv sync --no-dev`
3. Run the app: `streamlit run app.py`

### Using `requirements.txt`

1. Create a virtual environment: `python3 -m venv .venv`
2. Activate the virtual environment: `. .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`
