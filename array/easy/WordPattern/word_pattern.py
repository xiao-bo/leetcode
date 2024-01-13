class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 2024 method1 using two hashmap to achieve 1-1 map condition
        # runtime 33ms Beats 83.63% of users with Python3
        # Memory 17.38MB Beats 17.95%of users with Python3
        s_list = s.split(' ')
        hashmap = {}
        if len(s_list) != len(pattern):
            return False
        
        for index in range(0,len(s_list)):
            if pattern[index] not in hashmap:
                hashmap[pattern[index]] = s_list[index]
            else:
                if hashmap[pattern[index]] != s_list[index]:
                    return False

        reverse_hashmap = {}
        for index in range(0,len(pattern)):
            if s_list[index] not in reverse_hashmap:
                reverse_hashmap[s_list[index]] = pattern[index] 
            else:
                if reverse_hashmap[s_list[index]] != pattern[index]:
                    return False
        return True
