# robotic_arm.py
# @doc docs/python/robotic_arm.rst
# @export_name robotic_arm_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def move(x, y, wait_for_complete=True) -> None:
    """设置机械臂运动的相对位置

    Args:
        x (int32): 设置机械臂水平运动的距离，正数为向前运动，负数为向后运动，精确度为 1 mm
        y (int32): 设置机械臂垂直运动的距离，正数为向上运动，负数为向下运动，精确度为 1 mm
        wait_for_complete (bool): 是否等待执行完成，默认为 True

    Returns:
        None: 无

    Example:
        >>> robotic_arm_ctrl.move(40, 50, True)
        # 设置机械臂向前移动 20 mm，向上移动 30 mm，等待执行完成
    """
    return None

def moveto(x, y, wait_for_complete=True) -> None:
    """设置机械臂运动到绝对坐标

    Args:
        x (int32): 设置机械臂水平运动的坐标值，精确度为 1 mm
        y (int32): 设置机械臂垂直运动的坐标值，精确度为 1 mm
        wait_for_complete (bool): 是否等待执行完成，默认为 True

    Returns:
        None: 无

    Example:
        >>> robotic_arm_ctrl.moveto(40, 50, True)
        # 设置机械臂移动到（x=40mm，y=50mm）的绝对坐标，等待执行完成
    """
    return None

def get_position() -> list[int]:
    """获取机械臂位置

    Args:
        None: 无

    Returns:
        list[int]: 机械臂的绝对坐标，精确度为 1 mm

    Example:
        >>> [x, y] = robotic_arm_ctrl.get_position()
        # 获取机械臂的绝对坐标
    """
    return [0, 0]

def recenter() -> None:
    """设置机械臂回中

    Args:
        None: 无

    Returns:
        None: 无

    Example:
        >>> robotic_arm_ctrl.recenter()
        # 设置机械臂回中
    """
    return None
