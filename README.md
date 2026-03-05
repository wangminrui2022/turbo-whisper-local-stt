# 🚀 faster-whisper-local-stt

**高性能本地音频转文本工具**  
基于 **Faster-Whisper**（large-v3 / turbo 等模型），专为 OpenClaw Skill 开发，也支持独立命令行使用。支持单文件与**整个目录批量转录**，自动保留目录结构，输出 `.txt` 或极简 `.json` 文件。

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GPU](https://img.shields.io/badge/GPU-CUDA%2011.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ 核心特性

- ✅ **单文件 / 批量目录** 一键处理（递归遍历子文件夹）
- ✅ **自动下载模型**（`--model large-v3` 首次自动从 Hugging Face 下载，永久缓存）
- ✅ **输出格式灵活**：
  - `--output txt` → 纯文本 `.txt`
  - `--output json` → 严格格式 `{"success": true, "text": "..."}`
- ✅ **完全保留原目录结构**（`输入/子文件夹/音频.wav` → `输出/子文件夹/音频.txt`）
- ✅ **中文优先优化** + VAD 静音检测 + 长音频智能分段
- ✅ **自动释放显存**，支持 GPU（int8_float16）与 CPU
- ✅ **OpenClaw 完美集成**（env_manager / ensure_package / config）
- ✅ **隐私安全**：全部本地运行，无需联网（下载后离线）

## 📁 项目结构

faster-whisper-local-stt/
├── scripts/
│   └── transcribe.py          # 主脚本（已集成所有功能）
├── models/                    # 自动下载的模型存放目录
├── SKILL.md                   # OpenClaw Skill 元数据
├── requirements.txt
├── README.md                  # 你正在看的文档
└── ...（你的 OpenClaw 配置文件）


## 🚀 快速安装

### 方式一：作为 OpenClaw Skill（推荐）
1. 把整个文件夹放到 `~/.openclaw/skills/faster-whisper-local-stt/`
2. 运行一次脚本（会自动安装依赖）

### 方式二：独立使用
```bash
git clone https://github.com/你的用户名/faster-whisper-local-stt.git
cd faster-whisper-local-stt
pip install -r requirements.txt