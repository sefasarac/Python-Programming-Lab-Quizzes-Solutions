wordCount =0
wordCount = int(input())
counter = 0
sozluk = {}
while(counter<wordCount):
    kelimeler = input().split(":")
    english=kelimeler[0]
    turkish=kelimeler[1]
    sozluk[english] = turkish
    counter+=1
sonSatir = input().split()
cevrilecek = sonSatir[0]
bulundu=False
bulunamayanlar = []
bulunanlar = []
# https://github.com/sefasarac
def keyGetir(val): 
    for key, value in sozluk.items(): 
         if val == value: 
             return key 
    return ""

if cevrilecek=="EN":
    for i in range(1,len(sonSatir)):
        for key ,value in dict(list(sozluk.items())[::-1]).items():
            if(sonSatir[i] == value):
                bulunanlar.append(value+"="+key)
                bulundu=True
                break
            bulundu=False
        if(bulundu==False):
            bulunamayanlar.append(sonSatir[i])    
else:
    for i in range(1,len(sonSatir)):
        for key ,value in sozluk.items():
            if(sonSatir[i] == key):
                bulunanlar.append(key+"="+value)
                bulundu=True
                break
            bulundu=False
        if(bulundu==False):
            bulunamayanlar.append(sonSatir[i])    
bulunanlar.sort()

def clearRepeatingItems(liste:list):
    for item in liste:
        if(liste.count(item)>1):
            liste.remove(item)
clearRepeatingItems(bulunanlar)
clearRepeatingItems(bulunamayanlar)
for item in bulunanlar:
    print(item)
if(len(bulunamayanlar)>0):
    string_notFound =""
    bulunamayanlar.sort()
    for kelime in bulunamayanlar:
        string_notFound+= kelime +" "
    string_notFound=string_notFound.strip()
    string_notFound=string_notFound.rstrip("\n")
    print(str(len(bulunamayanlar)) + " word not found: " + string_notFound,end="")

