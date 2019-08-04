def check_type(item, expected_type):
    """
    Checks a object to make sure that it is a certain type
    :param item: any type
    :param expected_type: string (ex:"str")
    :return: type
    """
    item_type = str(type(item))
    if "str" in expected_type.lower() and item_type == "<class 'str'>":
        pass
    elif "int" in expected_type.lower() and item_type == "<class 'int'>":
        pass
    elif "bool" in expected_type.lower() and item_type == "<class 'bool'>":
        pass
    elif "float" in expected_type.lower() and item_type == "<class 'float'>":
        pass
    elif "tuple" in expected_type.lower() and item_type == "<class 'tuple'>":
        pass
    elif "list" in expected_type.lower() and item_type == "<class 'list'>":
        pass
    elif "dict" in expected_type.lower() and item_type == "<class 'dict'>":
        pass
    elif "datetime" in expected_type.lower() and item_type == "<class 'datetime.datetime'>":
        pass
    elif "none" in expected_type.lower() and item_type == "<class 'NoneType'>":
        pass
    else:
        raise TypeError("{a} isn't a {b}".format(a=object, b=expected_type))
    return item_type
