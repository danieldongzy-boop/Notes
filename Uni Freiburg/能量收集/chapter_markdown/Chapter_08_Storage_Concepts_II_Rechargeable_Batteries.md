# Chapter 8 - Storage Concepts II: 充电电池看效率、自放电和寿命

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_8_Storage Concepts II - Rechargeable Batteries_SS_2026.pdf`
- Exercise: `Exercise 5_Capacitors , batteries , efficiencies and leakage currents_SOLVED.pdf` 中 Task 2-4

## 这一章在讲什么

电池适合长期储能，能量密度比电容高得多，但有几个麻烦点：

- 充放电效率不是 100%
- 会自放电
- 不能随便过充、过放
- 寿命和充放电深度、温度、电流有关

微能量收集系统里，电池常常不是“越大越好”，而是要看收集功率能不能补上自放电和负载。

## 作业重点公式

### 负载电流和运行时间

$$
I=\frac{P}{U}
$$

$$
t=\frac{C_0}{I}
$$

作业 NiMH 例子：

- $P=150 \ \mathrm{\mu W}$
- $U=1.0 \ \mathrm{V}$
- $C_0=15 \ \mathrm{mAh}$

$$
I=150 \ \mathrm{\mu A}=0.150 \ \mathrm{mA}
$$

$$
t=\frac{15 \ \mathrm{mAh}}{0.150 \ \mathrm{mA}}=100 \ \mathrm{h}
$$

### 自放电电流

如果自放电率是 SDR：

$$
\Delta C=SDR\cdot C_0
$$

$$
I_\mathrm{SD}=\frac{\Delta C}{\Delta t}
$$

说人话：自放电可以理解成电池内部一直有一个小负载在偷电。

### 考虑库仑效率的补偿电流

如果充进去的电荷只有 $\eta_C$ 能真正留下：

$$
I_\mathrm{charge}=\frac{I_\mathrm{SD}}{\eta_C}
$$

作业 NiMH 中：

$$
I_\mathrm{SD}=1.25 \ \mathrm{\mu A}
$$

$$
I_\mathrm{charge}=\frac{1.25}{0.68}\approx1.83 \ \mathrm{\mu A}
$$

### 完全充满需要的电荷量

$$
Q_\mathrm{in}=\frac{C_0}{\eta_C}
$$

作业中：

$$
Q_\mathrm{in}=\frac{15 \ \mathrm{mAh}}{0.68}\approx22.5 \ \mathrm{mAh}
$$

### 同时供负载和补自放电

如果负载直接由发电器供电，电池只需要补自放电：

$$
I_\mathrm{gen}=I_\mathrm{load}+I_\mathrm{SD}/\eta_C
$$

作业：

$$
I_\mathrm{gen}=150+1.83=151.83 \ \mathrm{\mu A}
$$

如果负载也通过电池供电，负载电荷也要除以库仑效率：

$$
I_\mathrm{gen}=\frac{I_\mathrm{load}}{\eta_C}+\frac{I_\mathrm{SD}}{\eta_C}
$$

作业：

$$
I_\mathrm{gen}=\frac{150}{0.68}+1.83\approx222.43 \ \mathrm{\mu A}
$$

## Li-Ion 作业公式

### 线性 C-V 近似

题目说 Li-Ion 在 $3.3$ 到 $4.1 \ \mathrm{V}$ 范围内近似线性：

$$
\frac{dC}{dU}=\frac{C_0}{U_\mathrm{full}-U_\mathrm{empty}}
$$

作业中：

$$
\frac{dC}{dU}=\frac{1.5 \ \mathrm{Ah}}{0.8 \ \mathrm{V}}
=1.875 \ \mathrm{Ah/V}
$$

### 等效并联漏电阻 EPR

这不是电池内阻，而是把自放电等效成一个并联电阻。

先算每月损失的电荷对应的平均电流：

$$
I=\frac{SDR\cdot C_0}{\Delta t}
$$

再估算这段时间的电压下降：

$$
\Delta U=\frac{\Delta C}{dC/dU}
$$

取平均漏电电压：

$$
U_\mathrm{avg}\approx U_\mathrm{full}-\frac{\Delta U}{2}
$$

最后：

$$
R_\mathrm{EPR}=\frac{U_\mathrm{avg}}{I}
$$

作业结果约：

$$
R_\mathrm{EPR}\approx103 \ \mathrm{k\Omega}
$$

### 补偿 Li-Ion 自放电的功率

考虑库仑效率：

$$
I_\mathrm{charge}=\frac{I_\mathrm{SD}}{\eta_C}
$$

$$
P=UI_\mathrm{charge}
$$

作业中：

$$
P\approx4.1 \ \mathrm{V}\cdot40.4 \ \mathrm{\mu A}
=165.7 \ \mathrm{\mu W}
$$

### 完全充满需要的能量

如果电压近似线性：

$$
U_\mathrm{avg}=\frac{U_\mathrm{start}+U_\mathrm{end}}{2}
$$

$$
E_\mathrm{in}=\frac{U_\mathrm{avg}C_0}{\eta_E}
$$

注意：

$$
1 \ \mathrm{V\cdot Ah}=1 \ \mathrm{Wh}
$$

作业中：

$$
E=\frac{3.7 \ \mathrm{V}\cdot1.5 \ \mathrm{Ah}}{0.9}
\approx6.16 \ \mathrm{Wh}
$$

## NiMH 和 Li-Ion 对比

### NiMH

优点：

- 比较耐用
- 对过充相对宽容
- 充电管理比 Li-Ion 简单一些

缺点：

- 自放电较大
- 电压低，单节约 $1.2 \ \mathrm{V}$
- 库仑效率和能量效率较低

### Li-Ion / LiPo

优点：

- 能量密度高
- 自放电较低
- 单节电压较高，常见 $3.3$ 到 $4.2 \ \mathrm{V}$
- 没有明显记忆效应

缺点：

- 充电管理严格，不能过充过放
- 高温和满电存储会加速老化
- 不适合简单涓流充电

## State of Charge 怎么估

作业问三节 LiPo 如何判断剩余电量。常见方法：

- 用电压查放电曲线
- 做 coulomb counting，也就是记录进出电荷
- 同时考虑温度、老化和负载电流

说人话：只看电压不总是可靠，因为很多电池有很平的电压平台；但如果已知放电曲线，电压仍然是最简单的估计方法。

## 易错点

- 自放电率必须先换成每小时或每秒的电流，再和负载电流比较。
- 库仑效率 $\eta_C$ 用在电荷/电流上，能量效率 $\eta_E$ 用在能量上。
- 电池容量 `Ah` 不是能量，乘平均电压才是 `Wh`。
- EPR 不是电池的真实内阻，只是用来描述自放电的等效并联电阻。

