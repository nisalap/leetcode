class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(99999)
        nums.sort()
        c = 1
        for i in range(len(nums)-1):
            print(c)
            if nums[i] != nums[i + 1]:
                if c == 1:
                    return nums[i]
                else:
                    c = 1
            else:
                c += 1
