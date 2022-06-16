class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(x) for x in strs]
        idx = lengths.index(min(lengths))
        term = strs[idx]
        pr = ""
        for i in range(1, len(term)+1):
            prefix = term[:i]
            count = 0
            for each in strs:
                if each.startswith(prefix):
                    count += 1
            if count == len(lengths):
                pr = prefix
        return pr
            
