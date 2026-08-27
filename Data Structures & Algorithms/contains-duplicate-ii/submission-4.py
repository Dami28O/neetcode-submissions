class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        subArr = []

        for i, val in enumerate(nums):
            if i < k:
                if val in subArr:
                    # duplicate found
                    return True
                # add to the subarr
                subArr.append(val)
            else:
                # check for duplicates within the fixed window
                if val in subArr:
                    return True

                # drop the earliest value
                if len(subArr) >= k and len(subArr) > 0:
                    subArr.pop(0)
                    
                subArr.append(val)

        return False
                
