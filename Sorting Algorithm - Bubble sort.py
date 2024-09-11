#using function of python
numbers=[1,2,3,4,5,0,10,23,14]

# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

#bubble sort
for i in range(0,len(numbers)):
    for j in range (i,len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i] , numbers[j] = numbers[j],numbers[i]
            print("sorted order: ",numbers)

