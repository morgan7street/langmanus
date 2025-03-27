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

# Reasoning LLM configuration (for complex reasoning tasks)
REASONING_MODEL = os.getenv("REASONING_MODEL", "openrouter/deepseek/deepseek-chat-v3-0324:free")
REASONING_BASE_URL = OPENROUTER_BASE_URL
REASONING_API_KEY = OPENROUTER_API_KEY
REASONING_AZURE_DEPLOYMENT = os.getenv("REASONING_AZURE_DEPLOYMENT", "deepseek-chat-v3-0324")
REASONING_HEADERS = {
    "HTTP-Referer": OPENROUTER_HTTP_REFERER,
    "X-Title": OPENROUTER_X_TITLE
}

# Non-reasoning LLM configuration (for straightforward tasks)
BASIC_MODEL = os.getenv("BASIC_MODEL", "openrouter/google/gemini-2.5-pro-exp-03-25:free")
BASIC_BASE_URL = OPENROUTER_BASE_URL
BASIC_API_KEY = OPENROUTER_API_KEY
BASIC_AZURE_DEPLOYMENT = os.getenv("BASIC_AZURE_DEPLOYMENT", "gemini-2.5-pro-exp-03-25")
BASIC_HEADERS = {
    "HTTP-Referer": OPENROUTER_HTTP_REFERER,
    "X-Title": OPENROUTER_X_TITLE
}

# Azure OpenAI配置（按LLM类型区分）
AZURE_API_BASE = os.getenv("AZURE_API_BASE", "https://langmanus.openai.azure.com/")
AZURE_API_KEY = os.getenv("AZURE_API_KEY", "your-azure-api-key")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")

# Vision-language LLM configuration (for tasks requiring visual understanding)
VL_MODEL = os.getenv("VL_MODEL", "openrouter/google/gemini-2.5-pro-exp-03-25:free")
VL_BASE_URL = OPENROUTER_BASE_URL
VL_API_KEY = OPENROUTER_API_KEY
VL_AZURE_DEPLOYMENT = os.getenv("VL_AZURE_DEPLOYMENT", "gemini-2.5-pro-exp-03-25")
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
