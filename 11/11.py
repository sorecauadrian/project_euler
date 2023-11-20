class Grid:
  def __init__(self, file_name : str = "input_file.txt",  rows : int = 20, columns : int = 20, adjacent_numbers : int = 4):
    self._data = self.store_file_grid(file_name)
    self._rows = rows
    self._columns = columns
    self._adjacent_numbers = adjacent_numbers
    
  def store_file_grid(self, file_name):
    grid = open(file_name, "r").readlines()
    data = []
    for row in grid:
      gridLine = row.split()
      dataLine = []
      for column in gridLine:
        dataLine.append(int(column))
      data.append(dataLine)
    return data

  def max_product(self):
    maximum = 0

    # horizontal maximum
    for row in range(self._rows):
      for column in range(self._columns - self._adjacent_numbers + 1):
        product = self._data[row][column] * self._data[row][column + 1] * self._data[row][column + 2] * self._data[row][column + 3]
        if product > maximum:
          maximum = product
    
    # vertical maximum
    for row in range(self._rows - self._adjacent_numbers + 1):
      for column in range(self._columns):
        product = self._data[row][column] * self._data[row + 1][column] * self._data[row + 2][column] * self._data[row + 3][column]
        if product > maximum:
          maximum = product

    # diagonally maximum
    for row in range(self._rows - self._adjacent_numbers + 1):
      for column in range(self._columns - self._adjacent_numbers + 1):
        product = self._data[row][column] * self._data[row + 1][column + 1] * self._data[row + 2][column + 2] * self._data[row + 3][column + 3]
        if product > maximum:
          maximum = product

    for row in range(self._rows - 1, self._adjacent_numbers - 2, -1):
      for column in range(0, self._columns - self._adjacent_numbers + 1):
        product = self._data[row][column] * self._data[row - 1][column + 1] * self._data[row - 2][column + 2] * self._data[row - 3][column + 3]
        if product > maximum:
          maximum = product

    return maximum

  def print_data(self):
    for line in self._data:
      print(line)

if __name__ == "__main__":
  grid = Grid()
  print(grid.max_product())