"""
    27. Remove Element
    https://leetcode.com/problems/remove-element/description/
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)


Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)  # 5