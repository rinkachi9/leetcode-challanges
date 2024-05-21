from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bucket = {}
        for index in range(len(nums)):
            if nums[index] in bucket:
                return True
            else:
                bucket[nums[index]] = True


solution = Solution()
print(solution.containsDuplicate([1, 1, 2]))
print(solution.containsDuplicate([1, 1, 1, 1, 1, 2, 2]))
print(solution.containsDuplicate([1, 1, 1, 1, 1, 2, 2, 3]))
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
