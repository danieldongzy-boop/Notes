# Chapter 3 - Thermoelectric Energy Harvesting: 热电发电就是温差、电压、热阻和负载匹配

来源：
- Lecture: `MicroEnergyHarvesting_Lecture_3_Thermoelectric Energy Harvesting_SS_2026.pdf`
- Exercise: `Exercise 3_Thermoelectric converters_SOLVED_SS_2026.pdf`

## 这一章在讲什么？

热电发电器 TEG 利用 Seebeck effect：材料两端有温差，就会产生电压。

但实际输出功率不只由外部温差决定，还取决于：

- 温差有多少真的落在 TEG 上。
- TEG 的 Seebeck 系数和热电偶对数。
- TEG 内阻和负载是否匹配。
- 散热片、导热膏、接触层是否吃掉温差。
- 输出电压能不能启动后面的 DC-DC。

一句话：热电发电要同时看热路和电路。

## 公式速查

### Seebeck 电压

单对热电偶：

$$
\Delta U=(S_p-S_n)\Delta T
$$

有 $m$ 对热电偶串联：

$$
U_0=m(S_p-S_n)\Delta T
$$

这里 $U_0$ 是开路电压。

注意：热电偶对数 $m$ 增加时，电压增加，但内阻通常也增加。

### 材料性能指标 ZT

材料层面的 figure of merit：

$$
ZT=\frac{S^2\sigma}{\kappa}T
$$

好的热电材料希望：

- $S$ 大：同样温差下电压高。
- $\sigma$ 大：导电好，内阻低。
- $\kappa$ 小：导热差，不容易把温差短路掉。

也就是：

$$
\text{导电好，但是导热差}
$$

这两个要求天然矛盾，所以高 $ZT$ 材料难做。

### 用器件参数估算 ZT

作业里常用整个 generator 的参数估算：

$$
ZT_\mathrm{gen}
\approx
\frac{\alpha_\mathrm{gen}^2 R_{\mathrm{th,gen}}}{R_{\mathrm{el,gen}}}T
$$

其中：

- $\alpha_\mathrm{gen}$：整个 TEG 的 Seebeck 系数，单位 $\mathrm{V/K}$。
- $R_{\mathrm{th,gen}}$：TEG 热阻，单位 $\mathrm{K/W}$。
- $R_{\mathrm{el,gen}}$：TEG 电阻，单位 $\Omega$。
- $T$：绝对温度，单位 $\mathrm{K}$。

这里的 $\alpha_\mathrm{gen}$ 已经是整个器件的，不是单对热电偶的。

### 热阻和电阻

一维导热热阻：

$$
R_\mathrm{th}=\frac{L}{\kappa A}
$$

TEG 中 $2m$ 条热电腿并联导热：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

所以：

$$
R_{\mathrm{th,gen}}
=
\frac{L_\mathrm{leg}}{\kappa\cdot2mA_\mathrm{leg}}
$$

电流路径中热电腿近似串联：

$$
R_{\mathrm{el,gen}}
=
\rho\frac{2mL_\mathrm{leg}}{A_\mathrm{leg}}
$$

理解：

- 腿越长，热阻大，但电阻也大。
- 腿越粗，电阻小，但热阻也小。
- 热路想保留温差，电路想降低损耗，这就是 TEG 设计矛盾。

### 热阻分压

外部温差不一定全部落在 TEG 上。

如果 TEG 和散热片串在同一条热路中：

$$
d=
\frac{R_{\mathrm{th,TEG}}}
{R_{\mathrm{th,TEG}}+R_{\mathrm{th,ext}}}
$$

$$
\Delta T_\mathrm{TEG}=d\Delta T_\mathrm{system}
$$

说人话：热阻像电阻一样分压。TEG 热阻越小，它分到的温差不一定越大。

### 负载功率

TEG 可以看成电压源 $U_0$ 加内阻 $R_g$。

接负载 $R_L$ 后：

$$
U_L=U_0\frac{R_L}{R_g+R_L}
$$

$$
P_L=\frac{U_L^2}{R_L}
$$

合并：

$$
P_L=
\frac{U_0^2R_L}{(R_g+R_L)^2}
$$

最大功率条件：

$$
R_L=R_g
$$

如果还要考虑热阻分压：

$$
P_\mathrm{el}
=
d^2
\frac{(mS\Delta T_\mathrm{system})^2R_L}{(R_g+R_L)^2}
$$

注意是 $d^2$，因为电压和 $d$ 成正比，而功率和电压平方成正比。

## Exercise 3 精简版

这份 Exercise 的核心不是把每个数都展开十几行，而是会用三类关系：

- Seebeck 电压：$U_0=mS\Delta T$。
- 热阻分压：先算真正落在 TEG 上的 $\Delta T$。
- 电负载分压：再算负载电压和功率。

## Task 1: 宏观 TEG

### Task 1a: 需要多少对热电偶得到 2.5 V？

已知：

$$
U_\mathrm{target}=2.5\ \mathrm{V},\quad \Delta T=10\ \mathrm{K}
$$

公式：

$$
m=\frac{U_\mathrm{target}}{(S_p-S_n)\Delta T}
$$

| 材料组合 | 有效 Seebeck 系数 | 单对电压 @ 10 K | 需要对数 |
|---|---:|---:|---:|
| Nichrome + Constantan | $60\ \mathrm{\mu V/K}$ | $0.6\ \mathrm{mV}$ | $4167$ |
| BiTe + SbBiTe | $465\ \mathrm{\mu V/K}$ | $4.65\ \mathrm{mV}$ | $538$ |

结论：金属热电偶电压太小，半导体热电材料更适合发电。

### Task 1b: 49 对放大到 257 对，面积多大？

Thermalforce TEG 049-150-30：

$$
A_{49}=25\ \mathrm{mm}\times25\ \mathrm{mm}=625\ \mathrm{mm^2}
$$

假设每对热电偶占用面积相同：

$$
A_\mathrm{per\ pair}=\frac{625}{49}=12.755\ \mathrm{mm^2}
$$

所以：

$$
A_{257}=257\cdot12.755\approx3278\ \mathrm{mm^2}
$$

正方形边长：

$$
L_{257}=\sqrt{3278}\approx57.3\ \mathrm{mm}
$$

结果：

$$
\boxed{A\approx3278\ \mathrm{mm^2},\quad L\approx58\ \mathrm{mm}}
$$

### Task 1c: 用 datasheet 估算 ZT

已知：

$$
R_{\mathrm{el,gen}}=0.57\ \Omega
$$

$$
\alpha_\mathrm{gen}=0.016\ \mathrm{V/K}
$$

$$
R_{\mathrm{th,gen}}=5.263\ \mathrm{K/W}
$$

$$
T=293\ \mathrm{K}
$$

公式：

$$
ZT_\mathrm{gen}
=
\frac{\alpha_\mathrm{gen}^2R_{\mathrm{th,gen}}}{R_{\mathrm{el,gen}}}T
$$

代入：

$$
ZT
=
\frac{(0.016)^2\cdot5.263}{0.57}\cdot293
\approx0.69
$$

结果：

$$
\boxed{ZT_\mathrm{gen}\approx0.69}
$$

### Task 1d: 热电腿几何和 active area

已知：

$$
\kappa=2\ \mathrm{W/(K\,m)},\quad R_{\mathrm{th,gen}}=5.263\ \mathrm{K/W}
$$

$$
m=49,\quad L_\mathrm{leg}=1.7\ \mathrm{mm}
$$

热阻：

$$
R_{\mathrm{th,gen}}
=
\frac{L_\mathrm{leg}}{\kappa\cdot2mA_\mathrm{leg}}
$$

解出：

$$
A_\mathrm{leg}\approx1.65\ \mathrm{mm^2}
$$

所以：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
\approx
\frac{1.7}{1.65}
\approx1.03\ \mathrm{mm^{-1}}
$$

active area：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
\approx2\cdot49\cdot1.65
=161.5\ \mathrm{mm^2}
$$

比例：

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
=
\frac{161.5}{625}
\approx25.8\%
$$

结果：

$$
\boxed{A_\mathrm{leg}\approx1.65\ \mathrm{mm^2}}
$$

$$
\boxed{L_\mathrm{leg}/A_\mathrm{leg}\approx1.03\ \mathrm{mm^{-1}}}
$$

$$
\boxed{A_\mathrm{act}/A_\mathrm{total}\approx25.8\%}
$$

## Task 2: 微型 TEG

对象：Micropelt `MPG-D751`。

已知：

$$
R_{\mathrm{el,gen}}=300\ \Omega
$$

$$
\alpha_\mathrm{gen}=0.140\ \mathrm{V/K}
$$

$$
R_{\mathrm{th,gen}}=12.5\ \mathrm{K/W}
$$

$$
m=540,\quad \rho=10^{-5}\ \Omega\mathrm{m}
$$

单条腿面积：

$$
A_\mathrm{leg}=(35\ \mathrm{\mu m})^2=1225\ \mathrm{\mu m^2}
$$

### Task 2a/b: 腿长和 active area

电阻公式：

$$
R_{\mathrm{el,gen}}
=
\rho\frac{2mL_\mathrm{leg}}{A_\mathrm{leg}}
$$

整理：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
=
\frac{R_{\mathrm{el,gen}}}{2m\rho}
$$

结果：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
\approx27.78\ \mathrm{mm^{-1}}
$$

由 $A_\mathrm{leg}=1225\ \mathrm{\mu m^2}$ 得：

$$
L_\mathrm{leg}\approx34\ \mathrm{\mu m}
$$

active area：

$$
A_\mathrm{act}=2\cdot540\cdot0.001225
=1.323\ \mathrm{mm^2}
$$

如果只算 thermoelectrically active part：

$$
A_\mathrm{total}=3.388\cdot3.339=11.3125\ \mathrm{mm^2}
$$

所以：

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
\approx11.7\%
$$

### Task 2c: 微型 TEG 的 ZT

$$
ZT
=
\frac{(0.140)^2\cdot12.5}{300}\cdot293
\approx0.239
$$

结果：

$$
\boxed{ZT\approx0.24}
$$

对比宏观 TEG 的 $ZT\approx0.69$，微型器件明显更差。

### Task 2d: 为什么腿不做长？

答案：主要是工艺限制。

微型 TEG 的腿来自薄膜沉积、刻蚀、键合等微加工步骤，几何还受 pyramid shape 等结构限制。它不是把宏观 TEG 等比例缩小。

总结：

- 宏观 TEG：腿长通常 $1$ 到 $2\ \mathrm{mm}$。
- 微型 TEG：这里约 $34$ 到 $40\ \mathrm{\mu m}$。
- 微型化会带来更高电阻、更强工艺限制和更复杂的热接触问题。

## Task 3: TEG + 散热片 + DC-DC

已知：

$$
m=144,\quad S=400\ \mathrm{\mu V/K}=0.0004\ \mathrm{V/K}
$$

$$
R_g=10\ \Omega,\quad R_L=3\ \Omega
$$

$$
R_{\mathrm{th,TEG}}=6.1\ \mathrm{K/W},\quad R_{\mathrm{th,HS}}=4\ \mathrm{K/W}
$$

$$
\Delta T_\mathrm{system}=15\ \mathrm{K}
$$

DC-DC 启动电压：

$$
U_\mathrm{start}=27\ \mathrm{mV}
$$

### Step 1: 热阻分压

$$
d=\frac{6.1}{6.1+4}=0.604
$$

所以：

$$
\Delta T_\mathrm{TEG}=0.604\cdot15=9.06\ \mathrm{K}
$$

### Step 2: 开路电压

$$
U_0=mS\Delta T_\mathrm{TEG}
$$

$$
U_0=144\cdot0.0004\cdot9.06
\approx0.52\ \mathrm{V}
$$

### Step 3: 负载电压和功率

$$
U_L=U_0\frac{R_L}{R_g+R_L}
$$

$$
U_L=0.52\cdot\frac{3}{10+3}
\approx0.12\ \mathrm{V}
$$

$$
P_L=\frac{U_L^2}{R_L}
=
\frac{0.12^2}{3}
\approx4.8\ \mathrm{mW}
$$

### Step 4: DC-DC 什么时候启动？

电压和系统温差成正比：

$$
\Delta T_\mathrm{min}
=
15\ \mathrm{K}\cdot\frac{0.027}{0.12}
\approx3.38\ \mathrm{K}
$$

结果：

$$
\boxed{U_0\approx0.52\ \mathrm{V}}
$$

$$
\boxed{U_L\approx0.12\ \mathrm{V},\quad P_L\approx4.8\ \mathrm{mW}}
$$

$$
\boxed{\Delta T_\mathrm{min}\approx3.38\ \mathrm{K}}
$$

## Task 4: TEG Optimization

目标：让 TEG 热阻匹配散热片热阻。

已知：

$$
R_{\mathrm{th,HS}}=4\ \mathrm{K/W}
$$

目标：

$$
R_{\mathrm{th,Gen}}=4\ \mathrm{K/W}
$$

材料和原始腿参数：

$$
\kappa=2\ \mathrm{W/(K\,m)}
$$

$$
L_\mathrm{leg}=1.7\ \mathrm{mm},\quad A_\mathrm{leg}=1.65\ \mathrm{mm^2}
$$

### Task 4a/b: 需要多少对热电偶？

单条腿热阻：

$$
R_{\mathrm{th,leg}}
=
\frac{L_\mathrm{leg}}{\kappa A_\mathrm{leg}}
\approx515\ \mathrm{K/W}
$$

需要的腿数：

$$
n_\mathrm{leg}
=
\frac{515}{4}
\approx128.75
$$

每对热电偶有两条腿，所以：

$$
m\approx64.4\approx65
$$

active area：

$$
A_\mathrm{act}=2\cdot65\cdot1.65=214.5\ \mathrm{mm^2}
$$

总面积：

$$
A_\mathrm{total}=25\cdot25=625\ \mathrm{mm^2}
$$

比例：

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
=
\frac{214.5}{625}
\approx34.3\%
$$

结果：

$$
\boxed{m\approx65,\quad A_\mathrm{act}/A_\mathrm{total}\approx34.3\%}
$$

### Task 4c/d: 改成 144 对，active area 25%

给定：

$$
m=144,\quad A_\mathrm{act}=0.25\cdot625=156.25\ \mathrm{mm^2}
$$

单条腿面积：

$$
A_\mathrm{leg}
=
\frac{156.25}{2\cdot144}
\approx0.54\ \mathrm{mm^2}
$$

如果截面近似正方形：

$$
a=\sqrt{0.54}\approx0.735\ \mathrm{mm}
$$

为了让总热阻仍为 $4\ \mathrm{K/W}$：

$$
L_\mathrm{leg}
=
R_{\mathrm{th,Gen}}\kappa(2mA_\mathrm{leg})
\approx1.24\ \mathrm{mm}
$$

内阻：

$$
R_{\mathrm{el,Gen}}
=
\rho\frac{2mL_\mathrm{leg}}{A_\mathrm{leg}}
$$

$$
R_{\mathrm{el,Gen}}
\approx6.61\ \Omega
$$

结果：

$$
\boxed{A_\mathrm{leg}\approx0.54\ \mathrm{mm^2}}
$$

$$
\boxed{L_\mathrm{leg}\approx1.24\ \mathrm{mm}}
$$

$$
\boxed{R_{\mathrm{el,Gen}}\approx6.61\ \Omega}
$$

理解：增加热电偶对数会提高开路电压，但也会提高串联内阻。

## Task 5: 多个 Micropelt D651 的系统

环境：

$$
T_\mathrm{hot}=35.5^\circ\mathrm{C},\quad T_\mathrm{cold}=27.5^\circ\mathrm{C}
$$

$$
\Delta T_\mathrm{system}=8\ \mathrm{K}
$$

散热片：

$$
R_{\mathrm{th,HS}}=2.75\ \mathrm{K/W}
$$

每个 D651：

$$
R_{\mathrm{th,D651}}=22\ \mathrm{K/W}
$$

$$
\alpha_\mathrm{D651}=75\ \mathrm{mV/K}
$$

$$
R_\mathrm{D651}=185\ \Omega
$$

导热膏：

$$
R_\mathrm{TCP}=0.05\ \mathrm{K/W}
$$

负载：

$$
R_L=100\ \Omega
$$

### Step 1: 能放多少个？

单个面积：

$$
A_\mathrm{D651}=3.375\cdot2.5=8.44\ \mathrm{mm^2}
$$

散热片面积：

$$
A_\mathrm{HS}=625\ \mathrm{mm^2}
$$

面积粗算：

$$
n\approx\frac{625}{8.44}\approx74
$$

按边长排布更实际是 $7\cdot10=70$。作业主结果用 $74$，下面也用 $74$。

### Step 2: 热阻分压

多个 D651 并排导热，热阻并联：

$$
R_{\mathrm{th,total}}
=
\frac{22}{74}
=0.297\ \mathrm{K/W}
$$

真正落在 TEG 上的温差：

$$
\Delta T_\mathrm{Gen}
=
8
\frac{0.297}{0.297+2\cdot0.05+2.75}
$$

$$
\Delta T_\mathrm{Gen}\approx0.755\ \mathrm{K}
$$

注意：外部有 $8\ \mathrm{K}$，TEG 上不到 $1\ \mathrm{K}$。

### Step 3: 开路电压

单个 D651：

$$
U_{0,\mathrm{single}}
=
75\ \mathrm{mV/K}\cdot0.755\ \mathrm{K}
\approx56.6\ \mathrm{mV}
$$

并联：

$$
U_{0,\mathrm{par}}=56.6\ \mathrm{mV}
$$

串联：

$$
U_{0,\mathrm{ser}}
=
74\cdot56.6\ \mathrm{mV}
\approx4.188\ \mathrm{V}
$$

### Step 4: 接 $100\ \Omega$ 负载

并联内阻：

$$
R_{\mathrm{par}}
=
\frac{185}{74}
\approx2.5\ \Omega
$$

并联负载电压：

$$
U_{L,\mathrm{par}}
=
56.6\ \mathrm{mV}
\frac{100}{100+2.5}
\approx55.2\ \mathrm{mV}
$$

并联功率：

$$
P_\mathrm{par}
=
\frac{(0.0552)^2}{100}
\approx30.5\ \mathrm{\mu W}
$$

串联内阻：

$$
R_{\mathrm{ser}}
=
74\cdot185
=13.69\ \mathrm{k\Omega}
$$

串联负载电压：

$$
U_{L,\mathrm{ser}}
=
4.188
\frac{100}{13690+100}
\approx30.4\ \mathrm{mV}
$$

串联功率：

$$
P_\mathrm{ser}
=
\frac{(0.0304)^2}{100}
\approx9.22\ \mathrm{\mu W}
$$

最终表：

| 连接方式 | 开路电压 | 等效内阻 | $100\ \Omega$ 负载功率 | 理解 |
|---|---:|---:|---:|---|
| 并联 | $56.6\ \mathrm{mV}$ | $2.5\ \Omega$ | $30.5\ \mathrm{\mu W}$ | 电压低，内阻小 |
| 串联 | $4.188\ \mathrm{V}$ | $13.69\ \mathrm{k\Omega}$ | $9.22\ \mathrm{\mu W}$ | 电压高，内阻巨大 |

实践评价：装配几十个微型 TEG 很麻烦，热接触难保证，价格很高，最后只有几十微瓦。这个例子主要用来理解热阻分压和串并联负载匹配。

## 本章易错点

- 外部温差不等于 TEG 温差，要先算热阻分压。
- 开路电压高不代表负载功率高。
- 最大功率通常需要 $R_L=R_g$。
- 串联提高电压，但也提高内阻。
- 并联不提高电压，但降低内阻。
- 输出功率和温差平方相关：$P\propto(\Delta T)^2$。
- $ZT$ 是材料/器件性能指标，不是效率。
- 微型 TEG 的腿短主要是工艺限制，不是因为理论上一定更优。
- DC-DC 启动电压很重要，温差太小时可能根本启动不了。
