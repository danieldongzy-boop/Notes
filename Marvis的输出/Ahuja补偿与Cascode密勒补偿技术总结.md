# Ahuja 补偿与 Cascode 密勒补偿技术总结

> 整理日期：2026-05-23 | 来源：IEEE 文献 + 网络技术博客综合

---

## 一、引言：为什么需要频率补偿

多级 CMOS 运算放大器因存在多个极点，在闭环负反馈下容易自激振荡。频率补偿的核心目标是**拉开极点间距**，使单位增益带宽（GBW）内只有一个主导极点，从而获得足够的相位裕度（通常 > 60°）。本文聚焦两种紧密关联的高级补偿技术：**Ahuja 补偿**（间接补偿）和 **Cascode 密勒补偿**（共源共栅密勒补偿）。

---

## 二、米勒补偿回顾（作为对比基线）

### 2.1 基本结构

传统的米勒补偿在两级运放中，将补偿电容 $C_c$ 直接跨接在第一级输出与第二级输出之间。

![Miller Compensation](https://i-blog.csdnimg.cn/direct/5745c1d340d44506818509501c9fdc06.png)

> 图：Miller 补偿的零极点分布（来源：CSDN / Ahuja 1983）

### 2.2 关键参数

- **主极点**：$\omega_{p1} \approx \dfrac{1}{g_{m2}R_2 R_1 C_c}$
- **次极点**：$\omega_{p2} \approx \dfrac{g_{m2}C_c}{C_1 C_L + C_c C_L + C_c C_1}$
- **右半平面零点**：$\omega_z = \dfrac{g_{m2}}{C_c}$
- **单位增益带宽**：$\omega_u \approx \dfrac{g_{m1}}{C_c}$

### 2.3 米勒补偿的缺点

1. **右半平面零点（RHP Zero）恶化相位裕度**。加调零电阻 $R_z \approx 1/g_{m2}$ 可消除，但需要精确匹配，工艺偏差下不稳定。
2. **PSRR 较差**：高频时 $C_c$ 阻抗降低，电源轨噪声直接耦合到输出。
3. **带载能力有限**：负载电容 $C_L$ 增大时次极点内移，稳定性恶化。典型约束 $C_{L} \leq 8.63\text{ pF}$（在 $C_c=5\text{pF}, C_1=0.5\text{pF}$ 条件下）。

---

## 三、Ahuja 补偿（间接频率补偿）

### 3.1 核心思想

Ahuja 补偿由 **B. K. Ahuja** 于 1983 年在 IEEE JSSC 上首次系统提出。核心思路是**用一个电流 buffer（共栅级）阻断前馈通路**。

传统米勒补偿电容上的电流为：

$$
I_{C_c,\text{Miller}} = C_c \frac{d(V_o - V_1)}{dt}
$$

其中 $V_1$ 项代表前馈通路贡献。若将 $C_c$ 一端接到一个**低阻抗交流地节点**（共栅级源端），则：

$$
I_{C_c,\text{Ahuja}} = C_c \frac{dV_o}{dt}
$$

前馈通路被消除，右半平面零点消失。

![Ahuja Circuit](https://i-blog.csdnimg.cn/direct/cddf2aeab15241cc92ccbdd7de700de0.png)

> 图：Ahuja 补偿的电路实现（来源：CSDN / Ahuja 1983）

### 3.2 两种经典结构

| 结构 | 补偿电容 $C_c$ 接法 | 零点特征 |
|------|---------------------|----------|
| **原始版本**（Read & Wieser, 1982） | $C_c$ 接在**负载共栅管**源端与输出之间 | 单个 LHP 零点 |
| **流行版本** | $C_c$ 接在**输入差分对共栅管**源端与输出之间 | 一对镜像零点（1 LHP + 1 RHP），频率很高，影响小 |

两种结构的**极点表达式相同**。

### 3.3 传递函数分析

原始版本的开环传递函数：

$$
A(s) = A_0 \cdot \frac{\left(\frac{s}{s_z} + 1\right)}{\left(\frac{s}{s_{p1}} + 1\right)\left[\frac{s^2}{\omega_n^2} + \frac{2\zeta}{\omega_n}s + 1\right]}
$$

关键参数：

- **直流增益**：$A_0 = g_{m1}g_{m2}r_1 r_2$
- **主极点**：$s_{p1} = -\dfrac{g_{m1}}{A_0 C_c}$（与米勒补偿相同）
- **LHP 零点**：$s_z = -\dfrac{g_{m3}}{\sigma C_c}$，其中 $\sigma = 1 + C_3/C_c \approx 1$
- **复数极点对**：
  - 自然频率：$\omega_n = \sqrt{\dfrac{g_{m2}g_{m3}}{\rho C_1 C_2}}$
  - 阻尼系数：$\zeta = \dfrac{1}{2}\sqrt{\dfrac{C_1 g_{m3}}{\rho C_2 g_{m2}}}\left(1 + \dfrac{C_2}{C_c}\right)$
  - 其中 $\rho = 1 + C_3/C_c + C_3/C_2 \approx 1$

![Ahuja Pole-Zero](https://i-blog.csdnimg.cn/direct/3abe111a7d4941379bd6cdce25807936.png)

> 图：Ahuja 补偿的零极点分布（来源：CSDN / Ahuja 1983）

### 3.4 复数极点与阻尼系数——Ahuja 补偿的核心挑战

与米勒补偿的**实数次极点**不同，Ahuja 补偿的高频极点通常为**复数共轭对**。阻尼系数 $\zeta$ 决定了稳定性：

| $\zeta$ 值 | 表现 |
|------------|------|
| $\zeta \geq 0.7$ | 临界阻尼，无超调，理想 |
| $\zeta \geq 0.5$ | 可接受，有轻微 peaking |
| $\zeta < 0.3$ | 增益曲线出现明显 peaking，相位裕度恶化，阶跃响应振铃 |

由于 $C_1$（第一级输出寄生电容）很小而 $C_2$（含负载电容）较大，$\zeta$ 通常偏小。**增大补偿管跨导 $g_{m3}$ 是提升 $\zeta$ 的关键手段**。

### 3.5 $g_{m3}$ 的关键作用

| 参数 | 与 $g_{m3}$ 关系 | 增大 $g_{m3}$ 的效果 |
|------|------------------|---------------------|
| 零点频率 $\omega_z$ | $\propto g_{m3}$ | 推向更高频 |
| 自然频率 $\omega_n$ | $\propto \sqrt{g_{m3}}$ | 复数极点推向更高频 |
| 阻尼系数 $\zeta$ | $\propto \sqrt{g_{m3}}$ | 阻尼增大，更稳定 |

仿真数据（65nm 工艺，$g_{m3}$ 增大 4 倍）：

| 参数 | 普通 $g_{m3}$ | 4× $g_{m3}$ |
|------|--------------|------------|
| 偏置电流 | 10 μA | 40 μA |
| 阻尼系数 $\zeta$ | 0.25 | 0.48 |
| 零点频率 | 19.3 MHz | 78.9 MHz |
| 自然频率 | 46.2 MHz | 92.9 MHz |
| 增益裕度 | 20.5 dB | 31.1 dB |

### 3.6 Ahuja 补偿的优势

1. **更大的负载电容驱动能力**：$\dfrac{C_{L,\text{Ahuja}}}{C_{L,\text{Miller}}} \approx \dfrac{C_c}{C_1}$ 倍。同样条件下 $C_{L,\text{Ahuja}} \leq 95\text{ pF}$，远优于米勒补偿的 $8.63\text{ pF}$。
2. **更好的 PSRR**：低频 PSRR = $-20\log(A_1 A_2)$，高频无直接耦合路径。
3. **无 RHP 零点**（原始版本），无需调零电阻。
4. **更小的补偿电容**即可实现相同 GBW。

### 3.7 实际电路实现

![Ahuja Implementation](https://i-blog.csdnimg.cn/direct/d9adabf15fa34d6cab9056cbd093bbc2.png)

> 图：Ahuja 补偿的具体电路实现（来源：CSDN）

关键设计要点：
- 两个电流源 CS1、CS2 必须匹配，使 $C_c$ 的充放电电流全部流入/流出第一级输出节点。
- Cascode 管偏置电流 $I_1 > 2I_0$（$I_0$ 为差分对尾电流），保证压摆状态下 $V_{gs}$ 仍保持恒定。
- 该结构也称 **Grounded-Gate Cascode Compensation**。

---

## 四、Cascode 密勒补偿

### 4.1 与 Ahuja 补偿的关系

Cascode 密勒补偿是 Ahuja 补偿思想的**实用化演变**。两者本质相同——利用共栅级（cascode 管）作为 current buffer 隔离前馈通路。区别在于 Ahuja 补偿在论文中以**独立共栅级**呈现，而 Cascode 密勒补偿**复用**了运放中已有的 cascode 管，无需额外器件。

### 4.2 工作原理

Cascode 管 M10 作为 current buffer：

- **正向通路**（输出→补偿）：Vout 的电压摆动通过 $C_c$ 转换为电流，经 M10 注入第一级输出节点（点 6），实现补偿。
- **反向通路被阻断**：点 6 的电压变化无法通过 $C_c$ 前馈回 Vout，因为 M10 的低输入阻抗（$\approx 1/g_{m10}$）隔离了电压信号。

定量分析：设 M10 输出阻抗 $r_{o10}$，M8 输出阻抗 $r_{o8}$，点 6 到点 4 的小信号增益被衰减约 $g_{m10}r_{o8}$ 倍。**有 M10 时 RHP 零点频率比无 M10 时提高了 $g_{m10}r_{o8}$ 倍**，实际上被推到极高频，对稳定性影响可忽略。

Cascode 补偿与 Miller 补偿的**主极点位置相同**。

### 4.3 Gain Peaking 问题及对策

由于 cascode 管是非理想 current buffer，系统传递函数在 GBW 以外可能出现 **gain peaking**。这是由一对**共轭极点 Q 值过大**引起的，即使相位裕度（PM）良好，瞬态响应仍可能有振铃。

**对策**：
- 增大 cascode 管的 $g_m$（即增大 $g_{m10}/g_{m11}$ 比值），让 current buffer 效果更理想，将共轭极点推向更高频。
- 在 rail-to-rail 运放中，p-cascode 和 n-cascode 各加一个对称补偿电容，增大 cascode 管的 $g_m$ 来抑制 peaking。

![Cascode Compensation Summary](https://i-blog.csdnimg.cn/direct/cd0a281c0b7042baa4f2458513c94503.png)

> 图：多种补偿结构对比总结（来源：EETOP 论坛 / CSDN）

### 4.4 主动跨导倍增（Active Transconductance Multiplication）

直接增大 $g_{m3}$ 需成比例增加偏置电流，功耗代价高。主动跨导倍增技术可**用小电流实现等效大 $g_{m3}$**：

- **原理**：在补偿管源端加增益为 $A$ 的辅助放大器，栅源电压变为 $-(1+A)v_s$，等效漏电流 $i_d = -(1+A)g_{m3}v_s$，$g_{m3}$ 被放大 $(1+A)$ 倍。
- **效果**：用 4.75 倍倍增、仅 2 倍电流（20→40 μA），阻尼系数从 0.27 提升到 0.60。
- **约束**：辅助放大器需为宽带放大器，-3dB 带宽需满足 $\omega_p > g_{m2}/C_a$。

---

## 五、核心文献支撑

### 文献 1：Ahuja 补偿原始论文（奠基之作）

> **B. K. Ahuja**, "An Improved Frequency Compensation Technique for CMOS Operational Amplifiers," *IEEE Journal of Solid-State Circuits*, vol. 18, no. 6, pp. 629–633, Dec. 1983.  
> DOI: [10.1109/JSSC.1983.1052012](https://doi.org/10.1109/JSSC.1983.1052012)

**贡献**：
- 首次系统提出利用电流 buffer 消除前馈通路的间接频率补偿技术。
- 推导了 Ahuja 补偿的完整传递函数，证明主极点与 Miller 补偿相同、次极点更远、无 RHP 零点。
- 给出了具体 CMOS 电路实现（含偏置设计、压摆率分析）。
- 证明了 PSRR 相比 Miller 补偿有显著改善。

### 文献 2：MOS 运放设计综述（背景与基础）

> **P. R. Gray and R. G. Meyer**, "MOS Operational Amplifier Design — A Tutorial Overview," *IEEE Journal of Solid-State Circuits*, vol. SC-17, no. 6, pp. 969–982, Dec. 1982.

**贡献**：
- 全面总结了 MOS 运放设计方法论，包括 Miller 补偿的详细分析。
- 为 Ahuja 补偿的提出提供了直接的研究背景和问题动机。
- 分析了 Miller 补偿中 RHP 零点产生机制及调零电阻法的局限性。

### 文献 3：Ahuja 补偿的工程问题分析

> **U. Dasgupta**, "Issues in 'Ahuja' Frequency Compensation Technique," *IEEE RFIT*, 2009.

**贡献**：
- 系统分析了 Ahuja 补偿在实际应用中的问题，包括两种电路形式（Fig.1 和 Fig.2）的对比。
- 深入讨论了复数共轭极点导致的稳定性隐患。
- 提出通过增大 $g_{m3}$ 提升阻尼系数 $\zeta$ 的解决方案。
- 指出某些场景下 cascode 补偿与 Miller 补偿可同时使用以进一步提升稳定性。

---

## 六、技术对比总结

| 对比维度 | 米勒补偿 | Ahuja 补偿 | Cascode 密勒补偿 |
|----------|---------|-----------|-----------------|
| **核心机制** | $C_c$ 直接跨接，密勒效应极点分裂 | 电流 buffer 阻断前馈，间接补偿 | 复用 cascode 管作 current buffer |
| **主极点** | $\dfrac{1}{g_{m2}R_2R_1C_c}$ | **相同** | **相同** |
| **次极点** | 实数极点 | 复数共轭对 | 复数共轭对 |
| **RHP 零点** | 有（需调零电阻） | 无（原始版本） | 被推到极高频 |
| **PSRR** | 较差（高频耦合） | 好 | 好 |
| **带载能力** | $C_L$ 受限 | $C_L$ 范围大 $\approx C_c/C_1$ 倍 | 同 Ahuja |
| **补偿电容** | 需较大 $C_c$ | 可用更小 $C_c$ | 可用更小 $C_c$ |
| **额外器件** | 可选 $R_z$ | 需独立共栅级 + 匹配电流源 | 复用已有 cascode 管 |
| **核心风险** | RHP 零点 | 阻尼不足导致 peaking | Gain peaking（共轭极点 Q 过高） |
| **适用场景** | 简单、低功耗、快速原型 | 高 PSRR、大容性负载 | 已有 cascode 结构的运放 |

---

## 七、设计要点速查

1. **补偿电容选取**：$C_c$ 由目标 GBW 决定：$f_u \approx g_{m1} / (2\pi C_c)$
2. **阻尼系数目标**：$\zeta \geq 0.5$（可接受），$\zeta \approx 0.7$（理想）
3. **$\zeta$ 不足时的对策**：
   - 直接增大 $g_{m3}$（增大偏置 / W/L）→ 功耗增加
   - 主动跨导倍增 → 功耗效率高，但增加设计复杂度
   - 增大 $C_c$ → $\zeta \propto (1 + C_2/C_c)$，但会降低 GBW
4. **辅助放大器带宽约束**（若使用主动倍增）：$\omega_p > g_{m2}/C_a$
5. **结构选择**：原始版本 DC 增益较低但设计简单；流行版本 DC 增益高但需注意镜像零点

---

## 参考文献

1. B. K. Ahuja, "An Improved Frequency Compensation Technique for CMOS Operational Amplifiers," *IEEE J. Solid-State Circuits*, vol. 18, no. 6, pp. 629–633, Dec. 1983.
2. P. R. Gray and R. G. Meyer, "MOS Operational Amplifier Design — A Tutorial Overview," *IEEE J. Solid-State Circuits*, vol. SC-17, pp. 969–982, Dec. 1982.
3. U. Dasgupta, "Issues in 'Ahuja' Frequency Compensation Technique," *IEEE RFIT*, 2009.
4. R. J. Reay and G. T. A. Kovacs, "An Unconditionally Stable Two-Stage CMOS Amplifier," *IEEE J. Solid-State Circuits*, 1995.
5. Willy M. C. Sansen, *模拟集成电路设计精粹* (Analog Design Essentials).

---

> **免责说明**：本文电路截图来源于公开网络技术博客（CSDN、知乎），仅用于学习交流。文中公式推导参考了上述 IEEE 原始文献及中文技术社区的解读文章。建议读者直接阅读原始 IEEE 论文获取最权威的推导和实验数据。