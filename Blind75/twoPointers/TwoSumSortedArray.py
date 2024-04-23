from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        total_length = len(numbers)
        left_pointer = 0
        right_pointer = total_length-1

        while left_pointer < right_pointer:
            cur_sum = numbers[left_pointer] + numbers[right_pointer]
            if cur_sum == target:
                return [left_pointer,right_pointer]

            if cur_sum > target:
                right_pointer = right_pointer-1

            if cur_sum < target:
                left_pointer = left_pointer + 1

        return []


solution = Solution()
res = solution.twoSum([1,3,4,5,7,10,11], 9)
res = solution.twoSum([2,7,11,15], 9)
print(res)