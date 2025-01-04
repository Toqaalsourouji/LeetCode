class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3: # since there are two ways to climb the stairs either 1 step of 2 steps , so if n is 1 or 2 just return n 
            return n 
     
        Table = [0 for _ in range(n+1)] # using the tabulation approach ( a dynamic programming bottom-up approach ) i created a table to store the number of ways at each n. I initialized the table with zeros and the size is n+1 because we start the table with n=0
        Table[1] = 1 # = by already knowing that when n=1 the number of ways is to climb the stairs is 1 and the same when n=2, i set the values at n= 1 and 2 
        Table[2] = 2
 
        for i in range(3, n+1): # then for each i starting from n=3 till the end of the table I add the previous 2 numbers and store at that i 
            Table[i] = Table[i-2] + Table[i-1]

        return Table[n] # when the loop is done return the number of ways I can climb the stairs at the input n 

# Time complexity: O(n) because it takes linear time to create the table and loop through the table
# Space complexity: O(n) which is the size of the table

