class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for n in nums:
            if n in seen_set:
                return True
            seen_set.add(n)
        return False
