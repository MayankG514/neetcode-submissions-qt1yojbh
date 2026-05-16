class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False
        alphanum = "abcdefghjiklmnopqrstuvwxyz1234567890"
        resS = ""
        s = s.lower()
        for c in s:
            if c not in alphanum or c == " ":
                continue
            resS+=c
        
        n = len(resS)

        for i in range(n//2):
            if resS[i] != resS[n-i-1]:
                return False
            
        return True
        
            