from abc import ABC, abstractmethod

class KartuKredit(ABC):
    
    @abstractmethod
    def do_transaction(self):
        pass