def latice_paths(dimension : int = 20):
    matrix = [[-1 for i in range(dimension + 1)] for j in range(dimension + 1)]
    for i in range(dimension + 1):
      matrix[i][0] = matrix[0][i] = 1
    for i in range(1, dimension + 1):
       for j in range(1, dimension + 1):
          matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[dimension][dimension]

if __name__ == "__main__":
    print(latice_paths())