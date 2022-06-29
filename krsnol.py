def hello():
    print("  Вам предоставляется возможность  ")
    print("      поучаствовать в игре  ")
    print("         крестики нолики  ")
    print("-----------------------------------")
    print("  Выши ходы должны записываться    ")
    print("      в виде координат x и y       ")
    print("           x - строка          ")
    print("           y - столбец         ")



field = [[" "] * 3 for i in range(3)]


def pole():
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")


def move():
    while True:
        crds = input("  Ваш ход: ").split()
        if len(crds) != 2:
            print("  Введите две координаты")
            continue

        x, y = crds

        if not(x.isdigit()) or not(y.isdigit()):
            print("  Введите два числа")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("  Введите координаты в диапозоне от 0 до 2")
            continue

        if field[x][y] != " ":
            print("  В этой клетке уже стоит ход ")
            continue

        return x, y


def winner():
    w_crds = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
              ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
              ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for crd in w_crds:
        sym = []
        for c in crd:
            sym.append(field[c[0]][c[1]])
        if sym == ["X", "X", "X"]:
            print("  Выиграли крестики")
            return True
        if sym == ["0", "0", "0"]:
            print("  Выиграли нолики")
            return True
    return False



hello()
n = 0
while True:
    n += 1
    pole()
    if n == 9:
        print("  Ничья")
        break
    if n % 2 != 0:
        print("  Ходят крестики ")
    else:
        print("  Ходят нолики")

    x, y = move()
    if n % 2 != 0:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if winner():
        break

    if n == 9:
        print("  Ничья")
        break



