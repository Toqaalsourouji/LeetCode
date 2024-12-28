class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #created a hashmap to keep track of the numbers and their index 
        
        for i, num in enumerate(nums): #enumerate() function is used to loop throught the list and keep track of every index in nums and to return the index and the value
            compliment = target - nums[i] #for every num we calculate the compliment which basically taking that number and subtracting the target from it.

            if compliment in hashmap: # to make our lives easier we take that compliment and check if its in the hashmap, if it is we return the index of that compliment 
                return [hashmap[compliment], i]
            hashmap[num] = i # then we set the integer i which is the index in the list of indexes and return the answer 
