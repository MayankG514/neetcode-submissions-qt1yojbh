class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)

        # return s==t
        # time complexity -> O(nlogn+ mlogm)

        if len(s)!=len(t):
            return False

        hm = {}

        for ch in s:
            hm[ch] = 1 + hm.get(ch,0)
        
        for ch in t:
            if ch not in hm or hm.get(ch,0)==0:
                return False
            hm[ch]-=1
        
        return True
            
