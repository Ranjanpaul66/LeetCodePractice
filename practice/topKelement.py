from typing import List


class Solution():

    def top_element(self, nums: List[int], k: int) -> List[int]:

        all_list = [[] for i in range(len(nums) + 1)]

        dic = {}
        ans = []
        for el in nums:
            dic[el] = dic.get(el, 0) + 1

        for key, value in dic.items():
            all_list[value].append(key)

        for el in range(len(all_list) - 1, 0, -1):
            for i in all_list[el]:
                ans.append(i)
                if len(ans) == k:
                    return ans


sol = Solution()
print(sol.top_element([1, 2, 3, 1, 2, 5, 4, 2, 3], 2))
