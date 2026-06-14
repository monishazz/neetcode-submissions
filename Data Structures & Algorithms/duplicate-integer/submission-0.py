class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = dict()
        for i in set(nums):
            count_dict[i] = 0
        for i in nums:
            count_dict[i] += 1
        for j in count_dict.values():
            if j >= 2:
                return True
        return False
