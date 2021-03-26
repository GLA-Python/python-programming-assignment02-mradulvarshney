n=int(input())
list1=list(map(int,input().split()))
a=1
c=1
for i in range(n):
	if list1[i]==1:
		d=i
		break
for i in range(d,n):
	if list1[i]==1:
		a=a*c
		c=1
	else:
		c=c+1
print(a)
