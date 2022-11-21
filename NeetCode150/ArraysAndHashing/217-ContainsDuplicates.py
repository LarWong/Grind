from typing import List

def solution(nums: List[int]) -> bool:
    # Runtime: O(n)
    # Space: O(n)
    check = set()
    for n in nums:
        if n in check:
            return True
        check.add(n)
    return False
