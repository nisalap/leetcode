class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def gen_para(st, o_count, c_count, n):
            if o_count == c_count and o_count == n:
                ret.append(st)
            elif o_count > n or c_count > n:
                return
            else:
                gen_para(st + "(", o_count + 1, c_count, n)
                if o_count > c_count:
                    gen_para(st + ")", o_count, c_count + 1, n)
        
        gen_para("", 0, 0, n)
        return ret
