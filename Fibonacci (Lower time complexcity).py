#fibonacci series - addition of previous 2 numbers and starting numbers are 0 and 1

#method 2 - optimization
def fibonacci(n,memo={}):
    #check if n is in memo
    if n in memo:
        return memo[n]
    
    #base case: n==0 or 1
    if n <= 1:
        return n
    else:
        #recursive case
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]
    
n=10
for i in range(0,n):
    print(fibonacci(i))

#time complexity: O(n)
#space complexity: O(n)
