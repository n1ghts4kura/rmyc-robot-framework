# ir_distance_sensor.py
# @doc docs/python/ir_distance_sensor.rst
# @export_name ir_distance_sensor_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def enable_measure(port_id) -> None:
    """开启红外深度传感器测距功能

    Args:
        port_id (int): 红外深度传感器模块编号，范围为[1:4]

    Returns:
        None: 无

    Example:
        >>> ir_distance_sensor_ctrl.enable_measure(1)
        # 开启 1 号红外深度传感器测距功能
    """
    return None

def disable_measure(port_id) -> None:
    """关闭红外深度传感器测距功能

    Args:
        port_id (int): 红外深度传感器模块编号，范围为[1:4]

    Returns:
        None: 无

    Example:
        >>> ir_distance_sensor_ctrl.disable_measure(1)
        # 关闭 1 号红外深度传感器测距功能
    """
    return None

def get_distance_info(port_id) -> int:
    """获取红外深度传感器测距信息

    Args:
        port_id (int): 红外深度传感器模块编号，范围为[1:4]

    Returns:
        int: 红外深度传感器前方障碍物的距离，精确度为 1 cm

    Example:
        >>> ir_distance_sensor_ctrl.get_distance_info(1)
        # 获取 1 号红外深度传感器测距信息
    """
    return 0

def cond_wait(condition: str) -> None:
    """等待红外深度传感器模块前方障碍物距离满足条件时，执行下一条指令

    Args:
        condition (str): 用于距离比较的字符串，格式为 ``ir_distance_[port_id]_[compare_type]_[dist]``

    Returns:
        None: 无

    Example:
        >>> ir_distance_sensor_ctrl.cond_wait('ir_distance_1_gt_50')
        # 等待 1 号红外深度传感器模块前方障碍物距离大于 50 cm 时，执行下一条指令
    """
    return None

def check_condition(condition: str) -> bool:
    """判断红外深度传感器模块前方障碍物距离是否满足条件

    Args:
        condition (str): 用于距离比较的字符串，格式为 ``ir_distance_[port_id]_[compare_type]_[dist]``

    Returns:
        bool: 是否满足条件，满足条件时返回真，否则返回假。

    Example:
        >>> ir_distance_sensor_ctrl.check_condition('ir_distance_1_gt_50')
    """
    return False
