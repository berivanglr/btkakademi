from dataclasses import dataclass
@dataclass

class Mesaj:
    kullanici: str
    mesaj: str
    email: str
             

class Bildirim:
    def send(self, mesaj: Mesaj):
        pass


class EmailServis(Bildirim):
    def send(self, mesaj: Mesaj):
        print(f"E‑posta gönderildi -> \n Kullanici: {mesaj.kullanici}\n Email: {mesaj.email}\n Mesaj: {mesaj.mesaj}\n")


class SmsServisi(Bildirim):
    def send(self, mesaj: Mesaj):
        print(f"SMS gönderildi -> \n Kullanici: {mesaj.kullanici}\n Mesaj: {mesaj.mesaj}\n")


class BildirimYoneticisi:
    def __init__(self, servisler):
        self.servisler = servisler

    def hepsineGonder(self, mesaj: Mesaj):
        for servis in self.servisler:
            servis.send(mesaj)


if __name__ == "__main__":
    mesaj = Mesaj("Sisteme giriş yaptınız.", "Berivan GÜLER", "berivanglr@gmail.com")

    servisler = [EmailServis(), SmsServisi()]
    yonetici = BildirimYoneticisi(servisler)

    yonetici.hepsineGonder(mesaj)