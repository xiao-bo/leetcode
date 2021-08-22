def get_two_sum(nums, target):
	if len(nums) < 2:
		return []

	for x in range(0,len(nums)):
		for y in range(x + 1, len(nums)):
			if nums[x] + nums[y] == target:
				return [x,y]


