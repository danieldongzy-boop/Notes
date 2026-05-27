# SAR ADC 数字校准（Digital Calibration）论文汇总

> 整理日期: 2026-05-27
> 涵盖范围: 综述论文、经典节点突破论文，优先 ISSCC / JSSC / TCAS-I / TCAS-II / VLSI Symposium 等顶会顶刊

---

## 一、综述 / 教程 / 入门必读

| # | 论文标题 | 作者 | 年份 | 来源 | 核心贡献 |
|---|---------|------|------|------|---------|
| 1 | **Digitally Assisted Data Converter Design** (Keynote) | B. Murmann | 2013 | ESSCIRC | **数字辅助模拟设计的纲领性文章**，系统阐述如何用数字信号处理能力换取模拟功耗降低，是理解整个领域的必读起点 |
| 2 | **Digitally Assisted Pipeline ADCs: Theory and Implementation** | B. Murmann, B.E. Boser | 2004 | Springer 专著 | 第一本系统论述数字辅助流水线 ADC 的专著，提出基于统计学的系统辨识技术进行数字校准 |
| 3 | **The Race for the Extra Decibel: A Brief Review of Current ADC Performance Trajectories** | B. Murmann | 2015 | IEEE Solid-State Circuits Magazine | ADC 性能演进轨迹综述，涵盖数字校准对 SNDR/FoM 提升的宏观趋势 |
| 4 | **ADC Performance Survey 1997-2023** | B. Murmann | 2023 | GitHub / Online | ISSCC & VLSI 会议 ADC 性能数据库，是追踪数字校准带来性能提升的最佳数据源 |
| 5 | **基于神经网络的数字校准技术综述** | 李嘉燊, 李龙, 邓红辉 等 | 2022 | 《微电子学》 | 系统梳理神经网络校准原理、分类与优劣，14位流水线ADC仿真验证 ENOB 从10b→12.5b，SFDR 80dB→100dB |
| 6 | **高精度逐次逼近型ADC及其校准技术研究** | 曹超 | 2017 | 西安电子科技大学博士论文 | 中文文献中系统研究高精度 SAR 校准的典范，提出失调双注入校准和拆分型校准，SMIC 0.18μm 流片验证 16 位 SAR ADC，ENOB 达 14.46~15.04 bit，FoM ~170 dB |
| 7 | **SAR ADC数字校准的挑战与对策** | — | 2025 | CSDN 文库 | 面向工程实践的总览，从误差分析到校准算法分类，适合作为校准知识框架梳理 |

---

## 二、节点突破 / 里程碑论文

### 2.1 基础理论 & 开创性工作（2000-2015）

| # | 论文标题 | 作者 | 年份 | 来源 | 核心贡献 |
|---|---------|------|------|------|---------|
| 8 | **"Split ADC" Architecture for Deterministic Digital Background Calibration of a 16-bit 1-MS/s ADC** | J. McNeill, M. Coln, B. Larivee | 2005 | **JSSC** | **Split-ADC 后台校准的开山之作**。将 ADC 面积拆分为两个独立转换器，利用输出差值驱动 LMS 自适应校准，~10,000 次转换即可收敛，16-bit 1MS/s，0.25μm CMOS |
| 9 | **A 12-bit, 45-MS/s, 3-mW Redundant Successive-Approximation-Register ADC with Digital Calibration** | — | ~2011 | **JSSC** | **Sub-radix-2 冗余 + 扰动校准的经典**。首次系统证明冗余不仅保证数字可校正的静态非线性，还能对抗动态误差，加速 SAR 转换速度 |
| 10 | **Digitally Assisted Pipeline ADCs** (JSSC 版本) | B. Murmann, B.E. Boser | ~2004 | **JSSC** | 基于统计学的后台数字校准首次应用于流水线 ADC，开创"数字辅助模拟"范式 |

### 2.2 SAR ADC 校准（2016-2025）

| # | 论文标题 | 作者 | 年份 | 来源 | 核心贡献 |
|---|---------|------|------|------|---------|
| 11 | **A low-cost digital-domain foreground calibration for high resolution SAR ADCs** | Rui Guan, Jin Jing, Jianjun Zhou | 2018 | Microelectronics Journal | 重用 SAR ADC 内部冗余和子 DAC，无需额外校准 DAC，在数字域同时估计主/子 DAC 失配。16位 SAR ADC 行为级仿真 SNDR 67.3→92.8 dB |
| 12 | **A 18-bit 1-MS/s fully-differential SAR ADC with digital calibration achieving 96.1 dB SNDR** | P. Zhang, W. Feng, P. Zhao, Y. Song | — | ScienceDirect | **18 位 SAR ADC 教科书级案例**。前台数字自校准 + 多种数字增强技术，基于归一化满量程参考的 L 段电容权重校正。实测 SNDR 96.1dB，SFDR 110.7dB，INL/DNL ±0.5 LSB |
| 13 | **一种基于数字前台校正的列级 SAR ADC 的设计** | 国长宇, 申人升, 张皓雯 等 | — | 《微电子学与固体电子学》 | 针对 12 位列级 SAR ADC，改进 LMS 前台校准 + sub-radix 分段电容阵列。收敛速度提升 10 倍以上，SNDR 57.9→68.6 dB，INL/DNL ±0.5 LSB |
| 14 | **一种前后台结合的 SAR ADC 的校准算法** | 黄立朝, 芮小军, 章宇新 等 | 2023 | 《微电子学》 | **电容重组 + LMS 后台校准混合方案**。电容重组显著提高 LMS 收敛速度，收敛时间缩短至 ~1k 转换周期，ENOB 10.59→13.79 bit，SFDR 71.33→112.93 dB |
| 15 | **基于整数权重的非二进制 SAR ADC 及其校准算法** | 刘宇航, 曹晓东, 张雪莲, 张其鑫 | 2022 | 《北京交通大学学报》 | 整数权重非二进制分段电容阵列 + 扰动校准，SFDR 60→106.3 dB，ENOB 9.28→13.75 bit，展示"结构+校准"协同设计优势 |
| 16 | **Metastable-Dither-Based Digital Background Calibration of Interstage Gain Nonlinearity in Pipelined SAR ADC** | L. Chen, Y. Cao, L. Ling, S. Liu, H. Han | 2025 | **IEEE TVLSI** | 首次利用比较器**亚稳态注入多电平抖动**，LMS 后台校准流水线 SAR 级间增益非线性。14 位 ADC SNDR 60.4→84.5 dB，SFDR 73.6→110.0 dB，收敛 ~0.8M 样本 |
| 17 | **A digital background calibration scheme for non-linearity of SAR ADC using back-propagation algorithm** | — | — | ScienceDirect | 将 SAR ADC 非线性建模为可微网络，**首次使用 BP 算法**在后台直接校正电容失配，比传统 LMS 收敛更快、精度更高 |

### 2.3 流水线 / Pipelined-SAR ADC 校准

| # | 论文标题 | 作者 | 年份 | 来源 | 核心贡献 |
|---|---------|------|------|------|---------|
| 18 | **A 10.0 ENOB, 6.2 fJ/conv.-step, 500 MS/s Ringamp-Based Pipelined-SAR ADC with Background Calibration and Dynamic Reference Regulation in 16nm CMOS** | J. Lagos, N. Markulic, B. Hershberg 等 | 2021 | **VLSI Symposium** | 单通道全动态流水线 SAR ADC，利用 novel quantizer + 窄带抖动注入实现 DAC 失配/级间增益/ringamp 偏置的快速全面后台校准。500MS/s，3.3mW，Walden FoM 6.2 fJ/c.s |
| 19 | **A 12b 1GS/s Pipelined ADC with Digital Background Calibration of Inter-stage Gain, Capacitor Mismatch, and Kick-back Errors** | — | 2023 | JSSC | 相关型后台校准同时校正**级间增益 + 电容失配 + kick-back 误差**，1GS/s 12b，解决高速采样下的三大误差源 |

---

## 三、核心技术脉络梳理

### 3.1 校准策略分类

| 大类 | 子类 | 代表方法 | 关键论文 |
|------|------|---------|---------|
| **前台校准 (Foreground)** | 数字域自校准 | 按比特权重测量+校正 | #11, #12 |
| | 参考ADC辅助 | 多路ADC均值做参考 | #13 |
| **后台校准 (Background)** | Split-ADC | 双通道差值驱动LMS | #8 (McNeill 2005) |
| | 扰动/抖动 (Dither-based) | PN序列/亚稳态抖动 + 相关 | #16, #18, #19 |
| | 盲校准 (Blind) | Sub-radix-2 冗余 + 统计 | #9, #15 |
| | 神经网络/ML | BP算法反向传播校正 | #5, #17 |
| **混合校准** | 前台+后台 | 电容重组+LMS后台 | #14 |

### 3.2 关键演进节点

```
2004 ─ Murmann & Boser: 数字辅助流水线ADC (统计学辨识)
  │
2005 ─ McNeill & Coln: Split-ADC 后台校准 (JSSC)
  │
2011 ─ Sub-radix-2 冗余 + 扰动校准 (JSSC)
  │
2013 ─ Murmann: "Digitally Assisted Data Converter Design" (ESSCIRC Keynote)
  │
2018 ─ 数字域低成本前台校准 (Microelectronics Journal)
  │
2021 ─ VLSI: Ringamp Pipelined-SAR 全动态后台校准, FoM 6.2 fJ/c.s
  │
2022 ─ 神经网络校准综述
  │
2023 ─ 前后台混合校准 (电容重组+LMS)
  │
2025 ─ 亚稳态抖动后台校准 + BP算法校准 (TVLSI)
```

---

## 四、推荐阅读路径

1. **入门** → #1 Murmann Keynote (2013) + #3 ADC Performance Trajectories (2015)
2. **理解 Split-ADC** → #8 McNeill JSSC (2005)
3. **理解 SAR 冗余校准** → #9 sub-radix-2 JSSC (~2011) + #11 低成本前台校准 (2018)
4. **工程实现参考** → #12 18-bit SAR (ScienceDirect) + #14 混合校准 (2023)
5. **前沿方向** → #16 亚稳态抖动 (2025) + #17 BP算法校准

---

## 五、检索来源

- IEEE Xplore (JSSC, TCAS-I, TCAS-II, TVLSI)
- ISSCC / VLSI Symposium 会议论文集
- Google Scholar
- ScienceDirect
- 知网 / 万方 (中文文献)
- GitHub: ADC Performance Survey (Murmann)
