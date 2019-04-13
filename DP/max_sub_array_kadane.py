#code for finding maximum sub array sum

max_so_far = nums[0]	
max_ending_here = nums[0]

for i in range(1, len(nums)):
	max_ending_here = max(nums[i], max_ending_here + nums[i])
	max_so_far = max(max_so_far, max_ending_here)

return max_so_far