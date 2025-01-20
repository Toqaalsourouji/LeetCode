class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Initialize a list prefix with the first element of nums to store the cumulative sum of the array as we iterate.
        prefix = [nums[0]]

        # Iterate through the nums array starting from the second element and for each element, calculate the cumulative sum and append it to prefix.
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        # Find the minimum value in the prefix sum list so we can use it to determine the lowest step-by-step total.
        minPrefixsum = min(prefix)

        # If the minimum prefix sum is already greater than or equal to 1 this means the startValue can be 1, as all step-by-step sums will be valid
        if minPrefixsum >= 1:
            return 1 

        # else calculate the minimum positive startValue needed. To make the smallest step-by-step sum equal to 1, we need startValue = 1 - minPrefixsum.
        startValue = 1 - minPrefixsum   
        return startValue

# Time Complexity: O(n) ;  the for loop iterates through the nums array once which is O(n) and calculating min(prefix) also takes O(n) since it iterates through the prefix list so overall we have O(n) + O(n) = O(n) 
# Space Complexity: O(n) ; prefix list is used to store the cumulative sums requires O(n) space.
      
