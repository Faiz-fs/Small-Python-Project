import random
def start(attempt):
        a=random.randrange(1,11)
        while True:
            b=int(input('enter the num from 1-10'))
            if a==b:
                print ('YOU WON ')
                break
            else:
                print('try again the number is less than',a+3)
                attempt+=1
def level2 (attempt):
    a=random.randrange(1,51)
    c=0
    while True:
        c+=1
        b=int(input('enter the num from 1-50'))
        if a==b:
            print ('YOU WON ')
            break
        elif c>3:
            print('out of hints')
        else:
            if a<10:
                print('try again the number is between',1,10)
                attempt+=1
                if c==2:
                    if a<=5:
                        print('the number less than 5')
                        attempt+=1
                    else:
                        print('the number greater than 5')

            elif a>=40 and a<50:
                print('try again the number is between',40,50)
                attempt+=1
                if c==2:
                    if a<=45:
                        print('the number less than 45')
                        attempt+=1
                    else:
                        print('the number greater than 45')
    
            elif a>=10 and a<20:
                print('try again the number is between',10,20)
                attempt+=1
                if c==2:
                    if a<=15:
                        print('the number less than 15')
                        attempt+=1
                    else:
                        print('the number greater than 15')

            elif a>=20 and a<30:
                print('try again the number is between',20,30)
                attempt+=1
                if c==2:
                    if a<=25:
                        print('the number less than 25')
                        attempt+=1
                    else:
                        print('the number greater than 25')

            elif a>=30 and a<40:
                print('try again the number is between',30,40)
                attempt+=1
                if c==2:
                    if a<=35:
                        print('the number less than 35')
                        attempt+=1
                    else:
                        print('the number greater than 35')


            


attempt=0
while True:
    print('1.to start the game')
    print('2.to got to level 2')
    print('3. to view your attempts')
    q=int(input('enter your choice'))

    if q==2:
        level2(attempt)
    elif q==1:
        start(attempt)
    elif q==3:
        print(attempt)
    else:
        print('INVALOD INPUT GAME ENDED')
        break    

