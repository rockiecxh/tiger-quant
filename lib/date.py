import datetime

from pandas._libs.tslibs.timestamps import Timestamp


def date_2_month(date: datetime.datetime):
    """
    将日期格式化为月份
    :param date:
    :return: 月份
    """
    return date.strftime('%Y/%m')


def timestamp_2_month(arr: []):
    """
    将时间戳类型的数组转换为日期数组
    :param arr:
    :return: list
    """
    temp = []
    for x in arr.tolist():
        temp.append(datetime.datetime.fromtimestamp(x / 1000).strftime('%Y-%m'))

    return temp


def timestamp_2_date(arr: []):
    """
    将时间戳类型的DataFrame Series 转换为日期数组
    :param arr:
    :return: list
    """
    temp = []
    for x in arr:
        if isinstance(x, int):
             temp.append(datetime.datetime.utcfromtimestamp(x))
        elif isinstance(x, Timestamp):
            temp.append(x)

    return temp


def timestr_2_date(arr: []):
    temp = []
    for x in arr:
        temp.append(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

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
    target_date = target_date.strftime('%Y-%m-%d')
    return target_date


