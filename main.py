# file from another assignment
def listMax(list):
    if not list:
        return None
    max_num = -999999999999
    for i in list:
        if i > max_num:
            max_num = i

    return max_num


def doTest(list):
    if list == None:
        return None
        pass
    else:
        n = len(list)
        for i in range(0, n):
            if i < n - 1:
                pass
            pass
        pass
    max = listMax(list)
    if max == None:
        return None
        pass
    else:
        return max
        pass
    pass


def main():
    list1 = [77, 33, 19, 99, 42, 6, 27, 4]
    list2 = [-3, -42, -99, -1000, -999, -88, -77]
    list3 = [425, 59, -3, 77, 0, 36]
    assert doTest(list1) == 99
    assert doTest(list2) == -3
    assert doTest(list3) == 425


if __name__ == "__main__":
    main()
    pass
