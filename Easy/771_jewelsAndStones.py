class Solution:
    def numJewelsInStones(self, J, S):
        j_dict = list(J)
        numOfJewels = 0
        for c in S:
            if c in j_dict:
                numOfJewels += 1
        return numOfJewels