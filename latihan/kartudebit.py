from abc import ABC, abstractmethod

class KartuDebit(ABC):
    
    @abstractmethod
    def do_transaction(self):
        pass