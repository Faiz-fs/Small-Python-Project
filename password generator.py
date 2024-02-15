import random
a=['!','@','#','$','%','&','?','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
q=int(input('enter the length of the password:'))
b=''
for i in random.sample(a,q):
    b+=i
print(b)    

