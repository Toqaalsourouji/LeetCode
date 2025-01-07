class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
     maxWords = 0 # create an integer and initialize to zero to keep track of the max numbers of words in a string

     for str in sentences: # iterate through every string in the input list and for every string split the string to words and keep track of the word count by maxWords 
        maxWords = max(maxWords, len(str.split())) # we use the max function to make sure that the maxWords can be found in any string not only the last. If we didnt use the max function we will return the word count of 
       # the last string only

     return maxWords  # after the loop ends return the count


# Time complexity : O(n) ; n being the strings we iterate through 
# Space complexity : O(1) ; since we are not using any storage that increases as the input increase so the space is constant 

