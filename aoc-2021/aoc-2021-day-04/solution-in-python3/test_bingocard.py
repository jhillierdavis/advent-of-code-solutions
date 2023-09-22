import bingocard
import grid

sample_grid_data = [[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5],[2,0,12,3,7]]

def test_creation_of_bingo_card_instance():
    # Given:
    bingo_card = bingocard.BingoCard(grid.Grid2d(sample_grid_data))

    # Then:
    assert bingo_card

def test_not_bingo():
    # Given:
    bingo_card = bingocard.BingoCard(grid.Grid2d(sample_grid_data))

    # Then:
    assert False == bingo_card.isBingo()
    
def test_bingo():
    # Given:
    bingo_card = bingocard.BingoCard(grid.Grid2d(sample_grid_data))

    # When: Add number not on card
    assert False == bingo_card.isMatchedNumber(1)

    # When: Add most of 1st row
    assert True == bingo_card.isMatchedNumber(14)
    assert True == bingo_card.isMatchedNumber(21)
    assert True == bingo_card.isMatchedNumber(17)
    assert True == bingo_card.isMatchedNumber(24)
    assert False == bingo_card.isBingo()
    
    # When: Complete 1st row
    assert True == bingo_card.isMatchedNumber(4)

    # Then:
    assert True == bingo_card.isBingo()

def test_unmarked():
    # Given:
    bingo_card = bingocard.BingoCard(grid.Grid2d(sample_grid_data))

    # When: Add 1st row and additional numbers
    assert True == bingo_card.isMatchedNumber(14)
    assert True == bingo_card.isMatchedNumber(21)
    assert True == bingo_card.isMatchedNumber(17)
    assert True == bingo_card.isMatchedNumber(24)
    assert True == bingo_card.isMatchedNumber(4)
    assert True == bingo_card.isMatchedNumber(9)
    assert True == bingo_card.isMatchedNumber(23)
    assert True == bingo_card.isMatchedNumber(11)
    assert True == bingo_card.isMatchedNumber(5)
    assert True == bingo_card.isMatchedNumber(2)
    assert True == bingo_card.isMatchedNumber(0)
    assert True == bingo_card.isMatchedNumber(7)

    # Then:
    unmarked = bingo_card.getUnmarkedNumbers()
    assert sum(unmarked) == 188
