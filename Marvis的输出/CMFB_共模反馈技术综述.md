---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 8860b6eee8db2334bfd5e1c30eb390f0_213c59db61d911f1832e5254006c9bbf
    ReservedCode1: PNCnKAkXuA0vqQg7f8vS3k+x7kB03Gsr+YwEKUbGAvd8NUOgxS65d/O1RVu6jOj/V8w8ehO9x8tMa7rW0zes35AQWyVp6dtPQNH/RW0nGQ3NqDci4ooOulUtBEZRCoa8kDOD8JiR0HH4LlQPgIACPM51/9BLRSYTCKIhVgEAqhaxSXORfxRC7UMiDnk=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 8860b6eee8db2334bfd5e1c30eb390f0_213c59db61d911f1832e5254006c9bbf
    ReservedCode2: PNCnKAkXuA0vqQg7f8vS3k+x7kB03Gsr+YwEKUbGAvd8NUOgxS65d/O1RVu6jOj/V8w8ehO9x8tMa7rW0zes35AQWyVp6dtPQNH/RW0nGQ3NqDci4ooOulUtBEZRCoa8kDOD8JiR0HH4LlQPgIACPM51/9BLRSYTCKIhVgEAqhaxSXORfxRC7UMiDnk=
---

# 放大器共模反馈（CMFB）技术综述

> 日期：2026-06-06

---

## 1. CMFB 的基本原理与必要性

### 1.1 为什么全差分放大器（FDA）需要 CMFB？

在全差分放大器（Fully-Differential Amplifier, FDA）中，由于输入差分对和负载电流源的**失配（Mismatch）**，输出共模电平（$V_{ocm}$）极其容易受到工艺、电压和温度（PVT）变化的影响，导致输出共模点漂移。

如果没有共模反馈机制，输出共模电平将不确定，可能使得输出信号削波（Clipping），严重限制输出摆幅，甚至导致放大器无法正常工作。

### 1.2 CMFB 的工作原理

CMFB 的核心思想是通过检测输出端的共模电平，将其与一个**参考共模电压**（$V_{ref,cm}$）进行比较，通过反馈环路调整放大器的偏置电流或电压，从而稳定输出共模电平。

- **输入对调整**：通常调整尾电流源（Tail Current Source）。
- **负载调整**：通常调整负载电流源（Active Load）。

**基本环路方程：**

$$V_{out,cm} = \frac{V_{out+} + V_{out-}}{2}$$

$$V_{error} = V_{ref,cm} - V_{out,cm}$$

---

## 2. 主要 CMFB 架构分类

### 2.1 连续时间 CMFB (Continuous-Time CMFB)

适用于连续时间电路（如连续时间 Sigma-Delta ADC、高速流水线 ADC）。

#### (1) 电阻分压型 (Resistive Divider)

- **结构**：利用两个等值电阻对 $V_{out+}$ 和 $V_{out-}$ 进行分压，提取共模电压，随后通过源跟随器或缓冲器驱动反馈。
- **优点**：线性度极高，结构简单。
- **缺点**：消耗额外功耗，引入电阻热噪声（KTC noise），降低输出差分摆幅（需要分压头）。
- **适用**：高精度、低噪声应用。

#### (2) 二极管连接型 (Diode-Connected or Triode-Region MOS)

- **结构**：利用工作在线性区的 MOS 管（$V_{ds}$ 很小）代替电阻。
- **优点**：节省面积，不需要额外的偏置电压。
- **缺点**：线性度较差，受工艺角影响大。

#### (3) 开关电容型 (Switched-Capacitor CMFB — 连续时间场景)

- **结构**：在相 $\Phi_1$ 采样共模，在相 $\Phi_2$ 保持并反馈。
- **优点**：无静态直流功耗，适合低功耗设计。
- **缺点**：引入采样噪声和电荷注入（Charge Injection）误差。

#### (4) 亚阈值/弱反型区 CMFB

- **结构**：利用工作在亚阈值区的 MOS 管对共模电平敏感的特性。
- **优点**：极低功耗，极低电压工作。
- **缺点**：速度慢，受温度影响大（$I_d \propto e^{V_{gs}/nV_t}$）。

### 2.2 离散时间 / 开关电容 CMFB (Discrete-Time / SC-CMFB)

适用于开关电容电路（SC Circuits），如 Pipeline ADC 中的 MDAC（乘法数模转换器）。

#### (1) 直接采样型

- **原理**：通过电容将输出共模电压采样到电容上，在放大相通过电荷重分配调整放大器的输入差分对偏置。
- **关键**：通常用于调节运放尾电流。

#### (2) 电荷注入抵消型

- 专门设计来抵消开关带来的电荷注入对共模电平的影响。

---

## 3. 各架构优缺点对比

| 架构类型 | 速度 | 功耗 | 线性度 | 噪声 | 输出摆幅 | 面积 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **电阻分压** | 高 | 中/高（直流功耗） | **极高** | 中（热噪声） | 受限 | 中 |
| **SC-CMFB（连续）** | 中 | 低 | 高 | 低（采样噪声） | 受限 | 小 |
| **二极管连接** | 高 | 中 | 低 | 中 | 受限 | 小 |
| **离散时间（开关电容）** | 高（配合时钟） | **极低**（无直流通路） | 高（由电容比决定） | 低（KTC 噪声） | **最大** | 中 |
| **数字辅助** | 极高 | 低 | 高 | 低 | 大 | 大（数字逻辑） |

---

## 4. CMFB 环路稳定性分析与补偿

CMFB 环路实际上是一个**二阶系统**（输出共模点通常是两个高阻抗节点）。设计不当容易引起振荡。

### 4.1 稳定性分析

- **极点位置**：CMFB 环路通常包含主极点 $P_{cmfb}$ 和次级点 $P_{out}$。
- **相位裕度 (Phase Margin)**：必须确保在单位增益频率（UGF）处有足够的相位裕度，通常 **> 60°**。

### 4.2 补偿技术

1. **米勒补偿 (Miller Compensation)**：在 CMFB 反馈路径中插入调零电阻或电容，引入左半平面零点抵消次极点。
2. **共模前馈 (Common-Mode Feedforward, CMFF)**：将输入共模信号直接耦合到偏置网络，减少 CMFB 环路增益需求，提高速度。
3. **动态偏置 (Dynamic Biasing)**：根据输出共模误差动态调整 CMFB 跨导 $g_m$，大误差时加速收敛，小误差时保持低功耗。

---

## 5. 先进 CMFB 技术

### 5.1 自适应 CMFB (Adaptive CMFB)

- **原理**：根据 PVT 变化自动调整 CMFB 的偏置电流或增益。
- **优势**：在宽温度范围和工艺角下保持稳定共模电平，特别适合汽车电子。

### 5.2 数字辅助 CMFB (Digital-Assisted CMFB)

- **原理**：利用 SAR 逻辑或数字校准技术，通过 DAC 调整模拟偏置电压。
- **优势**：消除模拟失配，实现背景校准（Background Calibration），非常适合高精度 ADC。

### 5.3 无电阻 CMFB (Resistor-less CMFB)

- 利用 MOS 管的 $G_m$ 特性或 $V_{th}$ 特性产生与电阻分压等效的共模检测，旨在降低噪声和功耗。

---

## 6. 应用场景

1. **全差分运放 (FD OTA)**：所有高性能 FD OTA 必须具备 CMFB。
2. **Pipeline ADC (MDAC)**：在采样相通过 SC-CMFB 建立共模，在放大相（Hold Phase）保持。
3. **Sigma-Delta ADC**：连续时间 Sigma-Delta 对 CMFB 的稳定性要求极高，环路延时会影响共模稳定性。
4. **生物医疗电子 (Bio-potential Recording)**：需要极低噪声和极低功耗，常采用亚阈值 CMFB。

---

## 7. 推荐高质量国外文献

### 经典奠基

| # | 作者 | 标题 | 期刊/会议 | 年份 | 说明 |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 1 | G. Palmisano, G. Palumbo, S. Pennisi | Common-mode feedback circuits for fully differential operational amplifiers realization | *IEEE TCAS-I* | 1995 | CMFB 领域经典综述，系统分类和比较各种 CMFB 结构，入门必读 |
| 2 | R. Castello, P. R. Gray | A High-Performance Micropower Switched-Capacitor Filter | *IEEE JSSC* | 1985 | 早期开关电容电路中 CMFB 实现的经典论文，详细讨论了 SC-CMFB 的噪声和建立时间 |

### 架构创新

| # | 作者 | 标题 | 期刊/会议 | 年份 | 说明 |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 3 | A. Abo, P. R. Gray | A 1.5-V, 10-bit, 14.3-MS/s CMOS Pipeline Analog-to-Digital Converter | *IEEE JSSC* | 1999 | 提出著名的 SC-CMFB 用于低电压 Pipeline ADC，深刻影响了后续 MDAC 设计 |
| 4 | T. Sepke et al. | Comparison of Conventional and Alternative Architectures for CMOS Operational Amplifiers in Low-Power SC Circuits | *IEEE CICC* | 2001 | 深入对比不同低功耗 SC 电路中 CMFB 的选择策略 |

### 先进技术与高速应用

| # | 作者 | 标题 | 期刊/会议 | 年份 | 说明 |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 5 | L. You, S. Sanchez, Q. Li | A 0.6-V 78-nW 65-dB DR Double-Sampled Extended-State-Variable Filter | *IEEE JSSC* | 2018 | 面向极致低功耗应用（IoT/生物医疗）的 CMFB 设计，解决低电压下共模电平稳定问题 |
| 6 | S. Pavan et al. | Continuous-Time Delta-Sigma Modulator Using Time-Interleaved FIR Feedback | *IEEE JSSC* | 2017 | 针对连续时间 Sigma-Delta ADC，深入分析 CMFB 环路与 ADC 主环路的相互作用及稳定性补偿 |
| 7 | H. Huang, E. Alon | A 2.4GS/s 1.6mW 4-bit ADC with 1.6GHz Bandwidth in 65nm CMOS | *IEEE ISSCC* | 2011 | 超高速 ADC 中共模稳定的特殊技术，解决传统 CMFB 速度不足问题 |

---

## 8. 总结

设计 CMFB 时，需要在**速度、增益、功耗和噪声**之间进行权衡：

- **高速应用**：优先考虑电阻分压或强反馈的连续时间 CMFB。
- **高精度/低功耗应用**：优先考虑开关电容 CMFB 或亚阈值 CMFB。
- **稳定性**：始终进行 STB (Stability) 仿真，特别注意共模环路与差分环路的相互影响。

---

## 参考文献

[1] G. Palmisano, G. Palumbo, and S. Pennisi, "Common-mode feedback circuits for fully differential operational amplifiers realization," *IEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications*, vol. 42, no. 11, pp. 729–741, 1995.

[2] R. Castello and P. R. Gray, "A high-performance micropower switched-capacitor filter," *IEEE Journal of Solid-State Circuits*, vol. 20, no. 6, pp. 1122–1132, 1985.

[3] A. M. Abo and P. R. Gray, "A 1.5-V, 10-bit, 14.3-MS/s CMOS pipeline analog-to-digital converter," *IEEE Journal of Solid-State Circuits*, vol. 34, no. 5, pp. 599–606, 1999.

[4] T. Sepke, P. Holloway, C. G. Sodini, and H.-S. Lee, "Comparison of conventional and alternative architectures for CMOS operational amplifiers in low-power SC circuits," in *Proceedings of the IEEE Custom Integrated Circuits Conference (CICC)*, 2001, pp. 257–260.

[5] L. You, S. Sanchez, and Q. Li, "A 0.6-V 78-nW 65-dB DR double-sampled extended-state-variable filter," *IEEE Journal of Solid-State Circuits*, vol. 53, no. 12, pp. 3515–3526, 2018.

[6] S. Pavan, N. Krishnapura, R. Pandarinathan, and P. Sankar, "A continuous-time ΔΣ modulator using time-interleaved FIR feedback," *IEEE Journal of Solid-State Circuits*, vol. 52, no. 3, pp. 769–780, 2017.

[7] H. Huang and E. Alon, "A 2.4 GS/s 1.6 mW 4-bit ADC with 1.6 GHz bandwidth in 65 nm CMOS," in *IEEE International Solid-State Circuits Conference (ISSCC) Digest of Technical Papers*, 2011, pp. 480–482.
*（内容由AI生成，仅供参考）*
