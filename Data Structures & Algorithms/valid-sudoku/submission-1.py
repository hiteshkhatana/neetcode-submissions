class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = {}
        for ir,row in enumerate(board):
            temp[ir] = []
            for ic,col in enumerate(row):
                if (ir == 0 and ic == 0) or (ir == 0 and ic == 3) or (ir == 0 and ic == 6) or \
                (ir == 3 and ic == 0) or (ir == 3 and ic == 3) or (ir == 3 and ic == 6) or \
                (ir == 6 and ic == 0) or (ir == 6 and ic == 3) or (ir == 6 and ic == 6):
                    temp[f"cube-{ir}-{ic}"] = []
                if col == ".":
                    continue
                if col in temp[ir]:
                    return False

                temp[ir].append(col)
                if f"col-{ic}" not in temp.keys():
                    temp[f"col-{ic}"] = [col]
                else:
                    if col in temp[f"col-{ic}"]:
                        return False
                    temp[f"col-{ic}"].append(col)

                if ir < 3 and ic < 3: 
                    cr = 0
                    cc = 0
                elif ir < 6 and ic < 3: 
                    cr = 3
                    cc = 0
                elif ir < 9 and ic < 3: 
                    cr = 6
                    cc = 0
                elif ir < 3 and ic < 6: 
                    cr = 0
                    cc = 3
                elif ir < 6 and ic < 6: 
                    cr = 3
                    cc = 3
                elif ir < 9 and ic < 6: 
                    cr = 6
                    cc = 3
                elif ir < 3 and ic < 9: 
                    cr = 0
                    cc = 6
                elif ir < 6 and ic < 9: 
                    cr = 3
                    cc = 6
                elif ir < 9 and ic < 9: 
                    cr = 6
                    cc = 6
                if col in temp[f"cube-{cr}-{cc}"]:
                    return False
                temp[f"cube-{cr}-{cc}"].append(col)

        return True
                
            