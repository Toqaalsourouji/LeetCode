class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # first check if the input list of strings is empty, if yes return empty string
        if len(strs) == 0:
            return ""

        # now we will start iterating the list by first going through the first string in the list strs[0]. Why? Because its LCP problem so we must find any common chars between the first string and the rest of the strings
        for i in range(len(strs[0])):
            char = strs[0][i] # for each char i in the first string in the list str[0] , save the value in char because we will use it later to compare
            for string in strs: #since we are done with the first string its time to iterate through the rest of the strings in the strs list
              if i == len(string) or string[i] != char: # while iterating we are checking two conditions, 
              # 1) if the length of the string i am at now is shorter than strs[0], if yes we stop the loop at the shortest string, if we didn't we could get out of index error
              # 2) we check if the string we are at now at index i is not equal to the index i at the first string which means we started to get mismatching chars so the LCP ended
                return strs[0][:i] # if any of the cases happened, we slice the first string from the begining till the mismatch or the shorted string len 
        return strs[0] # if none of the conditions/operations happened, return the first string because its the LCP. 


      # Time Complexity: O(N*M) ; where N is the number of strings in the list and M is the len of the shortest string in the list. Why M is the len of the shortest string? Because if we found the shortest string we exist the loop bec the LCP that we have is at this point
      # will never be longer that the LCP we have at the shortest string.
      # Space Complexity: O(1) 
            
   

            
