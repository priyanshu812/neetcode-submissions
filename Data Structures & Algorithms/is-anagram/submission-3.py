class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        else :
            sd = {}
            td = {}
            for i in s :
                if i in sd :
                    sd[i] += 1 
                else :
                    sd[i ] = 1

            for i in t :
                if i in td :
                    td[i] += 1
                else :
                    td[i] = 1

            if sd == td :
                return True 
            else:
                return False 
                

        