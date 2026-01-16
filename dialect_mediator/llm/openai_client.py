from dialect_mediator.core.models import Text, MediationResult
from .base import BaseLLMClient


class OpenAIClient(BaseLLMClient):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def mediate(self, system_prompt: str, text: Text) -> MediationResult:
        # TODO: real implementation
        raise NotImplementedError("OpenAI client not implemented yet")

