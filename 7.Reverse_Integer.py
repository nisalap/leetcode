class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))
        if x >= 0:
            reverse = int(num[::-1])
        else:
            reverse = -int(num[::-1])
        if reverse > (2**31 - 1) or reverse < -2**31:
            return 0
        return reverse
