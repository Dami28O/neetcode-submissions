class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLen = 0
        l = 0

        # advance the right pointer
        for r in range(len(s)):

            # check if in our substr
            if s[r] in s[l:r]:
                # forward the left pointer
                while s[r] in s[l:r]:
                    l += 1

            subLen = len(s[l:r + 1])
            maxLen = max(maxLen, subLen)
        
        return maxLen


                
            
        
        