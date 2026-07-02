---
name: reference_sync
description: vault 的 git 同步方式与跨设备(Win/Mac)注意事项
type: reference
---

Vault 本身是 git 仓库,远端 origin = https://github.com/danieldongzy-boop/Notes.git,主分支 main。

**跨设备同步:** Windows 和 Mac 两台设备都通过 git push / pull 同步这个 vault(不是靠本地路径互通)。Claude 的记忆放在 vault 内的 `claude-memory/` 文件夹,因此随 git 一起同步,两边 pull 后即一致。

**重要约束:** 记忆内容里**不要写死本地绝对路径**(Win 是 `D:\Obsidian\...`,Mac 是 `/Users/zaynndong/obsidian/...`,不通用)。引用 vault 内文件时用相对于 vault 根的相对路径(如 `IC/NSsar/xxx.md`)。

**注意:** Windows 侧的物理文件删除受 Cowork 沙箱限制,可能需用户手动在资源管理器删除;git 层面的移除(git rm)照常有效。
