class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # iterate over each number in the list
        for i in (nums):
            # initialise counter
            count = 0

            # compare to every other number
            for j in nums:
                if i == j:
                    count += 1

            # debug
            print(count)

            if count > 1:
                return True

        return False