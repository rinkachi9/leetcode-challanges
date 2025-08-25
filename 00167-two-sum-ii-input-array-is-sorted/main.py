from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
        return []

solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([-1, 0], -1))
print(solution.twoSum([5,25,75], 100))
print(solution.twoSum([1,2,3,4,4,9,56,90], 8))

assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert solution.twoSum([2, 3, 4], 6) == [1, 3]
assert solution.twoSum([-1, 0], -1) == [1, 2]
assert solution.twoSum([5,25,75], 100) == [2, 3]
assert solution.twoSum([1,2,3,4,4,9,56,90], 8) == [4, 5]

