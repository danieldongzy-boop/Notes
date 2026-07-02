---
name: feedback_vault_workflow
description: 用户 vault 的组织方式,以及 Cowork Project/Task 的映射规则
type: feedback
---

**规则:** 用"文件夹层级 → Cowork 层级"来组织学习。课程/大主题文件夹 → 一个 Project;章节/子主题 → 一个 Task。

**Why:** 同一门课/大主题内部章节有连贯性(如 ATPG 建立在 fault model 上),需要共享上下文,所以放同一个 Project 共享记忆。拆成多个 Project 会切断上下文。

**How to apply:**
- Test & Reliability 这类课:一个 Project 对应整个课程文件夹,CH1/CH2/CH3/CH4 各一个 Task。
- 模拟 IC 这种大领域:不要建一个笼统的大 Project,按 vault 已有模块分:SAR ADC(SARADC+NSsar)、Amplifier(AMP)、Data Converter、Noise 各一个 Project;每个具体子主题(如"CDAC 失配分析""kT/C 噪声预算")一个 Task。
- Task 粒度 ≈ 一次能连续学完的一块内容(一章或一个推导专题)。

**精读节奏(用户偏好):** PDF 当主屏,Claude 当旁边的讲师;让 Claude 直接读 vault 里的 `*_annot.pdf`,用户说"讲第 X 页"即可对齐。循环:用户读几页 → 提问 → Claude 推导讲解 → 把关键结论/推导写回对应章节文件夹的笔记。
