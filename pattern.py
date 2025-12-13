class logger:
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(). __new__(cls)
        return cls._instance 
        
    def log(self, mesaj: str):
        print("[LOG],mesaj")
        
        
        
class FiyatStratejisi():
    def hesapla(self, fiyat):
        pass
    
class IndirimsizStrateji(FiyatStratejisi):
    def hesapla(self, fiyat:float):
        return fiyat

class OgrenciIndirimiStrateji(FiyatStratejisi):
    def hesapla(self, fiyat:float)->float:
        return fiyat * 0.7

class BlackFridayStrateji(FiyatStratejisi):
    def hesapla(self, fiyat:float)->float:
        return fiyat * 0.5
    
    
    
class OdemeYontemi():
    def odeme(self, tutar:float)->float:
        pass

class KrediKartiOdeme(OdemeYontemi):
    def odeme(self, tutar:float)->float:
        print(f"{tutar} TL kredi karti ile ödendi.")

class PayPalOdeme(OdemeYontemi):
    def odeme(self, tutar:float)->float:
        print(f"{tutar} TL PayPal ile ödendi.")

class OdemeFabrikasi:
    def odemeYontemi(yontem):
        if yontem == "kart":
            return KrediKartiOdeme()
        elif yontem == "paypal":
            return PayPalOdeme()
        else:
            raise ValueError("Desteklenmeyen ödeme yöntemi")
        


        
