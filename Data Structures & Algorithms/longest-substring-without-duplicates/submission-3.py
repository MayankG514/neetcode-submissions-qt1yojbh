class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        n = len(s)
        res = 0 
        l = 0 

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res



