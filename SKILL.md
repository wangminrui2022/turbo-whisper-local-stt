---
name: turbo-whisper-local-stt
description: |-
  本地高性能音频转文本工具，使用 Faster-Whisper large-v3-ct2 模型。
  支持中文优先、长音频 VAD 分段、GPU 加速（int8_float16），完全离线隐私安全。
  特别适合会议录音、语音笔记、视频字幕等中文音频场景。
metadata:
  openclaw:
    requires:
      bins:
        - python
---

# Turbo-Whisper-Local-STT

**功能**：当用户提供音频文件（wav/mp3/m4a 等）或音频文件夹，需要转为文字时立即调用。特别适用于以下场景：
* 需要高准确率的中文转录。
* 处理较长音频（内置 VAD 静音检测）。
* 要求完全本地化处理以保障隐私安全。
* 需要获取结构化输出（完整文本 + 分段信息 + 语言检测）。

## 支持的模型（推荐顺序）
1. **faster-whisper-base-ct2** → 默认推荐（低配设备 / 追求极速）
2. **faster-whisper-large-v3-ct2** → 高精度需求 / 会议转录
3. **faster-whisper-large-v3-turbo-ct2** → 性能与精度的平衡点

## 执行步骤
1. **解析目录**：识别用户的源路径（支持单个音频文件或整个文件夹）。
2. **默认目标**：若未指定输出路径，默认在输入同级创建 `[源文件名].json/.txt` 文件。
3. **调用命令**：使用以下兼容性命令启动脚本（优先 python3，失败则 python）。脚本会自动创建虚拟环境、检测 GPU 并安装对应版本。

   ```bash
   (python3 scripts/transcribe.py --audio_path "<音频路径>" [--output_dir "<输出目录>"] [--language <zh/en>] [--model_path "<模型路径>"] [--output <json/text>] [--beam_size 5] [--separator " "]) || (python scripts/transcribe.py --audio_path "<音频路径>" [--output_dir "<输出目录>"] [--language <zh/en>] [--model_path "<模型路径>"] [--output <json/text>] [--beam_size 5] [--separator " "])

