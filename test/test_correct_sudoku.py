from src.checkSudoku import checkSudoku
from test.casos_test import *
import pytest

@pytest.mark.correct_sudoku

def test_check_square():
    assert checkSudoku(correct) == True
    assert checkSudoku(correct2) == True
    assert checkSudoku(correct3) == True
    assert checkSudoku(correct4) == True