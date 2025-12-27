# Common.py
# @doc docs/python/custom_ui_doc/Common.rst
# @export_name common_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

from typing import Any

def set_active(status) -> None:
    """控制当前控件是否显示

    Args:
        status (bool): 控件的活动状态，True 表示显示当前控件，False 表示隐藏当前控件

    Returns:
        None: 无

    Example:
        >>> my_Slider.set_active(Flase)
        # 设置 my_Slider 控件为隐藏状态
    """
    return None

def get_active(void) -> bool:
    """获取当前控件的显示状态

    Args:
        void (Any): 无

    Returns:
        bool: bool, 表示控件的显示状态

    Example:
        >>> status = my_Slider.get_active()
        # 获取 my_Slider 控件的显示状态，赋值给 status 变量
    """
    return False

def set_name(name) -> None:
    """设置当前控件的名字

    Args:
        name (string): 控件的名字

    Returns:
        None: 无

    Example:
        >>> my_Dropdown.set_name('my_dropdown')
        # 设置 my_Dropdown 控件的名字为『my_dropdown』
    """
    return None

def get_name(void) -> str:
    """获取当前控件的名字

    Args:
        void (Any): 无

    Returns:
        str: string，表示控件的名字

    Example:
        >>> name = my_Dropdown.get_name()
        # 获取 my_Dropdown 控件的名字，赋值给 name 变量
    """
    return ""

def set_position(x, y) -> None:
    """设置控件的位置坐标，原点在屏幕的中心位置

    Args:
        x (int): 控件的横坐标，取值为屏幕上实际像素的位置，0 点在屏幕水平中心位置，向右为正方向
        y (int): 控件的纵坐标，取值为屏幕上实际像素的位置，0 点在屏幕垂直中心位置，向上为正方向

    Returns:
        None: 无

    Example:
        >>> my_Text.set_position(-200, 500)
        # 设置 my_Text 控件的坐标为 (-200，500)
    """
    return None

def get_position(void) -> Any:
    """获取控件的位置坐标

    Args:
        void (Any): 无

    Returns:
        Any: [x,y]，表示控件的位置

    Example:
        >>> pos = my_Text.get_position()
        # 获取 my_Text 控件的位置，赋值给变量 pos，pos 为一个列表
    """
    return None

def set_size(w, h) -> None:
    """设置控件的大小

    Args:
        w (int): 控件的宽度
        h (int): 控件的高度

    Returns:
        None: 无

    Example:
        >>> my_Button.set_size(300, 200)
        # 设置 my_Button 控件的宽度为 300，高度为 200
    """
    return None

def get_size(void) -> Any:
    """获取控件的大小

    Args:
        void (Any): 无

    Returns:
        Any: [w,h], 表示控件的大小

    Example:
        >>> size = my_Button.get_size()
        # 获取 my_Button 控件的大小，赋值给变量 size，size 为一个列表
    """
    return None

def set_rotation(degree) -> None:
    """设置控件的旋转角度

    Args:
        degree (int): 控件的旋转角度，范围为 [0, 360]，正值为顺时针旋转，负值为逆时针旋转

    Returns:
        None: 无

    Example:
        >>> my_Button.set_rotation(90)
        # 设置 my_Button 控件顺时针旋转 90 度
    """
    return None

def get_rotation(void) -> int:
    """获取控件的旋转角度

    Args:
        void (Any): 无

    Returns:
        int: int, 表示控件的旋转角度，范围为 [0, 360]，正值为顺时针旋转，负值为逆时针旋转

    Example:
        >>> degree = my_Button.get_rotation()
        # 获取 my_Button 控件的旋转角度，赋值给变量 degree
    """
    return 0

def set_privot(x, y) -> None:
    """设置控件的锚点坐标，输入参数是归一化参数，原点位于控件的左下角，控件的锚点默认为控件中心即 (0.5,0.5)，控件的位置和旋转均以锚点作为控制点

    Args:
        x (int): 锚点的 x 坐标，范围为 [0, 1]，向右为正方向
        y (int): 锚点的 y 坐标，范围为 [0, 1]，向上为正方向

    Returns:
        None: 无

    Example:
        >>> my_Button.set_privot(0, 1)
        # 设置控件的锚点为控件的左上角
    """
    return None

def get_privot(void) -> Any:
    """获取控件的锚点坐标

    Args:
        void (Any): 无

    Returns:
        Any: [x,y]，表示控件的锚点坐标

    Example:
        >>> privot = my_Button.get_privot()
        # 获取控件的锚点坐标，赋值给变量 privot，privot 为一个列表
    """
    return None

def set_order(order) -> None:
    """设置控件的显示优先级，当多个控件重叠时，优先级高的控件在上层，数字越大优先级越高

    Args:
        order (int): 控件的指定优先级，控件重叠时优先级高的优先显示

    Returns:
        None: 无

    Example:
        >>> my_Button.set_order(8)
        # 将控件的显示优先级设置为 8，当控件重叠时，低于此优先级的控件将被覆盖
    """
    return None

def get_order(void) -> int:
    """获取控件的显示优先级

    Args:
        void (Any): 无

    Returns:
        int: int，表示控件的显示优先级

    Example:
        >>> order = my_Button.get_order()
        # 获取 my_Button 控件的显示优先级，赋值给变量 order
    """
    return 0

def callback_register(event, callback) -> None:
    """注册控件事件触发的回调函数，当控件检测到相应的事件后，执行注册的回调函数

    Args:
        event (string): 指定回调函数的触发事件
        callback (function): 需要注册的回调函数，回调函数的统一签名为： ``def callback(widget,*args,**kw):`` ，其中 widget 为触发事件的控件引用，args，kw为参数.

    Returns:
        None: 无

    Example:
        >>> common_object.callback_register(event, callback)
    """
    return None
