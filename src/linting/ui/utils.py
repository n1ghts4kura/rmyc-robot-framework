# utils.py
# 共享 UI 工具（对齐枚举等）

class __TextAnchor:
    """
    文字对齐方式枚举类

    Attributes:
        upper_left (int): 顶端左对齐
        upper_center (int): 顶端居中对齐
        upper_right (int): 顶端右对齐
        middle_left (int): 中部左对齐
        middle_center (int): 中部居中对齐
        middle_right (int): 中部右对齐
        lower_left (int): 底端左对齐
        lower_center (int): 底端居中对齐
        lower_right (int): 底端右对齐
    """

    upper_left = 0
    upper_center = 1
    upper_right = 2
    middle_left = 3
    middle_center = 4
    middle_right = 5
    lower_left = 6
    lower_center = 7
    lower_right = 8


def _make_text_anchor() -> __TextAnchor:
    # 返回对齐枚举实例
    return __TextAnchor()


text_anchor = _make_text_anchor()

__all__ = ["__TextAnchor", "text_anchor"]
