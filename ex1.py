def find(nums, target): 
    seen = {} #stores numbers already seen with index
    for i, num in enumerate(nums): #enumerate(nums) gives i (index) and num(number at index). e.g. {2: 0}: number 2 at index 0
        check = target - num #check = needed to reach target
        if check in seen: 
            return [seen[check], i] #found pair
        seen[num] = i    #stores index of current number
    else:
        return None
    
nums = [3, 2, 4]
target = 6

print(find(nums, target))
