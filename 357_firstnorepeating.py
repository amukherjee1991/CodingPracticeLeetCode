class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):

            if s[i] not in s[:i] and s[i] not in s[i+1:]:

                return i

        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,chr in enumerate(s):
            
            if s.count(chr)==1:
                return i
                break
        return -1