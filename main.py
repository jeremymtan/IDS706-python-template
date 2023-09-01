def listmax(list_max):
    """Function returning max of list"""
    if not list_max:
        return None
    max_num = -999999999999
    for i in list_max:
        if i > max_num:
            max_num = i

    return max_num
