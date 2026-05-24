# Bootstrap Switch 在 ADC 中的应用 —— 顶会/顶刊调研

> 整理日期：2026-05-24 | 聚焦 ISSCC / JSSC / VLSI Symposium / SSC Magazine

---

## 1. 什么是 Bootstrap Switch

在高速高精度 ADC 中，采样开关的导通电阻 $R_{ON}$ 随输入电压 $V_{in}$ 变化：

$$R_{ON} = \frac{1}{\mu C_{ox} \frac{W}{L} (V_{GS} - V_{TH})}$$

$V_{GS}$ 随 $V_{in}$ 漂移 → $R_{ON}$ 非线性 → 谐波失真。**Bootstrap Switch（栅压自举开关）** 通过一个自举电容 $C_b$ 将采样管栅压抬升至 $V_{DD} + V_{in}$，使 $V_{GS}$ 在整个输入范围内恒定，从而消除 $R_{ON}$ 的信号依赖性，实现高线性度采样。

---

## 2. 产业界主流结构与性能全景

| 结构类型 | 分辨率 | 采样率 | 工艺 | 代表工作 | 发表 |
|---------|--------|--------|------|---------|------|
| **经典栅压自举** | 10 bit | 14.3 MS/s | 0.6 μm | Abo & Gray | JSSC 1999 |
| **单调电容切换 SAR + 自举** | 10 bit | 50 MS/s | 0.13 μm | Liu et al. | JSSC 2010 |
| **开关自举 + USPC DAC** | 7 bit | 1.25 GS/s | 28 nm | Ramkaj et al. | JSSC 2018 |
| **双路径自举开关** | 8 bit | 10 GHz (TI) | — | Swindlehurst et al. | JSSC 2021 |
| **自举采样 + Class-AB Buffer** | 8 bit | 56 GS/s (64× TI) | 4 nm | IBM/Samsung | VLSI 2022 |

### 趋势总结

| 维度 | 趋势 |
|------|------|
| **分辨率** | 7–10 bit 为主流（高速场景），更高精度需配合校准或 ΔΣ 架构 |
| **采样率** | 从 14.3 MS/s (1999) → 56 GS/s (2022)，每 7–8 年提升一个数量级 |
| **工艺** | 0.6 μm → 4 nm，先进节点下可靠性问题（栅氧击穿）成为核心挑战 |
| **结构演进** | 单路径 → 双路径 → 多路径，核心是隔离寄生电容、加速栅压建立 |
| **应用** | 无线通信（RF 直采）、SerDes 接收器、数据中心光互联、仪器仪表 |

---

## 3. 核心论文详析（6 篇）

---

### 论文 1（开山之作）

**A 1.5-V, 10-bit, 14.3-MS/s CMOS Pipeline Analog-to-Digital Converter**

| 项目 | 内容 |
|------|------|
| **作者** | Andrew M. Abo, Paul R. Gray (UC Berkeley) |
| **期刊** | IEEE Journal of Solid-State Circuits (JSSC), Vol. 34, No. 5, pp. 599–606, 1999 |
| **引用** | ~950+ |
| **DOI** | 10.1109/4.760369 |

**核心贡献**：首次在低电压（1.5 V）条件下实现了完整的栅压自举开关，并系统解决了器件可靠性问题（栅氧击穿）。采用 clock multiplier 将时钟自举到 $2V_{DD}$ 以驱动预充开关，确保自举电容充分预充到 $V_{DD}$。

**关键参数**：
- 工艺：0.6 μm CMOS
- 分辨率：10 bit，14.3 MS/s
- SNDR：58.5 dB（~9.5 ENOB）
- DNL/INL：< 0.5 / 0.7 LSB
- 功耗：36 mW @ 1.5 V

> 这篇是 Bootstrap Switch 在 ADC 中应用的奠基性工作，几乎后续所有相关论文都会引用。

---

### 论文 2（高引用 SAR ADC）

**A 10-bit 50-MS/s SAR ADC With a Monotonic Capacitor Switching Procedure**

| 项目 | 内容 |
|------|------|
| **作者** | Chun-Cheng Liu, Soon-Jyh Chang, Guan-Ying Huang, Ying-Zu Lin (成功大学) |
| **期刊** | IEEE Journal of Solid-State Circuits (JSSC), Vol. 45, No. 4, pp. 731–740, 2010 |
| **引用** | ~2100+ |
| **DOI** | 10.1109/JSSC.2010.2042254 |

**核心贡献**：提出单调电容切换策略，相比传统 SAR 切换，开关功耗降低 81%，总电容减半。前端采用 Bootstrap Switch 保证采样线性度，是 SAR ADC 领域引用量最高的论文之一。

**关键参数**：
- 工艺：0.13 μm 1P8M CMOS
- 分辨率：10 bit，50 MS/s
- SNDR：57.0 dB（~9.2 ENOB）
- 功耗：0.826 mW @ 1.2 V
- FOM：29 fJ/conv-step（当时最低）
- 面积：195 × 265 μm²

> 这篇文章中使用的 Bootstrap Switch 电路（11 管结构）成为 SAR ADC 设计的标准参考电路，被 Razavi 在 SSC Magazine 教程中详细拆解。

---

### 论文 3（毫米波 RF 采样）

**A 1.25-GS/s 7-b SAR ADC With 36.4-dB SNDR at 5 GHz Using Switch-Bootstrapping, USPC DAC and Triple-Tail Comparator in 28-nm CMOS**

| 项目      | 内容                                                |
| ------- | ------------------------------------------------- |
| **作者**  | Athanasios T. Ramkaj 等                            |
| **期刊**  | IEEE Journal of Solid-State Circuits (JSSC), 2018 |
| **DOI** | 10.1109/JSSC.2018.2866948                         |

**核心贡献**：在 28 nm CMOS 下实现 1.25 GS/s SAR ADC，前端采用 switch-bootstrapping 保证 5 GHz 输入下的线性度。USPC（Unified Switching Probabilistic Control）DAC 和 triple-tail 比较器进一步提升速度与能效。

**关键参数**：
- 工艺：28 nm CMOS
- 分辨率：7 bit，1.25 GS/s
- 输入频率：高达 5 GHz
- SNDR：36.4 dB @ 5 GHz
- 适用场景：毫米波/RF 直接采样前端

> 证明了 Bootstrap Switch 在 28 nm 下仍可实现 RF 频率的线性采样。

---

### 论文 4（10 GHz 时间交织）

**An 8-bit 10-GHz 21-mW Time-Interleaved SAR ADC With Grouped DAC Capacitors and Dual-Path Bootstrapped Switch**

| 项目 | 内容 |
|------|------|
| **作者** | Eric Swindlehurst 等 |
| **期刊** | IEEE Journal of Solid-State Circuits (JSSC), 2021 |
| **DOI** | 10.1109/JSSC.2021.3066626 |

**核心贡献**：提出 **Dual-Path Bootstrapped Switch（双路径自举开关）**，两条路径分别驱动开关栅极和辅助节点，减小栅极电压摆幅与寄生效应。配合分组 DAC 电容，在 10 GHz 采样下仅消耗 21 mW。

**关键参数**：
- 架构：时间交织 SAR
- 分辨率：8 bit，10 GS/s
- 功耗：21 mW
- 核心技术：Dual-Path Bootstrapped Switch

> Dual-Path 结构是解决超高速采样中寄生电容瓶颈的代表性方案。

---

### 论文 5（56 GS/s 产业前沿）

**An 8-bit 56 GS/s 64× Time-Interleaved ADC With Bootstrapped Sampler and Class-AB Buffer in 4nm CMOS**

| 项目 | 内容 |
|------|------|
| **作者** | IBM Research / Samsung Foundry |
| **会议** | **IEEE VLSI Symposium on Technology and Circuits, 2022** |
| **链接** | [IBM Research](https://research.ibm.com/publications/an-8-bit-56gss-64x-time-interleaved-adc-with-bootstrapped-sampler-and-class-ab-buffer-in-4nm-cmos) |

**核心贡献**：在三星 4 nm 工艺下实现 56 GS/s 8-bit ADC，16×4 交织架构。第一级交织器采用 **novel bootstrapping technique**，实现宽输入共模范围（0.3–0.6 V），在 4.1 GHz 下 THD < −52 dB。Class-AB follower 解决基线漂移问题。

**关键参数**：
- 工艺：Samsung 4 nm (4LPP)
- 分辨率：8 bit，56 GS/s（64× TI）
- ENOB：6.5 @ 低频，> 5.2 @ Nyquist (28 GHz)
- 带宽：> 27 GHz
- 功耗效率：47 fJ/conv-step @ 0.8 V
- 应用：下一代 SerDes (112 Gb/s PAM4 及以上)

> 这是目前公开发表的采样率最高的 Bootstrap-Switch-based ADC 之一，代表了产业界最前沿水平。

---

### 论文 6（权威教程）

**The Bootstrapped Switch [A Circuit for All Seasons]**

| 项目 | 内容 |
|------|------|
| **作者** | Behzad Razavi (UCLA) |
| **期刊** | IEEE Solid-State Circuits Magazine, Vol. 7, No. 3, pp. 12–15, 2015 |
| **DOI** | 10.1109/MSSC.2015.2449714 |

**核心贡献**：系统讲解 Bootstrap Switch 的拓扑演化——从简单想法到实用电路的全过程，包括可靠性问题（栅氧击穿、衬底偏置）的解决方案。逐管分析 11 管经典结构的每个晶体管的作用。

**补充阅读**：Razavi 在 2021 年发表续篇 **"The Design of a Bootstrapped Sampling Circuit [The Analog Mind]"**（SSC Magazine, Vol. 13, No. 1, pp. 7–12），深入讨论了设计中的非理想效应（电荷注入、时钟馈通、寄生耦合）及版图考量。

> 这两篇是学习 Bootstrap Switch 的最佳入门与进阶资料，作者 Razavi 是《模拟 CMOS 集成电路设计》的作者。

---

## 4. 结构演进路线图

```
1999 ─── Abo & Gray (JSSC)
         │  经典栅压自举 + Clock Multiplier
         │  0.6μm, 10-bit, 14.3 MS/s
         │
2010 ─── Liu et al. (JSSC)
         │  11管标准结构 + 单调电容切换 SAR
         │  0.13μm, 10-bit, 50 MS/s
         │
2018 ─── Ramkaj et al. (JSSC)
         │  Switch-Bootstrapping @ 5 GHz 输入
         │  28nm, 7-bit, 1.25 GS/s
         │
2021 ─── Swindlehurst et al. (JSSC)
         │  Dual-Path Bootstrapped Switch
         │  8-bit, 10 GS/s (TI)
         │
2022 ─── IBM/Samsung (VLSI Symposium)
         │  Novel Bootstrapping + Class-AB Buffer
         │  4nm, 8-bit, 56 GS/s (64× TI)
         ▼
```

---

## 5. 关键设计考量

| 问题 | 描述 | 解决方案 |
|------|------|---------|
| **栅氧可靠性** | 自举后栅压可达 $2V_{DD}$，薄栅氧击穿风险 | 串联 cascode 管分压、限制栅源电压 |
| **寄生电容** | 自举节点寄生电容分走电荷，降低实际 $V_{GS}$ | 多路径驱动、减小关键路径负载 |
| **电荷注入** | 关断时沟道电荷注入采样电容，引入非线性 | 互补 CMOS 开关、dummy 管抵消 |
| **时钟馈通** | 时钟跳变通过 $C_{GD}$ 耦合到信号路径 | 差分结构、dummy 路径 |
| **衬底效应** | $V_{SB}$ 变化导致 $V_{TH}$ 调制 | 衬底接自举电压、深 N-well 隔离 |
| **漏电流** | 保持相漏电流导致采样电容放电 | Leakage Current Suppressed (LCS) 技术 |

---

## 6. 参考资源

- Razavi, B. "The Bootstrapped Switch [A Circuit for All Seasons]." *IEEE Solid-State Circuits Magazine*, 2015.
- Razavi, B. "The Design of a Bootstrapped Sampling Circuit [The Analog Mind]." *IEEE Solid-State Circuits Magazine*, 2021.
- Murmann, B. "ADC Performance Survey 1997–2024." [Online]. Available: https://github.com/bmurmann/ADC-survey

> **关于论文截图**：检索工具无法直接下载论文 PDF 中的图片。上述论文均标注了 DOI，可前往 [IEEE Xplore](https://ieeexplore.ieee.org) 检索 DOI 号下载原文获取电路原理图、仿真波形和芯片照片。Abo & Gray (JSSC 1999) 和 Liu et al. (JSSC 2010) 的电路图在 Razavi 的 SSC Magazine 教程中亦有清晰重绘版本。