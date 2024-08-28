#factorial
#5! = 5 x 4 x 3 x 2 x 1
#Logic of recursion: If 5! = 5 x 4!

def factorial(num):
    #base case: When num==0 or 1
    #Rule: 0! = 1 and 1! = 1
    if num==1 or num==1:
        return 1
    else:
        #recursive case:
        return num * factorial(num-1)
    
n=10
print(factorial(n))

#time complexity: O(n) as n increases-time for calculation increases
#scape complexity: O(n) as n increases - space for storage also increases
#graph: linear