from dialect_mediator.core.models import Text
from dialect_mediator.core.mediator import Mediator
from dialect_mediator.profiles.venezuelan import VenezuelanDialectProfile
from dialect_mediator.llm.base import BaseLLMClient
from dialect_mediator.core.models import MediationResult


class FakeLLM(BaseLLMClient):
    def mediate(self, system_prompt, text):
        return MediationResult(mediated_text="FAKE OUTPUT")


def test_mediator_runs():
    mediator = Mediator(
        profile=VenezuelanDialectProfile(),
        llm=FakeLLM()
    )

    result = mediator.mediate(Text(content="texto de prueba"))
    assert result.mediated_text == "FAKE OUTPUT"
