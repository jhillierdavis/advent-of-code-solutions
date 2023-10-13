import pytest

# Local
import solution
import helpers.grid as hg

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 17),
        pytest.param("puzzle-input-full.txt", 682), 
    ],    
)
def test_part1_solution(filename, expected):
    assert solution.process_first_fold_from_filename(filename) == expected



@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param("puzzle-input-example.txt", 
[
"#####",        
"#...#",
"#...#",
"#...#",
"#####",
".....",
"....."
]
),
        pytest.param("puzzle-input-full.txt", [
"####..##...##..#..#.###..####.#..#.####.",           
"#....#..#.#..#.#..#.#..#....#.#..#.#....",
"###..#..#.#....#..#.#..#...#..####.###..",
"#....####.#.##.#..#.###...#...#..#.#....",
"#....#..#.#..#.#..#.#.#..#....#..#.#....",
"#....#..#..###..##..#..#.####.#..#.####."
]), 
    ]    
)
def test_part2_solution(filename, expected):
    g = solution.process_all_folds_from_filename(filename) 
    g_lines = hg.grid_to_lines(g)
    hg.display_grid(g)
    assert g_lines == expected