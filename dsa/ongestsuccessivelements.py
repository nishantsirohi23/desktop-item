a= [1,2,2,1]
a.sort()
print(a)
l = 0
r = 0
res = 1
unique_array = list(set(a))
def longest_contiguous_subarray(arr):
    arr.sort()  # Sorting the array to identify contiguous elements
    max_length = 1  # Initialize the maximum length
    current_length = 1  # Initialize the current length
    
    for i in range(1, len(arr)):
        # Check if the current element and the previous element have a difference of one
        if arr[i] - arr[i - 1] == 1:
            current_length += 1
        else:
            # Reset the current length if the difference is not one
            current_length = 1
        
        # Update the maximum length if the current length is greater
        max_length = max(max_length, current_length)

    return max_length

print(longest_contiguous_subarray(unique_array))