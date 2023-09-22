import utils
import ast
import grid
import bingocard
import bingogame

def string_value_to_integer_array(string_value):
    str_array = string_value.split(',') # First line
    return [int(i) for i in str_array] # Convert to int array

def get_numbers_to_call_from_file(filename):
    lines = utils.get_file_lines(filename)
    return string_value_to_integer_array(lines[0])

def create_bingocard_from_data(data):
    return bingocard.BingoCard(grid.Grid2d(data))

def get_bingo_cards_from_file(filename):
    lines = utils.get_file_lines(filename)
    bingo_card_list = []
    arr = None
    for i in range(len(lines)):
        if i == 0:
            continue

        if lines[i] == "" or i == len(lines):
            if arr is not None:
                bingo_card_list.append( create_bingocard_from_data(arr))
            arr = [] # Reset           
        else:
            values = lines[i].strip().replace(' ', ',')
            values = values.replace(',,', ',')
            arr.append(ast.literal_eval('[%s]' % values))

    bingo_card_list.append( create_bingocard_from_data(arr))
            
    return bingo_card_list


def get_winning_board_final_score_from_file(filename):
    print(f"DEBUG: filename={filename}")

    number_list = get_numbers_to_call_from_file(filename)
    print(f"DEBUG: Number to call: number_list={number_list}")

    bingo_card_list = get_bingo_cards_from_file(filename)


    bingo_game = bingogame.BingoGame()

    for card in bingo_card_list:
        bingo_game.addCard(card)

    print(f"DEBUG: Number of cards: {bingo_game.getNumberOfCards()}")        

    for number in number_list:
        print(f"Calling: number={number}")
        bingo_game.callNumber(number)
        if True == bingo_game.hasWinningCards():
            list_winning_cards = bingo_game.getWinningCards()
            for winner in list_winning_cards:                
                print(f"Winning card:  winner={winner} at number={number}")
                unmarked_numbers = winner.getUnmarkedNumbers()
                return sum(unmarked_numbers) * number

    return -1 # No winner!

def get_last_board_to_bingo_final_score_from_file(filename):

    number_list = get_numbers_to_call_from_file(filename)
    bingo_card_list = get_bingo_cards_from_file(filename)

    bingo_game = bingogame.BingoGame()

    for card in bingo_card_list:
        bingo_game.addCard(card)

    last_winning_score = -1
    for number in number_list:
        bingo_game.callNumber(number)
        if True == bingo_game.hasWinningCards():
            list_winning_cards = bingo_game.getWinningCards()
            for winner in list_winning_cards:                
                last_winning_score = sum(winner.getUnmarkedNumbers()) * number
                print(f"DEBUG: Reseting winner: number_of_card={bingo_game.getNumberOfCards()} last_winning_score={last_winning_score} number={number} last_winning_card={winner}")
            bingo_game.resetWinners()

    return last_winning_score

