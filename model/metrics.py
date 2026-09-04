import psutil
from model.sujet import sujet
class MetriqueSysteme(sujet):
    def __init__(self):
        super().__init__()
        self._cpu = None
        self._ram = None
        self._disque = None
    def actualiser_metriques(self) -> None:
        self._cpu = psutil.cpu_percent(interval=None)
        self._ram = psutil.virtual_memory().percent
        self._disque = psutil.disk_usage('/').percent
        self.notifier()

    def get_donnees(self) -> dict:
        donnee = {
            "cpu": self._cpu,
            "ram": self._ram,
            "disque": self._disque
        }
        return donnee

