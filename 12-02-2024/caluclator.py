a=0
c=0
temp=None
while True:
  if a!=temp:
    a=int(input("enter the a value :"))
  choose=input('enter the operation +,-,*,/,p,= : ')
  if choose!="=" and choose!='p':
    b=int(input("enter the b value :"))
  if choose=='+':
    temp=(a+b)
    a,b=temp,c
  elif choose=='-':
    temp=(a-b)
    a,b=temp,c
  elif choose=='*':
    temp=(a*b)
    a,b=temp,c
  elif choose=='/':
    if b!=0:
      temp=(a/b)
      a,b=temp,c
    raise Exception('error : division by zero not allowed')
  elif choose=='p':
    n=int(input('enter the power value : '))
    temp=(a ** n)
    a,b=temp,c
  elif choose=='=':
    print(a) 
    break
  else:
    print('choose the proper operation as shown ')