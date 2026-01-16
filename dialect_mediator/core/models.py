from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass(frozen=True)
class Text:
    content: str
    language: str = "es"
    metadata: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class MediationResult:
    mediated_text: str
    notes: Optional[str] = None
    confidence: Optional[float] = None

