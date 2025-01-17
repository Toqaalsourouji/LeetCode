class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # initialize the left pointer to index 0 and the answer to 0
        # also the curr which is the current window should be 1 because we are multiplying each right index we add to the window to the current window and multiplying anything with 0 will remain 0. 
        left = ans = 0 
        curr = 1 

       # handle edge cases where k is zero or if k is 1 and the nums array is all 1s 
        if k <= 1:
            return 0     
            
        # logic of our sliding window, for every new right index we put in our window, multiply that int to what is in curr
        for right in range(len(nums)):
            curr *= nums[right]
          # the logic to handle when our window becomes invalid, the question wants us to return the subarray that has a product strictly less than k, so if curr becomes greater than ir equal k 
          # start dividing the first left index and keep incrementing the left pointer until we are out of the while loop
            while curr >= k:
                curr //= nums[left]
                left += 1
          # when done, return the answer which is the amount of all the valid windows (subarrays) found and thats why i said ans += the size of the window 
            ans += right - left + 1
        return ans            

# Time complexity : O(N) ; the size of nums that we iterate through 
# Space complexity: O(1) ; no extra storage was needed 
