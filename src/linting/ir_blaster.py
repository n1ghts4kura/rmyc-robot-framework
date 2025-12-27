# ir_blaster.py
# @doc docs/python/ir_blaster.rst
# @export_name ir_blaster_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def set_fire_count(color_enum) -> None:
    """设置红外光束的发射频率，即每秒射出的红外光束次数

    Args:
        color_enum (int): 发射频率，即每秒射出的红外光束次数，范围为[1:8]

    Returns:
        None: 无

    Example:
        >>> ir_blaster_ctrl.set_fire_count(4)
        # 设置红外光束的发射频率为 4
    """
    return None

def fire_once(void) -> None:
    """控制发射器只发射一次红外光束

    Args:
        void (Any): 无

    Returns:
        None: 无

    Example:
        >>> ir_blaster_ctrl.fire_once()
        # 控制发射器只发射一次红外光束
    """
    return None

def fire_continuous(void) -> None:
    """控制发射器持续发射红外光束

    Args:
        void (Any): 无

    Returns:
        None: 无

    Example:
        >>> ir_blaster_ctrl.fire_continuous()
        # 控制发射器持续发射红外光束
    """
    return None

def stop(void) -> None:
    """停止发射红外光束

    Args:
        void (Any): 无

    Returns:
        None: 无

    Example:
        >>> ir_blaster_ctrl.stop()
        # 停止发射红外光束
    """
    return None
