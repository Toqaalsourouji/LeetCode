class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Initialize a list 'runningSum' with the first element of 'nums'. This will be the base case since the running sum at index 0 is just nums[0].
        runningSum = [nums[0]]

        # Iterate through the 'nums' list starting from index 1 to calculate the running sum. We start from index 1 because the first element is already handled during initialization.
        for i in range(1, len(nums)):
            # We then add the current element of 'nums[i]' to the last element in 'runningSum' (which is the running sum up to the previous index).
            # append the result to the 'runningSum' list.
            runningSum.append(nums[i] + runningSum[-1])
          
        return runningSum


# Time Complexity: O(N) ; where n is the length of nums because we iterate through the list once.
# Space Complexity: O(N) ; because we create a new list runningSum of the same size as nums.
