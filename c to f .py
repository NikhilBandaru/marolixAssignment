value=int(input('enter the value :'))
cf=input('enter the C or F :')
C=((value-32)*(5/9))
F=(value*(9/5))+32
if cf=='C':
    print(f"the conversion of Fahrenheit to Celsius : {C}")
elif cf=='F':
    print(f"the conversion of Celsius to Fahrenheit  : {F}")
else:
    print('please enter C or F')