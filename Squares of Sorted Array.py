class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       # using two points to go through array nums
        i = 0 
        j = len(nums) - 1

      # to handle edge cases where the input nums has only one integer 
        if len(nums) == 1:
            return [nums[i] ** 2]
       # we go through the array nums and square each integer using the two pointers
        while i < j:  
            nums[i] = nums[i] ** 2
            nums[j] = nums[j] ** 2
            i += 1
            j -= 1
           # to handle the case when two pointers are pointing to the same integer in the middle 
            if i == j:
                nums[i] = nums[i] ** 2
        # after we are out of the while loop we sort the array using the .sort() function in python and return the array 
        nums.sort()  
        return nums

# Time complexity : O(N log N) ; because we iterate through the whole nums array which is N and we sort which takes log N
# Space complexity: O(1) ; if we will exclude the output from the calculation because we squared using nums array and sorted without creating any temp arrays
          



        
