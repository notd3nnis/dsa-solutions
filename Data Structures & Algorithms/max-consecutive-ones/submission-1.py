class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cont = 0
        prev = 0
        for num in nums:
          if num == 1:
             cont += 1
          else:
             cont = 0 
          prev = max(prev, cont)
        return prev