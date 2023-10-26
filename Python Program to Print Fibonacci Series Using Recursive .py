n=int(input('enter the number :'))
a=0
b=1
def fib (num):
    if num==0:
        return num
    elif num==1:
        return num
    else:
        return fib(num-1)+fib(num-2)
for i in range(0,n):
    print(fib(i))