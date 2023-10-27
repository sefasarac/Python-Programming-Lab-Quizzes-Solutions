N = int(input())
sum = 0 
# https://github.com/sefasarac

while (N>0):

    if(N==1):
        N = int(input())
        continue

    if(N==2):
        sum +=2
        N = int(input())
        continue

    for i in range(2,N):
        if(N%i) == 0 :
            break 
            
        else :
            sum +=N
            continue

    N = int(input())

print(sum)        

    
