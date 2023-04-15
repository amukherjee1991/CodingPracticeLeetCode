class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = {i: chr(i + 64) for i in range(1, 27)}
        result = ""  
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            result = mapping[remainder + 1] + result
            columnNumber = (columnNumber - 1) // 26
        
        return result