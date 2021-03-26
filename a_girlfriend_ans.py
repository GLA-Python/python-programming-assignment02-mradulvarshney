n=int(input())
s=0
for i in range(5,0,-1):
    if n!=0:
        a=n//i
        s+=a
        n=n%i
print(s)
