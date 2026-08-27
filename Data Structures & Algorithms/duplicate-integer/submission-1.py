class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # init an empty dict
        arr_dict = {}

        # iterate over every value
        for i in nums:
            # if already in the dict then it is a duplicate
            if i in arr_dict:
                # update tally
                arr_dict[i] += 1
                return True
            
            # if never seen then append it to the dict
            else:
                arr_dict[i] = 1

            # debug
            print(arr_dict)

        # if we go over each element and have not found a duplicate return false
        return False

        