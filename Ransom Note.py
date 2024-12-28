class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        if len(magazine) < len(ransomNote): #because if the magazine count is less than ransom note then we can never create the note from magazine
            return false

        magazineCount = Counter(magazine)  #use counter object as our dictionary to keep track of the frequency of char in magazine, i.e. the count of each character

        for char in ransomNote:  #we loop around each char in ransomnote and check the counter 
            if magazineCount[char] > 0: #we we found the char and the count of that char in the Counter is greater than 0 then we match the characters and we make sure to decrement the char count from the counter
                magazineCount[char] -= 1
            else :
                return False #else we return false 
        return True        
                  
# Time complexity = O(n + m) ; n being the number of char in ransomNote and m being the number of char in magazine
# Space complexity = O(1) : since the max num of char will be 26 because we only care about lowercase char so its a constant. Its important to note that the space complexity in general is supposed to be O(k) where k 
# is the number of distinct char in magazine however because the question put a constraint that magazine must be in lowercase so we know it can only have 26 distinct chars that is why its constant.
