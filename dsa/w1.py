nums = [0,1,0,3,2,3]

my_list = list(enumerate(nums))
print(my_list)
#fubction to find the number of which the index and the value are in increase order

sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)

#remove the element with same value in the list

for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        sorted_list.remove(nums[i])

print(sorted_list)
def count_increasing_elements(lst):
    count = 0
    for i in range(len(lst) - 1):
        if lst[i][0] < lst[i + 1][0] and lst[i][1] < lst[i + 1][1]:
            print(lst[i])
    return count

# Example usage
elements = [(0, 0), (2, 0), (1, 1), (4, 2), (3, 3), (5, 3)]
result = count_increasing_elements(elements)
print(result)
