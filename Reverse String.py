class Solution:
    def reverseString(self, s: List[str]) -> None:
      # created two points one staring from the begining of the string and the other from the end
        i = 0 
        j = len(s) - 1
       # keep iterating until i = j meaninf both pointers reached the same char in the string 
       # at each iteration keep swapping the i and j indices together and increment i and decrement j 
      # when the while loop is done at i = j we are done with swapping 
        while i < j:
            s[i] , s[j] = s[j] , s[i]
            i += 1
            j -= 1
          
# Time Complexity : O(N) ; because we are going through the whole string 
# Space Complexity : O(1) ; because we swapped at the same place without using and extra memory 

