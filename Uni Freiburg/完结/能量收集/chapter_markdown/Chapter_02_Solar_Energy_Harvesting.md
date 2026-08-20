# Chapter 2 - Solar Energy Harvesting: 太阳能先看光，再看电池

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_2_Solar Energy Harvesting_SS_2026.pdf`
- Exercise: `Exercise 2_Photovoltaics_SOLVED_SS_2026.pdf`
- Exercise information: Solems solar cell datasheet PDFs

## 这一章在讲什么

太阳能收集分两步：

1. 算到达太阳能板表面的光有多少。
2. 算太阳能电池能把这些光变成多少电功率。

所以本章的作业也分成两类：Task 1 算辐照度，Task 2 和 Task 3 算太阳能电池参数，Bonus Task 4 算太阳位置。

## 公式速查

### 光子能量

$$
E_\mathrm{photon}=hf=\frac{hc}{\lambda}
$$

说人话：波长越短，单个光子能量越高。算太阳能电池短路电流时，要先把光功率换成“每秒有多少个光子”。

### 倾斜太阳能板上的直射辐照度

如果太阳高度角是 $\alpha$，太阳能板相对地平线的倾角是 $\beta$：

$$
S_m=S_i\sin(\alpha+\beta)
$$

当 $\alpha+\beta=90^\circ$ 时，光线垂直打到板上，直射辐照度最大。

### 扩散光近似

作业里冬天那题使用：

$$
S_{m,\mathrm{diff}}=I_\mathrm{diff}\frac{180^\circ-\beta}{180^\circ}
$$

说人话：板子越平，能接收到的天空扩散光越多；板子越竖，扩散光越少。

### 太阳能电池短路电流

理想量子效率 $QE=1$ 时：

$$
I_{SC}=q\frac{P_\mathrm{in}}{E_\mathrm{photon}}
$$

也可以写成：

$$
I_{SC}=QE\frac{q\lambda}{hc}P_\mathrm{in}
$$

其中：

$$
P_\mathrm{in}=H A
$$

### 开路电压

$$
V_{OC}=\frac{nkT}{q}\ln\left(\frac{I_L}{I_0}+1\right)
$$

这里一般取：

$$
I_L\approx I_{SC}
$$

### 填充因子

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}
$$

常用近似：

$$
v_{OC}=\frac{qV_{OC}}{nkT}
$$

$$
FF\approx\frac{v_{OC}-\ln(v_{OC}+0.72)}{v_{OC}+1}
$$

### 效率

$$
\eta=\frac{P_\mathrm{max}}{P_\mathrm{in}}
=\frac{V_{OC}I_{SC}FF}{P_\mathrm{in}}
$$

## Exercise 2 逐题详解

## Task 1: Irradiance

### 题目

夏天晴天，太阳直射辐照度：

$$
I_D=850 \ \mathrm{W/m^2}
$$

太阳高度角：

$$
\alpha=45^\circ
$$

1. a) 太阳能板最佳朝向是多少？辐照度是多少？
2. b) 如果太阳能板倾角只有 $15^\circ$，辐照度是多少？
3. 冬天时，直射和扩散辐照度都取 $300 \ \mathrm{W/m^2}$，太阳高度角 $23^\circ$。分别计算 $\beta=15^\circ$ 和 $\beta=45^\circ$ 时的总辐照度。

### Task 1a: 夏天最佳角度

最佳情况是光线垂直打到太阳能板上：

$$
\alpha+\beta=90^\circ
$$

已知：

$$
\alpha=45^\circ
$$

所以：

$$
\beta=45^\circ
$$

先算直射部分：

$$
S_m=850\sin(45^\circ+45^\circ)
$$

$$
S_m=850\sin(90^\circ)=850 \ \mathrm{W/m^2}
$$

作业再乘一个经验扩散光系数 1.1：

$$
S_G=1.1S_m=1.1\cdot850=935 \ \mathrm{W/m^2}
$$

结果：

- 最佳倾角：$\beta=45^\circ$
- 直射到板上的辐照度：$850 \ \mathrm{W/m^2}$
- 加经验扩散光后的总辐照度：$935 \ \mathrm{W/m^2}$

### Task 1b: 夏天板子倾角 15 度

已知：

$$
\beta=15^\circ
$$

直射部分：

$$
S_m=850\sin(45^\circ+15^\circ)
$$

$$
S_m=850\sin(60^\circ)
$$

$$
S_m\approx736 \ \mathrm{W/m^2}
$$

加经验扩散光系数：

$$
S_G=1.1\cdot736\approx810 \ \mathrm{W/m^2}
$$

结果：

- 直射到板上的辐照度：$736 \ \mathrm{W/m^2}$
- 加经验扩散光后的总辐照度：$810 \ \mathrm{W/m^2}$

理解：倾角 $15^\circ$ 时，太阳光不是垂直打到板上，所以有效辐照度比最佳角度小。

### Task 1c: 冬天，太阳高度角 23 度，板子倾角 15 度

已知：

$$
\alpha=23^\circ,\quad \beta=15^\circ
$$

直射部分：

$$
S_m=300\sin(23^\circ+15^\circ)
$$

$$
S_m=300\sin(38^\circ)\approx185 \ \mathrm{W/m^2}
$$

扩散光部分：

$$
S_{m,\mathrm{diff}}=300\frac{180^\circ-15^\circ}{180^\circ}
$$

$$
S_{m,\mathrm{diff}}=300\frac{165}{180}=275 \ \mathrm{W/m^2}
$$

总辐照度：

$$
S_\mathrm{global}=185+275=460 \ \mathrm{W/m^2}
$$

结果：

$$
S_\mathrm{global}=460 \ \mathrm{W/m^2}
$$

### Task 1d: 冬天，太阳高度角 23 度，板子倾角 45 度

已知：

$$
\alpha=23^\circ,\quad \beta=45^\circ
$$

直射部分：

$$
S_m=300\sin(23^\circ+45^\circ)
$$

$$
S_m=300\sin(68^\circ)\approx278 \ \mathrm{W/m^2}
$$

扩散光部分：

$$
S_{m,\mathrm{diff}}=300\frac{180^\circ-45^\circ}{180^\circ}
$$

$$
S_{m,\mathrm{diff}}=300\frac{135}{180}=225 \ \mathrm{W/m^2}
$$

总辐照度：

$$
S_\mathrm{global}=278+225=503 \ \mathrm{W/m^2}
$$

结果：

$$
S_\mathrm{global}=503 \ \mathrm{W/m^2}
$$

### Task 1 小结

| 情况 | 直射部分 | 扩散/经验修正 | 总辐照度 |
|---|---:|---:|---:|
| 夏天，最佳 $\beta=45^\circ$ | $850 \ \mathrm{W/m^2}$ | 乘 1.1 | $935 \ \mathrm{W/m^2}$ |
| 夏天，$\beta=15^\circ$ | $736 \ \mathrm{W/m^2}$ | 乘 1.1 | $810 \ \mathrm{W/m^2}$ |
| 冬天，$\beta=15^\circ$ | $185 \ \mathrm{W/m^2}$ | $275 \ \mathrm{W/m^2}$ | $460 \ \mathrm{W/m^2}$ |
| 冬天，$\beta=45^\circ$ | $278 \ \mathrm{W/m^2}$ | $225 \ \mathrm{W/m^2}$ | $503 \ \mathrm{W/m^2}$ |

重点：晴天直射光占主导时，要让板子尽量垂直太阳光。阴天或冬天扩散光明显时，不能只看直射角度，还要把天空扩散光算进去。

## Task 2: Silicon Solar Cell

### 题目

一个硅太阳能电池：

- Band gap: $1.12 \ \mathrm{eV}$
- 单色钠灯照射：$\lambda=589 \ \mathrm{nm}$
- 辐照度：$1000 \ \mathrm{W/m^2}$
- 电池是正方形，边长 $5 \ \mathrm{cm}$
- 理想因子：$n=1.1$
- 暗电流：$I_0=1 \ \mathrm{pA}$
- 温度：$T=300 \ \mathrm{K}$
- 假设 $QE=1$，所有电子-空穴对都被收集
- 忽略寄生电阻

要求：

1. a) 算 $I_{SC}$、$V_{OC}$、$FF$ 和效率 $\eta$。
2. b) 如果前金属接触腐蚀导致串联电阻 $R_S=0.01 \ \Omega$，功率损失比例是多少？

### Task 2a Step 1: 面积和输入功率

面积：

$$
A=(5 \ \mathrm{cm})^2=25 \ \mathrm{cm^2}
$$

换成平方米：

$$
A=25\cdot10^{-4}=2.5\cdot10^{-3} \ \mathrm{m^2}
$$

输入光功率：

$$
P_\mathrm{in}=1000\cdot2.5\cdot10^{-3}=2.5 \ \mathrm{W}
$$

结果：

$$
P_\mathrm{in}=2.5 \ \mathrm{W}
$$

### Task 2a Step 2: 算短路电流

先用光谱响应公式：

$$
I_{SC}=QE\frac{q\lambda}{hc}P_\mathrm{in}
$$

代入：

$$
q=1.602176634\cdot10^{-19} \ \mathrm{C}
$$

$$
\lambda=5.89\cdot10^{-7} \ \mathrm{m}
$$

$$
h=6.62607015\cdot10^{-34} \ \mathrm{J\,s}
$$

$$
c=299792458 \ \mathrm{m/s}
$$

$$
P_\mathrm{in}=2.5 \ \mathrm{W}
$$

所以：

$$
I_{SC}
=1\cdot\frac{1.602176634\cdot10^{-19}\cdot5.89\cdot10^{-7}}
{6.62607015\cdot10^{-34}\cdot299792458}
\cdot2.5
$$

$$
I_{SC}\approx1.19 \ \mathrm{A}
$$

结果：

$$
I_{SC}=1.19 \ \mathrm{A}
$$

理解：589 nm 的光子能量约 $2.11 \ \mathrm{eV}$，大于硅的 band gap $1.12 \ \mathrm{eV}$，所以理想情况下能产生电子-空穴对。但多出来的能量不会都变成电能，会热化损失。

### Task 2a Step 3: 算开路电压

公式：

$$
V_{OC}=\frac{nkT}{q}\ln\left(\frac{I_L}{I_0}+1\right)
$$

这里：

$$
I_L\approx I_{SC}=1.19 \ \mathrm{A}
$$

代入：

$$
V_{OC}
=\frac{1.1\cdot1.380649\cdot10^{-23}\cdot300}
{1.602176634\cdot10^{-19}}
\ln\left(\frac{1.19}{1\cdot10^{-12}}+1\right)
$$

结果：

$$
V_{OC}\approx0.79 \ \mathrm{V}
$$

理解：$I_{SC}$ 很大、$I_0$ 很小，所以开路电压较高。但因为是 $\ln$，电压不会随光强线性增加。

### Task 2a Step 4: 算填充因子

先算 reduced open-circuit voltage：

$$
v_{OC}=\frac{qV_{OC}}{nkT}
$$

代入：

$$
v_{OC}
=\frac{1.602176634\cdot10^{-19}\cdot0.79}
{1.1\cdot1.380649\cdot10^{-23}\cdot300}
$$

$$
v_{OC}\approx27.8
$$

再用近似公式：

$$
FF=\frac{v_{OC}-\ln(v_{OC}+0.72)}{v_{OC}+1}
$$

$$
FF=\frac{27.8-\ln(27.8+0.72)}{27.8+1}
$$

$$
FF\approx0.849
$$

结果：

$$
FF=0.849
$$

### Task 2a Step 5: 算最大功率和效率

最大功率：

$$
P_\mathrm{max}=V_{OC}I_{SC}FF
$$

$$
P_\mathrm{max}=0.79\cdot1.19\cdot0.849
$$

$$
P_\mathrm{max}\approx0.80 \ \mathrm{W}
$$

效率：

$$
\eta=\frac{P_\mathrm{max}}{P_\mathrm{in}}
$$

$$
\eta=\frac{0.80}{2.5}=0.319
$$

结果：

$$
\eta=31.9\%
$$

### Task 2a 最终结果

| 参数 | 结果 |
|---|---:|
| $P_\mathrm{in}$ | $2.5 \ \mathrm{W}$ |
| $I_{SC}$ | $1.19 \ \mathrm{A}$ |
| $V_{OC}$ | $0.79 \ \mathrm{V}$ |
| $FF$ | $0.849$ |
| $P_\mathrm{max}$ | $0.80 \ \mathrm{W}$ |
| $\eta$ | $31.9\%$ |

### Task 2b Step 1: 特征电阻

串联电阻：

$$
R_S=0.01 \ \Omega
$$

特征电阻近似：

$$
R_{CH}\approx\frac{V_{OC}}{I_{SC}}
$$

$$
R_{CH}=\frac{0.79}{1.19}=0.666 \ \Omega
$$

### Task 2b Step 2: 归一化串联电阻

$$
r_S=\frac{R_S}{R_{CH}}
$$

$$
r_S=\frac{0.01}{0.666}\approx0.015
$$

### Task 2b Step 3: 串联电阻后的 FF

使用经验公式：

$$
FF_S\approx FF_0\left(1-1.1r_S+\frac{r_S^2}{5.4}\right)
$$

代入：

$$
FF_S\approx0.849\left(1-1.1\cdot0.015+\frac{0.015^2}{5.4}\right)
$$

$$
FF_S\approx0.835
$$

### Task 2b Step 4: 新最大功率

$$
P'_\mathrm{max}=V_{OC}I_{SC}FF_S
$$

$$
P'_\mathrm{max}=0.79\cdot1.19\cdot0.835
$$

$$
P'_\mathrm{max}\approx0.78 \ \mathrm{W}
$$

原来：

$$
P_\mathrm{max}\approx0.80 \ \mathrm{W}
$$

保留下来的比例：

$$
\frac{P'_\mathrm{max}}{P_\mathrm{max}}
=\frac{0.78}{0.80}
\approx98.4\%
$$

损失：

$$
100\%-98.4\%=1.6\%
$$

结果：

- 新的 $FF$：$0.835$
- 新的最大功率：约 $0.78 \ \mathrm{W}$
- 因串联电阻造成的功率损失：约 $1.6\%$

理解：$0.01 \ \Omega$ 看起来很小，但太阳能电池电流有 $1.19 \ \mathrm{A}$，所以它已经能造成可见的 FF 损失。

## Task 3: Indoor Photovoltaics

### 题目

使用 Solems 07/055/020 太阳能电池。根据数据表，在不同光照条件下计算并比较：

- 填充因子 $FF$
- 电池效率 $\eta$

数据表给出：

| 条件 | $V_{OC}$ | $I_{SC}$ | 最大功率点 |
|---|---:|---:|---:|
| 200 lux | $3.9 \ \mathrm{V}$ | $15 \ \mathrm{\mu A}$ | $12 \ \mathrm{\mu A}$ @ $2.8 \ \mathrm{V}$ |
| 1000 lux | $4.2 \ \mathrm{V}$ | $70 \ \mathrm{\mu A}$ | $62 \ \mathrm{\mu A}$ @ $3.0 \ \mathrm{V}$ |
| $200 \ \mathrm{W/m^2}$ | $4.5 \ \mathrm{V}$ | $2 \ \mathrm{mA}$ | $1.8 \ \mathrm{mA}$ @ $3.5 \ \mathrm{V}$ |
| $1000 \ \mathrm{W/m^2}$ | $5.0 \ \mathrm{V}$ | $11 \ \mathrm{mA}$ | $9.6 \ \mathrm{mA}$ @ $3.7 \ \mathrm{V}$ |

电池面积：

$$
A=11 \ \mathrm{cm^2}=1.1\cdot10^{-3} \ \mathrm{m^2}
$$

### Step 1: 最大功率点功率

公式：

$$
P_{MP}=V_{MP}I_{MP}
$$

200 lux：

$$
P_{MP}=2.8\cdot12 \ \mathrm{\mu A}=33.6 \ \mathrm{\mu W}\approx0.03 \ \mathrm{mW}
$$

1000 lux：

$$
P_{MP}=3.0\cdot62 \ \mathrm{\mu A}=186 \ \mathrm{\mu W}\approx0.19 \ \mathrm{mW}
$$

$200 \ \mathrm{W/m^2}$：

$$
P_{MP}=3.5\cdot1.8 \ \mathrm{mA}=6.30 \ \mathrm{mW}
$$

$1000 \ \mathrm{W/m^2}$：

$$
P_{MP}=3.7\cdot9.6 \ \mathrm{mA}=35.52 \ \mathrm{mW}
$$

### Step 2: 填充因子

公式：

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}
$$

200 lux：

$$
FF=\frac{33.6 \ \mathrm{\mu W}}{3.9\cdot15 \ \mathrm{\mu A}}
\approx0.57
$$

1000 lux：

$$
FF=\frac{186 \ \mathrm{\mu W}}{4.2\cdot70 \ \mathrm{\mu A}}
\approx0.63
$$

$200 \ \mathrm{W/m^2}$：

$$
FF=\frac{6.30 \ \mathrm{mW}}{4.5\cdot2 \ \mathrm{mA}}
\approx0.70
$$

$1000 \ \mathrm{W/m^2}$：

$$
FF=\frac{35.52 \ \mathrm{mW}}{5.0\cdot11 \ \mathrm{mA}}
\approx0.65
$$

### Step 3: 输入功率

对以 $\mathrm{W/m^2}$ 给出的情况：

$$
P_\mathrm{in}=H A
$$

$200 \ \mathrm{W/m^2}$：

$$
P_\mathrm{in}=200\cdot1.1\cdot10^{-3}=0.22 \ \mathrm{W}
$$

$1000 \ \mathrm{W/m^2}$：

$$
P_\mathrm{in}=1000\cdot1.1\cdot10^{-3}=1.1 \ \mathrm{W}
$$

对 lux 条件，作业使用数据表对应的换算结果：

- 200 lux: $P_\mathrm{in}=0.0022 \ \mathrm{W}$
- 1000 lux: $P_\mathrm{in}=0.011 \ \mathrm{W}$

### Step 4: 效率

公式：

$$
\eta=\frac{P_{MP}}{P_\mathrm{in}}
$$

200 lux：

$$
\eta=\frac{0.0336 \ \mathrm{mW}}{2.2 \ \mathrm{mW}}
\approx1.53\%
$$

1000 lux：

$$
\eta=\frac{0.186 \ \mathrm{mW}}{11 \ \mathrm{mW}}
\approx1.69\%
$$

$200 \ \mathrm{W/m^2}$：

$$
\eta=\frac{6.30 \ \mathrm{mW}}{220 \ \mathrm{mW}}
\approx2.86\%
$$

$1000 \ \mathrm{W/m^2}$：

$$
\eta=\frac{35.52 \ \mathrm{mW}}{1100 \ \mathrm{mW}}
\approx3.23\%
$$

### Task 3a 最终表

| 条件 | $P_{MP}$ | $FF$ | $P_\mathrm{in}$ | $\eta$ |
|---|---:|---:|---:|---:|
| 200 lux | $0.03 \ \mathrm{mW}$ | 0.57 | $0.0022 \ \mathrm{W}$ | 1.53% |
| 1000 lux | $0.19 \ \mathrm{mW}$ | 0.63 | $0.011 \ \mathrm{W}$ | 1.69% |
| $200 \ \mathrm{W/m^2}$ | $6.30 \ \mathrm{mW}$ | 0.70 | $0.22 \ \mathrm{W}$ | 2.86% |
| $1000 \ \mathrm{W/m^2}$ | $35.52 \ \mathrm{mW}$ | 0.65 | $1.1 \ \mathrm{W}$ | 3.23% |

理解：室内光下输出功率很小，只有几十到几百微瓦。强光下效率更高，但这个室内光伏电池总体效率仍然只有几个百分点。

### Task 3b: 搭配什么电池系统？

作业答案：合理选择是 Li-ion 系统，并且必须加 charge controller。

原因：

- 太阳能电池最大功率点电压大约 $2.8$ 到 $3.7 \ \mathrm{V}$。
- Li-ion 电池电压范围和这个比较接近。
- 但 Li-ion 不能随便充电，必须限制过充、过放和充电电流。
- 加 charge controller 会有损耗，这个损耗必须接受。

结果：

$$
\text{Li-ion battery + charge controller}
$$

### Task 3c: 除了供电还能做什么？

可以当光传感器。

理由：

$$
I_{SC}\propto \text{light intensity}
$$

也就是说，短路电流越大，光越强。用这个关系可以估计环境光强。

## Bonus Task 4: Position of the Sun

### 题目

地点：Toronto, Canada

$$
\varphi=43.66135^\circ
$$

$$
\mathrm{Longitude}=-79.383087^\circ
$$

时间：November 12th, 10:00 local time, UTC-5

要求计算：

1. Hour Angle, HRA
2. Elevation angle, $\alpha$
3. Azimuth

### Step 1: Local Standard Time Meridian

UTC-5 对应：

$$
LSTM=15^\circ\cdot(-5)=-75^\circ
$$

### Step 2: 日期参数 B

11 月 12 日是一年中的第 $316$ 天：

$$
d=316
$$

$$
B=\frac{360^\circ}{365}(d-81)
$$

$$
B=\frac{360^\circ}{365}(316-81)=231.8^\circ
$$

### Step 3: Equation of Time

公式：

$$
EoT=9.87\sin(2B)-7.53\cos(B)-1.5\sin(B)
$$

代入：

$$
EoT\approx15.4 \ \mathrm{min}
$$

### Step 4: Time Correction

公式：

$$
TC=4(\mathrm{Longitude}-LSTM)+EoT
$$

代入：

$$
TC=4(-79.383087-(-75))+15.4
$$

$$
TC\approx-2.1 \ \mathrm{min}
$$

### Step 5: Local Solar Time

$$
LST=LT+\frac{TC}{60}
$$

$$
LST=10+\frac{-2.1}{60}
$$

$$
LST\approx9.965 \ \mathrm{h}
$$

也就是大约 9:57。

### Step 6: Hour Angle

$$
HRA=15^\circ(LST-12)
$$

$$
HRA=15^\circ(9.965-12)
$$

$$
HRA\approx-30.5^\circ
$$

结果：

$$
HRA=-30.5^\circ
$$

负号表示还没到太阳正午。

### Step 7: Declination angle

$$
\delta=23.45^\circ\sin\left(\frac{360^\circ}{365}(d-81)\right)
$$

$$
\delta=23.45^\circ\sin(231.8^\circ)
$$

$$
\delta\approx-18.42^\circ
$$

### Step 8: Elevation angle

公式：

$$
\alpha=\sin^{-1}\left(\sin\delta\sin\varphi+\cos\delta\cos\varphi\cos(HRA)\right)
$$

代入：

$$
\alpha=\sin^{-1}\left(
\sin(-18.42^\circ)\sin(43.66^\circ)
+\cos(-18.42^\circ)\cos(43.66^\circ)\cos(-30.5^\circ)
\right)
$$

结果：

$$
\alpha\approx21.90^\circ
$$

### Step 9: Azimuth

作业使用：

$$
Azimuth=\cos^{-1}
\left(
\frac{
\sin\delta\cos\varphi-\cos\delta\sin\varphi\cos(HRA)
}
{\cos\alpha}
\right)
$$

代入后：

$$
Azimuth\approx153.5^\circ
$$

结果：

- $HRA=-30.5^\circ$
- $\alpha=21.90^\circ$
- $Azimuth=153.5^\circ$

## 本章易错点

- 面积一定要换成平方米：$25 \ \mathrm{cm^2}=2.5\cdot10^{-3} \ \mathrm{m^2}$。
- $V_{OC}I_{SC}$ 不是最大输出功率，还要乘 $FF$。
- lux 不是 $\mathrm{W/m^2}$，室内光题必须使用数据表或题目给的换算。
- 串联电阻主要通过降低 $FF$ 影响功率。
- 阴天/冬天不能只算直射光，扩散光可能占很大比例。
