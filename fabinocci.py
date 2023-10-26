n=int(input('enter the value :'))
a=0
b=1
resut=0
for i in range(0,n):
    if i<=1:
        result=i
    else:
        result=a+b
        a,b=b,result
    print(result)
