import pytest

import solution

@pytest.mark.parametrize(
    "legal_chunk",
    [
        pytest.param("()"),
        pytest.param("((()))"),
        pytest.param("[]"),
        pytest.param("()"),
        pytest.param("([])"),
        pytest.param("{()()()}"),
        pytest.param("<([{}])>"),
        pytest.param("[<>({}){}[([])<>]]"),
        pytest.param("(((((((((())))))))))"),
    ],    
)

def test_legal_chunk(legal_chunk):
    assert solution.is_legal_chunk(legal_chunk) == True

@pytest.mark.parametrize(
    "corrupted_chunk",
    [
        pytest.param("(]"),
        pytest.param("{()()()>"),
        pytest.param("(((()))}"),
        pytest.param("<([]){()}[{}])"),
    ],    
)

def test_corrupted_chunk(corrupted_chunk):
    assert solution.is_corrupted_chunk(corrupted_chunk) == True    

@pytest.mark.parametrize(
    "chunk,expected",
    [
        # Corrupted chunks
        pytest.param("{([(<{}[<>[]}>{[]{[(<()>", '}'),
        pytest.param("[[<[([]))<([[{}[[()]]]", ')'),
        pytest.param("[{[{({}]{}}([{[{{{}}([]]", ']'),
        pytest.param("[<(<(<(<{}))><([]([]()", ')'),
        pytest.param("<{([([[(<>()){}]>(<<{{", '>'),

        # Other (legal or incomplete)
        pytest.param("[({(<(())[]>[[{[]{<()<>>", ''),
        pytest.param("[(()[<>])]({[<{<<[]>>(", ''),
        pytest.param("(((({<>}<{<{<>}{[]{[]{}", ''),
        pytest.param("<{([{{}}[<[[[<>{}]]]>[]]", ''),
    ],    
)
def test_corruption_point(chunk:str, expected:chr):
    assert solution.get_corruption_char(chunk) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 26397),
        pytest.param("puzzle-input-full.txt", 436497),
    ],    
)

def test_part1_solution(filename, expected):
    assert solution.get_corruption_chunk_score_from_file(filename) ==  expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 288957),
        pytest.param("puzzle-input-full.txt", 2377613374),
    ],    
)
def test_part2_solution(filename, expected):
    assert solution.get_middle_autocomplete_score_from_file(filename) == expected
