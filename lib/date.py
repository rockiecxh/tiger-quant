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
