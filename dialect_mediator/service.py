from dialect_mediator.core.mediator import Mediator
from dialect_mediator.core.models import Text
from dialect_mediator.profiles.venezuelan import VenezuelanDialectProfile
from dialect_mediator.llm.gemini_client import GeminiClient


def mediate_venezuelan_text(raw_text: str, api_key: str | None = None):
    text = Text(content=raw_text)
    profile = VenezuelanDialectProfile()
    llm = GeminiClient(api_key=api_key)

    mediator = Mediator(profile, llm)
    return mediator.mediate(text)
