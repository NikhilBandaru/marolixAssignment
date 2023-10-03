def prime(number):
    if number <= 1:
        return False  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return ('not prime')  
    return ('prime')  
number=int(input('enter the value :'))    
print(prime(number))  
