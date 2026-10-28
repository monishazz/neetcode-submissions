class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]   # 1-indexed
            elif total > target:
                r -= 1                  # need a smaller sum
            else:
                l += 1 