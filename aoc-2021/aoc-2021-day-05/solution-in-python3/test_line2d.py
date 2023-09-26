import point2d
import line2d

def test_line2d_creation():
    # Given: a 2-D line
    line = line2d.Line2D(point2d.Point2D(1,2), point2d.Point2D(2,3))

    # Then: check an instance is created
    assert line is not None
    assert type(line) is line2d.Line2D

def test_point2d_accessors():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,2)
    end = point2d.Point2D(2,3)
    line = line2d.Line2D(begin, end)

    # Then: check that the X & Y co-ords are as provided
    assert line.getBeginPoint() == begin
    assert line.getEndPoint() == end

def test_point2d_is_not_horizontal_line():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,2)
    end = point2d.Point2D(2,3)
    line = line2d.Line2D(begin, end)

    # Then: ensure not a horizontal line
    assert line.isHorizontalLine() == False

def test_point2d_is_horizontal_line():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,1)
    end = point2d.Point2D(1,9)
    line = line2d.Line2D(begin, end)

    # Then: ensure a horizontal line
    assert line.isHorizontalLine() == True

    # And: not virtical or diagonal
    assert line.isVerticalLine() == False
    assert line.isDiagonalLine() == False


def test_point2d_is_not_vertical_line():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,2)
    end = point2d.Point2D(2,3)
    line = line2d.Line2D(begin, end)

    # Then: ensure not a horizontal line
    assert line.isVerticalLine() == False



def test_point2d_is_vertical_line():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,5)
    end = point2d.Point2D(3,5)
    line = line2d.Line2D(begin, end)

    # Then: ensure a vertical line
    assert line.isVerticalLine() == True

    # And: not horizontal or diagonal
    assert line.isHorizontalLine() == False
    assert line.isDiagonalLine() == False

def test_getAllPoints_for_horizontal_line():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,5)
    end = point2d.Point2D(1,0)
    line = line2d.Line2D(begin, end)

    # When:
    coords = line.getAllPoints()

    # Then:
    #assert begin in coords
    #assert end in coords
    #assert point2d.Point2D(2,5) in coords
    print(f"DEBUG: coords={coords}")
    assert len(coords) == 6

def test_getAllPoints_for_vertical_line():
    # Given: 2-D points that begin & end a line
    begin = point2d.Point2D(1,5)
    end = point2d.Point2D(3,5)
    line = line2d.Line2D(begin, end)

    # When:
    coords = line.getAllPoints()

    # Then:
    #assert begin in coords
    #assert end in coords
    #assert point2d.Point2D(2,5) in coords
    print(f"DEBUG: coords={coords}")
    assert len(coords) == 3
