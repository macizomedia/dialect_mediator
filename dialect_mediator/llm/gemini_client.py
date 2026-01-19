import os

from google import genai

from dialect_mediator.core.models import Text, MediationResult
from dialect_mediator.llm.base import BaseLLMClient


class GeminiClient(BaseLLMClient):
    def __init__(
        self,
        api_key: str | None = None,
        model: str = "gemini-2.5-pro",
        temperature: float = 0.3,
    ):
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("Missing GEMINI_API_KEY")

        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.temperature = temperature

    def mediate(self, system_prompt: str, text: Text) -> MediationResult:
        prompt = f"""{system_prompt}

TEXT:
{text.content}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=self.temperature,
            ),
        )

        content = response.text.strip() if response.text else ""

        return MediationResult(
            mediated_text=content,
            confidence=None,
            notes=None,
        )

