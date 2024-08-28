def fibonacci(n):
    #base case: if n==0 or 1
    if n==0 or n==1:
        return n
    else:
        #rocurive case when n>1
        return fibonacci(n-1) + fibonacci(n-2)
    
n=10
for i in range(0,n):
    print(fibonacci(i))

    #time complexity: O(n^2) #worst case
    #space complexity: O(n)