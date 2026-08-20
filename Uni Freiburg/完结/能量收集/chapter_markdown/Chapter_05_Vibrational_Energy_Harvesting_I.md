# Chapter 5 - Vibrational Energy Harvesting I: 振动能量收集先抓住谐振

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_5_Vibrational Energy Harvesting_SS_2025.pdf`
- Exercise: `Exercise 3_with_solutions.pdf` 中的振动题 Task 1-3

说明：习题文件名里写的是 `Exercise 3`，文件夹写的是 `Excercise 4_ Vibrational Energy Harvesting`。这里按主题归到振动章节。

## 这一章在讲什么

振动能量收集的基本思路是：让一个质量块跟环境振动发生相对运动，再把这部分机械能转换成电能。

核心问题只有三个：

- 振动频率能不能对上谐振频率？
- 质量块能不能做得足够大？
- 发电阻尼能不能和损耗阻尼匹配？

## 作业重点公式

### 固有频率

$$
\omega_0=\sqrt{\frac{K}{m}}
$$

$$
f_0=\frac{\omega_0}{2\pi}
$$

设计质量块时常用反过来的形式：

$$
m=\frac{K}{(2\pi f_0)^2}
$$

说人话：弹簧越硬，频率越高；质量越大，频率越低。要对上环境振动频率，就要调 $K$ 和 $m$。

### 振动中存的能量

$$
W=\frac{1}{2}K A^2
$$

因为 $K=m\omega_0^2$，也可以写成：

$$
W=\frac{1}{2}m\omega_0^2A^2
$$

$A$ 是位移振幅。作业中 $m=1 \ \mathrm{g}$，$f=70 \ \mathrm{Hz}$，$A=3 \ \mathrm{mm}$，得到约：

$$
W \approx 873 \ \mathrm{\mu J}
$$

如果一次无线发送需要 $200 \ \mathrm{\mu J}$，最多大约 4 次；发送频率 $0.5 \ \mathrm{Hz}$，可以撑约 8 秒。

### 品质因数 Q

课件和作业都强调：

$$
Q=2\pi\frac{\text{stored energy}}{\text{energy lost per cycle}}
$$

对轻阻尼振子：

$$
Q=\frac{1}{2\zeta}=\frac{m\omega_0}{c_\mathrm{tot}}
$$

$$
c_\mathrm{tot}=c_\mathrm{dis}+c_\mathrm{harv}
$$

说人话：$Q$ 高表示能量留得住、谐振峰很尖；$Q$ 低表示能量散得快、频带更宽。

带宽近似：

$$
\Delta f \approx \frac{f_0}{Q}
$$

### 环境激励力

如果基座振动位移振幅是 $x_\mathrm{vib}$：

$$
a_\mathrm{vib}=\omega_0^2x_\mathrm{vib}
$$

$$
F_0=ma_\mathrm{vib}=m\omega_0^2x_\mathrm{vib}
$$

### 谐振时的输出功率

发电阻尼为 $c_\mathrm{harv}$，机械损耗阻尼为 $c_\mathrm{dis}$：

$$
P_\mathrm{el}
=\frac{1}{2}
\frac{c_\mathrm{harv}}{(c_\mathrm{harv}+c_\mathrm{dis})^2}
m^2a_\mathrm{vib}^2
$$

也可以写成：

$$
P_\mathrm{el}
=\frac{1}{2}
\frac{c_\mathrm{harv}}{(c_\mathrm{harv}+c_\mathrm{dis})^2}
m^2\omega_0^4x_\mathrm{vib}^2
$$

### 最佳阻尼匹配

最大功率条件：

$$
c_\mathrm{harv}=c_\mathrm{dis}
$$

此时：

$$
P_\mathrm{max}
=\frac{1}{8c_\mathrm{dis}}m^2a_\mathrm{vib}^2
$$

或者：

$$
P_\mathrm{max}
=\frac{1}{8c_\mathrm{dis}}m^2\omega_0^4x_\mathrm{vib}^2
$$

说人话：发电器不能太弱，也不能太“刹车”。太弱拿不到能量；太强会把振动压没。最佳是发电阻尼等于本来损耗阻尼。

## Exercise 3 逐题详解

这份 Exercise 里 Task 1-3 是振动能量收集 I 的内容。Task 4-5 分别是压电和电磁收集器，放到后面的振动章节更合适。

## Task 1: Quality Factor

### 题目

题目给出品质因数的定义：

$$
Q
=2\pi
\frac{\text{energy stored}}
{\text{average energy lost per period}}
$$

也就是：

$$
Q
=2\pi\frac{W}{P\cdot T_0}
$$

因为：

$$
T_0=\frac{2\pi}{\omega_0}
$$

所以也可以写成：

$$
Q=\frac{W}{P/\omega_0}
$$

题目要求：从动能和势能出发，推导阻尼谐振子的 $Q$。

### Step 1: 写出位移和速度

阻尼振动位移近似写成：

$$
x(t)=x_0 e^{-t/\tau}\cos(\omega_0 t)
$$

其中：

$$
\tau=\frac{1}{\zeta\omega_0}
$$

题目提示：在一个周期内，指数项变化很慢，可以先把 $e^{-t/\tau}$ 当成常数。

所以速度主要来自 $\cos(\omega_0t)$ 的导数：

$$
\dot{x}(t)
\approx
-\omega_0x_0e^{-t/\tau}\sin(\omega_0t)
$$

这里忽略了指数项求导带来的小项，因为题目假设：

$$
\zeta \ll 1
$$

也就是轻阻尼。

### Step 2: 写出动能和势能

动能：

$$
W_\mathrm{kin}
=
\frac12m\dot{x}^2
$$

代入速度：

$$
W_\mathrm{kin}
=
\frac12m\omega_0^2x_0^2e^{-2t/\tau}\sin^2(\omega_0t)
$$

势能：

$$
W_\mathrm{pot}
=
\frac12kx^2
$$

代入位移：

$$
W_\mathrm{pot}
=
\frac12kx_0^2e^{-2t/\tau}\cos^2(\omega_0t)
$$

又因为：

$$
k=m\omega_0^2
$$

所以势能也可以写成：

$$
W_\mathrm{pot}
=
\frac12m\omega_0^2x_0^2e^{-2t/\tau}\cos^2(\omega_0t)
$$

### Step 3: 总能量

总能量是：

$$
W=W_\mathrm{kin}+W_\mathrm{pot}
$$

代入上面两项：

$$
W
=
\frac12m\omega_0^2x_0^2e^{-2t/\tau}
\left[
\sin^2(\omega_0t)+\cos^2(\omega_0t)
\right]
$$

因为：

$$
\sin^2(\omega_0t)+\cos^2(\omega_0t)=1
$$

所以：

$$
W
=
\frac12m\omega_0^2x_0^2e^{-2t/\tau}
$$

理解：阻尼让振幅按 $e^{-t/\tau}$ 衰减，而能量和振幅平方成正比，所以能量按 $e^{-2t/\tau}$ 衰减。

### Step 4: 能量损失功率

能量损失功率可以看成总能量随时间减少的速率：

$$
P=-\frac{dW}{dt}
$$

由于：

$$
W=W_0e^{-2t/\tau}
$$

所以：

$$
\frac{dW}{dt}
=
-\frac{2}{\tau}W
$$

因此：

$$
P=\frac{2}{\tau}W
$$

### Step 5: 代回 Q 的定义

从定义：

$$
Q=\frac{W}{P/\omega_0}
$$

代入：

$$
P=\frac{2}{\tau}W
$$

得到：

$$
Q
=
\frac{W}{\frac{2W}{\tau\omega_0}}
$$

所以：

$$
Q=\frac{\omega_0\tau}{2}
$$

又因为：

$$
\tau=\frac{1}{\zeta\omega_0}
$$

最终：

$$
Q=\frac{1}{2\zeta}
$$

结果：

$$
\boxed{Q=\frac{1}{2\zeta}}
$$

说人话：$Q$ 越高，表示每个周期损失的能量越少，振子可以振很久；$Q$ 越低，能量很快被阻尼吃掉。

## Task 2: Radio Protocol

### 题目

一次无线发送需要：

$$
E_\mathrm{send}=200\ \mathrm{\mu J}
$$

振动质量：

$$
m=1\ \mathrm{g}=0.001\ \mathrm{kg}
$$

谐振频率：

$$
f_0=70\ \mathrm{Hz}
$$

振幅：

$$
A=3\ \mathrm{mm}=0.003\ \mathrm{m}
$$

发送频率：

$$
f_\mathrm{send}=0.5\ \mathrm{Hz}
$$

假设储存在振子里的能量可以 $100\%$ 使用，问能发几次、能持续多久。

### Step 1: 角频率

$$
\omega_0=2\pi f_0
$$

代入：

$$
\omega_0=2\pi\cdot70
$$

$$
\omega_0\approx439.8\ \mathrm{rad/s}
$$

### Step 2: 等效弹簧刚度

固有频率关系：

$$
\omega_0=\sqrt{\frac{k}{m}}
$$

所以：

$$
k=m\omega_0^2
$$

代入：

$$
k=0.001\cdot(439.8)^2
$$

$$
k\approx193.4\ \mathrm{N/m}
$$

注意单位：

$$
1\ \mathrm{N/m}=1\ \mathrm{kg/s^2}
$$

### Step 3: 振动储能

最大势能：

$$
W=\frac12kA^2
$$

代入：

$$
W
=
\frac12\cdot193.4\cdot(0.003)^2
$$

$$
W\approx0.000873\ \mathrm{J}
$$

也就是：

$$
W\approx873\ \mathrm{\mu J}
$$

### Step 4: 可以发送几次

每次发送需要：

$$
200\ \mathrm{\mu J}
$$

所以最多完整发送次数：

$$
n=
\left\lfloor
\frac{873}{200}
\right\rfloor
$$

$$
n=4
$$

剩余能量：

$$
873-4\cdot200=73\ \mathrm{\mu J}
$$

结果：

$$
\boxed{n=4}
$$

### Step 5: 可以持续多久

发送频率是：

$$
f_\mathrm{send}=0.5\ \mathrm{Hz}
$$

意思是每秒发送 $0.5$ 次，也就是每 $2$ 秒发送一次。

所以：

$$
t=\frac{n}{f_\mathrm{send}}
$$

代入：

$$
t=\frac{4}{0.5}=8\ \mathrm{s}
$$

结果：

$$
\boxed{t=8\ \mathrm{s}}
$$

理解：这里是非常理想的估算。实际系统还会有机械损耗、整流损耗、DC-DC 损耗和储能损耗，所以真实可用时间会更短。

## Task 3: Harvester Design

### 题目

环境振动有三个主频：

| 模式 | 频率 $f$ | 位移振幅 $x_\mathrm{vib}$ |
|---:|---:|---:|
| 1 | $100\ \mathrm{Hz}$ | $50\ \mathrm{\mu m}$ |
| 2 | $200\ \mathrm{Hz}$ | $20\ \mathrm{\mu m}$ |
| 3 | $2.5\ \mathrm{kHz}$ | $5\ \mathrm{\mu m}$ |

可选两个 harvester：

| 参数 | Harvester 1 | Harvester 2 |
|---|---:|---:|
| 刚度 $K$ | $1\ \mathrm{mN/\mu m}$ | $4\ \mathrm{mN/\mu m}$ |
| SI 单位 | $1000\ \mathrm{N/m}$ | $4000\ \mathrm{N/m}$ |
| 寄生阻尼 $c_\mathrm{dis}$ | $10\ \mathrm{g/s}$ | $200\ \mathrm{g/s}$ |
| SI 单位 | $0.01\ \mathrm{kg/s}$ | $0.2\ \mathrm{kg/s}$ |
| 发电阻尼 $c_\mathrm{harv}$ | 可自由选择 | $0.05$ 到 $0.15\ \mathrm{kg/s}$ |

要回答：

1. 选哪个 harvester、哪个频率、质量多大、发电阻尼多大？
2. 如果整流损失 $50\%$，应用端平均可用功率是多少？
3. 如果温度变化导致谐振频率漂移，哪个 harvester 更好？

### Step 1: 每种频率下需要的质量

为了让 harvester 在某个环境频率上谐振，需要：

$$
\omega_0=2\pi f
$$

并且：

$$
\omega_0=\sqrt{\frac{K}{m}}
$$

所以质量为：

$$
m=\frac{K}{(2\pi f)^2}
$$

计算结果：

| Harvester | $100\ \mathrm{Hz}$ | $200\ \mathrm{Hz}$ | $2.5\ \mathrm{kHz}$ |
|---|---:|---:|---:|
| $m_1$ | $2.5\ \mathrm{g}$ | $0.63\ \mathrm{g}$ | $4.1\ \mathrm{mg}$ |
| $m_2$ | $10.1\ \mathrm{g}$ | $2.5\ \mathrm{g}$ | $16\ \mathrm{mg}$ |

理解：频率越高，所需质量越小。到了 $2.5\ \mathrm{kHz}$，质量只能做到毫克级，所以即使频率高，能拿到的功率也不一定大。

### Step 2: 先看理论最大功率

谐振时输出功率：

$$
P_\mathrm{el}
=
\frac12
\frac{c_\mathrm{harv}}
{(c_\mathrm{harv}+c_\mathrm{dis})^2}
m^2\omega_0^4x_\mathrm{vib}^2
$$

如果发电阻尼可以调到最佳：

$$
c_\mathrm{harv}=c_\mathrm{dis}
$$

则：

$$
P_\mathrm{max}
=
\frac{1}{8c_\mathrm{dis}}
m^2\omega_0^4x_\mathrm{vib}^2
$$

Harvester 1 的 $c_\mathrm{harv}$ 可以自由选，所以可以直接做阻尼匹配：

$$
c_{\mathrm{harv},1}=c_{\mathrm{dis},1}=0.01\ \mathrm{kg/s}
$$

Harvester 2 最优本来应该是：

$$
c_{\mathrm{harv},2}=c_{\mathrm{dis},2}=0.2\ \mathrm{kg/s}
$$

但题目限制：

$$
0.05\le c_{\mathrm{harv},2}\le0.15\ \mathrm{kg/s}
$$

所以 Harvester 2 做不到完美匹配，只能取最大：

$$
c_{\mathrm{harv},2}=0.15\ \mathrm{kg/s}
$$

### Step 3: Harvester 1 的功率

Harvester 1 可以匹配阻尼，用：

$$
P_{\mathrm{max},1}
=
\frac{1}{8c_{\mathrm{dis},1}}
m^2\omega_0^4x_\mathrm{vib}^2
$$

代入答案表给出的结果：

| 模式 | 功率 |
|---:|---:|
| $100\ \mathrm{Hz}, 50\ \mathrm{\mu m}$ | $31\ \mathrm{mW}$ |
| $200\ \mathrm{Hz}, 20\ \mathrm{\mu m}$ | $20\ \mathrm{mW}$ |
| $2.5\ \mathrm{kHz}, 5\ \mathrm{\mu m}$ | $0.31\ \mathrm{mW}$ |

所以 Harvester 1 里最好的是：

$$
100\ \mathrm{Hz}
$$

对应：

$$
m_1\approx2.5\ \mathrm{g}
$$

$$
c_{\mathrm{harv},1}=0.01\ \mathrm{kg/s}
$$

### Step 4: Harvester 2 的功率

Harvester 2 不能达到 $c_\mathrm{harv}=c_\mathrm{dis}$，所以要用一般公式：

$$
P_{\mathrm{el},2}
=
\frac12
\frac{c_{\mathrm{harv},2}}
{(c_{\mathrm{harv},2}+c_{\mathrm{dis},2})^2}
m^2\omega_0^4x_\mathrm{vib}^2
$$

取：

$$
c_{\mathrm{harv},2}=0.15\ \mathrm{kg/s}
$$

$$
c_{\mathrm{dis},2}=0.2\ \mathrm{kg/s}
$$

答案表给出的结果：

| 模式 | 功率 |
|---:|---:|
| $100\ \mathrm{Hz}, 50\ \mathrm{\mu m}$ | $24.4\ \mathrm{mW}$ |
| $200\ \mathrm{Hz}, 20\ \mathrm{\mu m}$ | $15.7\ \mathrm{mW}$ |
| $2.5\ \mathrm{kHz}, 5\ \mathrm{\mu m}$ | $0.244\ \mathrm{mW}$ |

所以 Harvester 2 里最好也是：

$$
100\ \mathrm{Hz}
$$

对应：

$$
m_2\approx10.1\ \mathrm{g}
$$

$$
c_{\mathrm{harv},2}=0.15\ \mathrm{kg/s}
$$

### Step 5: 最终选择

比较两个最好结果：

| 方案 | 功率 |
|---|---:|
| Harvester 1 @ $100\ \mathrm{Hz}$ | $31\ \mathrm{mW}$ |
| Harvester 2 @ $100\ \mathrm{Hz}$ | $24.4\ \mathrm{mW}$ |

所以 Task 3a 的选择是：

$$
\boxed{\text{Harvester 1 at }100\ \mathrm{Hz}}
$$

参数：

$$
\boxed{m\approx2.5\ \mathrm{g}}
$$

$$
\boxed{c_\mathrm{harv}=0.01\ \mathrm{kg/s}}
$$

理由：Harvester 1 的寄生阻尼小，而且发电阻尼可以自由调到最佳匹配，所以虽然 Harvester 2 能挂更大的质量，最后还是 Harvester 1 输出功率更高。

### Step 6: 整流后可用功率

题目说整流器有 $50\%$ 损失，也就是效率：

$$
\eta_\mathrm{rect}=0.5
$$

前面选出的机械/电输出功率约：

$$
P_\mathrm{el}=31\ \mathrm{mW}
$$

应用端可用功率：

$$
P_\mathrm{app}
=
\eta_\mathrm{rect}P_\mathrm{el}
$$

代入：

$$
P_\mathrm{app}
=
0.5\cdot31\ \mathrm{mW}
$$

$$
P_\mathrm{app}\approx15.5\ \mathrm{mW}
$$

作业答案四舍五入写：

$$
\boxed{P_\mathrm{app}\approx15\ \mathrm{mW}}
$$

### Step 7: 温度变化时选哪个？

温度变化会让材料参数变动，从而让谐振频率漂移。

这时候不是只看峰值功率，还要看带宽。带宽近似：

$$
\Delta f\approx\frac{f_0}{Q}
$$

而：

$$
Q=\frac{m\omega_0}{c_\mathrm{dis}+c_\mathrm{harv}}
$$

对于 $100\ \mathrm{Hz}$ 的最优点：

| 方案 | 峰值功率 | 整流后功率 | 带宽 |
|---|---:|---:|---:|
| Harvester 1 | $31\ \mathrm{mW}$ | $15\ \mathrm{mW}$ | 约 $1.2\ \mathrm{Hz}$ |
| Harvester 2 | $24.4\ \mathrm{mW}$ | $12.2\ \mathrm{mW}$ | 约 $5.5\ \mathrm{Hz}$ |

Harvester 1 峰值功率更高，但是峰很尖；频率稍微偏掉，功率会掉得比较快。

Harvester 2 峰值低一点，但是带宽更宽。环境或材料参数变化时，它更不怕频率漂移。

所以 Task 3c 的答案是：

$$
\boxed{\text{温度变化明显时，Harvester 2 更稳}}
$$

说人话：如果环境频率非常稳定，选 Harvester 1；如果频率会漂，Harvester 2 可能更实用。

### 关于 Task 3 数字的小检查

严格从公式看，如果已经用：

$$
m=\frac{K}{\omega_0^2}
$$

调到谐振，那么：

$$
m^2\omega_0^4=K^2
$$

也就是说，在同一个 harvester 里，功率对频率本身不再显式依赖，而主要看 $x_\mathrm{vib}^2$ 和阻尼。

所以用 $200\ \mathrm{Hz}, 20\ \mathrm{\mu m}$ 严格代入时，会得到比答案表更小的功率。答案表里 $200\ \mathrm{Hz}$ 那列相当于用了更大的振幅。这里笔记保留答案表的结论，因为最终最优选择仍然是 Harvester 1 @ $100\ \mathrm{Hz}$，不影响主线判断。

## 易错点

- 高频不一定更好。高频虽然让 $\omega^4$ 看起来很大，但为了谐振，质量 $m$ 会按 $1/\omega^2$ 变小。
- 最大功率不是最大 $Q$。加入发电阻尼会降低 $Q$，但可能提高输出电功率。
- 最佳阻尼条件是 $c_\mathrm{harv}=c_\mathrm{dis}$，不是让 $c_\mathrm{harv}$ 越大越好。
- 公式里的 $x_\mathrm{vib}$ 是环境振动位移振幅，不是质量块放大后的相对位移。
- 整流后功率要乘效率。题目里 $50\%$ 损失，就是只剩一半。
- 如果频率会漂移，不能只看峰值功率，还要看带宽。
