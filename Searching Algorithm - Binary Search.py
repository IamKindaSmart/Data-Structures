#Binary Search

numbers=[1,15,11,16,4,5,6,7,8,19]
#condition: list has to be in order
numbers.sort()
print(numbers)

search_num=15

start=0
end=len(numbers)-1

flag=False #this variable will be made true when search element is found

while start<=end:
    mid=(start+end)//2 #floor division. #Only gives integers

    if numbers[mid]==search_num:
        print("We found the number!")
        flag=True
        break

    elif numbers[mid] > search_num: #First half of list
        end=mid-1

    else:       #second half of list
        start=mid+1

if flag==False:
    print("We never got this number")
