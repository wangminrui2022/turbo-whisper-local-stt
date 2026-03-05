---
name: turbo-whisper-local-stt
description: 本地高性能音频转文本工具，使用 Faster-Whisper large-v3-ct2 模型。支持中文优先、长音频 VAD 分段、GPU 加速（int8_float16），完全离线隐私安全。特别适合会议录音、语音笔记、视频字幕等中文音频场景。
version: 1.0.0
author: 自定义
tags: [speech-to-text, whisper, 音频转录, 中文语音, 本地AI, GPU加速, 隐私保护]
---

## 🎯 什么时候使用本 Skill
当用户提供音频文件（wav/mp3/m4a 等）或音频文件夹，需要转为文字时立即调用。特别适用于以下场景：
* 需要高准确率的中文转录。
* 处理较长音频（内置 VAD 静音检测）。
* 要求完全本地化处理以保障隐私安全。
* 需要获取结构化输出（完整文本 + 分段信息 + 语言检测）。

> **⚠️ 注意**：如果用户明确要求使用云端 API（如 OpenAI Whisper 官方 API），请**不要**使用本 Skill。

## 🚀 如何调用（Agent 直接执行）

执行任何转录命令前，请先进入工作目录：

http://googleusercontent.com/immersive_entry_chip/0

### 1. 单个音频文件转录
默认自动检测语言。适用于单个指定音频文件的处理。

* **基础调用（使用预设别名或在线仓库名）**：
    
http://googleusercontent.com/immersive_entry_chip/1

* **使用本地已下载的模型路径（无需联网）**：
    
http://googleusercontent.com/immersive_entry_chip/2

* **指定纯文本格式输出**（默认可能包含时间戳等结构化数据，使用 `--output text` 仅输出文本）：
    
http://googleusercontent.com/immersive_entry_chip/3

### 2. 批量处理（目录转录）
当 `--audio_path` 指向一个文件夹时，程序会自动批量处理其中的所有音频文件。

* **默认输出到同级目录**（自动在 `audio_path` 同级创建 `原目录名_transcripts` 文件夹）：
    
http://googleusercontent.com/immersive_entry_chip/4

* **自定义输出目录**（使用 `--output_dir` 指定保存路径）：
    
http://googleusercontent.com/immersive_entry_chip/5

***