triangles = [
    [3, 4, 5],
    [1, 2, 2],
    [6, 8, 10],
    [5, 5, 5],
    [7, 10, 12],
    [4, 5, 6],
    [2, 3, 4],
    [8, 15, 17],
    [9, 9, 12],
    [10, 11, 13]
]


def square(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    return s ** 0.5


def generate_areas(triangles):
    areas = []
    for t in triangles:
        areas.append(square(t[0], t[1], t[2]))
    return areas


def find_max(areas):
    return areas.index(max(areas))


areas = generate_areas(triangles)
i = find_max(areas)

print("Наибольший треугольник:", triangles[i])
print("Его площадь:", areas[i])