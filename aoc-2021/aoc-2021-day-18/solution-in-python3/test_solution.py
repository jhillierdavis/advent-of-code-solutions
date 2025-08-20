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
        pytest.param([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], 4140),
        pytest.param([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
        pytest.param([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
        pytest.param([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
        pytest.param([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488),
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
        pytest.param([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]]),     
        pytest.param([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], [[[[0,7],4],[7,[[8,4],9]]],[1,1]]),
    ],    
)
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
        pytest.param([[[[0,7],4],[[7,8],[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]),
        pytest.param([[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[7, 10], [[0, [11, 3]], [[6, 3], [8, 8]]]]] , [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[7, [5, 5]], [[0, [11, 3]], [[6, 3], [8, 8]]]]])
    ],    
)
def test_split(input, expected):
    result, was_split = solution.split(input)
    assert result == expected


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
        pytest.param( [[[[4,3],4],4],[7,[[8,4],9]]], [1,1] , [[[[0,7],4],[[7,8],[6,0]]],[8,1]] ),
        pytest.param( [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]] , [7,[[[3,7],[4,3]],[[6,3],[8,8]]]] , [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]] ),
        pytest.param( [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]] , [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]] , [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]] ),
        pytest.param( [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]] , [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]], [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]] ),
        pytest.param( [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]] ,  [7,[5,[[3,8],[1,4]]]] ,  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]] ),
        pytest.param( [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]] , [[2,[2,2]],[8,[8,1]]], [[[[6,6],[6,6]],[[6,0],[6,7]]] ,[[[7,7],[8,9]],[8,[8,1]]]] ),
        pytest.param( [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]] , [2,9] , [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]] ),
        pytest.param( [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]] , [1,[[[9,3],9],[[9,0],[0,7]]]] , [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]] ),
        pytest.param( [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]] , [[[5,[7,4]],7],1] , [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]] ),
        pytest.param( [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]] , [[[[4,2],2],6],[8,7]] , [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] ),
    ],    
) 
#@pytest.mark.skip(reason="TODO")
def test_snailfish_number_add_and_reduce(x,y,expected):
    assert solution.add_and_reduce(x, y) == expected


input_example_addition_1 = "puzzle-input-example-addition-1.txt"
input_example_addition_2 = "puzzle-input-example-addition-2.txt"
input_example_addition_3 = "puzzle-input-example-addition-3.txt"
input_example_addition_4 = "puzzle-input-example-addition-4.txt"
input_example = "puzzle-input-example.txt"
input_full = "puzzle-input-full.txt"


@pytest.mark.parametrize(
    "filename, expected_reduced_snailfish_number, expected_magnitude",
    [
        pytest.param(input_example_addition_1, [[[[1,1],[2,2]],[3,3]],[4,4]], 445),
        pytest.param(input_example_addition_2, [[[[3,0],[5,3]],[4,4]],[5,5]], 791),
        pytest.param(input_example_addition_3, [[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
        pytest.param(input_example_addition_4, [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488),
        pytest.param(input_example, [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], 4140),
        pytest.param(input_full, [[[[6, 7], [7, 7]], [[7, 7], [7, 7]]], [[[0, 7], [8, 8]], [[8, 7], [6, 1]]]], 3892),
    ],    
)
#@pytest.mark.skip(reason="TODO")
def test_solve_part1(filename, expected_reduced_snailfish_number, expected_magnitude):
    result = solution.solve_part1(filename)
    
    assert result == expected_reduced_snailfish_number
    assert solution.get_magnitude(result) == expected_magnitude


