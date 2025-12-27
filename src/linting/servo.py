# servo.py
# @doc docs/python/servo.rst
# @export_name servo_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def get_angle(servo_id) -> int:
    """获取舵机旋转角度

    Args:
        servo_id (uint8): 舵机编号，范围为[1:3]

    Returns:
        int: 舵机角度，精确度为 0.1 度

    Example:
        >>> angle = servo_ctrl.get_angle(1)
        # 获取编号为 1 的舵机旋转角度
    """
    return 0

def set_angle(servo_id, angle, wait_for_complete) -> None:
    """设置舵机旋转角度

    Args:
        servo_id (uint8): 舵机编号，范围为[1:3]
        angle (int32): 旋转角度，精确度为 0.1 度，正数为顺时针旋转，负数为逆时针旋转
        wait_for_complete (bool): 是否等待执行完成，默认为 True

    Returns:
        None: 无

    Example:
        >>> servo_ctrl.set_angle(1, 900, True)
        # 设置编号为 1 的舵机顺时针旋转 90°，等待执行完成
    """
    return None

def recenter(servo_id, wait_for_complete) -> None:
    """设置舵机回中

    Args:
        servo_id (uint8): 舵机编号，范围为[1:3]
        wait_for_complete (bool): 是否等待执行完成，默认为 True

    Returns:
        None: 无

    Example:
        >>> servo_ctrl.recenter(1, True)
        # 设置编号为 1 的舵机回中，等待执行完成
    """
    return None

def set_speed(servo_id, speed) -> None:
    """设置舵机旋转速度

    Args:
        servo_id (uint8): 舵机编号，范围为[1:3]
        speed (int32): 旋转速度，精确度为 1 度/秒，正数为顺时针旋转，负数为逆时针旋转

    Returns:
        None: 无

    Example:
        >>> servo_ctrl.set_speed(1, 5)
        # 设置编号为 1 的舵机顺时针旋转，旋转速度为 5 度/秒
    """
    return None
