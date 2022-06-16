class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)>0:
            minval = min(nums)
            idx = 0
            nums[idx] = minval
            idx += 1
            for e in nums[1:]:
                if e == minval:
                    continue
                if e > minval:
                    nums[idx] = e
                    minval = e
                    idx += 1
            return idx
        else:
            return 0
