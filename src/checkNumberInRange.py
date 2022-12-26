def checkNumbersInRange(sudoku):

    assert isinstance(sudoku, list)

    ValidNumbers = range(1, len(sudoku) + 1)

    for row in sudoku:

      for number in row:

          if not isinstance(number, int) or number not in ValidNumbers:
            
            return False

    return True