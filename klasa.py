class Drzwi:
    zablokowane = False
    otwarte = False
    model = "Model1"
    textura = "drewniane_drzwi.png"
    hp = 100

    def otworz(self):
        if self.zablokowane == False:
            self.otwarte = True
    
    def zamknij(self):
        if self.otwarte == True:
            self.otwarte = False

    def __repr__(self):
        return f"<Drzwi: zablokowane: {self.zablokowane}, otwarte: {self.otwarte}>"


drzwi_wejsciowe = Drzwi()
drzwi_do_pokoju = Drzwi()

drzwi_do_pokoju.model = "Model2"
drzwi_wejsciowe.textura = "metalowe_drzwi.png"
drzwi_wejsciowe.hp = 200
drzwi_wejsciowe.zablokowane = True

drzwi_wejsciowe.otworz()
drzwi_do_pokoju.otworz()

print(drzwi_do_pokoju)
print(drzwi_wejsciowe)