class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # get a dict for every anagram in the list based on anagram dict
        grouped_dict = {}

        # init empty list
        ls = []
    
        # isolate each string into anagram
        for s in strs:
            str_dict = {}
            # update the string dictionary
            for i in range(len(s)):
                str_dict[s[i]] = 1 + str_dict.get(s[i], 0)

            key = tuple(sorted(str_dict.items()))
            print(key)

            if key not in grouped_dict:
                # init new list
                grouped_dict[key] = []
                # add the string
                grouped_dict[key].append(s)
            
            else:
                grouped_dict[key].append(s)


        # with everything in the same dictionary
        ls = list(grouped_dict.values())

        return(ls)        

        
        
        

            
            