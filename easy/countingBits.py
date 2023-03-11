class Solution:
    def countBits(self, n: int) -> List[int]:
        import math
        # first method, generate bits depended on previous result
        # like DP
        # 83 ms Beats 95.13%, memory 20.8 MB Beats 79.76%

        # a[2] = a[0] +1, a[3] = a[1] + 1
        # a[4] = a[0]+1, a[5] = a[1]+1... ,a[7] = a[3]+1
        # a[8] = a[0]+1, .... ,a[15] = a[7]+1
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        ret = [0,1]

        i = 2
        pow_value = 1 # 計算batch，因為每次batch是2指數成長 
        while i <= n:
            batch = int(math.pow(2,pow_value))
            for j in range(0, batch):
                # 每次計算，會依賴0~j的結果
                ret.append(ret[j] + 1)
            i = i * 2
            pow_value = pow_value + 1
        return ret[:n+1]

