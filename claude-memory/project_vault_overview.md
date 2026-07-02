---
name: project_vault_overview
description: Obsidian vault 的结构、已清理项、以及需要小心的坑
type: project
---

**结构:**
- `IC/` — 核心学习区,按主题分:SARADC、NSsar、AMP、DAC、data converter、noise、比较器、开关、BGR、Jitter、Sunnan_ADC、实例;还有"ADC 教程 李福乐 清华大学"。`IC/Linux/` 是真实 Cadence Spectre 仿真工程(含 8-bit SAR ADC、ADI ADA4528 opamp 等)。
- `Uni Freiburg/` — 弗莱堡课程:Analog Cmos、RF_Design、data converter、Test and reliability(按 CH1-CH4 分章,每章有课件/习题 PDF + 中英对照笔记)、Imma、能量收集、居留。
- `xdu/` — 西电本科作业(模集、fab homework、物联网大作业)。
- `Marvis的输出/` — 保留的 AI 生成技术综述(NS-SAR、CMFB、Ahuja/Cascode 补偿、SAR 数字校准等),用户认为有用。
- `claude-memory/` — Claude 的记忆(本文件夹)。

**已清理(2026-07-02):** 删除了 copilot/(旧 Copilot 对话与 gpt-5.5 记忆)、codex/(空)、..push_result.txt(旧自动化脚本产物);并加入 .gitignore。

**Why:** 用户不再用 Obsidian Copilot,之前多个 AI 把统计/产物文件弄乱了。

**坑(重要):**
- `IC/Linux/**` 下大量 `.state` / `ADE_state.info` / `.oalib` 是 Cadence 仿真状态文件,**不是 AI 垃圾,绝不能删**。
- 曾出现 `.git/index.lock` 残留导致 git index 被清空、所有文件误显示为 deleted;用 `git reset HEAD`(不加 --hard)从 HEAD 重建 index 即可修复,物理文件不受影响。以后遇到全量"D"先怀疑 index 损坏,不要直接提交。

**How to apply:** 新笔记写进对应 `IC/<主题>/` 或课程章节文件夹;涉及 git 时保护敏感文件、先检查 index 完整性。
