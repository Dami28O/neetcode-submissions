class Solution:
    def search(self, nums: List[int], target: int) -> int:

        r = len(nums) - 1
        l = 0
        m = r // 2

        while True:
            # check the left and right bounds and midpoint
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] == target: 
                return m
            else:
                if nums[m] > target:
                    # update the right bound
                    r = m
                    winSize = r - l
                    m = l + winSize // 2
                else:
                    # update the left bound
                    l = m
                    winSize = r - l
                    m = l + winSize // 2

            if m == l or m == r:
                break
        return -1