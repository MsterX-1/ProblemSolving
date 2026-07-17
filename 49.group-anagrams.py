#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}

        for word in strs:
            # sort the word to make the key "eat" = key"aet"
            key = "".join(sorted(word))

            if key not in groups:
                # "aet" = []
                groups[key] = []
            # "aet" = ["eat"]
            groups[key].append(word)
        return list(groups.values())    
# @lc code=end

