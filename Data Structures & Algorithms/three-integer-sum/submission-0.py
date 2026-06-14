class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # ✅ Sort first!
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates for fixed element!
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    # Skip duplicates for j and k!
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1  # ✅ Need bigger sum!
                else:
                    k -= 1  # ✅ Need smaller sum!

        return result
