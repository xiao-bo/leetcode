class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # using hash map 
        # Runtime 54ms Beats 68.74 %of users with Python3
        # Memory 16.73 MB Beats 68.77% of users with Python3
        hash_map = {}
        # make hash map
        for c in magazine:
            if c in hash_map:
                hash_map[c] = hash_map[c] + 1
            else:
                hash_map[c] = 1
        
        i = 0
        while i < len(ransomNote):
            if ransomNote[i] in hash_map and hash_map[ransomNote[i]] != 0:
                hash_map[ransomNote[i]] = hash_map[ransomNote[i]] - 1
                i = i + 1
            else:
                return False

        return True

