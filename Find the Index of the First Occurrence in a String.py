class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack) #the length of string haystack
        m = len(needle) #the length of string needle

        for i in range (n-m+1): # outer loop to iterate through the whole string of haystack. Why n-m+1? Ex: if n=8 and m=3 , then n-m = 8-3= 5 however we actually have 6 indexes in haystack to check not only 5 thats why we add +1
            for j in range (m): #inner loop to check if the chars of size m provided from haystack are equal to needle or not
                if needle[j] != haystack[i + j]: # if not equal break and wait for another subset of char from haystack of size m 
                    break 
            else: #if we finally sound the subset of size m in haystack that matches the needle return the index of that occurance since we are only looking for the first occurance
                return i
                    
        return -1  #if we went through the haystack string and didn't find any match return -1      

                    
