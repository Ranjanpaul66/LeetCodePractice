from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_mul, r_mul = 1, 1
        l_list = [0] * n
        r_list = [0] * n
        # l = [1,
        for i in range(n):
            j = -i - 1
            l_list[i] = l_mul
            r_list[j] = r_mul
            l_mul = l_mul * nums[i]
            r_mul = r_mul * nums[j]

        return [l * r for l, r in zip(l_list, r_list)]


sol = Solution()
print(sol.productExceptSelf([10,2,13,4]))
