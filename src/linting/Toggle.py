# Toggle.py
# @doc docs/python/custom_ui_doc/Toggle.rst
# @export_name toggle_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def set_text(string, color_r=None, color_g=None, color_b=None, color_a=None, align=None, size=None) -> None:
    """设置开关控件的文字属性

    Args:
        string (string): 控件上显示的字符串内容
        color_r (int | None): 文字颜色 R，0-255，可选
        color_g (int | None): 文字颜色 G，0-255，可选
        color_b (int | None): 文字颜色 B，0-255，可选
        color_a (int | None): 文字透明度，0-255，可选
        align (enum): 可选参数，枚举类型，需要显示文字的对齐方式，详细见表格 :data:`align`
        size (int): 显示文字的字号大小

    Returns:
        None: 无

    Example:
        >>> my_Toggle.set_text(120, 120, 120, 200, text_anchor.upper_left, 12)
        # 设置文字的 rgb 值为（120, 120, 120），透明度为 200，字体对齐方式为顶端左对齐，字号大小为 12 号
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
        >>> my_Toggle.set_text_color(120, 120, 120, 200)
        # 设置字体的 rgb 值为（120, 120, 120），透明度为 200
    """
    return None

def set_text_align(align) -> None:
    """设置文字的对齐方式

    Args:
        align (enum): 可选参数，枚举类型，需要显示文字的对齐方式，详细见表格 :data:`align`

    Returns:
        None: 无

    Example:
        >>> my_Toggle.set_text_align(text_anchor.upper_left)
        # 设置字体的对齐方式为顶端左对齐
    """
    return None

def set_text_size(size) -> None:
    """设置文字的字号大小

    Args:
        size (int): 文字的字号值

    Returns:
        None: 无

    Example:
        >>> my_Toggle.set_text_size(12)
        # 设置文字的字号为 12 号
    """
    return None

def set_background_color(r, g, b, a) -> None:
    """设置控件的背景色

    Args:
        r (int): 背景颜色的 r 值，范围为 [0, 255]
        g (int): 背景颜色的 g 值，范围为 [0, 255]
        b (int): 背景颜色的 b 值，范围为 [0, 255]
        a (int): 背景颜色的透明度，[0, 255]

    Returns:
        None: 无

    Example:
        >>> my_Toggle.set_background_color(200, 200, 200, 230)
        # 设置背景色的 rgb 值为 (200, 200, 200)，透明度为 230
    """
    return None

def set_checkmark_color(r, g, b, a) -> None:
    """设置控件选中图标的颜色

    Args:
        r (int): 图标颜色的 r 值，范围为 [0, 255]
        g (int): 图标颜色的 g 值，范围为 [0, 255]
        b (int): 图标颜色的 b 值，范围为 [0, 255]
        a (int): 图标颜色的透明度，范围为 [0, 255]

    Returns:
        None: 无

    Example:
        >>> my_Toggle.set_checkmark_color(200, 200, 200, 230)
        # 设置选中图标的 rgb 值为 (200, 200, 200)，透明度为 230
    """
    return None

def set_is_on(status) -> None:
    """设置控件的状态

    Args:
        status (bool): 设置控件是否为打开状态，True 表示打开，False 表示关闭

    Returns:
        None: 无

    Example:
        >>> my_Toggle.set_is_on(True)
        # 设置 Toggle 控件为打开状态
    """
    return None
