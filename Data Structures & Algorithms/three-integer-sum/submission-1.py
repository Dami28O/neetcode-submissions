class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Brute force

        # triplets = []
        # seenSets = []

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if i != j and i != k and j != k:
        #                 total = nums[i] + nums[j] + nums[k]
        #                 if total == 0:
        #                     subarr = [nums[i], nums[j], nums[k]]
        #                     subarr.sort()
        #                     if set(subarr) not in seenSets:
        #                         seenSets.append(set(subarr))
        #                         triplets.append(subarr)

        # return triplets

        # two pointer solution
        # logic order the array and move through linearly fixing an anchor left most and doing two pointers between the remainin

        orderedArr = sorted(nums)
        triplets = []
        seenSets = []

        for i in range(len(orderedArr)):
            anchor = orderedArr[i]
            if anchor > 0:
                break
            l = i + 1
            r = len(orderedArr) - 1
            # two pointer thro remaining subarr
            while l < r:
                # check whether sum = 0
                total = orderedArr[l] + orderedArr[r] + anchor
                if total == 0:
                    subarr = [anchor, orderedArr[l], orderedArr[r]]
                    subarr.sort()
                    if set(subarr) not in seenSets:
                        seenSets.append(set(subarr))
                        triplets.append(subarr)
                    r -= 1 # keep checking

                if total < 0:
                    l += 1
                if total > 0:
                    r -= 1

        return triplets
