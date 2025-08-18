import pytest

# Local
import solution

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([9,1], 29),
        pytest.param([1,9], 21),
        pytest.param([[9,1],[1,9]], 129),
        pytest.param([[1,2],[[3,4],5]],143),
        pytest.param([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384),
        pytest.param([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
        pytest.param([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
        pytest.param([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
        pytest.param([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488),
        pytest.param([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], 4140),
    ],    
)
def test_snailfish_number_get_magnitude(input, expected):
    assert solution.get_magnitude(input) == expected



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
#@pytest.mark.skip(reason="TODO")
def test_snailfish_number_explode(original, expected):
    assert solution.explode(original) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param(1, 1), # Unchanged (no splitting required)
        pytest.param(9, 9), # Unchanged (no splitting required)
        pytest.param(10, [5,5]),
        pytest.param(11, [5,6]),
        pytest.param(12, [6,6]),        
    ],    
)
def test_split_number(input, expected):
    assert solution.split_number(input) == expected    

@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param([[[[0,7],4],[15,[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,13]]],[1,1]]),
        pytest.param([[[[0,7],4],[[7,8],[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
    ],    
)
def test_split(input, expected):
    assert solution.split(input) == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        pytest.param([[[[4,3],4],4],[7,[[8,4],9]]], [1,1], [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
    ],    
) 
#@pytest.mark.skip(reason="TODO")
def test_snailfish_number_add(x,y,expected):
    assert solution.add(x, y) == expected

@pytest.mark.parametrize(
    "x, y, expected",
    [
        pytest.param([[[[4,3],4],4],[7,[[8,4],9]]], [1,1], [[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    ],    
) 
#@pytest.mark.skip(reason="TODO")
def test_snailfish_number_add_and_reduce(x,y,expected):
    assert solution.add_and_reduce(x, y) == expected