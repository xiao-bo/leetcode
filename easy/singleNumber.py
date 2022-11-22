class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2022 rechanllenge
        # method1 o(n^2)
        # Runtime 3842 ms Beats 8.5% Memory 16.6 MB Beats 84.66%
        ret = []
        for x in nums:
            if x not in ret:
                ret.append(x)
            else:
                ret.remove(x)
        return ret[0]

        # method2 O(n)
        # Runtime 350 ms Beats 30.14% Memory 17 MB Beats 13.53%
        ret = {}
        for x in nums:
            if x not in ret:
                ret[x] = 1
            else:
                del ret[x]
        return list(ret.keys())[0]

        a = []
        for x in nums:
            if x not in a:
                a.append(x)
        print(a)
        for x in a:
            nums.remove(x)
        for x in nums:
            a.remove(x)

        return a[0]


def main():
    a = Solution()
    #nums = [2,2,1,3,3]
    nums = [1, 2, 2, 3, 3]
    #nums = [1]
    ans = a.singleNumber(nums)
    print(ans)


if __name__ == '__main__':
    main()
