class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = j = 0 # create two points and they both will start at the first index of both strings s and t
      
        while i < len(s) and j < len(t): # we will move through the strings 
          # if we found a match or in other words we found a char in string s that is also in string t we increment i, if no match or a match happened we will increment j regardless
            if s[i] == t[j]:
                i += 1
            j += 1    

       # we are expected to return a boolean, however in python, this expression returns boolean. So I am checking when the loop ends and we reached the last char in s or the end of string s, meaning that we found s in t, python returns true. Else false
        return i == len(s)

# Time complexity : O(n) ; assuming that n = n which is the len of s + m which is the len of t 
# Space complexity : O(1) ; constant space regardless of the input size
           
        
