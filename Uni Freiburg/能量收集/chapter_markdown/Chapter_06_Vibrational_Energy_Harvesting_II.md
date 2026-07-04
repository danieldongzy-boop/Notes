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

## Exercise 3 逐题详解

这一章对应振动 Exercise 的 Task 4 和 Task 5：

- Task 4：压电 harvester，调质量和负载电阻。
- Task 5：电磁 harvester，算线圈、负载和输出功率。

## Task 4: Piezoelectric Harvester Design

### 题目

目标谐振频率：

$$
f_0=100\ \mathrm{Hz}
$$

环境振动位移振幅：

$$
x_\mathrm{vib}=10\ \mathrm{\mu m}
$$

弹簧刚度：

$$
K=1000\ \mathrm{N/m}
$$

机械阻尼：

$$
c_\mathrm{mech}=0.02\ \mathrm{kg/s}
$$

压电电容：

$$
C=100\ \mathrm{nF}
$$

耦合系数：

$$
\theta=0.0008\ \mathrm{A\,s/m}
$$

要求：通过调整质量 $m$ 和负载电阻 $R$，让谐振输出功率最大，并求最大功率和功率带宽。

### Step 1: 调质量到 100 Hz

谐振频率近似等于机械固有频率：

$$
\omega_0=2\pi f_0
$$

$$
\omega_0=2\pi\cdot100\approx628.3\ \mathrm{rad/s}
$$

由：

$$
\omega_0=\sqrt{\frac{K}{m}}
$$

得到：

$$
m=\frac{K}{\omega_0^2}
$$

代入：

$$
m=\frac{1000}{(2\pi\cdot100)^2}
$$

$$
m\approx0.00253\ \mathrm{kg}
$$

也就是：

$$
\boxed{m\approx2.53\ \mathrm{g}}
$$

### Step 2: 算压电耦合因子

题目给：

$$
k=\sqrt{\frac{\theta^2}{CK}}
$$

代入：

$$
k
=
\sqrt{
\frac{(0.0008)^2}{100\cdot10^{-9}\cdot1000}
}
$$

$$
k=\sqrt{0.0064}=0.08
$$

结果：

$$
\boxed{k=0.08}
$$

理解：这个耦合不算强，所以负载对谐振频率的影响很小。

### Step 3: 判断能不能做到阻尼匹配

理想最大功率通常希望：

$$
c_\mathrm{el}=c_\mathrm{mech}
$$

但这题的压电耦合较弱，答案里用判据得到：

$$
\frac{c_\mathrm{mech}(1-k^2)}
{k^2m\omega_0}
\approx1.96>\frac12
$$

意思是：靠这个压电耦合，电阻尼 $c_\mathrm{el}$ 做不到和机械阻尼一样大。

所以策略不是强行匹配，而是：

$$
\text{让 }c_\mathrm{el}\text{ 尽可能大}
$$

### Step 4: 最优负载电阻

电阻尼最大时：

$$
R_\mathrm{opt}
=
\frac{1-k^2}{C\omega_0}
$$

代入：

$$
R_\mathrm{opt}
=
\frac{1-0.08^2}
{100\cdot10^{-9}\cdot628.3}
$$

$$
R_\mathrm{opt}\approx15.9\ \mathrm{k\Omega}
$$

结果：

$$
\boxed{R_\mathrm{opt}\approx15.9\ \mathrm{k\Omega}}
$$

### Step 5: 负载引起的谐振频率变化

题目给了一个修正公式。把最优电阻代进去后，答案得到：

$$
\omega_R\approx1.00002\omega_0
$$

也就是说谐振频率几乎没变。

所以前面算出的质量不需要再重新调整：

$$
m\approx2.53\ \mathrm{g}
$$

### Step 6: 品质因数和带宽

在最优负载附近，答案得到电阻尼：

$$
c_\mathrm{el}\approx0.01\ \mathrm{kg/s}
$$

总阻尼：

$$
c_\mathrm{tot}=c_\mathrm{mech}+c_\mathrm{el}
$$

$$
c_\mathrm{tot}=0.02+0.01=0.03\ \mathrm{kg/s}
$$

品质因数：

$$
Q=\frac{m\omega_0}{c_\mathrm{tot}}
$$

代入：

$$
Q=\frac{0.00253\cdot628.3}{0.03}
$$

$$
Q\approx52.7
$$

功率带宽近似：

$$
\Delta f\approx\frac{f_0}{Q}
$$

所以：

$$
\Delta f\approx\frac{100}{52.7}
$$

$$
\Delta f\approx1.9\ \mathrm{Hz}
$$

结果：

$$
\boxed{Q\approx52.7,\quad \Delta f\approx1.9\ \mathrm{Hz}}
$$

### Step 7: 最大输出功率

沿用振动收集器功率公式：

$$
P_\mathrm{el}
=
\frac12
\frac{c_\mathrm{el}}
{(c_\mathrm{el}+c_\mathrm{mech})^2}
m^2\omega_0^4x_\mathrm{vib}^2
$$

答案代入后得到：

$$
P_\mathrm{el}\approx557\ \mathrm{\mu W}
$$

结果：

$$
\boxed{P_\mathrm{max}\approx557\ \mathrm{\mu W}}
$$

说人话：这题的关键不是死算公式，而是看懂“压电负载电阻会产生电阻尼”。调 $R$ 的本质是在调机械系统里被电路抽走的能量。

## Task 5: Electrodynamic Harvester

### 题目

磁铁是 NdFeB，密度：

$$
\rho_m=7.819\ \mathrm{g/cm^3}
$$

磁铁是边长 $10\ \mathrm{mm}$ 的立方体，所以体积：

$$
V=1\ \mathrm{cm^3}
$$

整体高度：

$$
h=15\ \mathrm{mm}
$$

磁铁高度：

$$
h_\mathrm{mag}=10\ \mathrm{mm}
$$

线径：

$$
d_D=40\ \mathrm{\mu m}
$$

线圈每圈近似为边长 $l=a=10\ \mathrm{mm}$ 的矩形，导线电阻：

$$
r'=13.6\ \Omega/\mathrm{m}
$$

机械阻尼比：

$$
\zeta_m=0.015
$$

谐振频率：

$$
f=33\ \mathrm{Hz}
$$

振动加速度：

$$
A_g=1\ \mathrm{m/s^2}
$$

### Step 1: 线圈匝数

可绕线高度是：

$$
h-h_\mathrm{mag}=15\ \mathrm{mm}-10\ \mathrm{mm}=5\ \mathrm{mm}
$$

每层导线直径：

$$
d_D=40\ \mathrm{\mu m}=0.04\ \mathrm{mm}
$$

所以匝数：

$$
N=\frac{5\ \mathrm{mm}}{0.04\ \mathrm{mm}}
$$

$$
N=125
$$

结果：

$$
\boxed{N=125}
$$

### Step 2: 线圈电阻

每圈线长约：

$$
l_\mathrm{turn}=4l=4\cdot10\ \mathrm{mm}=40\ \mathrm{mm}
$$

总线长：

$$
l_\mathrm{wire}=Nl_\mathrm{turn}
$$

$$
l_\mathrm{wire}=125\cdot40\ \mathrm{mm}=5000\ \mathrm{mm}
$$

也就是：

$$
l_\mathrm{wire}=5\ \mathrm{m}
$$

线圈电阻：

$$
R_0=l_\mathrm{wire}r'
$$

$$
R_0=5\cdot13.6=68\ \Omega
$$

结果：

$$
\boxed{R_0=68\ \Omega}
$$

### Step 3: 磁铁质量

磁铁体积：

$$
V=1\ \mathrm{cm^3}
$$

所以质量：

$$
m=\rho_m V
$$

$$
m=7.819\ \mathrm{g}
$$

也就是：

$$
\boxed{m=0.007819\ \mathrm{kg}}
$$

角频率：

$$
\omega=2\pi f
$$

$$
\omega=2\pi\cdot33\approx207.3\ \mathrm{rad/s}
$$

### Step 4: 最优负载电阻

题目先给一个耦合因子估计值：

$$
k=0.25
$$

答案使用：

$$
R_{L,\mathrm{opt}}
=
R_0+
\frac{k^2}{m\omega\zeta_m}
$$

代入后：

$$
R_{L,\mathrm{opt}}\approx70.57\ \Omega
$$

结果：

$$
\boxed{R_{L,\mathrm{opt}}\approx70.6\ \Omega}
$$

理解：最优负载和线圈内阻是同一个量级，不是无限大，也不是短路。

### Step 5: 真实电磁转换因子

题目给：

$$
\int_0^{h_\mathrm{coil}}B_x(x)\,dx
=0.00132\ \mathrm{T\,m}
$$

转换因子：

$$
k_t
=
N\cdot
\frac{a}{h_\mathrm{coil}}
\int_0^{h_\mathrm{coil}}B_x(x)\,dx
$$

其中：

$$
N=125,\quad a=10\ \mathrm{mm},\quad h_\mathrm{coil}=5\ \mathrm{mm}
$$

所以：

$$
k_t
=125\cdot\frac{10}{5}\cdot0.00132
$$

$$
k_t\approx0.33
$$

结果：

$$
\boxed{k_t\approx0.33}
$$

说人话：$k_t$ 越大，同样速度产生的电压越大，同时电流产生的反向阻尼也越强。

### Step 6: 输出功率

机械阻尼：

$$
c_\mathrm{mech}
=
2m\omega\zeta_m
$$

电磁电阻尼：

$$
c_\mathrm{el}
=
\frac{k_t^2}{R_0+R_L}
$$

负载功率还要乘线圈内阻分压因子：

$$
\frac{R_L}{R_0+R_L}
$$

谐振时答案给出的负载输出功率为：

$$
P_L\approx13.35\ \mathrm{mW}
$$

结果：

$$
\boxed{P_L\approx13.35\ \mathrm{mW}}
$$

这题要特别小心：线圈内阻 $R_0$ 会吃掉一部分电功率，所以不能只看电磁转换产生了多少功率，还要看负载真正分到多少。

### Task 4/5 小结

| 题目 | 关键调参 | 最终结果 |
|---|---|---|
| Task 4 压电 | 调 $m$ 到 100 Hz，调 $R$ 到电阻尼最大 | $m=2.53\ \mathrm{g}$，$R_\mathrm{opt}=15.9\ \mathrm{k\Omega}$，$P\approx557\ \mathrm{\mu W}$ |
| Task 5 电磁 | 算线圈匝数、内阻、最优负载 | $N=125$，$R_0=68\ \Omega$，$R_L\approx70.6\ \Omega$，$P\approx13.35\ \mathrm{mW}$ |

## 易错点

- 压电不是普通电压源，它本身有电容，负载会改变机械响应。
- 电磁收集器的线圈内阻不能忽略，否则会高估负载功率。
- 公式里的 $k$ 在压电和电磁中含义不同：压电 $k$ 是耦合因子，电磁 $k_t$ 是转换因子。
- 静电收集器如果没有偏置电压或驻极体，很难凭空输出有用能量。
