#find the largest element in an array

# brute force sorting 
arr = [1,4,3,45,78,87,2]
arr.sort()
print(arr[-1])
#time complexity O(Nlogn)


#optimal solution
max = arr[0]
for i in range(1,len(arr)):
    if arr[i] > max:
        max = arr[i]


print(max)
#time complexity is O(N)