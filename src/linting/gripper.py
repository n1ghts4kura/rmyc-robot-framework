# gripper.py
# @doc docs/python/gripper.rst
# @export_name gripper_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def open(void) -> None:
    """控制机械爪打开

    Args:
        void (Any): 无

    Returns:
        None: 无

    Example:
        >>> gripper_ctrl.open()
        # 控制机械爪打开
    """
    return None

def close(void) -> None:
    """控制机械爪关闭

    Args:
        void (Any): 无

    Returns:
        None: 无

    Example:
        >>> gripper_ctrl.close()
        # 控制机械爪关闭
    """
    return None

def stop(void) -> None:
    """控制机械爪停止运动

    Args:
        void (Any): 无

    Returns:
        None: 无

    Example:
        >>> gripper_ctrl.stop()
        # 控制机械爪停止运动
    """
    return None

def update_power_level(level) -> None:
    """设置机械爪力度档位

    Args:
        level (int): 机械爪的力度档位，范围为[1:4]档，默认为 1

    Returns:
        None: 无

    Example:
        >>> gripper_ctrl.update_power_level(1)
        # 设置机械爪力度档位为 1
    """
    return None

def is_closed(void) -> bool:
    """获取机械爪夹紧状态

    Args:
        void (Any): 无

    Returns:
        bool: 机械爪夹紧状态，若机械爪夹紧则返回 true，否则返回 false

    Example:
        >>> ret = gripper_ctrl.is_closed()
        # 获取机械爪夹紧状态
    """
    return False

def is_open(void) -> bool:
    """获取机械爪张开状态

    Args:
        void (Any): 无

    Returns:
        bool: 机械爪张开状态，若机械爪完全张开则返回 true，否则返回 false

    Example:
        >>> ret = gripper_ctrl.is_open()
        # 获取机械爪张开状态
    """
    return False
