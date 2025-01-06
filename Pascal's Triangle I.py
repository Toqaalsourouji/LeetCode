class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
      Triangle = [[] for _ in range(numRows)] # an empty list with the size of the input numRows 

      if numRows <= 1: # this if statement handles edge cases like if numRows is equal to 1 or 0 
        return [[1]] * numRows

      for rows in range (numRows): # the outerloop focuses on creating a "rows" for each n in the input numRows
        row = [None for _ in range(rows+1)] # then for each "rows" we created a list of size rows + 1 by the name "row" 
        row[0] , row[-1] = 1, 1 # since pascal's triangle has 1 in the first and last position in a row, we handle this case here
        
        for j in range(1, len(row)-1): # the innerloop handles the filing of positions in each row that isn't the first or last position. 
        # we fill them by using the logic of pascal's triangle which is adding the 2 numbers directly above the block we want to get the value for. Using tabulation I created this formula. At any block I want to calculate
        # lets say block j, i go to the previous row and at the 2 blocks directly above j, I add them and fill block j with the value of the addition
         row[j] = Triangle[rows-1][j-1] + Triangle[rows-1][j]

        Triangle[rows] = row # after calculating each row append to the traingle list so we can return the list of lists when we are done with the loop
        
      return Triangle # return the result

# Time Complexity: O(n^2) ; because we create each row of the triangle of size n and we fill the positions in each row which are n positions so we have n*n which is n^2
# Space Complexity: O(n^2) ; the same because we need n*n storage to store and the rows and positions of the triangle

