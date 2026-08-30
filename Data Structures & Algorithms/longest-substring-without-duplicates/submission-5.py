class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # --- optimal ---

        last_index = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in last_index:
                l = max(l, last_index[s[r]] + 1)
            last_index[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest


            # if s[r] not in last_index or last_index[s[r]] < l:
            #     longest = max(longest, r - l + 1)
            # elif s[r] not in last_index:
            #     last_index[s[r]] = r
            # else:
            #     l = last_index[s[r]]

        return longest

        # --- good but not optimal ---

        # window = set()
        # longest = 0
        # l = 0
        # for r in range(len(s)):
        #     if s[r] not in window:
        #         longest = max(longest, r - l + 1)
        #         window.add(s[r])
        #     else:
        #         while s[r] in window:
        #             window.remove(s[l])
        #             l += 1
        #         window.add(s[r])

        # return longest
