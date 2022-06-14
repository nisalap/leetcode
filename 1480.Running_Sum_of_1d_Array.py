class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        res = []
        for each in nums:
            sum += each
            res.append(sum)
        return res
