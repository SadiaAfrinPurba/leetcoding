#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in storage:
                return [storage[complement], i]
            else:
                storage[nums[i]] = i

        
# @lc code=end

