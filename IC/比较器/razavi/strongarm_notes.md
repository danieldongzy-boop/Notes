# StrongARM Latch 深度学术总结

> **来源**：Behzad Razavi, "The StrongARM Latch," *IEEE Solid-State Circuits Magazine*, Vol. 7, No. 2, pp. 12–17, Spring 2015.
>
> **DOI**：[10.1109/MSSC.2015.2418155](https://doi.org/10.1109/MSSC.2015.2418155)

---

## 1. 背景与动机

StrongARM Latch 得名于 Digital Equipment Corporation 的 StrongARM 微处理器，最早由 Toshiba 的 Kobayashi 等人于 1992 年提出基本结构 [2]，后经 Montanaro 等人在 StrongARM 处理器中推广 [1]。

该电路广泛应用于 **读出放大器（Sense Amplifier）**、**比较器（Comparator）** 以及通用高灵敏度锁存器。其三大核心优势：

1. **零静态功耗** — 无直流导通路径；
2. **轨到轨输出** — 直接产生 $0 \to V_{DD}$ 的数字电平；
3. **低输入失调** — 输入参考失调电压主要仅由一对差分对贡献。

---

## 2. 电路结构与基本工作原理

### 2.1 电路拓扑

![图1(b) 改进型 StrongARM Latch 拓扑]

电路由以下部分组成：

| 元件 | 功能 |
|---|---|
| $M_1, M_2$ | 时钟控制差分输入对 |
| $M_3, M_4$ | NMOS 交叉耦合对 |
| $M_5, M_6$ | PMOS 交叉耦合对 |
| $M_7$ | 时钟控制尾电流源 |
| $S_1 \sim S_4$ | 预充电开关（将节点 P, Q, X, Y 预充至 $V_{DD}$） |

> **与原始版本的区别**：图 1(a) 原始版本无 $M_8$ 或仅含 $M_8$ 做预充电均衡，节点 P, Q 无法准确均衡，且放大阶段起点在 $V_{DD} - V_{THN}$ 附近，增益不足，动态失调严重。图 1(b) 改进版通过四个预充电开关解决了上述问题。

### 2.2 四阶段工作过程

#### 阶段一：预充电（CK = 0）

$M_1, M_2$ 截止，$S_1 \sim S_4$ 导通，节点 P, Q, X, Y 全部预充电到 $V_{DD}$。

#### 阶段二：放大模式（Amplification Mode）

CK 跳变为高电平，$S_1 \sim S_4$ 关断，$M_1, M_2$ 导通。差分电流 $\propto (V_{in1} - V_{in2})$ 从 $C_P, C_Q$ 抽取电荷，$V_P, V_Q$ 以不同速率下降，产生电压增益。

在此期间尾电流近似恒定：

$$V_P - V_Q \approx \frac{g_{m1,2} \cdot (V_{in1} - V_{in2}) \cdot t}{C_{P,Q}}$$

式中 $C_{P,Q} = C_P = C_Q$，$g_{m1,2}$ 为 $M_1, M_2$ 的小信号跨导。

当 $V_P, V_Q$ 下降至 $V_{DD} - V_{THN}$ 时，NMOS 交叉耦合对 $M_3, M_4$ 导通，放大模式结束。放大模式持续时间约为：

$$t_{amp} \approx \frac{C_{P,Q} \cdot V_{THN}}{I_{CM}}$$

其中 $I_{CM}$ 为从每个电容抽取的共模电流。

**放大模式电压增益**：

$$A_v \approx \frac{g_{m1,2} \cdot V_{THN}}{I_{CM}} \tag{1}$$

#### 阶段三：NMOS 交叉耦合对导通

$M_3, M_4$ 导通后，$M_1, M_2$ 的部分漏极电流开始从 X, Y 节点流出。节点方程：

$$C_X \frac{dV_X}{dt} = -g_{m3} (V_Y - V_P) \tag{2}$$

$$C_Y \frac{dV_Y}{dt} = -g_{m4} (V_X - V_Q) \tag{3}$$

$$C_P \frac{dV_P}{dt} = C_X \frac{dV_X}{dt} - \Delta I \tag{4}$$

$$C_Q \frac{dV_Q}{dt} = C_Y \frac{dV_Y}{dt} + \Delta I \tag{5}$$

其中 $+\Delta I$ 和 $-\Delta I$ 代表 $M_1, M_2$ 产生的差分电流。

由 (2) – (3) 相减并代入 P, Q 积分关系，得到描述 $V_{XY} = V_X - V_Y$ 的微分方程：

$$C_{X,Y} \frac{dV_{XY}}{dt} = -g_{m3,4} \left[ \left(1 - \frac{C_{X,Y}}{C_{P,Q}} \right) V_{XY} + \frac{2\Delta I \cdot t}{C_{P,Q}} \right] \tag{8}$$

#### 再生时间常数

设 $g_{m3,4}$ 近似恒定，该方程揭示出自然响应形式为 $\exp(t / \tau_{reg})$：

$$\tau_{reg} = \frac{C_{X,Y}}{g_{m3,4} \left(1 - \dfrac{C_{X,Y}}{C_{P,Q}} \right)} \tag{9}$$

> **关键洞察**：$C_P, C_Q$ 带来的源极退化效应使 $\tau_{reg}$ 增大了 $1 / (1 - C_{X,Y} / C_{P,Q})$ 倍。由于实际中 $C_{X,Y}$（含后级输入电容）通常大于 $C_{P,Q}$，NMOS 交叉耦合对在此阶段提供的再生作用有限。

#### 阶段四：PMOS 交叉耦合对导通

当 $V_X, V_Y$ 继续下降至 $V_{DD} - V_{THP}$ 时，$M_5, M_6$ 导通。PMOS 交叉耦合对的正反馈最终将一个输出拉回 $V_{DD}$，另一个拉至 0，完成轨到轨锁存。

---

## 3. 各晶体管的关键作用

| 晶体管 | 核心作用 |
|---|---|
| $M_1, M_2$ | 差分输入对，主导输入参考失调和噪声 |
| $M_3, M_4$ | ① NMOS 交叉耦合再生 ② **第四阶段末期切断 $V_{DD}$ 到地的直流通路，防止静态功耗** |
| $M_5, M_6$ | **将输出高电平恢复至 $V_{DD}$**（否则小信号输入下 X/Y 共模放电导致高电平退化） |
| $S_1, S_2$ | ① **消除 P, Q 节点历史状态，抑制动态失调** ② 建立 $V_{DD}$ 初始电压，使 $M_1, M_2$ 进入线性区前获得放大增益 |
| $S_3, S_4$ | 预充 X, Y 至 $V_{DD}$，确保放大阶段 $M_5, M_6$ 保持截止，避免引入额外失调 |

### 3.1 若无 $M_3, M_4$ 会怎样？

若省略 $M_3, M_4$：
- 对于约 100mV 的差分输入，$V_X$ 下降、$V_Y$ 上升，$M_5$ 关断，电路退化为 $V_{DD}$ 到地的直流通路，产生静态功耗；
- 仅当输入为轨到轨摆幅时，$M_5, M_6$ 之一才可靠关断，因此**若输入始终为轨到轨，可以省略 $M_3, M_4$**。

---

## 4. 功耗

StrongARM Latch 功耗主要来自电容的充放电：

$$P \approx f_{CK} \cdot (2C_{P,Q} + C_{X,Y}) \cdot V_{DD}^2$$

其中 $f_{CK}$ 为时钟频率，系数 2 源于 P 和 Q 每周期均放电至接近地。

---

## 5. 输入失调电压（Offset）

### 5.1 失调来源分析

预充电动作使 $M_3 \sim M_6$ 初始截止，有效降低其失调贡献：

| 失配来源 | 输入参考衰减因子 |
|---|---|
| $M_3, M_4$ | $\approx 1 / A_v \approx 1/4$ |
| $M_5, M_6$ | $\approx 1/10$（因导通时间晚） |
| **$M_1, M_2$** | **主导贡献者** |

### 5.2 失调校准方法 — 可编程电容法

利用 $C_P \neq C_Q$ 产生不对称放电速率，人为引入与随机失调相反的"内置失调"实现抵消。

$$V_P = V_{DD} - \frac{g_{m1}(V_{in1} - V_{in2}) t}{2C_P} - \frac{I_{CM} t}{C_P} \tag{10}$$

$$V_Q = V_{DD} + \frac{g_{m2}(V_{in1} - V_{in2}) t}{2C_Q} - \frac{I_{CM} t}{C_Q} \tag{11}$$

$$\begin{aligned}
V_P - V_Q = &\ \frac{g_m (C_P + C_Q)}{C_P C_Q} \cdot \frac{V_{in1} - V_{in2}}{2} \cdot t \\
           &+ \frac{C_P - C_Q}{C_P C_Q} \cdot I_{CM} \cdot t
\end{aligned} \tag{12}$$

在放大模式期间，$V_P - V_Q$ 累积了一个等于 $\frac{C_P - C_Q}{C_P C_Q} \cdot I_{CM} \cdot t$ 的失调项，可用于抵消随机失调。

放大模式持续时间：$t \approx V_{THN} \cdot (C_P + C_Q) / (2 I_{CM})$（以 $(C_P + C_Q)/2$ 近似）。

**内置失调量**：

$$V_{OS,built-in} \approx \frac{V_{THN}}{2} \left( \frac{C_Q}{C_P} - \frac{C_P}{C_Q} \right)$$

**校准流程**：将主输入端短接 → 时钟驱动电路 → 输出判决驱动寄存器控制 $C_P, C_Q$ 的 unit capacitor 阵列。

> **Trade-off**：将失调从 30mV 降至 1mV 需要大量小 unit capacitor，会**降低速度**并**增加功耗**。

### 5.3 其他失调校准方法

参考文献 [6] 描述了另一种面向 StrongARM Latch 的失调消除方案（Yoshioka et al., 2010）。

---

## 6. 电子噪声（Electronic Noise）

### 6.1 噪声来源分析

预充电动作同样降低了 $M_3 \sim M_6$ 的噪声贡献。输入参考噪声主要来源：

1. **$M_1, M_2$ 的热噪声**（主导）
2. **$S_1, S_2$ 的 $kT/C$ 噪声**

> 其他晶体管在显著增益建立后才介入，噪声贡献被大幅衰减。

### 6.2 放大模式输出噪声方差

在放大模式下，等效电路表现为积分器，$M_1, M_2$ 产生的输出噪声电压方差随时间增长：

$$\overline{V_{n,PQ}^2} = \frac{8kT}{C_{P,Q}^2} \cdot g_{m1,2}^2 \cdot t \tag{13}$$

### 6.3 输入参考总噪声

代入放大模式持续时间 $t_{amp} \approx C_{P,Q} V_{THN} / I_{CM}$ 和 $g_{m1,2} \approx 2 I_{CM} / (V_{GS} - V_{THN})_{1,2}$，并加入 $S_1, S_2$ 的 $kT/C$ 噪声，除以增益平方：

$$\overline{V_{n,in}^2} = \frac{kT}{C_{P,Q}} \left[ 4 \cdot \frac{V_{THN}}{(V_{GS} - V_{THN})_{1,2}} + 2 \cdot \frac{V_{THN}^2}{(V_{GS} - V_{THN})_{1,2}^2} \right] \tag{15}$$

| 项次 | 含义 | 典型幅值关系 |
|---|---|---|
| 第 1 项 | $M_1, M_2$ 噪声贡献 | 通常为第 2 项的 4~8 倍 |
| 第 2 项 | $S_1, S_2$ 的 $kT/C$ 噪声 | 次要 |

### 6.4 比较器噪声仿真方法

比较器噪声仿真面临特殊挑战：比较器不像小信号模拟电路那样直接提供输出噪声和增益。

**方法论**（基于瞬态噪声仿真的统计方法）：

1. **Step 1**：零失调、零差分输入下多次时钟触发 → 亚稳态由内部高斯噪声打破，输出等概率出现 0 和 1。
2. **Step 2**：施加小差分输入 $V_S$（几 mV）→ 判决概率偏移，0 仅当输入参考噪声 $< -V_S$ 时出现。
3. **Step 3**：统计 $n_0$（输出 0 次数）和 $n_1$（输出 1 次数）：

$$\frac{n_1}{n_0} = \frac{\displaystyle\int_{-V_S}^{+\infty} f_X(x) \, dx}{\displaystyle\int_{-\infty}^{-V_S} f_X(x) \, dx} \tag{16}$$

由此反推 $f_X(x)$（高斯分布）的方差，即输入参考噪声电压的平方。

> $V_S$ 的选取原则：足够大以使 $n_1/n_0$ 明显偏离 1，但不能过大导致 $n_0$ 或 $n_1$ 过小而失去统计意义。

---

## 7. 回踢噪声（Kickback Noise）与电源瞬态

### 7.1 回踢噪声

StrongARM Latch 从输入端抽取高瞬态电流，在 Flash ADC 等大量比较器并行工作的场景中尤为严重。

**回踢噪声的两种分量**：

| 分量 | 机理 | 特性 |
|---|---|---|
| **差分分量** | $V_P, V_Q$ 以不同速率下降 → 经 $C_{GD1}, C_{GD2}$ 耦合到输入端；$M_1, M_2$ 进入线性区后 $C_{GD}$ 增大加剧此效应 | 较小 |
| **共模分量** | $M_7$ 导通瞬间从 $C_{GS1}, C_{GS2}$ 抽取漏极电流；$M_7$ 关断瞬间 CK 经 $C_{GD7}$（含 $C_{GS7}$）耦合 | **远大于差分分量** |

![图7：回踢噪声路径示意]

### 7.2 降低回踢噪声的替代拓扑

图 8(a) 将输入对改为漏极路径时钟控制（$M_7, M_8$ 控制锁存）：

- **优点**：降低回踢噪声
- **代价**：$M_1, M_2$ 在放大模式工作于线性区 → **输入失调增大**

可通过加宽 $M_3, M_4$ 和 $M_7, M_8$ 缓解，但预充电阶段 A/B 节点放电缓慢 → $V_P, V_Q$ 严重不平衡 → **动态失调增大**。

### 7.3 电源瞬态

$S_1 \sim S_4$ 的预充电动作在 CK 快速下降时，三个开关瞬间进入饱和区（第四个漏极电压为 $V_{DD}$ 故在线性区），从 $V_{DD}$ 抽取大电流。

> **关键点**：低平均功耗的设计仍可能抽取高峰值电流 → 要求**低电源阻抗**。

---

## 8. 输出接口：RS 锁存器

StrongARM Latch 在大约半个时钟周期内输出无效（$V_X = V_Y = V_{DD}$）。后续逻辑需 RS Latch 正确解读输出，典型连接如图 4：

```
StrongARM Latch → 反相器缓冲 → RS Latch
```

反相器作为缓冲器，确保仅当 $V_X$ 或 $V_Y$ 真正下降时 RS Latch 才翻转。

---

## 9. 设计 Trade-off 总结

| 性能指标 | 优化方向 | 约束 / 代价 |
|---|---|---|
| **失调** | 增大 $M_1, M_2$ 尺寸 → 减小 $V_{TH}$ 失配 | 增加输入电容 → 降低速度、增加回踢噪声 |
| **失调校准** | 可编程电容阵列 | 失调降低量 vs 速度退化 + 功耗增加 |
| **噪声** | 增大 $C_{P,Q}$ | 降低 $kT/C$ 噪声，但增加功耗（$P \propto C$） |
| **速度** | 增大 $g_{m3,4}$、减小 $C_{X,Y}$ | 增大 $C_{X,Y}/C_{P,Q}$ 导致 $\tau_{reg}$ 退化 |
| **回踢噪声** | 漏极时钟控制拓扑 | 增加输入失调 |
| **功耗** | 减小电容、降低 $f_{CK}$ | 噪声、速度折中 |

---

## 10. 关键结论

1. **StrongARM Latch 的本质**：集成了预充电、放大、两级交叉耦合再生的四阶段动态锁存器，以零静态功耗实现轨到轨输出。

2. **$M_3, M_4$ 的双重角色**：既参与 NMOS 交叉耦合再生，又在第四阶段结束时切断直流通路避免静态功耗。若输入保证轨到轨摆幅，可省略此对管。

3. **预充电开关 $S_1 \sim S_4$ 至关重要**：改进版的核心创新——消除动态失调（均衡 P/Q 历史状态）、提供放大所需初始条件、抑制 $M_5, M_6$ 额外失调。

4. **$C_P, C_Q$ 的退化效应**：在 NMOS 再生阶段通过源极退化增大 $\tau_{reg}$，设计中 $C_{X,Y}$ 常大于 $C_{P,Q}$ 使得 NMOS 交叉耦合对再生增益有限，主要再生依赖 PMOS 交叉耦合对。

5. **输入参考失调主导源**：$M_1, M_2$ ——其他器件失调被增益大幅衰减（$M_3, M_4 \approx 1/4$，$M_5, M_6 \approx 1/10$）。

6. **噪声与失调同源**：预充电机制同时抑制了 $M_3 \sim M_6$ 的噪声贡献，$M_1, M_2$ 热噪声和 $S_1, S_2$ 的 $kT/C$ 噪声主导。

7. **回踢噪声的共模支配性**：$M_7$ 开关瞬态引起的共模回踢远大于差分回踢，且电源瞬态要求低阻抗供电。

---

## 参考文献

[1] J. Montanaro et al., "A 160-MHz 32-b 0.5-W CMOS RISC microprocessor," *IEEE J. Solid-State Circuits*, vol. 31, pp. 1703–1714, Nov. 1996.

[2] T. Kobayashi et al., "A current-mode latch sense amplifier and a static power saving input buffer for low-power architecture," *Proc. VLSI Circuits Symp.*, pp. 28–29, June 1992.

[3] Y. T. Wang and B. Razavi, "An 8-bit 150-MHz CMOS A/D converter," *IEEE J. Solid-State Circuits*, vol. 35, pp. 308–317, Mar. 2000.

[4] P. Nuzzo et al., "Noise analysis of regenerative comparators for reconfigurable ADC architectures," *IEEE Trans. Circuits Syst. I*, vol. 55, pp. 1441–1454, July 2008.

[5] M. J. E. Lee, W. J. Dally, and P. Chiang, "Low-power area-efficient high-speed I/O circuit techniques," *IEEE J. Solid-State Circuits*, vol. 35, pp. 1591–1599, Nov. 2000.

[6] M. Yoshioka et al., "A 10-b 50-MS/s 820uW SAR ADC with on-chip digital calibration," *IEEE Trans. Biomed. Circuits Syst.*, vol. 4, pp. 411–418, Dec. 2010.

[7] S. W. Chiang and B. Razavi, "A 10-bit 800-MHz 19-mW CMOS ADC," *IEEE J. Solid-State Circuits*, vol. 49, pp. 935–949, Apr. 2014.

[8] T. Sepke et al., "Noise analysis of comparator-based circuits," *IEEE Trans. Circuits Syst. I*, vol. 56, pp. 541–553, Mar. 2009.

[9] R. J. Baker, *CMOS Circuit Design, Layout, and Simulation*. Wiley, 2010.