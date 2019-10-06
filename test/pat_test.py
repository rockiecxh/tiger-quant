"""
https://www.nowcoder.com/pat/6/problem/4077
"""

nums = input()
nums = int(nums)
input_list = [0] * nums
for i in range(nums):
    input_list[i] = input()

for i in range(nums):
    raw_str = input_list[i]
    numArrs = raw_str.split(" ")

    a = int(numArrs[0])
    b = int(numArrs[1])
    c = int(numArrs[2])

    if((a + b) > c):
        print("Case #" + str(i + 1) + ": true")
    else:
        print("Case #" + str(i + 1) + ": false")
