def numWays(words, target):
        MOD = 10 ** 9 + 7
        m, n = len(words[0]), len(target)
        #charAtIndexCnt = [[0] * m for _ in range(128)]
        charAtIndexCnt =[]
        #128 characters of ASCII
        for _ in range(128):
            charAtIndexCnt.append([0]*m)
            
        # Count the number of character `c` at index `i` of all words
        for word in words:
            for i, c in enumerate(word):
                # ord(c):return c's ASCII number
                charAtIndexCnt[ord(c)][i] += 1

              

        def dp(k, i):
            # Formed a valid target
            if i == n:  
                return 1
            # Reached to length of words[x] but don't found any result
            if k == m:  
                return 0
            c = target[i]
            # Skip k_th index of words
            ans = dp(k + 1, i)  
            # Take k_th index of words if found character `c` at index k_th
            if charAtIndexCnt[ord(c)][k] > 0: 
                ans += dp(k + 1, i + 1) * charAtIndexCnt[ord(c)][k]
                ans %= MOD
            return ans

        return dp(0, 0)

    
def main():
    words = ["acca","bbbb","caca"]
    target = "aba"
    numWays(words, target)
main()
