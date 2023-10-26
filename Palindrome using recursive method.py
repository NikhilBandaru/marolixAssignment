
def pal (a,b):
    if a==b:
        b=int(b)
        return('it is a palindrome')
    else:
        return('its not palindrone')
a=input('enter the value :')
b=a[::-1]
print(pal(a,b))
