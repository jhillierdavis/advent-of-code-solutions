import pytest

import solution

input_example = "AOC-2020-Day-01_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-01_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename, target_sum, expected_term1, expected_term2, expected_product",
    [
        pytest.param(input_example, 2020, 1721, 299, 514579),
        pytest.param(input_full, 2020, 1301, 719, 935419),
    ],    
)
def test_find_terms(filename, target_sum, expected_term1,expected_term2, expected_product):
    assert solution.find_two_terms_for_sum(filename, target_sum) == [expected_term1, expected_term2]

    print("DEBUG: product = ", expected_term1 * expected_term2)
    assert expected_term1 * expected_term2 == expected_product

@pytest.mark.parametrize(
    "filename, target_sum, expected_term1, expected_term2, expected_term3, expected_product",
    [
        pytest.param(input_example, 2020, 979, 366, 675, 241861950),
        pytest.param(input_full, 2020, 889, 1079, 52, 49880012),
    ],    
)
def test_find_terms(filename, target_sum, expected_term1,expected_term2, expected_term3, expected_product):
    assert solution.find_three_terms_for_sum(filename, target_sum) == [expected_term1, expected_term2, expected_term3]

    product = expected_term1 * expected_term2 * expected_term3
    #print("DEBUG: product = ", product)
    assert product == expected_product