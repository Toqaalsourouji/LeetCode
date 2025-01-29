class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = curr = 0 # start by initializing the two pointers left and right, where left is the start of the window and right is the end of the window. curr is all the elements in window 
        minSum = float("inf") # minSum is initialized to infinity to ensure any valid subarray length will replace it.

        if target > sum(nums): # to handle edgecases where the sum of any window could never be greater than or equal to the target, in this case we return zero  
            return 0
      # we keep expanding the window by adding the elements in the right index to the curr window
        for right in range(len(nums)): 
            curr += nums[right]
          # if the sum of the elements in the window became greater than or equal to target we save that window size to minSum since we are asked in the question to return the number of elements in the window. 
            while curr >= target:
                minSum = min(minSum, right - left + 1) # right-left+1 is the size of any window
                curr -= nums[left] # after we save the size of the window we subtract the left index to continue iterating through nums. 
                # Why? The question is asking for the min size of a window so even if we found a window that has the sum greater than or equal target that doesn't mean that its the window we are looking for. 
                left += 1 # we keep incrementing the left pointer by one       
        return minSum       

# Time complexity: O(n) ; because we iterate through the nums input of size n 
# Space complexity: 0(1) ; no extra storage was needed because we only initialized a few variables thats it
            

        
