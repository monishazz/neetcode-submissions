class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num , 0) + 1
        result = sorted(freq_dict, key=freq_dict.get, reverse=True)
        return result[:k]
        
        