class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        # Runtime 103ms Beats 83.73% of users with Python3 
        # Memory 17.44MB Beats 66.55 %of users with Python3
        i = 0
        k = len(numbers)-1
        while i < k:
            tmp = numbers[i] + numbers[k]
            if tmp == target:
                return [i+1, k+1]
            elif tmp < target:
                i = i + 1
            elif tmp > target:
                k = k - 1
