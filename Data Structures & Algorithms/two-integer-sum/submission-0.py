class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # # BRUTE FORCE
        # T = (O^2), S = 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Hashmap Approach
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            # query the map
            if nums[i] in map:
                return [map[nums[i]], i]
            
            # add to hashmap
            map[complement] = i
            
        