firstLine= input().split()
secondLine = input().split()
#https://github.com/sefasarac
matched=False

def subStringBul(yazi,part):
    indexes = []
    counter = 0
    partUzunluk = len(part)
    for i in range(0,len(yazi)):
        if(yazi[i]==part[0]):
            bolum=yazi[i:i+partUzunluk]
            if(bolum == part):
                indexes.append(i)
                counter+=1
    if(counter>0):
        print(yazi + " " + part + " "+  str(counter) + " " + str(indexes))
        return True
    return False            


for word in firstLine:
    for part in secondLine:
        if(subStringBul(word,part)):
            matched=True

if(matched==False):
    print("None")