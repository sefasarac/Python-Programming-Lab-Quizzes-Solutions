class ListClass:
    sayilarimiz = []
    ismimiz=""
    def __init__(self, sayilar, isim):
        self.sayilarimiz=sayilar
        self.ismimiz=isim
    def __str__(self):
        sayilarStr="["
        for sayi in self.sayilarimiz:
            sayilarStr+=str(sayi) + " "
        sayilarStr=sayilarStr.strip()
        sayilarStr+="]"
        return sayilarStr
    def printName(self):
        print("Name: " + self.ismimiz)
    def getLength(self):
        return len(self.sayilarimiz)
    def printOdds(self):
        tekler=""
        for sayi in self.sayilarimiz:
            if(sayi%2==1):
                tekler +=str(sayi)+" "
        tekler=tekler.strip()
        print(tekler)
    def printEvens(self):
        ciftler=""
        for sayi in self.sayilarimiz:
            if(sayi%2==0):
                ciftler +=str(sayi)+" "
        ciftler=ciftler.strip()
        print(ciftler)
    def changeItem(self,sayimiz,yeniSayi):
        for i in range(0,len(self.sayilarimiz)):
            if(self.sayilarimiz[i]==sayimiz):
                self.sayilarimiz[i]=yeniSayi
    def addItem(self,yeniSayi):
        self.sayilarimiz.append(yeniSayi)
    def addItems(self,yeniSayilar=[]):
        esitlik=False
        for yeniSayi in yeniSayilar:
            for sayi in self.sayilarimiz:
                if(sayi==yeniSayi):
                    esitlik=True
                    break
            if(esitlik==False):
                self.sayilarimiz.append(yeniSayi)
            esitlik=False
    def removeItem(self,silinecek):
        self.sayilarimiz.remove(silinecek)
    def removeItems(self,silinecekler=[]):
        esitlik=False
        for yeniSayi in silinecekler:
            for sayi in self.sayilarimiz:
                if(sayi==yeniSayi):
                    esitlik=True
                    break
            if(esitlik==True):
                self.sayilarimiz.remove(yeniSayi)
            esitlik=False
    def __lt__(self,other):
        toplam=0
        for sayi in self.sayilarimiz:
            toplam+=sayi
        digerToplam=0
        for digerSayi in other.sayilarimiz:
            digerToplam+=digerSayi
        if(toplam<digerToplam):
            return True
        else:
            return False
# https://github.com/sefasarac