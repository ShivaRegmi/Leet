class Solution:
    def addDigits(self, num: int) -> int:
        while num == 0:
            return 0
        return 1 + (num -1)%9
    
        

# this is concept of digital roots.
        