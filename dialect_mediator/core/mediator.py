from .models import Text, MediationResult
from .ports import DialectProfile, LLMClient


class Mediator:
    def __init__(self, profile: DialectProfile, llm: LLMClient):
        self._profile = profile
        self._llm = llm

    def mediate(self, text: Text) -> MediationResult:
        if not text.content.strip():
            raise ValueError("Input text is empty")

        system_prompt = self._profile.system_prompt()
        return self._llm.mediate(system_prompt, text)

