"""FizzBuzz：经典入门题，规则简单，方便练习加规则、加测试。"""


def fizzbuzz(n: int) -> str:
    """返回 1..n 的 FizzBuzz 结果，每行一个值。

    规则：
    - 能被 3 整除 -> "Fizz"
    - 能被 5 整除 -> "Buzz"
    - 同时能被 3 和 5 整除 -> "FizzBuzz"
    - 其余 -> 数字本身
    """
    if n < 1:
        raise ValueError("n 必须是正整数")

    lines = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            lines.append("FizzBuzz")
        elif i % 3 == 0:
            lines.append("Fizz")
        elif i % 5 == 0:
            lines.append("Buzz")
        else:
            lines.append(str(i))
    return "\n".join(lines)
