class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        tmp = n
        while tmp > 0:
            if tmp % 2 == 1:
                count += 1
            tmp = tmp >> 1

        return count
