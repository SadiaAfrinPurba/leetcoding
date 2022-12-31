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
       
        if all(num == 0 for num in nums):
            return nums


        res = [1] * len(nums)

        if 0 in nums:
            copy_nums = copy.deepcopy(nums)

            for idx, num in enumerate(nums):
                if num != 0:
                    res[idx] = 0
                else:
                    copy_nums.remove(0)
                    res[idx] = reduce(mul, copy_nums)
            return res

        res[0] = reduce(mul, nums[1:])
        for idx in range(1, len(nums)):
            res[idx] = (res[idx - 1] * nums[idx - 1]) // nums[idx]

        return res
        
if __name__ == '__main__':
    # Failing case-1: [0, 0]
    # Failing case-2: [0, 4, 0]
    # Learning: think about how to handle zero in computations 
    # of product

    res = Solution().productExceptSelf(nums=[0, 4, 0])
    print(res)

        
# @lc code=end

