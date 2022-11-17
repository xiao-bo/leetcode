class Solution:
    def longestPalindrome(self, s: str) -> int:

        ## method1 brute method
        #runtime Beats 6.26%, Memory Beats 67.52%
        flag = 0
        hashtable = {}

        for char in s:
            hashtable[char] = 0
        for char in s:
            hashtable[char] = hashtable[char] + 1
        ret = 0
        maximun_odd_value = 0
        maximun_odd_key = 0
        # ret = 超過3次的第二個之後的每個奇數次數-1 + 每個偶數次數 + 第一次出現3次以上的奇數
        for key, value in hashtable.items():
            if value %2 == 0:
                ret = ret + value 
            else:
                if value > maximun_odd_value:
                    maximun_odd_value = value 
                    maximun_odd_key = key
        ret = ret + maximun_odd_value

        for key, value in hashtable.items():
            if value%2 ==0 :
                continue
            else:
                if key == maximun_odd_key:
                    continue
                else:
                    ret = ret + value - 1
        return ret
        
