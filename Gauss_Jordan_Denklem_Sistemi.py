def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end = " ")
        print()

def augmented_matrix_creation(equations):
    augmented = equations[:-1]
    a = 0
    for i in augmented:
        i.append(equations[-1][a])
        a += 1

    return augmented
    
def equation_system_solve(z):
    x = augmented_matrix_creation(z)

    for i in range (len(x)):
        for j in range (len(x) - 1, i, -1):
            multiplier = x[j][i] / x[i][i]
            for k in range (len(x[0])):
                x[j][k] -= multiplier * x[i][k]

    for i in range(len(x) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            multiplier = x[j][i] / x[i][i]
            for k in range(len(x[0])):
                x[j][k] -= multiplier * x[i][k]

    for i in range (len(x)):
        x[i][-1] /= x[i][i]
        x[i][i] /= x[i][i]
    
    print_matrix(x)
    return x

A1 = [1, 2]
A2 = [3, 4]
A_res = [4, 9]

print(equation_system_solve([A1,A2,A_res]))

B1 = [3, 4, 8]
B2 = [1, 6, 2]
B3 = [2, 7, 6]
B_res = [9, 7, 5]

print(equation_system_solve([B1,B2,B3,B_res]))

C1 = [7, 4, 3, 4]
C2 = [6, 2, 5, 6]
C3 = [1, 4, 2, 8]
C4 = [9, 3, 4, 7]
C_res = [14, 13, 4, 11]

print(equation_system_solve([C1,C2,C3,C4,C_res]))