#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        sorted_hash = sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [key for key, value in sorted_hash[:k]]
# @lc code=end

