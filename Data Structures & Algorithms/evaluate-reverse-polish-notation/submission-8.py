class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                st.append(int(tokens[i]))
            else:
                t2 = st.pop()
                t1 = st.pop()
                if tokens[i] == '+':
                    st.append((t1+t2))
                elif tokens[i] == '-':
                    st.append((t1-t2))
                elif tokens[i] == '*':
                    st.append((t1*t2))
                elif tokens[i] == '/':
                    st.append(int(t1/t2))
        return st.pop()