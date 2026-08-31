class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # find longest contiguous block of chars allowing up to k 
        # characters that dont contribute to longest substr

        l = 0
        hm = {}         # frequency of characters within the window

        # initialise first character as the target
        # hm[s[l]] = 1
        # # winLen = 1
        # maxLen = 0
        max_len = 0
        max_freq = 0


        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            max_freq = max(max_freq, hm[s[r]])

            # If replacements needed exceed k, shrink the window
            if (r - l + 1) - max_freq > k:
                hm[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len

        # for r in range(1, len(s)):
            
        #     if s[r] == target:
        #         hm[s[r]] += 1
        #         # update window length
        #         winLen = r - l + 1
        #     else:
        #         # if it is not the target then 
        #         # add to hashmap
        #         count = hm.get(s[r], 0)
        #         count += 1
        #         hm[s[r]] = count

        #         # check if we have enough replacements
        #         winLen = r - l + 1

        #         # extract freq of target char in hm
        #         replacements = winLen - hm[target]

        #         if replacements > k:
        #             # shrink the window until we reduce replacements or
        #             # consider a new target
        #             while replacements > k:
        #                 # shift left pointer forward
        #                 hm[s[l]] -= 1
        #                 l += 1
                        
        #                 # update replacements 
        #                 winLen = r - l + 1
        #                 replacements = winLen - hm[target]

        #                 # if the target is no longer the majority 
        #                 # pick the now highest freq and update the target
        #                 if hm[target] < winLen // 2:
        #                     # get a list of key value pairs
        #                     chars = list(hm.items())
        #                     chars.sort(reverse=True, key=lambda x: x[1])
        #                     target = chars[0][0]

        #     # update the longest window length seen so far
        #     maxLen = max(maxLen, winLen)

        # return maxLen    