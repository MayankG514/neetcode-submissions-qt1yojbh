class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1>l2:
            return False
        
        hm1, hm2 = [0]*26, [0]*26

        for i in range(l1):
            hm1[ord(s1[i])-ord('a')] +=1
            hm2[ord(s2[i])-ord('a')] +=1

        matches = 0
        
        for i in range(26):
            matches+= (1 if hm1[i]==hm2[i] else 0)
        l=0

        for r in range(l1,l2):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            hm2[index]+=1

            if hm1[index]==hm2[index]:
                matches+=1

            elif hm1[index]+1 == hm2[index]:
                matches-=1
            
            index = ord(s2[l]) - ord('a')
            hm2[index]-=1

            if hm1[index]==hm2[index]:
                matches+=1

            elif hm1[index]-1 == hm2[index]:
                matches-=1
            l+=1
        return matches == 26

            
        

        
