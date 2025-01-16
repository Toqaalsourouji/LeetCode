class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = curr = 0 
      
        # Logic to create the first window of size k and sum all the integers in that windows and assign to ans
        for i in range(k): 
            curr += nums[i]
        ans = curr 

      # Logic to keep iterating through nums to find new subarray or windows bu simply adding the element on the right and subtracting the element at i-k which is the left index of curr window
        for i in range(k , len(nums)):
            curr += nums[i] - nums[i-k]
          # while iterating keep updating the sum of curr and use the max function to retunn the max sum of all the subarrays in nums array 
            ans = max(ans, curr)
       # Since we want to return the average and not the sum only we simply divide the sum by the number of elements in the subarray which is k 
        return ans / k 

# Time complexity: O(n) ; because we are iterating through nums only where n is the len of nums 
# Space complexity: O(1) ; because no extra space was used 

