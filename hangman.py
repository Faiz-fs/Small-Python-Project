def check(b,a,l,i):
    for k in range(len(b)):
        l+=b[k]
    if l==a[i]:
        return l
    else:
        return b
            
import random
l=''
a=['account','brother','hangman','captian']
b=['_','_','_','_','_','_','_']
i=random.randrange(0,len(a))
chance=0
while chance!=7  :
    c=input('guess the word by alphabets')
    q=list(a[i])
    if c in q:
        r=0
        for p in q:
            if p==c:
                b[r]=c
                r+=1
            else:
                r+=1
        x=check(b,a,l,i)
        if x in a:
            print(x)
            break
        else:
            print(x)
    else:
        chance+=1 
        print('you lost : TRY AGAIN')    
  


   


    


