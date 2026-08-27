class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1

        maxA = 0
        while l < r:
            # compute current area
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height

            # update maxA
            maxA = max(maxA, area)

            # update by shifting the smallest value inward
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return maxA