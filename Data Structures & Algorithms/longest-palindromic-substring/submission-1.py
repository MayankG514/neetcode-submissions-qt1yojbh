class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res, resLen = "", 0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         l,r  = i,j
        #         while l<r and s[l]==s[r]:
        #             l+=1
        #             r-=1
                
        #         if l>=r and resLen < (j-i+1):
        #             res = s[i:j+1]
        #             resLen = j-i+1
        # return res

        # time complexity -> O(n**3)
        # space -> O(n)

        # res = ""
        # resLen = 0

        # for i in range(len(s)):
        #     l,r = i,i
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if resLen < (r-l+1):
        #             resLen = r-l+1
        #             res = s[l:r+1]
        #         l-=1
        #         r+=1
        
        # for i in range(len(s)):
        #     l,r = i,i+1

        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if resLen < (r-l+1):
        #             resLen = r-l+1
        #             res = s[l:r+1]
        #         l-=1
        #         r+=1
        
        # return res

        # time complexity -> O(n**2)
        # space complexity -> O(n) + O(1)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resID, resLen  = 0,0

        for i in range(n-1,-1,-1):
            for j in range(0,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i+1):
                        resID = i
                        resLen = j-i+1
        return s[resID : resID+resLen]

