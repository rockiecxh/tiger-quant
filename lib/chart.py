import cmath
import random


def random_color():
    """
    获取随机颜色
    :return: 返回随机颜色字符串
    """
    color_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += color_arr[random.randint(0, 14)]

    return "#" + color


def subplot_num(total: int):
    """
    根据子图数量计算subplot 9 = (3, 3) 10=(4, 3)
    :param index:
    :return:
    """
    sqrt = cmath.sqrt(total).real
    if sqrt.real.is_integer():
        return sqrt, sqrt
    else:
        return int(sqrt) + 1, int(sqrt)