from graphics import *
import random

matrix=[[0,0,0],[0,0,0],[0,0,0]]
win = GraphWin("19290322",300,350)
bitti_mi=False
label = tk.Label(win,text="")
label.place(x=125,y=316)
kazanan=0

def randomXY():
    global matrix,label
    randX =random.randrange(0, 3)
    randY= random.randrange(0,3)
    if(matrix[randX][randY]==1 or matrix[randX][randY]==2):
        randX,randY=randomXY()
    return randX,randY

def kontrol():
    global matrix,bitti_mi
    if(bitti_mi==True):
        return
    for row in matrix:
        for sayi in row:
            if 0 == sayi:
                bitti_mi=False
                return
    bitti_mi=True
    label.config(text="Draw!")
    return

def check_win():
    global matrix,kazanan,bitti_mi
    for i in range(len(matrix)):
        for j in matrix[i]:
            if(matrix[i][j]!=0):
                found_one=matrix[i][j]
                bitti_mi = all(x==matrix[i][j] for x in matrix[i] )#yatay
                if(bitti_mi):
                    kazanan=found_one
                    return
                for k in range(0,len(matrix)):#dikey
                    if(matrix[k][j] != found_one):
                        bitti_mi=False
                        kazanan=0
                        break
                    bitti_mi=True
                    kazanan=found_one
                if(bitti_mi):
                    return
                if(matrix[0][0] == found_one and matrix[1][1] == found_one and matrix[2][2] == found_one):
                    bitti_mi=True
                    kazanan=found_one
                    return
                if(matrix[0][2] == found_one and matrix[1][1] == found_one and matrix[2][0] == found_one):
                    bitti_mi=True
                    kazanan=found_one
                    return
                
def tikla(x,y):
    global matrix,bitti_mi,label
    if(bitti_mi):
        return
    if(matrix[x][y]!=0):
        label.config(text="You  cannot click  the  filled  squares")
        label.place(x=50,y=316)
        return
    label.config(text="")
    matrix[x][y]=1
    buton_yazdir()
    check_win()
    kontrol()
    if bitti_mi == False:
        rX,rY=randomXY()
        matrix[rX][rY]=2
        check_win()
        buton_yazdir()

    if kazanan == 1:
        label.config(text="X Wins")
        label.place(x=125,y=316)
    elif kazanan==2:
        label.config(text="O Wins")
        label.place(x=125,y=316)
def buton_yazdir():
    global win
    global matrix
    x,y=0,0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if(matrix[i][j]==0):
                btn = tk.Button(win,text="",compound="c",command=lambda i=i,j=j: tikla(i,j))
                btn.place(x=x,y=y,width=100,height=100)
            elif(matrix[i][j]==1):
                btn = tk.Button(win,text="X",compound="c",command=lambda i=i,j=j: tikla(i,j))
                btn.place(x=x,y=y,width=100,height=100)
            else:
                btn = tk.Button(win,text="O",compound="c",command=lambda i=i,j=j: tikla(i,j))
                btn.place(x=x,y=y,width=100,height=100)
            x+=100
        y+=100
        x=0

def main():
    global bitti_mi
    buton_yazdir()
    q=win.getKey()
    while(q!='q' or bitti_mi==False):
        q=win.getKey()

main()
