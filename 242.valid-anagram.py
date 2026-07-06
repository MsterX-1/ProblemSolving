#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_from_s = set()
        seen_from_t= set()
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            if s[i] not in seen_from_s:
                seen_from_s.add(s[i])
                map_s[s[i]] = 1
            else:
                map_s[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in seen_from_t:
                seen_from_t.add(t[i])
                map_t[t[i]] = 1
            else:
                map_t[t[i]] += 1

        return map_t == map_s      
    

# smart solution 
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         for n in set(s):
#             if s.count(n) == t.count(n):
#                 continue
#             else:
#                 return False
#         return True
# @lc code=end

