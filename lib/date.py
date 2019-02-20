import datetime


def timestamp_2_date_str(arr: object) -> object:
    """
    将时间戳类型的DataFrame Series 转换为日期数组
    :param arr:
    :return: list
    """
    # convert = lambda a: datetime.utcfromtimestamp(a).strftime('%Y-%m-%d')
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.fromtimestamp(x / 1000.0).strftime('%Y-%m-%d'))

    return temp


def timestamp_2_month_str(arr: object) -> object:
    """
    将时间戳类型的DataFrame Series 转换为月数组
    :param arr:
    :return: list
    """
    # convert = lambda a: datetime.utcfromtimestamp(a).strftime('%Y-%m-%d')
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.fromtimestamp(x / 1000.0).strftime('%Y-%m'))

    return temp


def timestamp_2_year_str(arr: object) -> object:
    """
    将时间戳类型的DataFrame Series 转换为年数组
    :param arr:
    :return: list
    """
    # convert = lambda a: datetime.utcfromtimestamp(a).strftime('%Y-%m-%d')
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.fromtimestamp(x / 1000.0).strftime('%Y'))

    return temp


def timestamp_2_date(arr: object) -> object:
    """
    将时间戳类型的DataFrame Series 转换为日期数组
    :param arr:
    :return: list
    """
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.utcfromtimestamp(x / 1000.0).strftime('%Y-%m-%d'))

    return temp