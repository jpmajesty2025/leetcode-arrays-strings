from find_highest_altitude import largest_altitude


def test_example_1():
    assert largest_altitude([-5, 1, 5, 0, -7]) == 1


def test_example_2():
    assert largest_altitude([-4, -3, -2, -1, 4, 3, 2]) == 0


def test_single_positive_gain():
    assert largest_altitude([7]) == 7


def test_single_negative_gain():
    assert largest_altitude([-7]) == 0


def test_all_positive_gains():
    assert largest_altitude([1, 2, 3, 4]) == 10


def test_all_negative_gains():
    assert largest_altitude([-1, -2, -3, -4]) == 0


def test_mixed_gains_with_late_peak():
    assert largest_altitude([2, -1, -2, 5, -1]) == 4
