---
title: "USER.md - 用户档案"
summary: "用户档案——用户背景、隐私偏好与沟通偏好"
importance: 3
platform: common
created_at: <YYYY-MM-DD>
read_when:
  - Bootstrapping a workspace manually
---

# USER.md - About Your Human

> **示例模板，不含真值。** 本文件与 `MEMORY.md`、`IDENTITY.md` 一样**不入公开库**：它们被平台按固定路径注入每个会话（注入通道见 [MACHINE.md](../MACHINE.md) 及其软件文件），就地改成占位会让每个会话都丢掉用户背景，所以走「真值留本机、库里只放样例」。
> 用法：复制本文件到治理根为 `USER.md` 再填真值；填好的真值**不要**提交回库（见 [GIT.md](../GIT.md)「排除版本控制的内容」）。

## 速写字段

- **Name:** —— 按用户意愿填；对方未提供就不主动收集（判据见「隐私偏好」）
- **What to call them / Pronouns / City:** —— 可留空
- **Notes:** —— 一句话：与这位用户协作时最容易出错的地方

## Context

只写**会改变回答方式**的事实：知识背景（决定术语深度与解释起点）、已修课程或熟悉领域、能承受的信息密度。不写可唯一识别本人的信息。

## 隐私偏好

- **隐私判断标准**：能否通过信息唯一确定用户本人。能唯一确定的（如姓名、家庭住址等）不可记录；不能唯一确定的（如学校、专业等）可以记录。**本机用户名与本机路径不计入**——它们只是环境标识。
- 这条判据同时是 [GIT.md](../GIT.md)「推送前私密性审核」与 `git-workflow` skill（未随公开仓上传）同节的判据来源，两边口径应保持一致。

## 沟通偏好

- 只写**跨项目**的表达与协作偏好；操作行为类规则归 [OPERATIONS.md](../OPERATIONS.md)，人格准则归 [SOUL.md](../SOUL.md)（归类标准见 OPERATIONS.md「治理文件修改流程」第 7 步）。
- 每条写「偏好 + 一句原因或由来」：将来判断该不该改这条时，靠的就是这个原因。
