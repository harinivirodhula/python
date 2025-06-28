n=int(input("Enter how many fibonacci numbers you want: "))
l=[]
a=0
b=1
for i in range(n-2):
  c=a+b
  l.append(c)
  a=b
  b=c
print(*l)
