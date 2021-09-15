def test_plane():
    from coordinate_function import plane
    result = plane(0,0,2,2)
    expected = 2.828
    assert result == expected