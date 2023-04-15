class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        for char in s:
            if char.isalnum():
                str+=char.lower()
        return str==str[::-1]