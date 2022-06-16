class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack):
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1
        else:
            if len(needle):
                return -1
            return 0
