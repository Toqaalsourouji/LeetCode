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
                  

