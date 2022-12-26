from src.checkSudoku import checkSudoku
from test.casos_test import *
import pytest

@pytest.mark.incorrect_sudoku

def test_incorrect_sudoku():
    assert checkSudoku(incorrect) == False
    assert checkSudoku(incorrect2) == False
    assert checkSudoku(incorrect3) == False
    assert checkSudoku(incorrect4) == False
    assert checkSudoku(incorrect5) == False
    assert checkSudoku(irregular) == False
    assert checkSudoku(irregular2) == False