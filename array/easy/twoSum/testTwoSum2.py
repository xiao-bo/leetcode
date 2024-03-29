
from twoSum2 import get_two_sum

def test_get_two_sum():
	nums = [1]
	target = 1
	expected_result = []
	result = get_two_sum(nums,target)
	assert result == expected_result

	
	nums = [2,7,11,15]
	target = 9
	expected_result = [0,1]
	result = get_two_sum(nums, target)
	assert result == expected_result
	
	nums = [3,2,4]
	target = 6
	expected_result = [1,2]
	result = get_two_sum(nums, target)
	assert result == expected_result

	nums = [3,3]
	target = 6
	expected_result = [0,1]
	result = get_two_sum(nums, target)
	assert result == expected_result

	nums = [3,1,1,3]
	target = 6
	expected_result = [0,3]
	result = get_two_sum(nums, target)
	assert result == expected_result
	
	nums = [-3,4,3,90]
	target = 0
	expected_result = [0,2]
	result = get_two_sum(nums, target)
	assert result == expected_result
	