class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # method 1 string
        strx = str(x)
        ans = ''
        
        for i in range(0,len(strx)):
            if strx[i] == strx[len(strx)-i-1]:
                continue
            else:
                return False
        return True

        # method2 using divider and reminder
        # Runtime117 ms Beats 59.93% Memory14 MB Beats 16.25%
        nums = []
        if x < 0:
            return False
        while x > 0:
            nums.append(x % 10)
            x = int(x / 10)
        for i in range(0, int(len(nums)/2)):
            if nums[i] != nums[-i-1]:
                return False
        return True
