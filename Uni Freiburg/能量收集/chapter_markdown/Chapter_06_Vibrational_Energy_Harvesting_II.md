# Chapter 6 - Vibrational Energy Harvesting II: 压电、电磁、静电三种转换方式

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_6_Vibrational Energy Harvesting II _SS_2025.pdf`
- Exercise: `Exercise 3_with_solutions.pdf` 中的振动题 Task 4-5

## 这一章在讲什么

上一章讲“振动系统怎样拿到机械能”，这一章讲“怎样把这部分机械能变成电能”。

主要有三类：

- Piezoelectric：压电，受力产生电荷，电压高、电流小。
- Electrodynamic：电磁，磁通变化产生电压，适合稍大尺寸，电压偏低。
- Electrostatic：静电，电容变化产生能量，常需要偏置电压或驻极体。

作业重点是压电和电磁。

## 作业重点公式：压电

### 压电基本关系

课件里的线性压电方程可以简化理解为：

$$
D=\varepsilon E+d\sigma
$$

$$
\varepsilon_\mathrm{mech}=\frac{\sigma}{Y}+dE
$$

- $D$：电位移，和表面电荷有关
- $E$：电场
- $\sigma$：机械应力
- $d$：压电系数
- $Y$：杨氏模量

说人话：压电材料是机械和电耦合的。你压它，它出电荷；你给电压，它也会变形。

### 调谐质量

压电梁也可以按振动收集器来设计：

$$
m=\frac{K}{(2\pi f_0)^2}
$$

作业 Task 4 中：

- $K=1000 \ \mathrm{N/m}$
- $f_0=100 \ \mathrm{Hz}$

得到：

$$
m \approx 2.53 \ \mathrm{g}
$$

### 耦合因子

作业给出的耦合因子形式：

$$
k=\sqrt{\frac{\chi^2}{CK}}
$$

说人话：$k$ 越大，机械能和电能之间“互相拉扯”越强。强耦合时，负载电阻会明显改变谐振频率和 Q 值。

### 压电最优负载

定义：

$$
X=\frac{RC\omega_0}{1-k^2}
$$

低耦合情况下，最大化电阻尼时取：

$$
X=1
$$

所以：

$$
R_\mathrm{opt}=\frac{1-k^2}{C\omega_0}
$$

作业中得到：

$$
R_\mathrm{opt}\approx 15.9 \ \mathrm{k\Omega}
$$

### 压电电阻尼

在 $X=1$ 时可用近似：

$$
c_\mathrm{el}
\approx
m\omega_0 \frac{k^2}{2(1-k^2)}
$$

总阻尼：

$$
c_\mathrm{tot}=c_\mathrm{mech}+c_\mathrm{el}
$$

品质因数：

$$
Q=\frac{m\omega_0}{c_\mathrm{tot}}
$$

作业算出 $Q\approx52.7$。

### 压电输出功率

继续沿用振动功率公式，把 $c_\mathrm{harv}$ 换成 $c_\mathrm{el}$：

$$
P_\mathrm{el}
=\frac{1}{2}
\frac{c_\mathrm{el}}{(c_\mathrm{el}+c_\mathrm{mech})^2}
m^2\omega_0^4x_\mathrm{vib}^2
$$

作业结果约：

$$
P_\mathrm{max}\approx557 \ \mathrm{\mu W}
$$

## 作业重点公式：电磁

### 法拉第电磁感应

$$
U=-N\frac{d\Phi}{dt}
$$

如果磁通随位置变化：

$$
U=-N\frac{d\Phi}{dz}\dot z
$$

定义电磁转换因子：

$$
k_t=\frac{U}{\dot z}=\frac{F}{I}
$$

说人话：$k_t$ 同时描述“运动产生多少电压”和“电流产生多少反作用力”。

如果近似磁场梯度恒定：

$$
k_t \approx N A \frac{dB}{dz}
$$

作业最后根据磁场积分算出：

$$
k_t \approx 0.33
$$

### 线圈电阻

$$
R_0=l_\mathrm{wire}r'
$$

作业中线圈每圈约 $4l$，匝数 $N=125$：

$$
R_0 = 4lN r' \approx 68 \ \Omega
$$

### 电磁电阻尼

$$
c_\mathrm{el}=\frac{k_t^2}{R_0+R_L}
$$

负载只能拿到总电功率的一部分：

$$
\frac{R_L}{R_0+R_L}
$$

因为线圈自身电阻也会发热。

### 电磁最优负载

作业按阻尼比 $\zeta_m$ 直接写成：

$$
R_{L,\mathrm{opt}}=R_0+\frac{k_t^2}{m\omega_0\zeta_m}
$$

如果先定义机械阻尼常数：

$$
c_\mathrm{mech}=2m\omega_0\zeta_m
$$

那么同一个匹配条件也常会写成含 $c_\mathrm{mech}$ 的形式。这里跟作业保持一致，避免符号约定混淆。

作业结果：

$$
R_{L,\mathrm{opt}}\approx70.57 \ \Omega
$$

### 电磁输出功率

谐振时：

$$
P_L=
\frac{1}{2}
\frac{c_\mathrm{el}}{(c_\mathrm{el}+c_\mathrm{mech})^2}
m^2a_\mathrm{vib}^2
\frac{R_L}{R_0+R_L}
$$

作业结果约：

$$
P_L\approx13.35 \ \mathrm{mW}
$$

## 静电收集器公式

### 电容

$$
C=\varepsilon_0\varepsilon_r\frac{A}{d}
$$

### 电容能量

$$
W=\frac{1}{2}CU^2
$$

也可以写成：

$$
W=\frac{Q^2}{2C}
$$

静电收集器靠改变 $C$ 来做功。常见方式：

- Constant voltage：电压近似保持，改变电容会转移电荷。
- Constant charge：电荷近似保持，电容变小会让电压升高。
- Electret：用驻极体提供内置偏置，不需要外部预充电源。

## 三种方式怎么选

| 类型 | 优点 | 缺点 |
|---|---|---|
| 压电 | 电压高，能量密度高，结构紧凑 | 材料脆，电流小，负载影响明显 |
| 电磁 | 原理成熟，放大尺寸后好用，磁铁可当质量块 | 微型化困难，电压偏低 |
| 静电 | 适合 MEMS，容易微型化 | 需要偏置或驻极体，源阻抗高 |

## 易错点

- 压电不是普通电压源，它本身有电容，负载会改变机械响应。
- 电磁收集器的线圈内阻不能忽略，否则会高估负载功率。
- 公式里的 $k$ 在压电和电磁中含义不同：压电 $k$ 是耦合因子，电磁 $k_t$ 是转换因子。
- 静电收集器如果没有偏置电压或驻极体，很难凭空输出有用能量。
