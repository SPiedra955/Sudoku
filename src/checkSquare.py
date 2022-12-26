def checkSquares(sudoku):

	assert isinstance(sudoku, list)

	sudokuIsCorrect = True
	number_of_rows = len(sudoku)

	for row in sudoku:
		
		if len(row) != number_of_rows:
			sudokuIsCorrect = False
			break

	assert isinstance(sudokuIsCorrect, bool)

	return sudokuIsCorrect