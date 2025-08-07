from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_sorted = sorted(nums)
        longest_sequence = 1
        current_sequence = 1
        for index in range(len(num_sorted) - 1):
            if num_sorted[index] == num_sorted[index + 1]:
                continue
            if num_sorted[index] + 1 == num_sorted[index + 1]:
                current_sequence += 1
                continue
            else:
                if current_sequence > longest_sequence:
                    longest_sequence = current_sequence
                current_sequence = 1

        if current_sequence > longest_sequence:
            longest_sequence = current_sequence

        return longest_sequence

solution = Solution()
print(solution.longestConsecutive([]))
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([1,0,1,2]))