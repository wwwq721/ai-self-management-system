---
title: "FILE-AUDIT-RECORDS.md - 文件读取审计记录"
summary: "文件读取审计规范——记录读了什么、读到什么程度并避免虚报"
importance: 4
platform: common
created_at: 2026-07-27
requested_by: WorkBuddy
---

# 文件读取审计记录

> 每次处理文件集时，如实标注每个文件的读取状态：FULL READ（已读全部内容）、PARTIAL READ（只读了部分）、NOT READ（只读了文件名/列表）、SCANNED（扫描件无法提取文字）。
> 四种读取状态的**唯一定义在 [OPERATIONS.md](OPERATIONS.md) 第 8 节**；本文件只记审计原则。

## 审计原则

1. 对每个文件，先判断能否直接提取文字（pdfplumber → pypdf → 渲染OCR）
2. CAD矢量图：标注为"NOT READ - 纯矢量CAD图，无可提取文字"
3. 扫描件：标注为"NOT READ - 纯扫描PDF，需OCR"
4. 读取失败必须记录原因，不得虚报
5. 同名重复文件标注为NOT READ - 重复


