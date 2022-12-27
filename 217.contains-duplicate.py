#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
                if count[num] == 2:
                    return True
            else:
                count[num] = 1
        return False
        
# @lc code=end

