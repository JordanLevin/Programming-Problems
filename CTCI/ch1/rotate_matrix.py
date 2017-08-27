def rotate_matrix(mat):
    ret = list(mat)
    for i in range(len(mat)):
        for j in range(len(mat)):
            ret[len(mat)-i][j] = mat[i][j]
    return ret


rotate_matrix([
        [4, 2, 1, 5],
        [3, 1, 6, 8],
        [6, 1, 0, 9],
        [8, 4, 7, 3],
        ])
