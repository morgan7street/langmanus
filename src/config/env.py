import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Server Configuration
PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")

# OpenRouter Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your-openrouter-api-key")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_HTTP_REFERER = os.getenv("OPENROUTER_HTTP_REFERER", "https://github.com/langmanus/langmanus")
OPENROUTER_X_TITLE = os.getenv("OPENROUTER_X_TITLE", "LangManus")

# Azure OpenAI Configuration
AZURE_API_BASE = os.getenv("AZURE_API_BASE", "")
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")

# Azure OpenAI Deployments
BASIC_AZURE_DEPLOYMENT = os.getenv("BASIC_AZURE_DEPLOYMENT", "")
VL_AZURE_DEPLOYMENT = os.getenv("VL_AZURE_DEPLOYMENT", "")
REASONING_AZURE_DEPLOYMENT = os.getenv("REASONING_AZURE_DEPLOYMENT", "")

# Model Configuration
REASONING_MODEL = os.getenv("REASONING_MODEL", "deepseek-chat")
REASONING_BASE_URL = os.getenv("REASONING_BASE_URL", "https://api.deepseek.com/v1")
REASONING_API_KEY = os.getenv("REASONING_API_KEY", "")

BASIC_MODEL = os.getenv("BASIC_MODEL", "gemini-pro")
BASIC_API_KEY = os.getenv("BASIC_API_KEY", "")

VL_MODEL = os.getenv("VL_MODEL", "gemini-pro-vision")
VL_API_KEY = os.getenv("VL_API_KEY", "")

# Vision-language LLM configuration (for tasks requiring visual understanding)
VL_BASE_URL = OPENROUTER_BASE_URL
VL_HEADERS = {
    "HTTP-Referer": OPENROUTER_HTTP_REFERER,
    "X-Title": OPENROUTER_X_TITLE
}

# Chrome Instance configuration
CHROME_INSTANCE_PATH = os.getenv("CHROME_INSTANCE_PATH", "")
CHROME_HEADLESS = os.getenv("CHROME_HEADLESS", "true").lower() == "true"
CHROME_PROXY_SERVER = os.getenv("CHROME_PROXY_SERVER", "")
CHROME_PROXY_USERNAME = os.getenv("CHROME_PROXY_USERNAME", "")
CHROME_PROXY_PASSWORD = os.getenv("CHROME_PROXY_PASSWORD", "")
