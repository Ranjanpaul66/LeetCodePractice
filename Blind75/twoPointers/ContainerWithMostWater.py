from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        length = len(height)
        # mid_point = 0
        # if len(height)//2 == 0:
        #     mid_pont = length//2
        # else:
        #     mid_pont = length // 2+1
        left_pointer = 1
        right_pointer = length-2

        left_value = height[0]
        right_value = height[length-1]


        while(left_pointer<right_pointer):
            if left_value < height[left_pointer]:
                left_value = height[left_pointer]

            else:
                left_value = left_value
            left_pointer += 1

            if right_value > height[right_pointer]:
                right_value = height[right_pointer - 1]

            else:
                right_value = right_value


