class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums_r = [i for i in range(0, n+1)]
        return (set(nums_r) - set(nums)).pop()
