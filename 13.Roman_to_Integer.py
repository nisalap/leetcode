class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'E': 4, 'F': 9, 'G': 40, 'H': 90, 'J': 400,                      'K': 900}
        val = s[::-1].replace("VI", "E").replace("XI", "F").replace("LX", "G").replace("CX", "H").replace("DC", "J").replace("MC", "K")[::-1]
        sum = 0
        for each in val:
            sum += values[each]
        return sum
