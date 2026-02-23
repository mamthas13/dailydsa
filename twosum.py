nums = [3,2,4]
target = 6
hash_map = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in hash_map:
        print([hash_map[complement], i])
    hash_map[num] = i
    
