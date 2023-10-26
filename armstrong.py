#Armstrong number program in python
a=input('enter the number :')
b=0
for i in (a):
    c=int(i)
    b+=c**(len(a))
print(b)
a=int(a)
if b==a:
    print ('it is a armstrong number')
else:
    print('its not')
