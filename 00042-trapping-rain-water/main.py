from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left_index = 0
        right_index = n - 1
        left_max = 0
        right_max = 0
        total_trapped = 0

        while left_index < right_index:
            if height[left_index] <= height[right_index]:
                if height[left_index] >= left_max:
                    left_max = height[left_index]
                else:
                    total_trapped += left_max - height[left_index]
                left_index += 1
            else:
                if height[right_index] >= right_max:
                    right_max = height[right_index]
                else:
                    total_trapped += right_max - height[right_index]
                right_index -= 1

        return total_trapped


solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6