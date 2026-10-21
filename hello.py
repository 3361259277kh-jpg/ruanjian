# -*- coding: utf-8 -*-
"""一个简单的示例代码文件，用于验证 GitHub 仓库可以正常提交代码。

运行：python hello.py
"""


def hello(name: str = "GitHub") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello())
    print("第一个代码文件上传成功。")
