from abc import ABC, abstractmethod

class BarangElektonik(ABC):
    
    @abstractmethod
    def beroperasi(self):
        pass
    
    @abstractmethod
    def berhenti(self):
        pass