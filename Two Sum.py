class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums):
            compliment = target - nums[i]

            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[num] = i      
