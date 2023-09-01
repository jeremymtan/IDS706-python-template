"""
Test goes here

"""

from main import listmax


def test_max():
    """Function calling listMax"""

    list1 = [77, 33, 19, 99, 42, 6, 27, 4]
    list2 = [-3, -42, -99, -1000, -999, -88, -77]
    list3 = [425, 59, -3, 77, 0, 36]
    assert listmax(list1) == 99
    assert listmax(list2) == -3
    assert listmax(list3) == 425
