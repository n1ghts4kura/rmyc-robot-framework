# Text.py
# @doc docs/python/custom_ui_doc/Text.rst
# @export_name text_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def set_text(string, color_r=None, color_g=None, color_b=None, color_a=None, align=None, size=None) -> None:
    """设置文本控件的文字属性

    Args:
        string (string): 需要显示的字符串内容
        color_r (int | None): 文字颜色 R，0-255，可选
        color_g (int | None): 文字颜色 G，0-255，可选
        color_b (int | None): 文字颜色 B，0-255，可选
        color_a (int | None): 文字透明度，0-255，可选
        align (enum | None): 文字对齐方式，可选，详见 :data:`align`
        size (int | None): 文字字号，可选

    Returns:
        None: 无

    Example:
        >>> my_Text.set_text("Hello RoboMaster", 120, 120, 120, 200, text_anchor.center, 18)
        # 设置文字颜色的 rgb 值为（120, 120, 120），透明度为 200，文字对齐方式为居中对齐，字号为 18 号
    """
    return None

def set_text_color(r, g, b, a) -> None:
    """设置控件的文字颜色

    Args:
        r (int): 文字颜色的 r 值，范围为 [0, 255]
        g (int): 文字颜色的 g 值，范围为 [0, 255]
        b (int): 文字颜色的 b 值，范围为 [0, 255]
        a (int): 文字颜色的透明度，范围为 [0, 255]

    Returns:
        None: 无

    Example:
        >>> my_Text.set_text_color(120, 120, 120, 200)
        # 设置文字的 rgb 值为（120, 120, 120），透明度为 200
    """
    return None

def set_text_align(align) -> None:
    """设置文字的对齐方式

    Args:
        align (enum): 可选参数，枚举类型，需要显示文字的对齐方式，详细见表格 :data:`align`

    Returns:
        None: 无

    Example:
        >>> my_Text.set_text_align(text_anchor.upper_left)
        # 设置文字的对齐方式为顶端左对齐
    """
    return None

def set_text_size(size) -> None:
    """设置文字的字号大小

    Args:
        size (int): 文字的字号值

    Returns:
        None: 无

    Example:
        >>> my_Text.set_text_size(12)
        # 设置文字的字号为 12 号
    """
    return None

def set_border_active(active) -> None:
    """是否显示文字边框

    Args:
        active (bool): 是否显示文字边框，True 表示显示边框，False 表示不显示边框

    Returns:
        None: 无

    Example:
        >>> my_Text.set_border_active(True)
        # 显示文字边框
    """
    return None

def set_background_color(r, g, b, a) -> None:
    """设置控件的背景色

    Args:
        r (int): 背景颜色的 r 值，范围为 [0, 255]
        g (int): 背景颜色的 g 值，范围为 [0, 255]
        b (int): 背景颜色的 b 值，范围为 [0, 255]
        a (int): 背景颜色的透明度，范围为 [0, 255]

    Returns:
        None: 无

    Example:
        >>> my_Text.set_background_color(200, 200, 200, 230)
        # 设置背景色的 rgb 值为 (200, 200, 200)，透明度为 230
    """
    return None

def set_background_active(active) -> None:
    """是否显示文字背景

    Args:
        active (bool): 是否显示背景，True 表示显示背景，False 表示不显示背景

    Returns:
        None: 无

    Example:
        >>> my_Text.set_background_active(True)
        # 显示文字背景
    """
    return None

def append_text(content) -> None:
    """向 Text 控件中增加文本

    Args:
        content (string): 需要向 Text 中增加的文本

    Returns:
        None: 无

    Example:
        >>> my_Text.append_text('RoboMaster EP')
        # 向 Text 中增加的文字 ``RoboMaster EP``
    """
    return None
