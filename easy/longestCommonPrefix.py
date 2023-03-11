class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 2022 rechallenge 
        # Runtime 48 ms Beats 78.35% Memory 13.9 MB
        if len(strs) == 1:
            return strs[0]
        shortest = min([len(x) for x in strs])

        i = 0
        prefix = []

        while i < shortest:
            prefix = prefix + strs[0][i]
            for x in strs[1:]:
                if prefix[i] == x[i]:
                    continue
                else:
                    return prefix
            i +=1
        
        
        return prefix


        '''
        ## 2019
        Runtime 24 ms Beats 87.5% Memory 11.8 MB Beats 100%
        prefix = ""
        longPrefix = ""
        if not strs:
            return "none"
        shortest = min([len(x) for x in strs])
        
        print(shortest)
        #prefix = prefix+strs[0][0]
        #print(prefix[1])
        flag = True
        for i in range(0,shortest):
            if flag == False:
                ## 
                break

            prefix = prefix + strs[0][i]
            for y in range(1,len(strs)):
                
                print('y= {} i = {} prefix = {} strs[0][{}]={}'.format(y,i,prefix,i,strs[0][i]))

                if strs[y][i] == prefix[i]:
                    #print('y= {} i = {}'.format(y,i))
                    print(strs[y][i])
                else:
                    print("nono")
                    prefix = prefix[:len(prefix)-1]
                    flag = False
                    break
        return prefix
        '''

    def get_min_length(self, strs:List[str]):
        min_length = float(inf)

        for x in strs:
            if len(x) < min_length:
                min_length = len(x)

        return min_length

def main():
    a = Solution()
    #s = ["flower","flow","flowht"]
    s = ["dogw","dofl","dwht"]
    #s = []
    ans = a.longestCommonPrefix(s)
    print(ans)


if __name__ == '__main__':
    main()