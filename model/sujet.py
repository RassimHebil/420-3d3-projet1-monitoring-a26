class sujet(ABC):
    def abonner(self, observateur) -> None:
        self._observateurs.append(observateur)

    def desabonner(self, observateur) -> None:
        self._observateurs.remove(observateur)

    def notifier(self) -> None:
        for i in self._observateurs:
            i.actualiser(self)
    @abstractmethod
    def get_donnees(self) -> dict:
        pass