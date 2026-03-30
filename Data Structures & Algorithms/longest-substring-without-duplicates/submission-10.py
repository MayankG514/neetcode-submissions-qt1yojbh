class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l=0
        maxL = 0

        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]]+1,l)
            hm[s[r]] = r
            maxL = max(maxL,r-l+1)
        return maxL