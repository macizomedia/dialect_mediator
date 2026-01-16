from abc import ABC, abstractmethod
from .models import Text, MediationResult


class DialectProfile(ABC):
    @abstractmethod
    def system_prompt(self) -> str:
        """Returns the system prompt defining the dialect mediation rules."""
        pass


class LLMClient(ABC):
    @abstractmethod
    def mediate(self, system_prompt: str, text: Text) -> MediationResult:
        """Executes the mediation using an LLM."""
        pass
