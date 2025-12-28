# Toggle.py
# @doc docs/python/custom_ui_doc/Toggle.rst
# @export_name toggle_object
# 本文件由自动脚本生成，用于提供 linting/补全，真实逻辑请在原生环境实现

from .Common import Common
from .utils import text_anchor


class Toggle(Common):
    """开关控件"""

    def __init__(self) -> None:
        pass

    def set_text(
        self,
        string: str,
        color: list[int] | None = None,
        align: int = text_anchor.upper_left,
        size: int | None = None,
    ) -> None:
        """
        设置开关控件的文字属性

        Args:
            string (str): 控件上显示的字符串内容
            color (list[int] | None): 文字颜色 RGBA 列表，范围为 [0, 255]，可选
            align (int | None): 文字对齐方式，详细见 :data:`align`
            size (int | None): 显示文字的字号大小

        Returns:
            None: 无

        Example:
            >>> my_Toggle.set_text(120, 120, 120, 200, text_anchor.upper_left, 12)
            # 设置文字的 rgb 值为（120, 120, 120），透明度为 200，字体对齐方式为顶端左对齐，字号大小为 12 号
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
            >>> my_Toggle.set_text_color(120, 120, 120, 200)
            # 设置字体的 rgb 值为（120, 120, 120），透明度为 200
        """

        return None

    def set_text_align(self, align: int) -> None:
        """
        设置文字的对齐方式

        Args:
            align (int): 文字对齐方式，详见 :data:`align`

        Returns:
            None: 无

        Example:
            >>> my_Toggle.set_text_align(text_anchor.upper_left)
            # 设置字体的对齐方式为顶端左对齐
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
            >>> my_Toggle.set_text_size(12)
            # 设置文字的字号为 12 号
        """

        return None

    def set_background_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置控件的背景色

        Args:
            r (int): 背景颜色的 r 值，范围为 [0, 255]
            g (int): 背景颜色的 g 值，范围为 [0, 255]
            b (int): 背景颜色的 b 值，范围为 [0, 255]
            a (int): 背景颜色的透明度，[0, 255]

        Returns:
            None: 无

        Example:
            >>> my_Toggle.set_background_color(200, 200, 200, 230)
            # 设置背景色的 rgb 值为 (200, 200, 200)，透明度为 230
        """

        return None

    def set_checkmark_color(self, r: int, g: int, b: int, a: int) -> None:
        """
        设置控件选中图标的颜色

        Args:
            r (int): 图标颜色的 r 值，范围为 [0, 255]
            g (int): 图标颜色的 g 值，范围为 [0, 255]
            b (int): 图标颜色的 b 值，范围为 [0, 255]
            a (int): 图标颜色的透明度，范围为 [0, 255]

        Returns:
            None: 无

        Example:
            >>> my_Toggle.set_checkmark_color(200, 200, 200, 230)
            # 设置选中图标的 rgb 值为 (200, 200, 200)，透明度为 230
        """

        return None

    def set_is_on(self, status: bool) -> None:
        """
        设置控件的状态

        Args:
            status (bool): 设置控件是否为打开状态，True 表示打开，False 表示关闭

        Returns:
            None: 无

        Example:
            >>> my_Toggle.set_is_on(True)
            # 设置 Toggle 控件为打开状态
        """

        return None
