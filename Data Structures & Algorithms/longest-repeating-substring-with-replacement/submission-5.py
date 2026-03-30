class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res =0

        for i in range(len(s)):
            count = 0
            fmap = {}
            for j in range(i, len(s)):
                fmap[s[j]] = 1 + fmap.get(s[j],0)
                count = max(count,fmap[s[j]])

                if (j-i+1) - count <= k:
                    res = max(res,j-i+1)
        return res

