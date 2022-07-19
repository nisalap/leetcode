class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                if i != hashMap[complement]:
                    return [i, hashMap[complement]]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    output.append(i)
                    output.append(j)
                    return output
