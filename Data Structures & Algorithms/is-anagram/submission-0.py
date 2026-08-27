class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # iterate over each into a dict 
        s_dict = {}
        t_dict = {}

        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else: 
                s_dict[c] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else: 
                t_dict[i] = 1

        if s_dict != t_dict:
            return False
        else:
            return True