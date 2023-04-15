class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Time Complexity O(n)
        Space Complexity O(n)

        '''

        # Sliding window problem
        # using 2 pointer
        # remove from window and set
        charecSet = set()
        left=0
        res=0
        for right in range(len(s)):
            while s[right] in charecSet:
                charecSet.remove(s[left])
                left+=1
            charecSet.add(s[right])
            res = max(res,right-left+1)
        return res
       


            
        