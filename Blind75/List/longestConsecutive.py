from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for i in num_set:
            if i-1 not in num_set:
                length = 1
                while(i+length) in num_set:
                    length +=1
                longest = max(longest, length)
        return longest

sol = Solution()
print(sol.longestConsecutive([1,0,0,3,7,2,55,8,4,6,0,1]))
# print(sol.longestConsecutive([100,4,200,1,3,2]))
# print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
