import math
from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total_mult = 1
        number_of_zeros = 0
        for num in nums:
            if num == 0:
                number_of_zeros += 1
            else:
                total_mult *= num

        if number_of_zeros > 1:
            for i in range(len(nums)):
                result.append(0)
        elif number_of_zeros == 1:
            for num in nums:
                if num == 0:
                    result.append(total_mult)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(total_mult // num)

        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3]))
print(solution.productExceptSelf([1, 2, 3, 1]))
print(solution.productExceptSelf([1, 2, 3, 4]))
