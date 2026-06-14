class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
        return max_sum

        