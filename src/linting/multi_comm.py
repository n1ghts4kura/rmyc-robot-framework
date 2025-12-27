# multi_comm.py
# @doc docs/python/multi_comm.rst
# @export_name multi_comm_ctrl
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

from typing import Any

def set_group(send_group, recv_group_list) -> None:
    """设置机器的组号为 ``send_group`` ，机器可以接收来自 ``recv_group_list`` 中注册的组号的消息。如果不使用 ``recv_group_list`` 参数，默认接收组号 0 的消息

    Args:
        send_group (int): 当前机器的发送组号，默认组号为 0
        recv_group_list (list/tuple): 当前接收消息的组别列表，类型可以为列表或元组

    Returns:
        None: 无

    Example:
        >>> multi_comm_ctrl.set_group(1, (1,2,3))
        # 设置当前发送组号为 1， 接收组号 1,2,3 的消息，若接收组别包含发送组别，则会接收到自己发送的消息
    """
    return None

def send_msg(msg, group) -> None:
    """通过多机通信发送消息，可以单独设置该消息的发送组号

    Args:
        msg (int): 需要发送的消息
        group (int): 可选参数，指定当前消息发送组号，不指定则默认使用之前设置的组号

    Returns:
        None: 无

    Example:
        >>> multi_comm_ctrl.send_msg('RoboMaster EP', 3)
        # 向组号 3 发送消息 ``'RoboMaster EP'``
    """
    return None

def recv_msg(timeout) -> Any:
    """接收消息（当没有注册`recv_callback`时生效），可设置超时时间

    Args:
        timeout (int): 等待时间，接收函数等待的时间，精确度为 1 秒，默认为 72 秒

    Returns:
        Any: ``<msg_group>, <msg>`` 消息发送方的组号和消息内容

    Example:
        >>> group, recv_msg = multi_comm_ctrl.recv_msg(30)
        # 接收消息，等待时间为 30 秒，group 为信息发送方的组号，msg 为收到的消息内容
    """
    return None

def register_recv_callback(callback) -> None:
    """注册接收消息的回调函数，当接收到信息后，自动执行回调函数

    Args:
        callback (function): 需要注册的回调函数, 回调函数原型为 ``def callback(msg)``，其中 ``msg`` 参数类型为元组 ``(msg_group, msg)``

    Returns:
        None: 无

    Example:
        >>> multi_comm_ctrl.register_recv_callback(callback)
    """
    return None
