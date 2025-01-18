class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        ans = 0 # initialize ans to zero first 

      # I will use the prefix sum approach to reduce the time complexity of the problem. So we create a list "prefix" and the list starts at index zero of nums. 
        prefix = [nums[0]] 
      # We iterate from nums[1] till nums[n] and as are iterating we add that number to the last element in the prefix sum list. The last element in the prefix sum list is the sum of all the elements in the list. 
      # So after we are done we have a list that has the sum of all elements in nums which we can use for any operation in the future to save time.
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
          
      # Now after creating the list lets solve the question. We initialize i to iterate through the nums list - 1. Why -1? Because we are dividing the nums list to two subarrays and the second subarray should have at least one number and 
      # there should be at least one element to the right of i, thats why element n can never be a subarray alone. 
        for i in range (len(nums) - 1):
          # the sum of left section or subarray is the prefix at i and the sum of the right subarray is the total sum of the prefix minus the sum at index i. Why? Because we want the right subarray's sum to be independent of the left subarray's sum that why 
          # we subtract the total sum from the sum if the left subarray. 
            leftSubarray = prefix[i]
            rightSubarray = prefix[-1] - prefix[i]

          # the constraint of the problem is that a section of a subarray is valid if the left subarray's sum is greater than or equal the right subarray's sum, if thats the case then this is a valid way to split the array into two subarrays. 
            if leftSubarray >= rightSubarray:
                ans += 1
        return ans  

# Time complexity : O(n) ; where n is the length of nums 
# Space complexity : O(n) ; because we create a new array "prefix" of the size of nums which is n 


        
