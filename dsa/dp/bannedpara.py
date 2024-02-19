import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
mylist = re.split(r'[,\s]+', paragraph)
print(mylist)
symbols_to_remove = ['!', '?', "'", ',', ';','.']

processed_list = [word.lower().strip("".join(symbols_to_remove)) for word in mylist]
print(processed_list)
hashmap = {}
for word in processed_list:
    if word not in banned:
        if word in hashmap:
            hashmap[word]+=1
        else:
            hashmap[word]=1

print(hashmap)

max_element = max(hashmap, key=lambda k: hashmap[k])

print("Element with highest count:", max_element)