

def sum(*args):
    sum_last = 0
    for arg in args:
        sum_last = sum_last + arg
    return sum_last


def sub(*args):
    sub_last = 0
    for arg in args:
        sub_last = arg - sub_last
    return arg


def mul(*args):
    mul_last = 1
    for arg in args:
        mul_last = mul_last * arg
    return mul_last


if __name__ == '__main__':
    print(f"Sum of 2 number = {sum(10, 20)}")
    print(f"Sub of 2 number = {sub(20, 10)}")
    print(f"Mul of 2 number = {mul(10, 10)}")





