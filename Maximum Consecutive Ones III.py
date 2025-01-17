class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
       # initialze the left pointer and curr which is the window and the ans
       # we will be using the sliding window approach
        left = curr = ans = 0 

        # for every right index that enters our window while iterating the whole nums array 
        # if that right index is 0 go ahead and increment the count that we are keeping of zeros in our window to make sure we dont exceed k 
        for right in range(len(nums)):
            if nums[right] == 0 :
                curr += 1
            # if out window became invalid i.e. the count of zeros in our window is more than k which is the number of zeros we can flip per window (subarray) 
            while curr > k:
              # check if the left index is zero in that case remove the left index and update the count of zeros in our window by decrementing the number of zeros in the subarray
                if nums[left] == 0:
                    curr -= 1
                # keep incrementing the left pointer until the window becomes valid again
                left += 1 
            # since we are asked to return the max subarray we need to be keeping count of each subarray in each iteration, if we just returned the answer outside the for loop the program will only return the first valid subarray that meets the conditions of the problem
            # so we keep track of the ans or the subarray at each previous iteration which is ans and the subarray of the iteration which is are at now which is right - left + 1 (the size of any window) and we return the largest or the max of it 
            ans = max(ans, right - left + 1)
        return ans

# Time complexity : O(N) ; where n is the size of the input array nums since we must iterate through it till the end 
# Space complexity: O(1) ; because we just initialzed some variable but no extra stoarge was used to return the max subarray and thats one of the perks of using the sliding window approach
      
             



            
