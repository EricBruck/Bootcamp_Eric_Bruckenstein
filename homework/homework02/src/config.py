import os
from pathlib import Path
from dotenv import load_dotenv

# Set project root relative to src/ directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

def load_env():
    """Load environment variables from .env file."""
    return load_dotenv(PROJECT_ROOT / ".env")

def get_key(name, default=None):
    """Retrieve an environment variable value by key."""
    load_env()
    return os.getenv(name, default)

if __name__ == "__main__":
    load_env()
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:", DATA_DIR)
    print("API_KEY present:", get_key("API_KEY") is not None)
    print("DATA_DIR from env:", get_key("DATA_DIR", str(DATA_DIR)))
