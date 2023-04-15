class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list=s.split()
        ctr=0
        for char in s_list[-1]:
            ctr+=1
        return ctr