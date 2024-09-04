#Linear search
arr= [2,3,6,1,10,8,90]

search_num=10

#Method 1
for x in arr:
    if x==search_num:
        print(f"{search_num} is in this list")

#Method 2
if search_num in arr:
    print(f"{search_num} exists")

#Method 3
for i in range(0, len(arr)):
    if arr[i] == search_num:
        print("This is in list")