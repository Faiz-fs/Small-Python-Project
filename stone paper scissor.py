import random
print('1.rock')
print('2.paper')
print('3.scissor')
while True:
    a=int(input('enter your choice'))
    i=random.randrange(1,4)
    if a==i:
        print('you lost')
        break
    
    