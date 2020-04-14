import math
import sys


def main(radius):
    # make the grid base time 2*radius

    grid = []
    for i in range((radius*2)+1):
        grid.append([])
        for j in range((radius*2)+1):
            grid[i].append(0)

    for r in range(len(grid)):
        for c in range(len(grid)):
            x = abs(r - radius)
            y = abs(c - radius)
            dist = math.sqrt(x**2 + y**2)
            if (dist > radius):
                grid[r][c] = ' '
            else:
                grid[r][c] = 'o'

    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end=" ")
        print(' ')


main(int(sys.argv[1]))
