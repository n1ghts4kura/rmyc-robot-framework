# Button.py
# @doc docs/python/custom_ui_doc/Button.rst
# @export_name button_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def set_text(content, color_r=None, color_g=None, color_b=None, color_a=None, align=None, size=None) -> None:
    """设置按钮对象的文字属性

    Args:
        content (string): 按钮上显示的字符串内容
        color_r (int | None): 文字颜色 R，0-255，可选
        color_g (int | None): 文字颜色 G，0-255，可选
        color_b (int | None): 文字颜色 B，0-255，可选
        color_a (int | None): 文字透明度，0-255，可选
        align (enum | None): 文字对齐方式，可选，详见 :data:`align`
        size (int | None): 字号大小，可选

    Returns:
        None: 无

    Example:
        >>> my_Button.set_text(120, 120, 120, 255, text_anchor.upper_left, 12)
        # 设置文字颜色的 rgb 值为（120, 120, 120），透明度为 255，文字对齐方式为顶端左对齐，字号大小为 12 号
    """
    return None

def set_text_color(r, g, b, a) -> None:
    """设置文字的颜色

    Args:
        r (int): 文字颜色的 r 值，范围为 [0, 255]
        g (int): 文字颜色的 g 值，范围为 [0, 255]
        b (int): 文字颜色的 b 值，范围为 [0, 255]
        a (int): 文字颜色的透明度，范围为 [0, 255]

    Returns:
        None: 无

    Example:
        >>> my_button.set_text_color(120, 120, 120, 200)
        # 设置文字颜色的 rgb 值为（120, 120, 120），透明度为 200
    """
    return None

def set_text_align(align) -> None:
    """设置文字的对齐方式

    Args:
        align (enum): 可选参数，枚举类型，需要显示文字的对齐方式，详见表格 :data:`align`

    Returns:
        None: 无

    Example:
        >>> my_button.set_text_align(text_anchor.upper_left)
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
        >>> my_button.set_text_size(12)
        # 设置文字的字号为 12 号
    """
    return None

def set_background_color(r, g, b, a) -> None:
    """设置按钮的背景色

    Args:
        r (int): 字体颜色的 r 值，范围为 [0, 255]
        g (int): 字体颜色的 g 值，范围为 [0, 255]
        b (int): 字体颜色的 b 值，范围为 [0, 255]
        a (int): 字体颜色的透明度，范围为 [0, 255]

    Returns:
        None: 无

    Example:
        >>> my_button.set_background_color(200, 200, 200, 230)
        # 设置背景色的 rgb 值为 (200, 200, 200)，透明度为 230
    """
    return None
