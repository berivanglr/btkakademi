class Kullanici:
    def __init__(self,ad, mail ):
        self.ad = ad
        self.mail = mail
    
    def bilgi(self):
        return f"kullanici ismi {self.ad} \n kullanici maili {self.mail}"
    
class Öğrenci(Kullanici):
    def __init__(self,ad,mail,no):
        super().__init__(ad,mail)
        self.no=no
    def bilgi(self):
        return f"kullanici ismi {self.ad} \n kullanici maili {self.mail}, kullanici no {self.no}"

class Öğretmen(Kullanici):
    def __init__(self,ad,mail,brans):
        super().__init__(ad,mail)
        self.brans=brans
    def bilgi(self):
        return f"kullanici ismi {self.ad} \n kullanici maili {self.mail}\n kullanici branşi {self.brans}"
    
    
class Ders:
    def __init__(self,ad ,öğretmen):
        self.ad=ad
        self.öğretmen=Öğretmen
        
        
