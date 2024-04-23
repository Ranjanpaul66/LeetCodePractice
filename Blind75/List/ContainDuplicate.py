from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    ref_set = set()
    for i in nums:
        if i in ref_set:
            return True
        ref_set.add(i)
    return False

print(containsDuplicate([1,4,5,6,2,3,4]))
