class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        i = 0
        result = []
        while i < len(nums):
            result.append(math.prod(nums[i+1:] + nums[:i]))
            i +=1
        return result
