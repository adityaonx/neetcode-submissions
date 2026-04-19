class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows=set()
            cols=set()
            for j in range(9):
                row=board[i][j]
                if row!=".":
                    if row in rows:
                        return False
                    rows.add(row)
            for j in range(9):
                col=board[j][i]
                if col!=".":
                    if col in cols:
                        return False
                    cols.add(col)
        for i in range(0,9,3):
            for j in range(0,9,3):
                boxes=set()
                for r in range(i,i+3):
                    for c in range(j,j+3): 
                        box=board[r][c]
                        if box!=".":
                            if box in boxes:
                                return False
                            boxes.add(box)
        return True

                
