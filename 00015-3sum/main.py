from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res


solution = Solution()

print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 1, 1]))
print(solution.threeSum([0, 0, 0]))

assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1,-1,2],[-1,0,1]]
assert solution.threeSum([0, 1, 1]) == []
assert solution.threeSum([0, 0, 0]) == [[0,0,0]]

