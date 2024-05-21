from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, a in enumerate(nums):
            for idy, b in enumerate(nums):
                if idx == idy:
                    continue
                if a + b == target:
                    return [idx, idy]


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
print(solution.twoSum(nums=[3, 2, 4], target=6))
print(solution.twoSum(nums=[3, 3], target=9))
