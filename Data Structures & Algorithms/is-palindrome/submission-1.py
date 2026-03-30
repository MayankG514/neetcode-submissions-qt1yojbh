class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        checkStr = '1234567890abcdefghijklmnopqrstuvwxyz'
        s1 = s1.replace(" ","")
        n=len(s1)
        s2 = ""
        for i in range(0,n):
            if s1[i] in checkStr:
                s2+=s1[i]
        n=len(s2)
        for i in range(0,n//2):
            if s2[i]!=s2[n-i-1]:
                return False
            i+=1
        
        return True
