"""
https://www.nowcoder.com/pat/6/problem/4078
"""
# 从控制台读取测试用例数据
raw_input = input()
dalianmao = raw_input.split(" ")
dalianmao = [int(i) for i in dalianmao]

# print(dalianmao)

# A1 = 能被5整除的数字中所有偶数的和；
def calculate_a1(input_arr):
    result = 0
    for i in input_arr:
        if ((i % 5 == 0) and (i %2 == 0)):
            result = result + i

    return result


def calculate_a2(input_arr):
    return 0


def calculate_a3(input_arr):
    return 0


def calculate_a4(input_arr):
    return 0


def calculate_a5(input_arr):
    return 0

# 结果集
result_arr = [0] * 5

# A1 = 能被5整除的数字中所有偶数的和；
result_arr[0] = calculate_a1(dalianmao)
result_arr[1] = calculate_a2(dalianmao)
result_arr[2] = calculate_a3(dalianmao)
result_arr[3] = calculate_a4(dalianmao)
result_arr[4] = calculate_a5(dalianmao)

for i in result_arr:
    print(i, end=" ")
