def out(matrix):
    if matrix:
        for i in range(0, len(matrix)):
            print(matrix[i])
    return ''


def gur(A):
    koef = [1]
    k3 = (-A[0][0]*A[1][1]+A[0][1]*A[1][0])*A[2][2]+(A[0][0]*A[1][2]-A[0][2]*A[1][0])*A[2][1]+(-A[0][1]*A[1][2]+A[0][2]*
                                                                                               A[1][1])*A[2][0]
    k2 = ((A[1][1]+A[0][0])*A[2][2]-A[1][2]*A[2][1]-A[0][2]*A[2][0]+A[0][0]*A[1][1]-A[0][1]*A[1][0])
    k1 = -A[0][0] - A[1][1] - A[2][2]
    koef.append(k1)
    koef.append(k2)
    koef.append(k3)

    print("Характеристический полином:")
    signs = []
    sign = "+" if koef[1] > 0 else "-"
    signs.append(sign)
    sign = "+" if koef[2] > 0 else "-"
    signs.append(sign)
    sign = "+" if koef[3] > 0 else "-"
    signs.append(sign)

    print('s^3' + signs[0] + str(abs(koef[1])) + 's^2' + signs[1] + str(abs(koef[2])) + 's' + signs[2] + str(
        abs(koef[3])))
    print('\n')
    matrix = [[koef[1], koef[3], 0], [koef[0], koef[2], 0], [0, koef[1], koef[3]]]
    print("Матрица Гурвица:")
    print(out(matrix))
    if (koef[1] > 0) and (koef[1] * koef[2] - koef[0] * koef[3] > 0) and (koef[3] > 0):
        return "Система устойчива"
    elif (koef[2] > 0) and (koef[1] * koef[2] - koef[0] * koef[3] > 0) and (koef[3] == 0):
        return "Система находится на апериодической границе устойчивости"
    elif (koef[2] > 0) and (koef[1] * koef[2] - koef[0] * koef[3] == 0) and (koef[3] > 0):
        return "Система находится на на колебательной гарнице устойчивости"
    else:
        return "Система неустойчива"


if __name__ == '__main__':
    A = [[0, 1, 1], [0, -5, -5], [-2, 1, 1]]
    print("Матрица А:")
    print(out(A))
    print('\n')
    print(gur(A))
