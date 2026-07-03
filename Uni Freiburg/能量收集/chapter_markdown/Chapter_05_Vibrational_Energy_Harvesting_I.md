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

## 作业怎么解

### Task 1: 从能量推 Q

题目要你用动能、势能和能量损失推品质因数。逻辑是：

1. 写出总能量 $W=W_\mathrm{kin}+W_\mathrm{pot}$。
2. 阻尼会让振幅指数衰减，所以能量也指数衰减。
3. 每周期损失的能量越少，$Q$ 越高。

最后得到的理解比公式更重要：$Q$ 衡量“振子能把能量存多久”。

### Task 2: 无线协议能发几次

套路：

1. 用 $K=m\omega_0^2$ 得到等效弹簧刚度。
2. 用 $W=\frac12KA^2$ 算振动储能。
3. 用 $W/E_\mathrm{send}$ 算能发几次。
4. 用次数除以发送频率算持续时间。

### Task 3: 选择合适的振动收集器

题目给了三个环境振动：

- $100 \ \mathrm{Hz}, 50 \ \mathrm{\mu m}$
- $200 \ \mathrm{Hz}, 20 \ \mathrm{\mu m}$
- $2.5 \ \mathrm{kHz}, 5 \ \mathrm{\mu m}$

解题顺序：

1. 对每个频率，用 $m=K/(2\pi f)^2$ 算需要的质量。
2. 用 $P_\mathrm{max}$ 算理论最大功率。
3. 如果 $c_\mathrm{harv}$ 不能自由匹配，就用一般功率公式重算。
4. 乘整流效率。作业假设整流损失 50%，所以可用功率是输出的一半。

作业结论：

- 峰值功率最高的是 Harvester 1 @ 100 Hz，约 $31 \ \mathrm{mW}$。
- 整流后可用约 $15 \ \mathrm{mW}$。
- 如果温度变化导致谐振频率漂移，Harvester 2 反而更稳，因为带宽更宽。

## 易错点

- 高频不一定更好。虽然 $\omega^4$ 很诱人，但高频下要达到谐振通常需要很小的质量，功率不一定大。
- 最大功率不是最大 $Q$。加入发电阻尼后 $Q$ 会降低，但输出电功率可能增加。
- 公式里的 $x_\mathrm{vib}$ 是环境振动位移振幅，不是质量块放大后的相对位移。
- 实际系统还要整流和储能，机械端算出来的电功率不是最终可用功率。

