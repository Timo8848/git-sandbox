"""回文判断：忽略大小写、空格和标点，方便练习边界情况和多个测试用例。"""


def is_palindrome(text: str) -> bool:
    """判断 text 是否为回文（只看字母和数字，忽略大小写）。

    例如 "A man, a plan, a canal: Panama" 是回文。
    空字符串视为回文。
    """
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
