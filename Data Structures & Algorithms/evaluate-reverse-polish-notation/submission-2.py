class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t not in ['+','-','/','*']:
                st.append(int(t))
            else:
                t1=st.pop()
                t2=st.pop()
                if t == '+':
                    st.append(t1+t2)
                elif t== '-':
                    st.append(t2-t1)
                elif t=='/':
                    st.append(int(t2/t1))
                elif t=='*':
                    st.append(t1*t2)
        return st.pop()