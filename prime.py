p=int(input("enter the value:"))
f=0
for i in range(1,p+1):
    if p%i==0:
        f+=1
if f>2:
    print("it is not prime")
else:
        print("prime")        