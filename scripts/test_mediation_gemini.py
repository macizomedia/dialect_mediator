from dialect_mediator.core.models import Text
from dialect_mediator.core.mediator import Mediator
from dialect_mediator.profiles.venezuelan import VenezuelanDialectProfile
from dialect_mediator.llm.gemini_client import GeminiClient

def main():
    text = Text(
        content="Aquí nadie se chupa el dedo y esa gente solo jala pa su lado."
    )

    mediator = Mediator(
        profile=VenezuelanDialectProfile(),
        llm=GeminiClient(),   # usa GEMINI_API_KEY del entorno
    )

    result = mediator.mediate(text)
    print(result.mediated_text)


if __name__ == "__main__":
    main()
