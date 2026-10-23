class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashA = {}
        res =[]

        for i in range(len(nums)):

          if target - nums[i] in hashA:
           res = [hashA[target - nums[i]], i]
          else:
             hashA[nums[i]] = i
        return res      