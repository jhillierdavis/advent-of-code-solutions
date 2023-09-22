import aoc_2021_day_04

sample_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

def test_get_numbers_to_call():
    assert aoc_2021_day_04.get_numbers_to_call_from_file(sample_file) == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

def test_get_numbers_to_call_from_full_puzzle_input_data():
    assert aoc_2021_day_04.get_numbers_to_call_from_file(full_file) == [83,69,34,46,30,23,19,75,22,37,89,78,32,39,11,44,95,43,26,48,84,53,94,88,18,40,62,35,27,42,15,2,91,20,4,64,99,71,54,97,52,36,28,7,74,45,70,86,98,1,61,50,68,6,77,8,57,47,51,72,65,3,49,24,79,13,17,92,41,80,63,67,82,90,55,0,10,93,38,21,59,73,33,31,9,76,5,66,16,58,85,87,12,29,25,14,96,56,60,81]


def test_get_bingo_cards():
    bingo_card_list = aoc_2021_day_04.get_bingo_cards_from_file(sample_file)

    assert len(bingo_card_list) == 3

def test_get_bingo_cards_from_full_puzzle_input_data():
    bingo_card_list = aoc_2021_day_04.get_bingo_cards_from_file(full_file)

    assert len(bingo_card_list) == 100


def test_part1_puzzle_input_sample_result():
    assert aoc_2021_day_04.get_winning_board_final_score_from_file(sample_file) == 4512


def test_part1_puzzle_input_full_result():
    assert aoc_2021_day_04.get_winning_board_final_score_from_file(full_file) == 41668

def test_part2_puzzle_input_sample_result():
    assert aoc_2021_day_04.get_last_board_to_bingo_final_score_from_file(sample_file) == 1924

def test_part2_puzzle_input_full_result():
    assert aoc_2021_day_04.get_last_board_to_bingo_final_score_from_file(full_file) == 10478
