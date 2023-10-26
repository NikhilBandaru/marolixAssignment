a=input('enter the value :')
b=a[::-1]
while a==b:
    b=int(b)
    print('it is palindrome')
    break
else:
    print('its not palindrome')
