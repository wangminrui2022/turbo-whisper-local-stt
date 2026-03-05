#!/usr/bin/env python3
# -*- coding: utf-8, -*-

"""
Skill Name: PureVocals_UVR_Automator
Author: 王岷瑞/https://github.com/wangminrui2022
License: Apache License
Description: 自动安装缺失 Python 包的便捷工具函数（国内清华镜像加速）
主要功能：
    1. 检查目标包/模块是否已可导入
    2. 如果缺失，则使用清华镜像自动安装（只安装一次）
    3. 支持深层导入路径检查（如 apscheduler.schedulers.blocking.BlockingScheduler）
    4. 支持指定版本约束安装（如 urllib3<2、requests>=2.28.0）

使用场景：
    - 写一次性脚本、Jupyter Notebook、分享给别人的 .py 文件
    - 不想在开头写一堆 !pip install 或 requirements.txt
    - 希望脚本拿来就能跑，不依赖事先安装环境
"""

import sys
import subprocess

def pip(pip_pkg, import_name=None, sub_import=None):
    """
    自动检查并安装包（带清华源，只装一次）
    - pip_pkg: pip 安装名（如 "apscheduler"）
    - import_name: 导入路径（如 "apscheduler.schedulers.blocking"）
    - sub_import: 子对象名（如 "BlockingScheduler"）
    """
    if import_name is None:
        import_name = pip_pkg
    try:
        # 支持深层路径：逐步导入子模块
        parts = import_name.split('.')
        mod = __import__(parts[0])  # 顶层模块
        for part in parts[1:]:
            mod = getattr(mod, part)  # 逐步深入
        if sub_import:
            getattr(mod, sub_import)  # 检查子对象
        return  # 已存在，跳过
    except (ImportError, AttributeError):
        print(f"🔧 正在安装 {pip_pkg} ...（首次运行会慢一点）")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "--upgrade", pip_pkg,
            "-i", "https://pypi.tuna.tsinghua.edu.cn/simple",
            "--quiet"
        ])
        print(f"✅ {pip_pkg} 安装完成！")

def pip_v(pkg, version=None):
    #ensure_package.pip_v("urllib3", version="<2")
    """支持指定版本约束，如 urllib3 <2"""
    import_name = pkg  # 默认导入名同 pip 名 
    try:
        __import__(import_name)
        print(f"✅ {pkg} 已安装")
        return
    except ImportError:
        install_str = pkg
        if version:
            install_str += version  # 如 "urllib3<2"
        print(f"🔧 正在安装 {install_str} ...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            install_str,
            "-i", "https://pypi.tuna.tsinghua.edu.cn/simple",
            "--quiet"
        ])
        print(f"✅ {pkg} 安装完成！")