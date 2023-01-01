#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
import copy
from functools import reduce
from operator import mul
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        res = [1] * len(nums)

        # calculate prefix product
        prefix = 1
        for idx in range(len(nums)):
            res[idx] = prefix
            prefix *= nums[idx]

        postfix = 1
        for idx in range(len(nums) -1, -1, -1):
            res[idx] *= postfix
            postfix *= nums[idx]

        return res


# @lc code=end

