#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(0,len(nums)):
            if nums[i] in d and abs(d[nums[i]]-i) <= k:
                return True
            d[nums[i]]= i
        return False    
# @lc code=end

