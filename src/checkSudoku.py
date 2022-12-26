def checkSudoku(sudoku):

    assert isinstance(sudoku, list), "la interfaz exige que sudoku debe ser una lista"

    from src.checkSquare          import checkSquares
    from src.checkNumberInRange   import checkNumbersInRange
    from src.checkRows            import checkRows
    from src.checkColumns         import checkColumns
    
    sudokuIsCorrect = checkSquares(sudoku) and checkNumbersInRange(sudoku) and checkRows(sudoku) and checkColumns(sudoku)

    assert isinstance(sudokuIsCorrect, bool)

    return sudokuIsCorrect
