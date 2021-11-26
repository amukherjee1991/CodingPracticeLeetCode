def twoSum(array, targetSum):
    # Write your code here.
    hash={}
        
	for idx,n in enumerate(nums):
		if target - n in hash:
			return hash[target-n],idx
		else:
			hash[n]=idx