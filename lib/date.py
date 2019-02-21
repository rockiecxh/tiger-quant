import datetime


def timestamp_2_date_str(arr: object) -> object:
    """
    将时间戳类型的DataFrame Series 转换为日期数组
    :param arr:
    :return: list
    """
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


def get_today():
    """
    获取当天日期字符串
    :return:
    """
    return datetime.datetime.today().strftime('%Y-%m-%d')


def date_delta(week: int):
    """
    按周为单位对当前日期进行offset
    :param week: 要offset的周数
    :return: 日期字符串
    """
    target_date = datetime.datetime.today() + datetime.timedelta(weeks=week)
    target_date.strftime('%Y-%m-%d')
    return target_date


