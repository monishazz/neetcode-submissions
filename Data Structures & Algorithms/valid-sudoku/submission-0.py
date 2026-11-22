class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        subgrid = [[set() for i in range(3)] for i in range(3)]
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == '.':
                    continue
                if num in rows[row]:
                    return False
                if num in columns[column]:
                    return False
                if num in subgrid[row // 3][column // 3]:
                    return False
                rows[row].add(num)
                columns[column].add(num)
                subgrid[row // 3][column // 3].add(num)
        return True
        