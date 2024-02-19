# s= "10231"
# s = s.lstrip('0')
# print(s)
# nums = []
# for char in s:
#     nums.append(int(char))

# print(nums)
# count = 1
# l,r=0,1
# while r<=len(nums)-1:
#     number = int(s[l:r+1])
#     if number>=1 and number<=26:
#         count+=1
#         print(number)
#     l+=1
#     r+=1

# print(count)

def num_decodings(s):
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        one_digit = int(s[i - 1:i])
        two_digits = int(s[i - 2:i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# Example usage:
input_string = "2101"
print(input_string[1:2])
print(input_string[0:2])
