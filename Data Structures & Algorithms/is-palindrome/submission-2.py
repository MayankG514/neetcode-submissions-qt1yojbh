class Solution:
    def isPalindrome(self, s: str) -> bool:

        checkstr = "1234567890abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        st=""
        for c in s:
            if c in checkstr:
                st+=c
        l = len(st)
        for i in range(l//2):
            if st[i]!=st[l-i-1]:
                return False

        return True