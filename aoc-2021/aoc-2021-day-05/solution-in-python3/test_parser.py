import parser

def test_parser_parseLine():
    # Given: a string of input
    str = "0,9 -> 5,9"

    # When:
    line = parser.parseInputStringToLine2D(str)

    # Then:
    assert line.begin.getX() == 0 
    assert line.begin.getY() == 9
    assert line.end.getX() == 5 
    assert line.end.getY() == 9    