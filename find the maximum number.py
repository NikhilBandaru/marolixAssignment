def maxnum(arr): 
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
        
lst=[6,8,3,55,44,33]
maxnum(lst)
print('sorted list:',lst)
print(lst[-1])