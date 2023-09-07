a = int(input())
c=0
for i in range(a):
    b=0
    
    k=str(input()).split(" ")
    for d in range(0,3):
        if int(k[d])==1 or int(k[d])==0:
            b+=int(k[d])
    if b>=2:
        c+=1
print(c)                
