from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import load_yaml_config
from typing import Optional, Dict, Any
from pathlib import Path

from src.config import (
    REASONING_MODEL,
    REASONING_BASE_URL,
    REASONING_API_KEY,
    BASIC_MODEL,
    BASIC_API_KEY,
    VL_MODEL,
    VL_API_KEY,
    AZURE_API_BASE,
    AZURE_API_KEY,
    AZURE_API_VERSION,
    BASIC_AZURE_DEPLOYMENT,
    VL_AZURE_DEPLOYMENT,
    REASONING_AZURE_DEPLOYMENT,
)
from src.config.agents import LLMType


def create_openai_llm(
    model: str,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    temperature: float = 0.0,
    **kwargs,
) -> ChatOpenAI:
    """
    Create a ChatOpenAI instance with the specified configuration
    """
    llm_kwargs = {
        "model": model,
        "temperature": temperature,
        "api_key": api_key,
        **kwargs
    }

    if base_url:
        llm_kwargs["base_url"] = base_url

    return ChatOpenAI(**llm_kwargs)


def create_deepseek_llm(
    model: str,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    temperature: float = 0.0,
    **kwargs,
) -> ChatDeepSeek:
    """
    Create a ChatDeepSeek instance with the specified configuration
    """
    llm_kwargs = {
        "model": model,
        "temperature": temperature,
        "api_key": api_key,
        "api_base": base_url,
        **kwargs
    }
    return ChatDeepSeek(**llm_kwargs)


def create_gemini_llm(
    model: str,
    api_key: Optional[str] = None,
    temperature: float = 0.0,
    **kwargs,
) -> ChatGoogleGenerativeAI:
    """
    Create a Gemini instance with the specified configuration
    """
    llm_kwargs = {
        "model": model,
        "temperature": temperature,
        "google_api_key": api_key,
        **kwargs
    }
    return ChatGoogleGenerativeAI(**llm_kwargs)


def create_azure_llm(
    azure_deployment: str,
    azure_endpoint: str,
    api_version: str,
    api_key: str,
    temperature: float = 0.0,
) -> AzureChatOpenAI:
    """
    Create an Azure OpenAI instance with the specified configuration
    """
    return AzureChatOpenAI(
        azure_deployment=azure_deployment,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
        api_key=api_key,
        temperature=temperature,
    )


# Cache for LLM instances
_llm_cache: dict[LLMType, ChatOpenAI | ChatDeepSeek | AzureChatOpenAI | ChatGoogleGenerativeAI] = {}


def _create_llm_use_env(
    llm_type: LLMType,
) -> ChatOpenAI | ChatDeepSeek | AzureChatOpenAI | ChatGoogleGenerativeAI:
    if llm_type == "reasoning":
        if REASONING_AZURE_DEPLOYMENT:
            llm = create_azure_llm(
                azure_deployment=REASONING_AZURE_DEPLOYMENT,
                azure_endpoint=AZURE_API_BASE,
                api_version=AZURE_API_VERSION,
                api_key=AZURE_API_KEY,
            )
        else:
            llm = create_deepseek_llm(
                model=REASONING_MODEL,
                base_url=REASONING_BASE_URL,
                api_key=REASONING_API_KEY,
            )
    elif llm_type == "basic":
        if BASIC_AZURE_DEPLOYMENT:
            print("===== use azure ====")
            llm = create_azure_llm(
                azure_deployment=BASIC_AZURE_DEPLOYMENT,
                azure_endpoint=AZURE_API_BASE,
                api_version=AZURE_API_VERSION,
                api_key=AZURE_API_KEY,
            )
        else:
            llm = create_gemini_llm(
                model=BASIC_MODEL,
                api_key=BASIC_API_KEY,
            )
    elif llm_type == "vision":
        if VL_AZURE_DEPLOYMENT:
            llm = create_azure_llm(
                azure_deployment=VL_AZURE_DEPLOYMENT,
                azure_endpoint=AZURE_API_BASE,
                api_version=AZURE_API_VERSION,
                api_key=AZURE_API_KEY,
            )
        else:
            llm = create_gemini_llm(
                model=VL_MODEL,
                api_key=VL_API_KEY,
            )
    else:
        raise ValueError(f"Unknown LLM type: {llm_type}")
    return llm


def get_llm_by_type(
    llm_type: LLMType,
) -> ChatOpenAI | ChatDeepSeek | AzureChatOpenAI | ChatGoogleGenerativeAI:
    """
    Get LLM instance by type. Returns cached instance if available.
    """
    if llm_type in _llm_cache:
        return _llm_cache[llm_type]

    conf = load_yaml_config(
        str((Path(__file__).parent.parent.parent / "conf.yaml").resolve())
    )
    use_conf = conf.get("USE_CONF", False)
    if use_conf:
        raise NotImplementedError("Configuration-based LLM creation not implemented yet")
    else:
        llm = _create_llm_use_env(llm_type)

    _llm_cache[llm_type] = llm
    return llm


# Initialize LLMs for different purposes - now these will be cached
reasoning_llm = get_llm_by_type("reasoning")
basic_llm = get_llm_by_type("basic")
vl_llm = get_llm_by_type("vision")


if __name__ == "__main__":
    print(basic_llm.invoke("Hello"))
