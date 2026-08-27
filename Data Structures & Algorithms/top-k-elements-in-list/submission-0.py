class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        arr = list(map.items())

        # sort by value
        arr.sort(reverse = True, key=lambda x: x[1])

        res = [val[0] for i, val in enumerate(arr) if i < k]
        return res