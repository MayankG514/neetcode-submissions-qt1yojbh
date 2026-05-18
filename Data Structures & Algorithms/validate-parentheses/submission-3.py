class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        openB = ['(','[','{']
        closeB = [')',']','}']

        for c in s:
            if c in openB:
                st.append(c)
            else:
                if not st:
                    return False
                
                if c in closeB and st:
                    if (c==']' and st[-1]!='[') or (c=='}' and st[-1]!='{') or (c==')' and st[-1]!='(') :
                        return False
                st.pop()

        return len(st)==0
