# Dropdown.py
# @doc docs/python/custom_ui_doc/Dropdown.rst
# @export_name dropdown_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

from .Common import Common


class Dropdown(Common):
    """下拉框控件"""

    def __init__(self) -> None:
        pass

    def set_options(self, *options: str) -> None:
        """
        设置下拉框中的内容，输入为字符串列表，列表中元素个数为下拉框选项个数

        Args:
            options (tuple[str]): 下拉框中的选项内容，可变参数

        Returns:
            None: 无

        Example:
            >>> my_Dropdown.set_options('RoboMaser EP', 'People')
            # 下拉框中有两个选项，分别为 ``RoboMaster EP`` 与 ``People``
        """

        return None

    def set_background_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置下拉框中选中的条目的背景色

        Args:
            r (int): 背景颜色的 r 值，范围为[0, 255]
            g (int): 背景颜色的 g 值，范围为[0, 255]
            b (int): 背景颜色的 b 值，范围为[0, 255]
            a (int): 背景颜色的透明度，范围为[0, 255]

        Returns:
            None: 无

        Example:
            >>> my_DropDown.set_background_color(200, 200, 200, 230)
            # 设置下拉框中选中的条目的背景色的 rgb 值为(200, 200, 200) ，透明度为 230
        """

        return None

    def set_arrow_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置下拉框选箭头的颜色

        Args:
            r (int): 箭头颜色的 r 值，范围为[0, 255]
            g (int): 箭头颜色的 g 值，范围为[0, 255]
            b (int): 箭头颜色的 b 值，范围为[0, 255]
            a (int): 箭头颜色的透明度，范围为[0, 255]

        Returns:
            None: 无

        Example:
            >>> my_Dropdown.set_arrow_color(120, 120, 120, 200)
            # 设置下拉框选中箭头颜色的 rgb 值为（120, 120, 120），透明度为 200
        """

        return None

    def set_item_background_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置下拉框中未被选择的条目的背景色

        Args:
            r (int): 背景颜色的 r 值，范围为[0, 255]
            g (int): 背景颜色的 g 值，范围为[0, 255]
            b (int): 背景颜色的 b 值，范围为[0, 255]
            a (int): 背景颜色的透明度，范围为[0, 255]

        Returns:
            None: 无

        Example:
            >>> my_DropDown.set_item_background_color(200, 200, 200, 230)
            # 设置下拉框中未被选择的条目的背景色的 rgb 值为(200, 200, 200) ，透明度为 230
        """

        return None

    def set_item_checkmark_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置下拉框中选中图标的颜色

        Args:
            r (int): checkmark颜色的 r 值，范围为[0, 255]
            g (int): checkmark颜色的 g 值，范围为[0, 255]
            b (int): checkmark颜色的 b 值，范围为[0, 255]
            a (int): checkmark 颜色的透明度，范围为[0, 255]

        Returns:
            None: 无

        Example:
            >>> my_DropDown.set_item_checkmark_color(200, 200, 200, 230)
            # 设置下拉框中 checkmark 颜色的 rgb 值为(200, 200, 200) ，透明度为 230
        """

        return None

