class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        sorted_nums = sorted(hash, key=hash.get, reverse=True)
        return sorted_nums[:k]