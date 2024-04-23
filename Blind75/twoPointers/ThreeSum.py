from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while(left < right):
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    result.update([nums[left], nums[right], nums[i]])
                    break
                elif sum > 0:
                    right = right-1
                else:
                    left = left+1
        return result
sol = Solution()
sol.threeSum([-1,0,1,2,-1,-4])