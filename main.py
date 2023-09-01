def listmax(list_max):
    """Function returning max of list"""
    if not list_max:
        return None
    max_num = -999999999999
    for i in list_max:
        if i > max_num:
            max_num = i

    return max_num


def main():
    """Function calling listMax"""

    list1 = [77, 33, 19, 99, 42, 6, 27, 4]
    list2 = [-3, -42, -99, -1000, -999, -88, -77]
    list3 = [425, 59, -3, 77, 0, 36]
    assert listmax(list1) == 99
    assert listmax(list2) == -3
    assert listmax(list3) == 425


if __name__ == "__main__":
    main()
