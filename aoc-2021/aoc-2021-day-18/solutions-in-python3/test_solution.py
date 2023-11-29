import pytest

# Local
import solution


@pytest.mark.parametrize(
    "original, expected",
    [
        pytest.param([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]),
        pytest.param([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]),
        pytest.param([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
        pytest.param([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] ,[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
        pytest.param([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],[[3,[2,[8,0]]],[9,[5,[7,0]]]]),     
        pytest.param([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], [[[[0,7],4],[7,[[8,4],9]]],[1,1]]),
    ],    
)
def test_snailfish_number_explode(original, expected):
    assert solution.explode(original) == expected

@pytest.mark.parametrize(
    "x, y, expected",
    [
        pytest.param([[[[4,3],4],4],[7,[[8,4],9]]], [1,1], [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
    ],    
) 
def test_snailfist_number_add(x,y,expected):
    assert solution.add(x, y) == expected

@pytest.mark.parametrize(
    "x, y, expected",
    [
        pytest.param([[[[4,3],4],4],[7,[[8,4],9]]], [1,1], [[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    ],    
) 
def test_snailfist_number_add_and_reduce(x,y,expected):
    assert solution.add_and_reduce(x, y) == expected