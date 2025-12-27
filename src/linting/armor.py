# armor.py
# @doc docs/python/armor.rst
# @export_name armor_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def cond_wait(condition_enum) -> None:
    """等待机器人受到红外光束攻击时，执行下一条指令

    Args:
        condition_enum (Any): 事件类型，``rm_define.cond_ir_hit_detection`` 表示机器人受到红外光束攻击

    Returns:
        None: 无

    Example:
        >>> armor_ctrl.cond_wait(rm_define.cond_ir_hit_detection)
        # 等待机器人受到红外光束攻击时，执行下一条指令
    """
    return None

def check_condition(condition_enum) -> bool:
    """判断机器人是否受到红外光束攻击

    Args:
        condition_enum (Any): 事件类型，``rm_define.cond_ir_hit_detection`` 表示机器人受到红外光束攻击

    Returns:
        bool: 机器人是否受到红外光束攻击，受到攻击时返回真，否则返回假。

    Example:
        >>> if armor_ctrl.check_condition(rm_define.cond_ir_hit_detection):
        # 如果机器人受到红外光束攻击时，执行下一条指令
    """
    return False
