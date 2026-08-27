class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # sort the numbers
        numbers.sort()

        l = 1
        r = len(numbers)

        while l < r:
            
            num_sum = numbers[l - 1] + numbers[r - 1]

            if num_sum == target:
                return [l, r]
            elif num_sum < target:
                l += 1
            else: 
                r -= 1
        