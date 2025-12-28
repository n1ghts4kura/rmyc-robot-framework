# Button.py
# @doc docs/python/custom_ui_doc/Button.rst
# @export_name button_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

from typing import Optional

from .Common import Common
from .utils import text_anchor


class Button(Common):
    """
    按钮控件
    """

    def __init__(self) -> None:
        pass

    def set_text(
        self,
        content: str,
        color: Optional[list[int]] = None,
        align: Optional[int] = text_anchor.upper_left,
        size: Optional[int] = None,
    ) -> None:
        """
        设置按钮对象的文字属性

        Args:
            content (str): 按钮上显示的字符串内容
            color (Optional[list[int]]): 文字颜色的 RGBA 列表，范围为 [0, 255], 可选
            align (Optional[int]): 文字对齐方式，可选
                - ``text_anchor.upper_left`` : 顶端左对齐
                - ``text_anchor.upper_center`` : 顶端居中对齐
                - ``text_anchor.upper_right`` : 顶端右对齐
                - ``text_anchor.middle_left`` : 中部左对齐
                - ``text_anchor.middle_center`` : 中部居中对齐
                - ``text_anchor.middle_right`` : 中部右对齐
                - ``text_anchor.lower_left`` : 底端左对齐
                - ``text_anchor.lower_center`` : 底端居中对齐
                - ``text_anchor.lower_right`` : 底端右对齐
            size (Optional[int]): 字号大小，可选

        Returns:
            None: 无

        Example:
            >>> my_Button.set_text(120, 120, 120, 255, text_anchor.upper_left, 12)
            # 设置文字颜色的 rgb 值为（120, 120, 120），透明度为 255，文字对齐方式为顶端左对齐，字号大小为 12 号
        """

        return None

    def set_text_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置文字的颜色

        Args:
            r (int): 文字颜色的 r 值，范围为 [0, 255]
            g (int): 文字颜色的 g 值，范围为 [0, 255]
            b (int): 文字颜色的 b 值，范围为 [0, 255]
            a (int): 文字颜色的透明度，范围为 [0, 255]

        Returns:
            None: 无

        Example:
            >>> my_button.set_text_color(120, 120, 120, 200)
            # 设置文字颜色的 rgb 值为（120, 120, 120），透明度为 200
        """

        return None

    def set_text_align(self, align: int) -> None:
        """
        设置文字的对齐方式

        Args:
            align (int): 文字的对齐方式
                - ``text_anchor.upper_left`` : 顶端左对齐
                - ``text_anchor.upper_center`` : 顶端居中对齐
                - ``text_anchor.upper_right`` : 顶端右对齐
                - ``text_anchor.middle_left`` : 中部左对齐
                - ``text_anchor.middle_center`` : 中部居中对齐
                - ``text_anchor.middle_right`` : 中部右对齐
                - ``text_anchor.lower_left`` : 底端左对齐
                - ``text_anchor.lower_center`` : 底端居中对齐
                - ``text_anchor.lower_right`` : 底端右对齐

        Returns:
            None: 无

        Example:
            >>> my_button.set_text_align(text_anchor.upper_left)
            # 设置文字的对齐方式为顶端左对齐
        """

        return None

    def set_text_size(self, size: int) -> None:
        """
        设置文字的字号大小

        Args:
            size (int): 文字的字号值

        Returns:
            None: 无

        Example:
            >>> my_button.set_text_size(12)
            # 设置文字的字号为 12 号
        """

        return None

    def set_background_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置按钮的背景色

        Args:
            r (int): 字体颜色的 r 值，范围为 [0, 255]
            g (int): 字体颜色的 g 值，范围为 [0, 255]
            b (int): 字体颜色的 b 值，范围为 [0, 255]
            a (int): 字体颜色的透明度，范围为 [0, 255]

        Returns:
            None: 无

        Example:
            >>> my_button.set_background_color(200, 200, 200, 230)
            # 设置背景色的 rgb 值为 (200, 200, 200)，透明度为 230
        """

        return None
