n=int(input('enter :'))
def summ(num):
    if num < 1:
        return num
    else:
        return (num % 10+summ(num // 10))
    
ob=summ(n)
print(ob)