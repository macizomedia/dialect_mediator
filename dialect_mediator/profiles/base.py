from abc import ABC, abstractmethod


class BaseDialectProfile(ABC):
    @abstractmethod
    def system_prompt(self) -> str:
        pass

