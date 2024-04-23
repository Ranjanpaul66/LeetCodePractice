from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        for i in nums:
            mul = 1
            for j in range(len(nums)):
                if nums[j] != i:
                    mul = mul * nums[j]
            ans.append(mul)
        # print(ans)
        return ans


# sol = Solution()
# print(sol.productExceptSelf([1, 2, 3, 4]))
# print(sol.productExceptSelf([-1, 1, 0, -3, 3]))


# time complexity with O(n)
# https://youtu.be/yKZFurr4GQA
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul = 1
        r_mul = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i - 1
            l_arr[i] = l_mul
            r_arr[j] = r_mul
            l_mul *= nums[i]
            r_mul *= nums[j]

        return [l*r for l, r in zip(l_arr, r_arr)]

sol2 = Solution2()
print(sol2.productExceptSelf([1, 2, 3, 4]))



