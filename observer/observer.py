from abc import ABC, abstractmethod

class obvservateur(ABC):
    @abstractmethod
    def actualiser(self, sujet : sujet) -> None:
        pass