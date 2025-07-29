from typing import List


class Solution:
    empty = "."

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]  # 3x3 boxes (quadrants), indexed by: (row//3)*3 + col//3

        for row in range(9):
            for col in range(9):
                number = board[row][col]
                if number == self.empty:
                    continue

                # Get box index
                box_index = (row // 3) * 3 + (col // 3)

                # Update counts
                rows[row][number] = rows[row].get(number, 0) + 1
                columns[col][number] = columns[col].get(number, 0) + 1
                boxes[box_index][number] = boxes[box_index].get(number, 0) + 1

                # Check for duplicates
                if rows[row][number] > 1 or columns[col][number] > 1 or boxes[box_index][number] > 1:
                    return False

        return True


solution = Solution()
print(solution.isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(solution.isValidSudoku(
    [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(solution.isValidSudoku(
    [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."],
     [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."],
     [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
