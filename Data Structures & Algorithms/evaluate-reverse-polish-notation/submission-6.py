class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st =[]

        for i in range(0,len(tokens)):
            if tokens[i] not in ["+","-","/","*"]:
                st.append(int(tokens[i]))
            else:
                t1 = st.pop()
                t2 = st.pop()
                if tokens[i]=="+":
                    st.append(t1+t2)
                elif tokens[i]=="-":
                    st.append(t2-t1)
                if tokens[i]=="*":
                    st.append(t1*t2)
                if tokens[i]=="/":
                    st.append(int(t2/t1))
        return st[-1]