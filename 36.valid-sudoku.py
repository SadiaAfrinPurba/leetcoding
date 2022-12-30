#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nrows = len(board)
        ncols = len(board[0])
       
       # case - 1
        for row in range(nrows):
            current_row = board[row]
            storage = set()
            for val in current_row:
                if val not in storage and val != '.':
                    storage.add(val)
                elif val == '.': 
                    continue
                else:
                    return False
        
        # case - 2
        for col in range(ncols):
            col_storage = set()
            for row in range(nrows):
                current_value = board[row][col]
                if current_value not in col_storage and current_value != '.':
                    col_storage.add(current_value)
                elif current_value == '.':
                    continue
                else:
                    return False
        
        # case - 3
        storage = {}
        for row in range(nrows):
            for col in range(ncols):
                current_value = board[row][col]
                if (row // 3, col // 3) not in storage and current_value != '.':
                    storage[(row // 3, col // 3)] = [current_value]
                elif current_value == '.':
                    continue
                elif (row // 3, col // 3) in storage:
                    if current_value in storage[(row // 3, col // 3)]:
                        return False
                    else:
                        storage[(row // 3, col // 3)].append(current_value)

        return True

if __name__ ==  '__main__':
    import numpy as np
    # board = [[".",".","4",".",".",".","6","3","."],
    #         [".",".",".",".",".",".",".",".","."],
    #         ["5",".",".",".",".",".",".","9","."],
    #         [".",".",".","5","6",".",".",".","."],
    #         ["4",".","3",".",".",".",".",".","1"],
    #         [".",".",".","7",".",".",".",".","."],
    #         [".",".",".","5",".",".",".",".","."],
    #         [".",".",".",".",".",".",".",".","."],
    #         [".",".",".",".",".",".",".",".","."]]
        
    board = [[".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".","6",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".","8",".",".",".","."],
             ["9",".",".",".","7","5",".",".","."],
             [".",".",".",".","5",".",".","8","."]
             ,[".",".","9",".",".",".",".",".","."],
             ["2",".","6",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]


    res = Solution().isValidSudoku(board)
    print(res)
        
# @lc code=end

