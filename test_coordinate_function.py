def test_slope():
    from coordinate_function import slope
    result1 = slope(0,0,2,2)
    expected = 1
    assert result == expected

def test_plane():
    from coordinate_function import plane
    result = plane(1, 3, 0)
    expected = 3
    assert result == expected