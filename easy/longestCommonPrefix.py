class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

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

def main():
    a = Solution()
    #s = ["flower","flow","flowht"]
    s = ["dogw","dofl","dwht"]
    #s = []
    ans = a.longestCommonPrefix(s)
    print(ans)


if __name__ == '__main__':
    main()