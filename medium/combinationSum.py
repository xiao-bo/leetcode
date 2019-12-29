class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def recursion(ans,candidates,target,path,i):
            
            
            for x in range(i,len(candidates)):
                print("recursion x = {} target = {}".format(x,target))
                if target > 0:
                    
                    recursion(ans,candidates,target - candidates[x],path+[candidates[x]],x)                    
                    
                   
                    print("x = {} target = {} , ans = {}".format(x,target,ans))

                elif target == 0:
                    #ans.append(target)
                    #print(candidates[x])
                    ans.append(path)
                    
                    print("target == candidates = {} return = {}".format(candidates[x],ans))
                    return 
                else:
                    
                    #ans.append(False)
                    print("target < candidates = {} return = {}".format(candidates[x],ans))
                    return 
            return ans


        combination = []
        ans = []
        res = []
        combination = recursion(combination,candidates,target,res,0)
        #ans.append(combination)
        print("final = {}".format(combination))
        return combination
        ## for loop have put in recursion!!!

def test():
    testNums = [[2,3,6,7],[2,3,5]]
    target   = [     7   ,   8]
    ans      = [
                [[7],[2,2,3]],
                [[2,2,2,2],[2,3,3],[3,5]]
               ] 
    a = Solution()
    for x in range(0,len(testNums)):
        testAns = a.combinationSum(testNums[x],target[x])
        for y in range(0,len(testAns)):
            if testAns[y] not in ans[x]:
                print("false = {}".format(x))
                #print(ans[x])
                #print(testAns)
                return False

    return True
def main():
    a = Solution()
    nums = [2,3,6,7]
    target = 7
    print(test())
    #a.combinationSum(nums,target)
    

if __name__ == '__main__':
    main()