# При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
# представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
# A
#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *
# B
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
# C
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *                   *
#     *               *
#       *           *
#         *       *
#           *   *
#             *
# D
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *         *         *
#     *       *       *
#       *     *     *
#         *   *   *
#           * * *
#             *

# Фигура A
height = int(input("Введите высоту фигуры A: "))
weight = height * 2 - 1

for h in range(height):
    for w in range(weight):
        if h == height - 1:
            print('*', end=" ")
            continue
        if h + w == height - 1 or w - h == height - 1:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()

# Фигура В
height = int(input("Введите высоту фигуры В: "))
weight = height * 2 - 1

for h in range(height):
    for w in range(weight):
        if h + w <= height - 2 or w - h >= height:
            print(' ', end=" ")
            continue
        print('*', end=" ")
    print()

# Фигура C
height = (int(input("Введите высоту фигуры C:"))) // 2 + 1
weight = height * 2 - 1

for h in range(height):
    for w in range(weight):
        if h + w <= height - 2 or w - h >= height:
            print(' ', end=" ")
            continue
        print('*', end=" ")
    print()
for h in range(1, height):
    for w in range(weight):
        if h == w or h + w == weight - 1:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()

# Фигура D
height = (int(input("Введите высоту фигуры D: "))) // 2 + 1
weight = height * 2 - 1

for h in range(height):
    for w in range(weight):
        if h + w <= height - 2 or w - h >= height:
            print(' ', end=" ")
            continue
        print('*', end=" ")
    print()
for h in range(1, height):
    for w in range(weight):
        if h == w or h + w == weight - 1 or w == height - 1:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()
