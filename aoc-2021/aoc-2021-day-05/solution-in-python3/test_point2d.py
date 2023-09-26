import point2d

def test_point2d_creation():
    # Given: a 2-D point
    point = point2d.Point2D(1,2)

    # Then: check an instance is created
    assert point is not None
    assert type(point) is point2d.Point2D

def test_point2d_accessors():
    # Given: a 2-D point
    point = point2d.Point2D(1,2)

    # Then: check that the X & Y co-ords are as provided
    assert point.getX() == 1
    assert point.getY() == 2

def test_string_representation():
    # Given: a 2-D point
    point = point2d.Point2D(1,2)

    # When:
    point_as_str = str(point)

    # Then: check an instance is created
    assert "Point2D(id=" in point_as_str
    assert "x: 1" in point_as_str
    assert "y: 2" in point_as_str

