class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        for num in nums:
            count_hash[num] = count_hash.get(num, 0) + 1
        sorted_nums = sorted(count_hash, key= lambda x : count_hash[x], reverse = True)
        return sorted_nums[:k]
        
