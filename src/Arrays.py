import numpy

cars = ["Ford", "Volvo", "BMW"]

# iterate over cars and print each one
for car in cars:
    print(car)

tiles = numpy.empty((4, 4), dtype=object)

for i in range(4):
    for j in range(4):
        tiles[i][j] = (i, j)