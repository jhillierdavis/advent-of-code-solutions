import grid

sample_grid_data = [[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5],[2,0,12,3,7]]

def test_creation_of_grid2d_instance():
    # Given:
    grid2d = grid.Grid2d(sample_grid_data)

    # Then:
    assert grid2d 

def test_creation_of_grid2d_size():
    # Given:
    grid2d = grid.Grid2d(sample_grid_data)

    # Then:
    assert grid2d.getNumberOfRows() == 5
    assert grid2d.getNumberOfColumns() == 5

def test_creation_of_grid2d_get_row():
    # Given:
    grid2d = grid.Grid2d(sample_grid_data)

    # Then:
    assert grid2d.getRow(2) == [18,8,23,26,20]
    assert grid2d.getRow(4) == [2,0,12,3,7]

def test_creation_of_grid2d_get_column():
    # Given:
    grid2d = grid.Grid2d(sample_grid_data)

    # Then:
    assert grid2d.getColumn(1) == [21,16,8,11,0]
    assert grid2d.getColumn(2) == [17,15,23,13,12]