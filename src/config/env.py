import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Reasoning LLM configuration (for complex reasoning tasks)
REASONING_MODEL = os.getenv("REASONING_MODEL", "openrouter/deepseek/deepseek-chat-v3-0324:free")
REASONING_BASE_URL = OPENROUTER_BASE_URL
REASONING_API_KEY = OPENROUTER_API_KEY

# Non-reasoning LLM configuration (for straightforward tasks)
BASIC_MODEL = os.getenv("BASIC_MODEL", "openrouter/google/gemini-2.5-pro-exp-03-25:free")
BASIC_BASE_URL = OPENROUTER_BASE_URL
BASIC_API_KEY = OPENROUTER_API_KEY

# Azure OpenAI配置（按LLM类型区分）
AZURE_API_BASE = os.getenv("AZURE_API_BASE")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
# 各类型专用部署名称
BASIC_AZURE_DEPLOYMENT = os.getenv("BASIC_AZURE_DEPLOYMENT")
VL_AZURE_DEPLOYMENT = os.getenv("VL_AZURE_DEPLOYMENT")
REASONING_AZURE_DEPLOYMENT = os.getenv("REASONING_AZURE_DEPLOYMENT")

# Vision-language LLM configuration (for tasks requiring visual understanding)
VL_MODEL = os.getenv("VL_MODEL", "openrouter/google/gemini-2.5-pro-exp-03-25:free")
VL_BASE_URL = OPENROUTER_BASE_URL
VL_API_KEY = OPENROUTER_API_KEY

# Chrome Instance configuration
CHROME_INSTANCE_PATH = os.getenv("CHROME_INSTANCE_PATH")
CHROME_HEADLESS = os.getenv("CHROME_HEADLESS", "False") == "True"
CHROME_PROXY_SERVER = os.getenv("CHROME_PROXY_SERVER")
CHROME_PROXY_USERNAME = os.getenv("CHROME_PROXY_USERNAME")
CHROME_PROXY_PASSWORD = os.getenv("CHROME_PROXY_PASSWORD")
