class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r=0,0
        hmap = {}
        maxL = 0
        n=len(s)
        while r<n:
            if s[r] in hmap and hmap[s[r]]>=l:
                l = hmap[s[r]] + 1

            hmap[s[r]]=r
            maxL = max(maxL,r-l+1)
            r+=1
        return maxL
        
            