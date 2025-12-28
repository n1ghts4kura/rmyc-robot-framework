# sensor_adapter.py
# @doc docs/python/sensor_adapter.rst
# @export_name sensor_adapter_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

def get_sensor_adapter_adc(board_id, port_num, wait_for_complete) -> int:
    """获取传感器转接模块相应端口模拟引脚的 ADC 值

    Args:
        board_id (int): 传感器转接模块编号，范围为[1:6]
        port_num (uint8): 传感器转接模块上的端口号，范围为[1:2]
        wait_for_complete (bool): 是否等待执行完成，默认为 True

    Returns:
        int: 传感器转接模块相应端口模拟引脚的 ADC 值，范围为[0:1023]

    Example:
        >>> ret = sensor_adapter_ctrl.get_sensor_adapter_adc(1, 2)
        # 获取 1 号传感器转接模块 2 号端口模拟引脚的 ADC 值
    """
    return 0

def get_sensor_adapter_pulse_period(board_id: int, port_num: int) -> int:
    """获取传感器转接模块相应端口引脚的脉冲持续时间

    Args:
        board_id (int): 传感器转接模块编号，范围为[1:6]
        port_num (uint8): 传感器转接模块上的端口号，范围为[1:2]

    Returns:
        int: 传感器转接模块相应端口引脚的脉冲持续时间，精确度为 1 ms

    Example:
        >>> ret = sensor_adapter_ctrl.get_sensor_adapter_pulse_period(1, 2)
        # 获取 1 号传感器转接模块 2 号端口引脚脉冲持续时间
    """
    return 0

def cond_wait(condition: str) -> None:
    """等待传感器转接模块相应端口引脚脉冲为（高/低/跳变）时，执行下一条指令

    Args:
        condition (str): 事件条件字符串，形如 ``rm_define.cond_sensor_adapter[board_id]_port[port_id]_[judge_type]_event``

    Returns:
        None: 无

    Example:
        >>> sensor_adapter_ctrl.cond_wait(rm_define.cond_sensor_adapter1_port2_high_event)
        # 等待 1 号传感器转接模块 2 号端口引脚为高电平时，执行下一条指令
    """
    return None

def check_condition(condition: str) -> bool:
    """判断传感器转接模块相应端口引脚脉冲是否为（高/低/跳变）

    Args:
        condition (str): 事件条件字符串，形如 ``rm_define.cond_sensor_adapter[board_id]_port[port_id]_[judge_type]_event``

    Returns:
        bool: 是否满足条件，满足条件时返回真，否则返回假。

    Example:
        >>> sensor_adapter_ctrl.check_condition(rm_define.cond_sensor_adapter1_port2_trigger_event)
    """
    return False
