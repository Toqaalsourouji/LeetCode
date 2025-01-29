class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
       # This solution uses prefix sum. Typically, the prefix sum array starts with the first element of the input array,
       # but in this problem, it starts with 0 because the biker begins at altitude 0.
        prefixsum = [0]
      
       # iterate through the input array "gain". For each element gain[i], add it to the last value in the prefixsum array (prefixsum[-1]) and append the result to the prefixsum array.
        for i in range(len(gain)):
            prefixsum.append(gain[i] + prefixsum[-1])
          
      # after constructing the prefixsum array, find and return the maximum altitude (the largest value in prefixsum). 
        highestAltitude = max(prefixsum)
        return highestAltitude

# Time complexity: O(n) ; because we iterate through the input array "gain"
# Space complexity: O(n); the prefixsum array has a size of n + 1 (one extra for the initial 0), but constants are ignored in Big-O notation.
