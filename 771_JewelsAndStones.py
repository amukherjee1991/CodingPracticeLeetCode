class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d={}
        
        for items in S:
            if items not in d and items in J:
                d[items]=1
            elif items in d and items in J:
                d[items]+=1
        
        count=0
        for k,v in d.items():
            count=count+v
        return count