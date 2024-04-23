from typing import List

# https://leetcode.com/problems/two-sum/
def twoSum(nums: List[int], target: int) -> List[int]:
    num_dic = {}
    for index in range(len(nums)):
        com = target - nums[index]

        if com in num_dic:
            print(num_dic)
            return [num_dic[com], index]
        num_dic[nums[index]] = index
    return []


res = twoSum([12, 2, 5, 7, 11, 15], 9)
print(res)
