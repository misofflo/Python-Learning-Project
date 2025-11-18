import numpy

cars = ["Ford", "Volvo", "BMW"]

tiles = numpy.empty((4, 4), dtype=object)

for i in range(4):
    for j in range(4):
        tiles[i][j] = (i, j)

print(tiles[0][2])