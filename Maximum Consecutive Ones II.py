class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
      # Using the sliding window method, we initialized our left pointer and the current window that keeps track of how many zeros are in that window and the ans to zero
        left = curr = ans = 0 
       # We iterate through the input and if the new element that got added in the window is 0, we increment the count of zeros in curr
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1 
        # The window becomes invalid if we have more than one zero in our window so we check if thats the case. If we have more than one zero we start decrementing the curr window count by one using the left pointer. 
          # We keep iterating or incrementing the left pointer until the window becomes valid again i.e. we have one zero or no zeros in the window 
            while curr > 1:
                if nums[left] == 0:
                    curr -= 1 
                left += 1 
           # Finally after finishing the for loop or iterting through the whole input we return the max which is either ans = 0 if we didnt find the subarray we are looking for or the size of the window which is right - left + 1 because its zero indexed 
            ans = max (ans, right - left + 1)
        return ans            

# Time complexity : O(n) ; where n is the length of nums, as the work done in each loop iteration is amortized constant 
# Space complexity : O(1) ; because we used three interger variables and no extra space is needed
