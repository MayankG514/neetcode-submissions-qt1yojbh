class Solution:
    def longestPalindrome(self, s: str) -> str:
        # resLen = 0
        # res = ""
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):
        #         l,r = i, j

        #         while l<=r and s[l]==s[r]:
        #             l+=1
        #             r-=1
                
        #         if l>=r and resLen < (j-i+1):
        #             res = s[i:j+1]
        #             resLen = j-i+1
        # return res

        # time complexity -> O(n***3)

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        resId, resLen = 0,0
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if resLen < (j-i+1):
                        resId = i
                        resLen = j-i+1
        return s[resId: resId+resLen]
