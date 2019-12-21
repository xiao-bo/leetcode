class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ## Runtime: 988 ms, faster than 20.96% of Python online submissions for Range Sum Query - Immutable.
        ## Memory Usage: 15.4 MB, less than 76.92% of Python online submissions for Range Sum Query - Immutable.
        return sum(self.nums[i:j+1])
        
def main():
    nums = [-2, 0, 3, -5, 2, -1]
    a = NumArray(nums)
    print(a.sumRange(0,2))
    print(a.sumRange(2,5))
    print(a.sumRange(0,5))


if __name__ == '__main__':
    main()

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)