from dialect_mediator.core.mediator import Mediator
from dialect_mediator.core.models import Text
from dialect_mediator.profiles.venezuelan import VenezuelanDialectProfile
from dialect_mediator.llm.openai_client import OpenAIClient


def mediate_venezuelan_text(raw_text: str, api_key: str):
    text = Text(content=raw_text)
    profile = VenezuelanDialectProfile()
    llm = OpenAIClient(api_key=api_key)

    mediator = Mediator(profile, llm)
    return mediator.mediate(text)

