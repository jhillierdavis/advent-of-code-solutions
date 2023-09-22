import bingogame
import bingocard
import grid


sample_grid_data = [[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5],[2,0,12,3,7]]

def test_creation_of_bingogame_instance():
    # Given:
    bingo_game = bingogame.BingoGame()

    # Then:
    assert bingo_game

def test_add_bingocard():
    # Given:
    bingo_game = bingogame.BingoGame()
    bingo_card = bingocard.BingoCard(grid.Grid2d(sample_grid_data))

    # When
    bingo_game.addCard(bingo_card)

    # Then:
    assert bingo_game.getNumberOfCards() == 1

    # When: add duplicate card
    bingo_game.addCard(bingo_card)

    # Then: duplicate card is ignored in count
    assert bingo_game.getNumberOfCards() == 1

def test_winning_card_from_sample_data():
    # Given:    
    bingo_card = bingocard.BingoCard(grid.Grid2d(sample_grid_data))
    bingo_game = bingogame.BingoGame()
    bingo_game.addCard(bingo_card)

    # Then: Initially no winning card
    assert bingo_game.hasWinningCards() == False

    # While: no winning number
    for n in [7,4,9,5,11,17,23,2,0,14,21]:
        bingo_game.callNumber(n)
        assert bingo_game.hasWinningCards() == False

    # When: call winning number
    bingo_game.callNumber(24)
    assert bingo_game.hasWinningCards() == True

    # And: winning card has expected score
    list_winning_cards = bingo_game.getWinningCards()
    winning_card = list_winning_cards[0]
    assert sum(winning_card.getUnmarkedNumbers()) == 188

def test_winning_card_from_full_data():
    # Given:    
    bingo_card = bingocard.BingoCard(grid.Grid2d([[17, 40, 97, 51, 57], [92, 25, 38, 26, 23], [32, 44, 83, 87, 49], [54, 74, 33, 7, 12], [14, 36, 30, 8, 98]]))
    bingo_game = bingogame.BingoGame()
    bingo_game.addCard(bingo_card)

    # Then: Initially no winning card
    assert bingo_game.hasWinningCards() == False

    # While: no winning number
    for n in [83,69,34,46,30,23,19,75,22,37,89,78,32,39,11,44,95,43,26,48,84,53,94,88,18,40,62,35,27,42,15,2,91,20,4,64,99,71,54,97,52,36,28,7,74,45,70,86,98,1,61,50,68,6,77,8,57,47,51,72,65,3,49,24,79,13]:
        bingo_game.callNumber(n)
        assert bingo_game.hasWinningCards() == False

    # When: call winning number
    bingo_game.callNumber(17)
    assert bingo_game.hasWinningCards() == True

    # And: winning card has expected score
    list_winning_cards = bingo_game.getWinningCards()
    winning_card = list_winning_cards[0]
    assert winning_card == bingo_card
    assert sum(winning_card.getUnmarkedNumbers()) == 301