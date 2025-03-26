import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure OpenAI Configuration
AZURE_API_BASE = os.getenv("AZURE_API_BASE", "https://langmanus.openai.azure.com/")
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "your-azure-api-key")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")

# Reasoning LLM configuration (for complex reasoning tasks)
REASONING_MODEL = os.getenv("REASONING_MODEL", "deepseek-chat-v3-0324")
REASONING_BASE_URL = AZURE_API_BASE
REASONING_API_KEY = AZURE_API_KEY
REASONING_AZURE_DEPLOYMENT = os.getenv("REASONING_AZURE_DEPLOYMENT", "deepseek-chat-v3-0324")

# Non-reasoning LLM configuration (for straightforward tasks)
BASIC_MODEL = os.getenv("BASIC_MODEL", "gpt-4-turbo-preview")
BASIC_BASE_URL = AZURE_API_BASE
BASIC_API_KEY = AZURE_API_KEY
BASIC_AZURE_DEPLOYMENT = os.getenv("BASIC_AZURE_DEPLOYMENT", "gpt-4-turbo-preview")

# Vision-language LLM configuration (for tasks requiring visual understanding)
VL_MODEL = os.getenv("VL_MODEL", "gpt-4-vision-preview")
VL_BASE_URL = AZURE_API_BASE
VL_API_KEY = AZURE_API_KEY
VL_AZURE_DEPLOYMENT = os.getenv("VL_AZURE_DEPLOYMENT", "gpt-4-vision-preview")

# Chrome Instance configuration
CHROME_INSTANCE_PATH = os.getenv("CHROME_INSTANCE_PATH", "")
CHROME_HEADLESS = os.getenv("CHROME_HEADLESS", "true").lower() == "true"
CHROME_PROXY_SERVER = os.getenv("CHROME_PROXY_SERVER", "")
CHROME_PROXY_USERNAME = os.getenv("CHROME_PROXY_USERNAME", "")
CHROME_PROXY_PASSWORD = os.getenv("CHROME_PROXY_PASSWORD", "")
