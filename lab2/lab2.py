inputs = map(str, input().split())
yazi=""
isString=False
isReadString=False
sayi=0
isInteger=False
isReadInt=False
kesirli=0.0
isReadFloat=False
isFloat=False
#https://github.com/sefasarac
for input in inputs:
    for letter in input:
        if(ord(letter)>=65 and ord(letter)<=122):
            isReadString=True
            isString=True
            break
    if(isString==False):
        for letter in input:
            if(letter=="."):
                isFloat=True
                break
        if(isFloat==False):
            for letter in input:
                if(ord(letter)<48 or ord(letter)>57):
                    isString=True
                    break
                else:
                    isInteger=True
    if(isFloat==True):
        kesirli+=float(input)
        isReadFloat=True
    elif(isInteger==True):
        sayi+=int(input)
        isReadInt=True
    else:
        yazi+=input
    isString=False
    isFloat=False
    isInteger=False

if(isReadInt):
    print(sayi)
if(isReadFloat):
    print(kesirli)
if(isReadString):
    print(yazi)
