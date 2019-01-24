"""BiggestIsland"""
def floodfill(i, j, row, col, island):
    """Return 1 if (i, j) and its neighors are part of the island, 0 otherwise."""
    count = 0
    if island[i][j] == 1:
        count += 1
        island[i][j] = 2
        eightdirections = [(1, 0), (-1, 0), (0, 1), (0, -1),
                           (1, 1), (1, -1), (-1, 1), (-1, -1)]
        newpositions = [(i+x, j+y) for x, y in eightdirections]
        for posx, posy in newpositions:
            if posx in range(0, row) and posy in range(0, col):
                count += floodfill(posx, posy, row, col, island)
    return count

def count_island(row, col, island):
    """Return total number of islands in the map."""
    area = []
    for i in range(row):
        for j in range(col):
            area.append(floodfill(i, j, row, col, island))
    return area

def main():
    """Get input for map and print number of islands."""
    row, col = [int(x) for x in input().split()]
    island = [[int(x) for x in input().split()] for _ in range(row)]
    print(max(count_island(row, col, island)))

main()
