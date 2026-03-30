class Solution:
    def isPalindrome(self, s: str) -> bool:
        nstr=""
        checkStr = "abcdefghijklmnopqrstuvwxyz1234567890"
        s=s.lower()
        for ch in s:
            if ch in checkStr:
                nstr+=ch
        l = len(nstr)
        for i in range(l//2):
            if nstr[i]!=nstr[l-1-i]:
                return False
        
        return True