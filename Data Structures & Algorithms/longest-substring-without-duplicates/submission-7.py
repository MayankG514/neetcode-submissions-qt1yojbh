class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l=0
        r=0
        n=len(s)
        res = 0
        while r<n:
            if s[r] in hm:
                l = max(hm[s[r]]+1,l)
            hm[s[r]] = r
            res = max(res, r-l+1)
            r+=1
            
        return res

