---
name: turbo-whisper-local-stt
description: 本地高性能音频转文本工具，使用 Faster-Whisper large-v3-ct2 模型。支持中文优先、长音频 VAD 分段、GPU 加速（int8_float16），完全离线隐私安全。特别适合会议录音、语音笔记、视频字幕等中文音频场景。
version: 1.0.0
author: 自定义
tags: [speech-to-text, whisper, 音频转录, 中文语音, 本地AI, GPU加速, 隐私保护]
---

## 🎯 什么时候使用本 Skill

当用户提供音频文件（wav/mp3/m4a 等）需要转为文字时立即调用，尤其是：
- 需要高准确率的中文转录
- 处理较长音频（支持 VAD 静音检测）
- 要求完全本地处理（隐私敏感）
- 需要结构化输出（完整文本 + 分段 + 语言检测）

**不要使用**：用户明确要求云端 API（如 OpenAI Whisper）时。

## 🚀 如何调用（Agent 直接执行）

```bash
cd ~/.openclaw/skills/faster-whisper-local-stt
1、使用简洁别名
python scripts\transcribe.py --audio_path "F:/TestOutput/test.wav" --model large-v3-ct2 
2、测试自动检测语言
python scripts\transcribe.py --audio_path "F:/TestOutput/test.wav" --model wangminrui2022/faster-whisper-large-v3-ct2
3、测试手动模型路径
python scripts\transcribe.py --audio_path "F:/TestOutput/test.wav" --model_path "D:/faster-whisper-large-v3-ct2" 
4、批量目录
#自动在同级创建 原目录名_transcripts 文件夹
python scripts\transcribe.py --audio_path "F:/TestOutput"  --model wangminrui2022/faster-whisper-large-v3-ct2
#指定输出目录
python scripts\transcribe.py --audio_path "F:/TestOutput" --output_dir "F:/TestOutput/transcripts" --model wangminrui2022/faster-whisper-large-v3-ct2 
#使用指定本地模型
python scripts\transcribe.py --audio_path "F:/TestOutput" --output_dir "F:/TestOutput/transcripts" --model_path "D:/faster-whisper-large-v3-turbo-ct2" 
5、测试文本输出
python scripts\transcribe.py --audio_path "F:/TestOutput/test.wav" --model wangminrui2022/faster-whisper-large-v3-ct2  --output text
6、直接写完整仓库名
python scripts\transcribe.py --audio_path "F:/TestOutput/test.wav" --model wangminrui2022/faster-whisper-large-v3-ct2 