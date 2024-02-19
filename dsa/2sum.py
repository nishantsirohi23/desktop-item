nums = [1,2,1,1]
rob1,rob2 = 0,0

for n in nums:
    rob1,rob2 = rob2,max(rob1+n,rob2)
print(rob2)

