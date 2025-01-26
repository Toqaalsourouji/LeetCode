class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # The putpose of the question is to compute the averages of all possible sliding windows of size (2 * k + 1) in the input list nums
        # if a valid sliding window cant be formed for an index the result for that index is -1
        # return a list where each index contains the average of the sliding window centered at that index or -1 if a valid window cant be formed.
     
        # initialize the result array with -1 for all elements
        avgs = [-1] * len(nums)

        # calculate the size of the sliding window
        windowSize = k * 2 + 1

        # if the window size is larger than the nums array length return the initialized result array avgs
        if windowSize > len(nums):
            return avgs

        # calculate the initial window sum for the first valid window then compute the average of that array at index k 
        windowSum = sum(nums[:windowSize])
        avgs[k] = windowSum // windowSize

        # this for loop is used to slide the window across the array and compute averages
        for right in range(windowSize, len(nums)):
            # we update the window sum by subtracting the element leaving the window which is the leftmost element and add the right index to the sum
            windowSum = windowSum - nums[right - windowSize] + nums[right]
            
            # keep updating the average for the center of the current window which is at index right-k
            avgs[right - k] = windowSum // windowSize

        return avgs

# Time Complexity: O(n) ; the initial sum calculation takes O(windowSize), which is O(k * 2 + 1) = O(n) for a large array sliding the window involves O(1) updates for each element,
# iterating through the rest of the array, making it O(n).

# Space Complexity: O(n) ; because the result list `avgs` requires O(n) space.

