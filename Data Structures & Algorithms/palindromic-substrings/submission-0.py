class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         l,r = i,j
        #         while l<r and s[l]==s[r]:
        #             l+=1
        #             r-=1
                
        #         if l>=r:
        #             count+=1
        # return count
        # time complexity -> O(n***3)
        # space ->. O(1)
        n = len(s)
        dp = [[False]* n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]==True):
                    count+=1
                    dp[i][j] = True
        
        return count