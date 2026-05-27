# SAR ADC 数字校准（Digital Calibration）完全指南

> 整理日期: 2026-05-27
> 写给：懂 SAR ADC 但想系统理解数字校准的读者

---

## 一、为什么需要数字校准？

SAR ADC 的精度天花板受限于**电容阵列的匹配精度**。在传统设计中，要提高精度就只能增大电容面积来改善匹配——这让面积和功耗都很难受。到了 12-bit 以上，工艺能做到的电容匹配（通常 ~10-bit）已经不够用了。

数字校准的核心思想很简单：**既然模拟器件做不到完美匹配，那就在数字域把误差算出来并补偿掉**。

这句话听起来简单，但实现起来有三个核心难题：

1. **怎么知道误差是多少？** 你没法直接"测量"电容失配，得想办法"推断"出来
2. **怎么在正常工作时校准？** 如果每次校准都要打断正常工作（前台校准），那很多场景不适用
3. **怎么保证校准本身足够快？** 有些算法需要百万次转换才收敛，不可接受

数字校准的整个领域，就是围绕这三个问题展开的。

---

## 二、两大校准范式：前台 vs 后台

### 2.1 前台校准（Foreground Calibration）

**怎么工作：**
芯片上电或空闲时，注入已知参考信号 → 测量 ADC 输出 → 计算误差 → 存入查找表或校正系数 → 正常工作时用系数修正输出。

**优点：**
- 算法简单，硬件开销小
- 收敛极快，通常几百到几千次转换就能完成

**缺点：**
- 必须打断正常工作
- 无法跟踪温度/电压漂移导致的误差变化

**代表论文：** [#11] Guan et al. 2018（低开销数字域前台校准）、[#12] Zhang et al. 18-bit SAR（教科书级前台校准实现）

### 2.2 后台校准（Background Calibration）

**怎么工作：**
在 ADC 正常转换的同时"悄悄"提取误差信息，不中断正常数据流。

按技术路线分：

#### 2.2.1 Split-ADC（拆分型）
将 ADC 一分为二，两个独立转换器对同一输入同时转换。如果两个输出不一致，说明至少有一个需要校准。差值驱动 LMS 算法迭代修正。

- **开创者：** [#8] McNeill, Coln, Larivee, JSSC 2005
- **核心优势：** 确定性强，收敛快（~10k 次转换），不需要额外注入信号
- **代价：** 面积 ×2，功耗 ×2

#### 2.2.2 抖动/扰动法（Dither-based）
在模拟域注入一个已知的伪随机信号（dither），这个信号和输入不相关。在数字域用相关运算把 dither 引起的响应提取出来，反推出误差。

- **经典代表：** [#18] VLSI 2021 ringamp Pipelined-SAR（窄带抖动 + 全动态后台校准）
- **前沿突破：** [#16] Chen et al. 2025 TVLSI（利用比较器亚稳态产生抖动，不需要额外模拟电路注入）
- **优势：** 不打断工作，硬件开销适中
- **挑战：** dither 会吃掉一部分动态范围

#### 2.2.3 盲校准（Blind Calibration）
不注入任何额外信号，仅利用 sub-radix-2 冗余结构的特性，从正常转换结果中通过统计方法估计电容失配。

- **里程碑：** [#9] sub-radix-2 SAR ADC, JSSC ~2011
- **优势：** 零额外模拟开销
- **挑战：** 需要精心设计冗余结构，收敛较慢

#### 2.2.4 神经网络/ML 校准
将 SAR ADC 的非线性建模为一个可微网络，用反向传播直接校正电容权重。

- **先驱：** [#17] BP 算法校准（ScienceDirect）
- **综述：** [#5] 李嘉燊等, 2022（神经网络校准综述）
- **趋势：** 收敛比 LMS 更快，但硬件实现成本高，目前多在仿真阶段

---

## 三、关键技术概念速查

| 概念 | 一句话解释 | 为什么重要 |
|------|-----------|-----------|
| **Sub-radix-2 / 冗余** | 电容权重不再是严格的 2 的幂，相邻 bit 的权重有重叠 | 是盲校准和扰动校准的基础，提供了"容错空间" |
| **LMS 算法** | 最小均方误差自适应滤波 | 后台校准最常用的误差迭代估计方法 |
| **电容重组** | 在校准阶段切换电容连接方式来放大误差信号 | 可以显著加速 LMS 收敛（#14 黄立朝等, 2023） |
| **PN Dither** | 伪随机序列注入 | 相关型后台校准的核心手段 |
| **亚稳态抖动** | 故意让比较器进入亚稳态，利用其随机性产生抖动 | 不需要额外模拟电路，前沿方向（#16） |
| **Walden FoM / Schreier FoM** | ADC 能效评价指标 | 数字校准的终极目标是"在同样功耗下提高精度"，FoM 是衡量标尺 |

---

## 四、核心论文分级推荐

### 综述 / 入门（理解全景）

| # | 论文 | 作者 | 年份 | 来源 | 一句话 |
|---|------|------|------|------|--------|
| S1 | **Digitally Assisted Data Converter Design** (Keynote) | B. Murmann | 2013 | ESSCIRC | 数字辅助模拟的纲领性宣言，**数字校准的"圣经"级入门** |
| S2 | **Digitally Assisted Pipeline ADCs: Theory and Implementation** | B. Murmann, B.E. Boser | 2004 | Springer 专著 | 第一本专著，统计学系统辨识做校准的理论基础 |
| S3 | **基于神经网络的数字校准技术综述** | 李嘉燊 等 | 2022 | 《微电子学》 | 从传统校准到 AI 校准的桥梁 |
| S4 | **高精度逐次逼近型ADC及其校准技术研究** | 曹超 | 2017 | 西电博士论文 | 中文文献最系统的 SAR 校准研究，有流片验证 |
| S5 | **ADC Performance Survey 1997-2023** | B. Murmann | 持续更新 | GitHub | ISSCC/VLSI ADC 性能数据库，看数字校准带来性能提升的最佳数据源 |

### 节点突破（理解核心方法）

| # | 论文 | 作者 | 年份 | 来源 | 为什么是里程碑 |
|---|------|------|------|------|---------------|
| B1 | **"Split ADC" Architecture for Deterministic Digital Background Calibration of a 16-bit 1-MS/s ADC** | J. McNeill, M. Coln, B. Larivee | 2005 | **JSSC** | Split-ADC 后台校准**开山之作**，~10k 转换收敛，思想影响至今 |
| B2 | **A 12-bit, 45-MS/s, 3-mW Redundant SAR ADC with Digital Calibration** | — | ~2011 | **JSSC** | 首次证明 sub-radix-2 冗余 + 扰动校准可同时处理静/动态误差 |
| B3 | **A low-cost digital-domain foreground calibration for high resolution SAR ADCs** | R. Guan, J. Jin, J. Zhou | 2018 | Microelec. J. | **零额外校准 DAC**，重用内部冗余，SNDR 67→93 dB |
| B4 | **A 18-bit 1-MS/s fully-differential SAR ADC with digital calibration achieving 96.1 dB SNDR** | P. Zhang 等 | — | ScienceDirect | **18 位 SAR 教科书级实现**，实测 SNDR 96.1dB, SFDR 110.7dB |
| B5 | **一种前后台结合的SAR ADC校准算法** | 黄立朝 等 | 2023 | 《微电子学》 | 电容重组 + LMS 后台，收敛 ~1k 转换，SFDR 71→113 dB |
| B6 | **A 10.0 ENOB, 6.2 fJ/conv.-step, 500 MS/s Ringamp-Based Pipelined-SAR ADC with Background Calibration** | J. Lagos, N. Markulic, B. Hershberg 等 | 2021 | **VLSI Symposium** | **全动态 + 窄带抖动后台校准极致能效**，Walden FoM 6.2 fJ/c.s |
| B7 | **Metastable-Dither-Based Digital Background Calibration of Interstage Gain Nonlinearity in Pipelined SAR ADC** | L. Chen, Y. Cao 等 | 2025 | **IEEE TVLSI** | **亚稳态做抖动**，零额外模拟注入，SNDR 60→85 dB |
| B8 | **A digital background calibration scheme using back-propagation algorithm** | — | — | ScienceDirect | 首次把 SAR 校准视作深度学习问题，BP 替代 LMS |

---

## 五、推荐阅读路径（按顺序）

```
第1步：S1 (Murmann 2013 Keynote)
     → 理解"为什么用数字辅助模拟"这个核心范式

第2步：B1 (McNeill 2005 JSSC)
     → 理解 Split-ADC 怎么用两个不完美的 ADC 做出一个准的

第3步：B2 (~2011 sub-radix-2 JSSC) + B3 (Guan 2018)
     → 理解冗余结构怎么给校准"留余地"，以及低成本前台校准怎么实现

第4步：B4 (18-bit SAR) + B5 (混合校准 2023)
     → 看工程级的高精度实现和混合校准思路

第5步：B6 (VLSI 2021) + B7 (TVLSI 2025)
     → 了解最前沿：全动态 + 亚稳态抖动，FoM 做到极致
```

---

## 六、技术演进时间线

```
2004 ─ Murmann: 数字辅助流水线ADC，统计学辨识
  │
2005 ─ McNeill: Split-ADC 后台校准 (JSSC)  ← 范式开创
  │
2011 ─ Sub-radix-2 冗余 + 扰动校准 (JSSC)  ← SAR校准基础
  │
2013 ─ Murmann: "Digitally Assisted" Keynote ← 领域宣言
  │
2018 ─ 数字域低成本前台校准 (MEJ) ← 实用化
  │
2021 ─ VLSI: Ringamp Pipelined-SAR 全动态后台校准, FoM 6.2 fJ ← 极致能效
  │
2022 ─ 神经网络校准综述 ← AI路线总结
  │
2023 ─ 前后台混合校准 (电容重组+LMS) ← 混合思路
  │
2025 ─ 亚稳态抖动 / BP算法校准 (TVLSI) ← 最新前沿
```

---

*检索范围: IEEE Xplore (JSSC/TCAS-I/II/TVLSI), ISSCC, VLSI Symposium, ScienceDirect, Google Scholar, 知网/万方*
