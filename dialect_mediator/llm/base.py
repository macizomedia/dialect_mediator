from abc import ABC, abstractmethod
from dialect_mediator.core.models import Text, MediationResult


class BaseLLMClient(ABC):
    @abstractmethod
    def mediate(self, system_prompt: str, text: Text) -> MediationResult:
        pass
