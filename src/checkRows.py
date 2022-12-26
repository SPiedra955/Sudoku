def checkRows(sudoku):

    assert isinstance(sudoku, list)

    for row in sudoku:

        for (position, number) in enumerate(row):

            if number in row[position + 1:]:
                return False

    return True