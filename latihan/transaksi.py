from abc import ABC, abstractmethod

from latihan.kartubank import KartuBank

class Transaksi(KartuBank):
    
    @abstractmethod
    def Transaksi(self):
        pass
    
    def do_payment(self):
        pass