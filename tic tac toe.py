from tabulate import tabulate
class tictactoe:
    def box(self,a):
        print(tabulate(a,tablefmt='grid'))
    def moves(self,loc,a,obj,b):
        if loc in (1, 2, 3):
            if loc == 1:
                a[0][0] = obj
            elif loc == 2:
                a[0][1] = obj
            elif loc == 3:
                a[0][2] = obj
            b.box(a)

        elif loc in (4, 5, 6):
            if loc == 4:
                a[1][0] = obj
            elif loc == 5:
                a[1][1] = obj
            elif loc == 6:
                a[1][2] = obj
            b.box(a)
        elif loc in (7, 8, 9):
            if loc == 7:
                a[2][0] = obj
            elif loc == 8:
                a[2][1] = obj
            elif loc == 9:
                a[2][2] = obj
            b.box(a)
        else:
            print('invalid')
    def winner(self,a):
        for i in a:
            if (i.count('X')==3) :
                print('player X wins')
                return 1
            elif i.count('O')==3:
                print('player O wins')
                return 1
        for j in range (3):
            c=d=0
            for k in range(3):
                if a[k][j] =='X':
                    c+=1
                elif a[k][j]=='O':
                    d+=1
            if c==3:
                print('player x wins')
                return 1
            elif d==3:
                print('palyer O wins')
                return 1
        r=u=0
        for y in range(3):
            if a[y][y]=='X':
                r+=1
            elif a[y][y]=='O':
                u+=1
        if r==3 :
            print('player x wins')
            return 1
        elif u==3:
            print('player O wins')
            return 1
        elif a[0][2]=='X' and a[1][1]=='X' and a[2][0]=='X':
            print('player X wins')
            return 1
        elif a[0][2]=='O' and a[1][1]=='O' and a[2][0]=='O':
            print('player O wins')
            return 1

b=tictactoe()
a=[['','',''],['','',''],['','','']]
while True:
    loc=int(input('enter the loction of X or O'))
    obj=input('enter X or O')
    b.moves(loc,a,obj,b)
    o=b.winner(a)
    if o==1:
        break







