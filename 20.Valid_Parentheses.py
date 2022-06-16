class Solution:
    def isValid(self, s: str) -> bool:
        br = {'(':')','[':']','{':'}'}
        if s[0] in br.values():
            return False
        st = []
        for each in s:
            if each in br:
                st.append(each)
            else:
                if len(st) > 0:
                    if each == br[st.pop()]:
                        continue
                    else:
                        return False
                else: 
                    return False
        if len(st) > 0:
            return False
        else: 
            return True
