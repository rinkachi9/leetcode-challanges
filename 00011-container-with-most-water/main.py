from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            h_l, h_r = height[l], height[r]
            h = min(h_l, h_r)
            best = max(best, h * (r - l))

            if h_l <= h_r:
                l += 1
                while l < r and height[l] <= h_l:
                    l += 1
            else:
                r -= 1
                while l < r and height[r] <= h_r:
                    r -= 1

        return best

solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([0, 1, 1]))
print(solution.maxArea([0, 0, 0]))

assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert solution.maxArea([0, 1, 1]) == 1
assert solution.maxArea([0, 0, 0]) == 0

