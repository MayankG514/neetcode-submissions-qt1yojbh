class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        n=len(s)
        l=0
        res =0
        for r in range(n):
            if s[r] in hm:
                l=max(hm[s[r]] + 1,l)
            hm[s[r]] = r
            res = max(res,r-l+1)
        return res