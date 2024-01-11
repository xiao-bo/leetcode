class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # method 1 
        # 從陣列尾巴開始檢查char
        # 如果char不是文字，則跳到下一個index
        # 如果char是文字，則開始計算，直到非字元出現
        # 即可得到最後一個字的長度

        # edge case
        if len(s) == 1 and s.isalpha():
            return 1
        elif len(s) == 1 and not s.isalpha():
            return 0

        length = 0
        for index in range(len(s)-1, -1, -1):
            if s[index].isalpha():
                length = length + 1
            elif length > 0:
                break
            
        return length

