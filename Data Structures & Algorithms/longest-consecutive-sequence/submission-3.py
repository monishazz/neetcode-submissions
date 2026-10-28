class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        if len(nums) == 0 : return 0
        longest = curr = 1
        for i in range(1,len(num)):
            if num[i] == (num[i-1] + 1):
                curr += 1
            else: curr = 1
            longest = max(longest,curr)
        return longest