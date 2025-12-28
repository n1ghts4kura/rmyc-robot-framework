# uart.py
# @doc docs/python/uart.rst
# @export_name serial_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现
from typing import Optional

def serial_config(baud_rate, data_bit, odd_even_crc, stop_bit) -> None:
    """设置串口的波特率、数据位、校验位以及停止位属性

    Args:
        baud_rate (Any): 设置波特率，可选波特率为 9600、19200、38400、57600、115200
        data_bit (Any): 设置数据位，可选的数据位为 cs7、cs8
        odd_even_crc (Any): 设置奇偶校验，详细见表格 :data:`odd_even_crc`
        stop_bit (Any): 设置停止位，可选的停止位为 1、2

    Returns:
        None: 无

    Example:
        >>> serial_ctrl.serial_config(9600, 'cs8', 'none', 1)
        # 设置串口的波特率为 9600，数据位 8 位，不使用奇偶校验，停止位为 1 位
    """
    return None

def write_line(msg_string) -> None:
    """发送字符串信息，自动添加换行 ``'\n'``

    Args:
        msg_string (string): 需要发送的字符串信息，发送时字符串后自动添加 ``'\n'``

    Returns:
        None: 无

    Example:
        >>> serial_ctrl.write_line('RoboMaster EP')
        # 向串口写入 ``'RoboMaster EP\n'`` ，最后的换行自动添加，用户只需要发送 ``'RoboMaster EP'``
    """
    return None

def write_string(msg_string) -> None:
    """发送字符串信息

    Args:
        msg_string (string): 需要发送的字符串信息

    Returns:
        None: 无

    Example:
        >>> serial_ctrl.write_string('RoboMaster EP')
        # 向串口写入 ``'RoboMaster EP'``
    """
    return None

def write_number(value) -> None:
    """将数字参数转换成字符串，并通过串口发送出去

    Args:
        value (int): 需要发送的值

    Returns:
        None: 无

    Example:
        >>> serial_ctrl.write_number(12)
        # 向串口中写入字符串 ``'12'``
    """
    return None

def write_numbers(value1, value2, value3) -> None:
    """将数字列表转换成字符串，并通过串口发送出去

    Args:
        value1 (int): 需要发送数字列表的值
        value2 (int): 需要发送数字列表的值
        value3 (int): 需要发送数字列表的值

    Returns:
        None: 无

    Example:
        >>> serial_ctrl.write_numbers(12,13,14)
        # 向串口中写入字符串 ``'12,13,14'``
    """
    return None

def write_value(key, value) -> None:
    """将参数以键值对的形式组成字符串，并通过串口发送出去

    Args:
        key (string): 需要发送的关键字
        value (int): 需要发送的值

    Returns:
        None: 无

    Example:
        >>> serial_ctrl.write_value('x', 12)
        # 向串口中写入字符串 ``'x:12'``
    """
    return None

def read_line(timeout=None) -> str:
    """从串口中读取以 ``'\n'`` 结尾的字符串

    Args:
        timeout (Optional[float]): 可选，超时时间，单位为秒，默认为永久阻塞

    Returns:
        str: 通过串口读取到的字符串

    Example:
        >>> recv = serial_ctrl.read_line()
        # 从串口读取一行以 ``'\n'`` 结尾的字符串
    """
    return ""

def read_string(timeout=None) -> str:
    """从串口中读取字符串（字符串可以不以 ``'\n'`` 结尾）

    Args:
        timeout (Optional[float]): 可选，超时时间，单位为秒，默认为永久阻塞

    Returns:
        str: 通过串口读取到的字符串

    Example:
        >>> recv = serial_ctrl.read_string()
        # 从串口读取一个字符串
    """
    return ""

def read_until(stop_sig, timeout=None) -> str:
    """从串口中读取字符串，直到匹配到指定的结束字符 ``'stop_sig'``

    Args:
        stop_sig (Any): 指定的结束字符，参数类型为字符，范围为[ ``'\n'`` | ``'$'`` | ``'#'`` | ``'.'`` | ``':'`` | ``';'`` ]
        timeout (Optional[float]): 可选，超时时间，单位为秒，默认为永久阻塞

    Returns:
        str: 通过串口读取到的匹配字符串

    Example:
        >>> serial_ctrl.read_until('#')
        # 从串口中读取字符串，直到匹配到 ``'#'`` 停止读取
    """
    return ""
