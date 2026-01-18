import pytest

from dialect_mediator.core.mediator import Mediator
from dialect_mediator.core.models import Text, MediationResult


class StubProfile:
    def system_prompt(self) -> str:
        return "SYSTEM"


class StubLLM:
    def __init__(self):
        self.calls = []

    def mediate(self, system_prompt: str, text: Text) -> MediationResult:
        self.calls.append((system_prompt, text))
        return MediationResult(mediated_text="ok", notes="", confidence=1.0)


def test_mediator_rejects_empty_payload():
    mediator = Mediator(profile=StubProfile(), llm=StubLLM())

    with pytest.raises(ValueError):
        mediator.mediate(Text(content="   \n  "))


def test_mediator_passes_prompt_and_text():
    llm = StubLLM()
    mediator = Mediator(profile=StubProfile(), llm=llm)
    text = Text(content="hola mundo")

    result = mediator.mediate(text)

    assert result.mediated_text == "ok"
    assert llm.calls == [("SYSTEM", text)]
