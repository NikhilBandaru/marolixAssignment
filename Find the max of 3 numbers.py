a=int(input('enter the number a :'))
b=int(input('enter the number b :'))
c=int(input('enter the numbet c :'))
if a>b and a>c:
    print('"a" is greater')
elif b>c and b>a:
    print('"b" is greater')
elif c>a and c>b:
    print('"c" is greater')
else:
    print('all are equel or enter the currect number')