#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = Counter(s)
        freq_t = Counter(t)
        
        count = 0
        for ch in t:
            if ch in freq_s and freq_s[ch] == freq_t[ch]:
                count += 1 

        return count == len(s)
        
    
  
# @lc code=end

