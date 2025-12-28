# robot.py
# @doc docs/python/robot.rst
# @export_name robot_ctrl
# 以上所有信息均出自 src/linting/robot.py

def get_battery_percentage() -> int:
    """
    获取机器人当前电量百分比

    Returns:
        int: 当前电量百分比，(0, 100]

    Example:
        >>> get_battery_percentage()
        85
    """
    # pass
    return 0 # 因为需要标注返回值类型为 int 所以这里不使用pass 返回一个虚假值
