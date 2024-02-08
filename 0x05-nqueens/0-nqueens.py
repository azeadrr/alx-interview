#!/usr/bin/python3
"""N queens"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)


def resolve_mrx_for(queen, mrx, pos):
    """
    N queens
    """
    pos.append(queen)

    for cell in mrx[:]:
        if any([cell == queen, cell[0] == queen[0], cell[1] == queen[1],
                cell[0] - cell[1] == queen[0] - queen[1],
                cell[0] + cell[1] == queen[0] + queen[1]]):
            mrx.pop(mrx.index(cell))

    if len(mrx) == 0:
        if len(pos) == N:
            print(pos)
        return

    for possible_queen_pos in [cell for cell in mrx
                               if cell[0] == mrx[0][0]]:
        resolve_mrx_for(possible_queen_pos, mrx[:], pos[:])


for i in range(N):
    resolve_mrx_for([0, i], [[x, y] for x in range(N)
                       for y in range(N)], [])
