# Method 1:
class Solution:
    def isPalindrome(self, x: int) -> bool: 
        
        if x < 0: # the question didn't want us to handle negative integers thats why we add this condition
            return False

        reversed_number = int(str(x)[::-1]) # since i am solving this using python, python has the option of slicing , 
        # however, slicing can only be performed on string or lists but never integers thats why I reverted x as a str for the sake of slicing the reverted to int

        if reversed_number == x: # check if the input x is equal to the reversed number, if yes then this number is a palindrome number
            return True 
        else:
            return False    

# Time Complexity : O(Log(X))
# Space Complexity : O(Log(X)), hence not very efficient in the case of large numbers


# Method 2 :
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: # again checking for the same condition
            return False
        
        input_x = x # make sure to set the input x as x because we will change the value of x in the while loop
        reversed_number = 0

        while x > 0: # iterate untill x = 0
            last_digit = x % 10 # extract the last digit of the input x 
            reversed_number = reversed_number * 10 + last_digit # after applying this formula you will always get the reversed number. I didn't see it until I tried it on an example so I suggest you do the same. Else convince yoursef it works
            x = x // 10 # we keep dividing x until we get x = 0 and that when we exit the while loop

        if input_x == reversed_number: # check and return true if the number is a Palindrome number
            return True 
        else: 
            return False   

# Time Complexity : O(Log(X))
# Space Complexitiy : 0(1), good for large number so more efficient
