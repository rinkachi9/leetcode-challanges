from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNum = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        mostFrequents = []

        for index in range(k):
            mostFrequents.append(sortedNum[index][0])

        return mostFrequents


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent([1], 1))
