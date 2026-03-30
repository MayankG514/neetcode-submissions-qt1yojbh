class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1>l2:
            return False

        hm1 = {}

        for c in s1:
            hm1[c] = 1 + hm1.get(c,0)
        
        need = len(hm1)

        for i in range(l2):
            count = 0
            curr = {}
            for j in range(i,l2):
                curr[s2[j]] = 1 + curr.get(s2[j],0)
                if curr[s2[j]] > hm1.get(s2[j],0):
                    break
                if curr[s2[j]] == hm1.get(s2[j],0):
                    count+=1
                if count == need:
                    return True
        return False
