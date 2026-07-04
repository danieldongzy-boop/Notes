# Chapter 3 - Thermoelectric Energy Harvesting: 热电发电就是温差、电压、热阻和负载匹配

来源：
- Lecture: `MicroEnergyHarvesting_Lecture_3_Thermoelectric Energy Harvesting_SS_2026.pdf`
- Exercise: `Exercise 3_Thermoelectric converters_SOLVED_SS_2026.pdf`

## 这一章在讲什么？

热电发电器 TEG 利用的是 Seebeck effect：只要热电材料两端有温差，就会产生电压。

但是实际设计时不能只看“温差有多大”。真正决定输出功率的是：

1. 这个温差有多少真的落在 TEG 上。
2. TEG 的 Seebeck 系数够不够大。
3. TEG 的内阻和外部负载是否匹配。
4. 热端、冷端、导热膏、散热片的热阻有没有吃掉温差。
5. 输出电压能不能启动后面的 DC-DC 转换器。

一句话：热电发电不是“有热就有电”，而是要同时把热路和电路都匹配好。

## 公式速查

### Seebeck 电压

单个热电偶的电压：

$$
\Delta U=(S_p-S_n)\Delta T
$$

其中：
- $S_p$：p 型材料 Seebeck 系数
- $S_n$：n 型材料 Seebeck 系数
- $\Delta T$：热端和冷端温差

如果有 $m$ 对热电偶串联：

$$
U_0=m(S_p-S_n)\Delta T
$$

这里的 $U_0$ 是开路电压，也就是不接负载时的电压。

说人话：单对热电偶电压很小，通常是几百 $\mathrm{\mu V/K}$。所以要很多对热电偶串联，才能得到几十毫伏甚至几伏。

### 材料性能指标 ZT

材料层面的 figure of merit：

$$
ZT=\frac{S^2\sigma}{\kappa}T
$$

其中：
- $S$ 大：同样温差产生更高电压
- $\sigma$ 大：导电好，内阻小
- $\kappa$ 小：导热差，不容易把温差直接短路掉

所以好的热电材料最好是：

$$
\text{导电好，但是导热差}
$$

这本身很矛盾，所以高 $ZT$ 材料很难做。

### 用器件参数估算 ZT

作业里不是从材料微观参数算，而是用整个 generator 的参数估算：

$$
ZT_\mathrm{gen}
\approx
\frac{\alpha_\mathrm{gen}^2 R_{\mathrm{th,gen}}}{R_{\mathrm{el,gen}}}T
$$

其中：
- $\alpha_\mathrm{gen}$：整个 TEG 的 Seebeck 系数，单位 $\mathrm{V/K}$
- $R_{\mathrm{th,gen}}$：TEG 热阻，单位 $\mathrm{K/W}$
- $R_{\mathrm{el,gen}}$：TEG 电阻，单位 $\Omega$
- $T$：绝对温度，单位 $\mathrm{K}$

注意：这个公式里的 $\alpha_\mathrm{gen}$ 已经是整个器件的，不是单对热电偶的。

### 热阻

一维导热热阻：

$$
R_\mathrm{th}=\frac{L}{\kappa A}
$$

其中：
- $L$：热流方向长度
- $\kappa$：热导率
- $A$：导热截面积

对于 TEG，热流通过所有 p/n 热电腿并联传热。

如果有 $m$ 对热电偶，则总共有 $2m$ 条热电腿：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

所以：

$$
R_{\mathrm{th,gen}}
=
\frac{L_\mathrm{leg}}{\kappa A_\mathrm{act}}
=
\frac{L_\mathrm{leg}}{\kappa \cdot 2mA_\mathrm{leg}}
$$

### 电阻

电流路径里，热电腿大致是串联的，所以：

$$
R_{\mathrm{el,gen}}
=
\rho\frac{2mL_\mathrm{leg}}{A_\mathrm{leg}}
$$

理解：
- 腿越长，电阻越大，热阻也越大。
- 腿越粗，电阻越小，热阻也越小。
- 热路想要大热阻来保留温差，电路想要小电阻来减少损耗，这也是设计矛盾。

### 热阻分压

外部给出的温差不一定全部落在 TEG 上。

如果 TEG 和散热片、接触层串在同一条热路中：

$$
d=
\frac{R_{\mathrm{th,TEG}}}
{R_{\mathrm{th,TEG}}+R_{\mathrm{th,h}}+R_{\mathrm{th,c}}}
$$

$$
\Delta T_\mathrm{TEG}=d\Delta T_\mathrm{system}
$$

这个 $d$ 叫 thermal feed factor，可以理解成“温差分到 TEG 上的比例”。

说人话：热阻像电阻一样会分压。散热片、导热膏、接触面太差，就会把本来能用的温差分走。

### 负载功率

TEG 可以看成一个电压源 $U_0$ 加一个内阻 $R_g$。

接负载 $R_L$ 后：

$$
U_L=U_0\frac{R_L}{R_g+R_L}
$$

$$
P_L=\frac{U_L^2}{R_L}
$$

也可以合并写成：

$$
P_L=
\frac{U_0^2R_L}{(R_g+R_L)^2}
$$

最大功率出现在：

$$
R_L=R_g
$$

此时：

$$
P_\mathrm{max}=\frac{U_0^2}{4R_g}
$$

如果还要考虑热阻分压：

$$
P_\mathrm{el}
=
d^2
\frac{(mS\Delta T_\mathrm{system})^2R_L}{(R_g+R_L)^2}
$$

注意是 $d^2$，因为电压和 $d$ 成正比，而功率和电压平方成正比。

## Exercise 3 逐题详解

## Task 1: TEGs - Thermoelectric Generators

### Task 1a: 需要多少对热电偶才能得到 2.5 V？

题目给：

$$
U_\mathrm{target}=2.5\ \mathrm{V}
$$

$$
\Delta T=10\ \mathrm{K}
$$

总电压公式：

$$
U=m(S_p-S_n)\Delta T
$$

所以热电偶对数：

$$
m=\frac{U_\mathrm{target}}{(S_p-S_n)\Delta T}
$$

#### 情况 1：Nichrome + Constantan

给定：

$$
S_\mathrm{Nichrome}=25\ \mathrm{\mu V/K}
$$

$$
S_\mathrm{Constantan}=-35\ \mathrm{\mu V/K}
$$

所以单对热电偶的有效 Seebeck 系数：

$$
S_p-S_n=25-(-35)=60\ \mathrm{\mu V/K}
$$

单对热电偶在 $10\ \mathrm{K}$ 下产生：

$$
U_\mathrm{pair}
=60\ \mathrm{\mu V/K}\cdot10\ \mathrm{K}
$$

$$
U_\mathrm{pair}=600\ \mathrm{\mu V}=0.6\ \mathrm{mV}
$$

需要的对数：

$$
m=\frac{2.5\ \mathrm{V}}{0.0006\ \mathrm{V}}
$$

$$
m\approx4167
$$

结果：

$$
m_\mathrm{Nichrome-Constantan}\approx4167
$$

理解：金属热电偶的 Seebeck 系数太小，要做到 2.5 V 需要几千对，实际很不方便。

#### 情况 2：BiTe + SbBiTe

给定：

$$
S_\mathrm{BiTe}=-240\ \mathrm{\mu V/K}
$$

$$
S_\mathrm{SbBiTe}=225\ \mathrm{\mu V/K}
$$

有效 Seebeck 系数：

$$
S_p-S_n=225-(-240)=465\ \mathrm{\mu V/K}
$$

单对热电偶在 $10\ \mathrm{K}$ 下产生：

$$
U_\mathrm{pair}
=465\ \mathrm{\mu V/K}\cdot10\ \mathrm{K}
$$

$$
U_\mathrm{pair}=4650\ \mathrm{\mu V}=4.65\ \mathrm{mV}
$$

需要的对数：

$$
m=\frac{2.5\ \mathrm{V}}{0.00465\ \mathrm{V}}
$$

$$
m\approx538
$$

结果：

$$
m_\mathrm{BiTe/SbBiTe}\approx538
$$

结论：半导体热电材料比普通金属适合发电，因为同样温差下电压高得多。

### Task 1b: 从 49 对热电偶放大到 257 对，面积多大？

已知 Thermalforce TEG 049-150-30：

$$
A_{49}=25\ \mathrm{mm}\times25\ \mathrm{mm}=625\ \mathrm{mm^2}
$$

它有 49 对热电偶。

假设每对热电偶占用面积差不多一样：

$$
A_\mathrm{per\ pair}=\frac{625}{49}
$$

$$
A_\mathrm{per\ pair}\approx12.755\ \mathrm{mm^2}
$$

如果换成 257 对：

$$
A_{257}=257\cdot12.755
$$

$$
A_{257}\approx3278\ \mathrm{mm^2}
$$

如果仍然做成正方形，边长：

$$
L_{257}=\sqrt{3278}
$$

$$
L_{257}\approx57.3\ \mathrm{mm}
$$

约等于：

$$
L_{257}\approx58\ \mathrm{mm}
$$

结果：
- 面积约 $3278\ \mathrm{mm^2}$
- 边长约 $58\ \mathrm{mm}$

### Task 1c: 用 datasheet 参数估算宏观 TEG 的 ZT

题目给/从 datasheet 读到：

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

使用：

$$
ZT_\mathrm{gen}
=
\frac{\alpha_\mathrm{gen}^2R_{\mathrm{th,gen}}}{R_{\mathrm{el,gen}}}T
$$

先算前面的系数：

$$
\alpha_\mathrm{gen}^2
=(0.016)^2=0.000256
$$

$$
\frac{0.000256\cdot5.263}{0.57}
\approx0.002364\ \mathrm{K^{-1}}
$$

再乘温度：

$$
ZT=0.002364\cdot293
$$

$$
ZT\approx0.69
$$

结果：

$$
ZT_\mathrm{gen}\approx0.69
$$

理解：这个数小于 1，属于常见商业 BiTe 热电器件的量级。

### Task 1d: 计算热电腿的 $L_\mathrm{leg}/A_\mathrm{leg}$ 和 active area 比例

已知：

$$
\kappa_\mathrm{BiTe}=2\ \mathrm{W/(K\,m)}
$$

$$
R_{\mathrm{th,gen}}=5.263\ \mathrm{K/W}
$$

$$
m=49
$$

热电腿长度由 datasheet 得到：

$$
L_\mathrm{leg}=3.7\ \mathrm{mm}-2\cdot1\ \mathrm{mm}=1.7\ \mathrm{mm}
$$

热阻公式：

$$
R_{\mathrm{th,gen}}
=
\frac{L_\mathrm{leg}}{\kappa\cdot2mA_\mathrm{leg}}
$$

解出单条腿面积：

$$
A_\mathrm{leg}
=
\frac{L_\mathrm{leg}}{R_{\mathrm{th,gen}}\cdot2m\cdot\kappa}
$$

代入时注意单位统一。用 mm 写结果：

$$
A_\mathrm{leg}
=
\frac{1.7\ \mathrm{mm}}
{5.263\cdot2\cdot49\cdot2}
$$

$$
A_\mathrm{leg}\approx1.648\ \mathrm{mm^2}
$$

所以：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
=
\frac{1.7}{1.648}
$$

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
\approx1.03\ \mathrm{mm^{-1}}
$$

active area：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

$$
A_\mathrm{act}=2\cdot49\cdot1.648
$$

$$
A_\mathrm{act}\approx161.5\ \mathrm{mm^2}
$$

总面积：

$$
A_\mathrm{total}=625\ \mathrm{mm^2}
$$

比例：

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
=
\frac{161.5}{625}
$$

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
\approx0.258
$$

结果：
- $A_\mathrm{leg}\approx1.65\ \mathrm{mm^2}$
- $L_\mathrm{leg}/A_\mathrm{leg}\approx1.03\ \mathrm{mm^{-1}}$
- $A_\mathrm{act}/A_\mathrm{total}\approx25.8\%$

## Task 2: 微型 TEG

题目使用 Micropelt `MPG-D751` 微型热电发电器。

已知/从 datasheet 提取：

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
m=540
$$

$$
\rho=10^{-5}\ \Omega\mathrm{m}
$$

单条热电腿面积：

$$
A_\mathrm{leg}=(35\ \mathrm{\mu m})^2
$$

$$
A_\mathrm{leg}=1225\ \mathrm{\mu m^2}
=0.001225\ \mathrm{mm^2}
$$

器件有效面积：

$$
A_\mathrm{total}=3.388\ \mathrm{mm}\cdot3.339\ \mathrm{mm}
$$

$$
A_\mathrm{total}=11.3125\ \mathrm{mm^2}
$$

### Task 2a: 计算热电腿的 $L/A$ 和长度

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

用作业里的单位换算后：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
=
\frac{300\ \Omega}{2\cdot540\cdot10^{-5}\ \Omega\mathrm{m}}
$$

作业写成：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
=27.7778\ \mathrm{mm^{-1}}
$$

也就是：

$$
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}
=0.027778\ \mathrm{\mu m^{-1}}
$$

由此得到热电腿长度：

$$
L_\mathrm{leg}
=
\frac{L_\mathrm{leg}}{A_\mathrm{leg}}\cdot A_\mathrm{leg}
$$

$$
L_\mathrm{leg}
=0.027778\ \mathrm{\mu m^{-1}}\cdot1225\ \mathrm{\mu m^2}
$$

$$
L_\mathrm{leg}\approx34\ \mathrm{\mu m}
$$

结果：

$$
L_\mathrm{leg}\approx34\ \mathrm{\mu m}
$$

理解：宏观 TEG 的腿长通常是 $1$ 到 $2\ \mathrm{mm}$，这里只有几十微米，差了几十倍。

### Task 2b: active area 比例

总 active area：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

$$
A_\mathrm{act}=2\cdot540\cdot0.001225
$$

$$
A_\mathrm{act}=1.323\ \mathrm{mm^2}
$$

比例：

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
=
\frac{1.323}{11.3125}
$$

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
\approx0.117
$$

结果：

$$
A_\mathrm{act}/A_\mathrm{total}\approx11.7\%
$$

如果把接触区域也算进总面积，比例大约是 $9.4\%$。

### Task 2c: 计算微型 TEG 的 ZT

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
\frac{(0.140)^2\cdot12.5}{300}\cdot293
$$

先算：

$$
(0.140)^2=0.0196
$$

$$
0.0196\cdot12.5=0.245
$$

$$
\frac{0.245}{300}=0.0008167
$$

$$
ZT=0.0008167\cdot293
$$

$$
ZT\approx0.239
$$

结果：

$$
ZT\approx0.24
$$

对比宏观 TEG：

$$
ZT_\mathrm{macro}\approx0.69
$$

所以这个微型 TEG 的 $ZT$ 明显更小。

### Task 2d: 为什么微型 TEG 的腿不做长？

作业结论：

$$
L_\mathrm{leg}\approx34\ \mathrm{\mu m}
$$

或根据 datasheet 高度估计约：

$$
40\ \mathrm{\mu m}
$$

为什么不做长？

主要是工艺限制。Micropelt 这种微型器件的热电腿由薄膜沉积、刻蚀、键合等微加工步骤形成，结构还会受到类似 pyramid shape 的几何限制。不是想把腿做长就能简单拉长。

理解：
- 宏观 TEG 可以用毫米级块状材料。
- 微型 TEG 用微加工工艺，腿短、面积小、数量多。
- 微型化不是把宏观 TEG 等比例缩小，电阻、热阻、工艺限制都会变。

## Task 3: Thermoelectric Power Generation

这题是本章最典型的系统级计算：TEG + 散热片 + DC-DC 输入负载。

已知：

$$
m=144
$$

$$
S=400\ \mathrm{\mu V/K}=0.0004\ \mathrm{V/K}
$$

$$
R_g=10\ \Omega
$$

$$
R_L=3\ \Omega
$$

$$
R_{\mathrm{th,TEG}}=6.1\ \mathrm{K/W}
$$

$$
R_{\mathrm{th,HS}}=4\ \mathrm{K/W}
$$

$$
\Delta T_\mathrm{system}=15\ \mathrm{K}
$$

DC-DC 启动电压：

$$
U_\mathrm{start}=27\ \mathrm{mV}
$$

### Step 1: 先算温差有多少落在 TEG 上

热阻分压：

$$
d=
\frac{R_{\mathrm{th,TEG}}}
{R_{\mathrm{th,TEG}}+R_{\mathrm{th,HS}}}
$$

代入：

$$
d=\frac{6.1}{6.1+4}
$$

$$
d=0.60396
$$

所以 TEG 上的真实温差：

$$
\Delta T_\mathrm{TEG}
=d\Delta T_\mathrm{system}
$$

$$
\Delta T_\mathrm{TEG}
=0.60396\cdot15
$$

$$
\Delta T_\mathrm{TEG}=9.0594\ \mathrm{K}
$$

理解：外面看起来有 $15\ \mathrm{K}$，但只有约 $9.06\ \mathrm{K}$ 真正落在 TEG 上，剩下的温差掉在散热片热阻上。

### Step 2: 算 TEG 开路电压

$$
U_0=mS\Delta T_\mathrm{TEG}
$$

代入：

$$
U_0=144\cdot0.0004\cdot9.0594
$$

$$
U_0\approx0.522\ \mathrm{V}
$$

结果：

$$
U_0\approx0.52\ \mathrm{V}
$$

这是没有接负载时的 generator 输出电压。

### Step 3: 接上 $3\ \Omega$ 负载后的负载电压

电压分压：

$$
U_L=U_0\frac{R_L}{R_g+R_L}
$$

代入：

$$
U_L=0.522\cdot\frac{3}{10+3}
$$

$$
U_L\approx0.120\ \mathrm{V}
$$

结果：

$$
U_L\approx0.12\ \mathrm{V}
$$

这个是负载上真正拿到的电压。

### Step 4: 算负载功率

$$
P_L=\frac{U_L^2}{R_L}
$$

代入：

$$
P_L=\frac{(0.12)^2}{3}
$$

$$
P_L=0.0048\ \mathrm{W}
$$

$$
P_L=4.8\ \mathrm{mW}
$$

结果：

$$
P_L=4.8\ \mathrm{mW}
$$

也可以用完整公式直接算：

$$
P_L
=
\left(\frac{6.1}{6.1+4}\right)^2
\frac{(144\cdot0.0004\cdot15)^2}{3}
\left(\frac{3}{10+3}\right)^2
$$

$$
P_L\approx4.8\ \mathrm{mW}
$$

### Step 5: DC-DC 什么时候能启动？

已知当系统温差是 $15\ \mathrm{K}$ 时，负载电压：

$$
U_L=0.12\ \mathrm{V}
$$

DC-DC 需要：

$$
U_\mathrm{start}=0.027\ \mathrm{V}
$$

在其他参数不变时，电压和温差成正比：

$$
U_L\propto\Delta T
$$

所以最小温差：

$$
\Delta T_\mathrm{min}
=
15\ \mathrm{K}\cdot\frac{0.027}{0.12}
$$

$$
\Delta T_\mathrm{min}=3.375\ \mathrm{K}
$$

结果：

$$
\Delta T_\mathrm{min}\approx3.38\ \mathrm{K}
$$

理解：只要 heat sink 和 cold side 之间有大约 $3.38\ \mathrm{K}$ 的温差，这个 DC-DC 输入端就能达到启动电压。

## Task 4: TEG Optimization

这题的目标是：让 TEG 的热阻和散热片热阻匹配。

已知散热片热阻：

$$
R_{\mathrm{th,HS}}=4\ \mathrm{K/W}
$$

希望 TEG 也有：

$$
R_{\mathrm{th,Gen}}=4\ \mathrm{K/W}
$$

材料：

$$
\kappa_\mathrm{BiTe}=2\ \mathrm{W/(K\,m)}
$$

宏观热电腿参数：

$$
L_\mathrm{leg}=1.7\ \mathrm{mm}
$$

$$
A_\mathrm{leg}=1.65\ \mathrm{mm^2}
$$

### Task 4a: 需要多少对热电偶？

先算单条热电腿的热阻：

$$
R_{\mathrm{th,leg}}
=
\frac{L_\mathrm{leg}}{\kappa A_\mathrm{leg}}
$$

代入：

$$
R_{\mathrm{th,leg}}
=
\frac{1.7\ \mathrm{mm}}
{2\ \mathrm{W/(K\,m)}\cdot1.65\ \mathrm{mm^2}}
$$

换算后：

$$
R_{\mathrm{th,leg}}\approx515\ \mathrm{K/W}
$$

如果很多条腿并联导热，总热阻会降低：

$$
n_\mathrm{leg}
=
\frac{R_{\mathrm{th,leg}}}{R_{\mathrm{th,Gen}}}
$$

$$
n_\mathrm{leg}
=
\frac{515}{4}
$$

$$
n_\mathrm{leg}=128.75
$$

每对热电偶有两条腿，所以热电偶对数：

$$
m=\frac{128.75}{2}
$$

$$
m\approx64.4
$$

取整：

$$
m\approx65
$$

结果：

$$
\text{需要约 }65\text{ 对热电偶}
$$

### Task 4b: active area 占总面积多少？

散热片尺寸：

$$
A_\mathrm{total}=25\ \mathrm{mm}\times25\ \mathrm{mm}
$$

$$
A_\mathrm{total}=625\ \mathrm{mm^2}
$$

active area：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

$$
A_\mathrm{act}=2\cdot65\cdot1.65
$$

$$
A_\mathrm{act}=214.5\ \mathrm{mm^2}
$$

比例：

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
=
\frac{214.5}{625}
$$

$$
\frac{A_\mathrm{act}}{A_\mathrm{total}}
=0.343
$$

结果：

$$
A_\mathrm{act}/A_\mathrm{total}=34.3\%
$$

### Task 4c: 如果要放 144 对热电偶，且 active area 为 25%，腿面积和腿长是多少？

要求：

$$
m=144
$$

$$
A_\mathrm{act}=0.25A_\mathrm{total}
$$

总面积：

$$
A_\mathrm{total}=625\ \mathrm{mm^2}
$$

所以：

$$
A_\mathrm{act}=0.25\cdot625=156.25\ \mathrm{mm^2}
$$

又因为：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

所以：

$$
A_\mathrm{leg}
=
\frac{156.25}{2\cdot144}
$$

$$
A_\mathrm{leg}
=0.5425\ \mathrm{mm^2}
$$

约为：

$$
A_\mathrm{leg}\approx0.54\ \mathrm{mm^2}
$$

如果腿截面近似正方形，边长：

$$
a=\sqrt{A_\mathrm{leg}}
$$

$$
a=\sqrt{0.54}
$$

$$
a\approx0.735\ \mathrm{mm}
$$

接着用热阻目标：

$$
R_{\mathrm{th,Gen}}
=
\frac{L_\mathrm{leg}}{\kappa\cdot2mA_\mathrm{leg}}
$$

解出腿长：

$$
L_\mathrm{leg}
=
R_{\mathrm{th,Gen}}\cdot\kappa\cdot2mA_\mathrm{leg}
$$

代入：

$$
L_\mathrm{leg}
=
4\cdot2\cdot2\cdot144\cdot0.54\ \mathrm{mm^2}
$$

注意单位换算后，作业结果为：

$$
L_\mathrm{leg}\approx1.24\ \mathrm{mm}
$$

结果：
- 单条腿面积：$A_\mathrm{leg}\approx0.54\ \mathrm{mm^2}$
- 正方形边长：$a\approx0.735\ \mathrm{mm}$
- 腿长：$L_\mathrm{leg}\approx1.24\ \mathrm{mm}$

理解：热电偶数量变多后，如果总 active area 限定为 25%，每条腿要变细。为了仍然让总热阻等于 $4\ \mathrm{K/W}$，腿长也要配合调整。

### Task 4d: 这个 144 对热电偶 generator 的内阻是多少？

已知：

$$
\rho=10^{-5}\ \Omega\mathrm{m}
$$

$$
m=144
$$

$$
L_\mathrm{leg}=1.24\ \mathrm{mm}
$$

$$
A_\mathrm{leg}=0.54\ \mathrm{mm^2}
$$

电阻公式：

$$
R_{\mathrm{el,Gen}}
=
\rho\frac{2mL_\mathrm{leg}}{A_\mathrm{leg}}
$$

代入：

$$
R_{\mathrm{el,Gen}}
=
10^{-5}\ \Omega\mathrm{m}
\cdot
\frac{2\cdot144\cdot1.24\ \mathrm{mm}}
{0.54\ \mathrm{mm^2}}
$$

换算单位后：

$$
R_{\mathrm{el,Gen}}\approx6.61\ \Omega
$$

结果：

$$
R_{\mathrm{el,Gen}}\approx6.61\ \Omega
$$

对比：
- 65 对热电偶：约 $1.34\ \Omega$
- 49 对 Thermalforce：约 $0.54\ \Omega$
- 144 对优化版：约 $6.61\ \Omega$

理解：热电偶数量变多会提高开路电压，但也会增加串联电阻。电压变高不等于功率一定变好，还要看负载匹配。

## Task 5: Thermoelectric Harvesting System

这题是多个 Micropelt D651 微型 TEG 装在一个散热片上的系统计算。

已知环境：

$$
T_\mathrm{hot}=35.5^\circ\mathrm{C}
$$

$$
T_\mathrm{cold}=27.5^\circ\mathrm{C}
$$

所以外部温差：

$$
\Delta T_\mathrm{system}=8\ \mathrm{K}
$$

散热片在风速 $9\ \mathrm{km/h}=2.5\ \mathrm{m/s}$ 时：

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

导热膏接触热阻：

$$
R_\mathrm{TCP}=0.05\ \mathrm{K/W}
$$

负载：

$$
R_L=100\ \Omega
$$

### Step 1: 最多能放多少个 D651？

单个 D651 面积：

$$
A_\mathrm{D651}=3.375\ \mathrm{mm}\cdot2.5\ \mathrm{mm}
$$

$$
A_\mathrm{D651}=8.44\ \mathrm{mm^2}
$$

散热片面积：

$$
A_\mathrm{HS}=25\ \mathrm{mm}\cdot25\ \mathrm{mm}=625\ \mathrm{mm^2}
$$

用面积粗算：

$$
n_\mathrm{max}=\frac{625}{8.44}
$$

$$
n_\mathrm{max}\approx74
$$

如果按边长排布，更实际一点：

$$
\frac{25}{3.375}\approx7.4\Rightarrow7
$$

$$
\frac{25}{2.5}=10
$$

所以：

$$
n=7\cdot10=70
$$

作业主答案用 $74$，括号里给了 $70$ 的替代结果。下面按 $74$ 讲。

### Step 2: 多个 TEG 并排导热时，总热阻

热路上这些 TEG 是并联导热，所以：

$$
R_{\mathrm{th,total}}
=
\frac{R_{\mathrm{th,D651}}}{n}
$$

$$
R_{\mathrm{th,total}}
=
\frac{22}{74}
$$

$$
R_{\mathrm{th,total}}=0.297\ \mathrm{K/W}
$$

如果用 $70$ 个：

$$
R_{\mathrm{th,total}}=\frac{22}{70}=0.314\ \mathrm{K/W}
$$

### Step 3: 算真正落在 TEG 上的温差

热路总热阻包括：
- TEG 总热阻
- 两层导热膏
- 散热片热阻

所以：

$$
\Delta T_\mathrm{Gen}
=
\Delta T_\mathrm{system}
\frac{R_{\mathrm{th,total}}}
{R_{\mathrm{th,total}}+2R_\mathrm{TCP}+R_{\mathrm{th,HS}}}
$$

代入：

$$
\Delta T_\mathrm{Gen}
=
8
\frac{0.297}{0.297+2\cdot0.05+2.75}
$$

$$
\Delta T_\mathrm{Gen}
=8\cdot0.094
$$

$$
\Delta T_\mathrm{Gen}=0.755\ \mathrm{K}
$$

如果用 $70$ 个：

$$
\Delta T_\mathrm{Gen}\approx0.794\ \mathrm{K}
$$

理解：外部空气和墙之间虽然有 $8\ \mathrm{K}$，但真正落在每个微型 TEG 上不到 $1\ \mathrm{K}$。热路分压损失非常大。

### Step 4: 并联时的开路电压

并联时，每个 generator 两端电压相同，不会相加。

单个 D651 在这个温差下：

$$
U_{0,\mathrm{single}}
=
\alpha_\mathrm{D651}\Delta T_\mathrm{Gen}
$$

$$
U_{0,\mathrm{single}}
=75\ \mathrm{mV/K}\cdot0.755\ \mathrm{K}
$$

$$
U_{0,\mathrm{single}}=56.6\ \mathrm{mV}
$$

并联开路电压：

$$
U_{0,\mathrm{par}}=56.6\ \mathrm{mV}
$$

如果用 $70$ 个：

$$
U_{0,\mathrm{par}}\approx59.5\ \mathrm{mV}
$$

### Step 5: 串联时的开路电压

串联时电压相加：

$$
U_{0,\mathrm{ser}}=nU_{0,\mathrm{single}}
$$

$$
U_{0,\mathrm{ser}}=74\cdot56.6\ \mathrm{mV}
$$

$$
U_{0,\mathrm{ser}}\approx4.188\ \mathrm{V}
$$

如果用 $70$ 个：

$$
U_{0,\mathrm{ser}}\approx4.165\ \mathrm{V}
$$

### Step 6: 并联接 $100\ \Omega$ 负载时的功率

并联时，等效内阻变小：

$$
R_{\mathrm{par}}=\frac{R_\mathrm{D651}}{n}
$$

$$
R_{\mathrm{par}}=\frac{185}{74}
$$

$$
R_{\mathrm{par}}=2.5\ \Omega
$$

负载电压：

$$
U_{L,\mathrm{par}}
=
U_{0,\mathrm{par}}
\cdot
\frac{R_L}{R_{\mathrm{par}}+R_L}
$$

$$
U_{L,\mathrm{par}}
=
56.6\ \mathrm{mV}
\cdot
\frac{100}{2.5+100}
$$

$$
U_{L,\mathrm{par}}\approx55.22\ \mathrm{mV}
$$

功率：

$$
P_\mathrm{par}
=
\frac{U_{L,\mathrm{par}}^2}{R_L}
$$

$$
P_\mathrm{par}
=
\frac{(0.05522)^2}{100}
$$

$$
P_\mathrm{par}\approx30.5\ \mathrm{\mu W}
$$

结果：

$$
P_\mathrm{par}\approx30.5\ \mathrm{\mu W}
$$

### Step 7: 串联接 $100\ \Omega$ 负载时的功率

串联时，电压相加，但内阻也相加：

$$
R_{\mathrm{ser}}=nR_\mathrm{D651}
$$

$$
R_{\mathrm{ser}}=74\cdot185
$$

$$
R_{\mathrm{ser}}=13690\ \Omega
$$

负载电压：

$$
U_{L,\mathrm{ser}}
=
U_{0,\mathrm{ser}}
\cdot
\frac{R_L}{R_{\mathrm{ser}}+R_L}
$$

$$
U_{L,\mathrm{ser}}
=
4.188
\cdot
\frac{100}{13690+100}
$$

$$
U_{L,\mathrm{ser}}\approx0.03036\ \mathrm{V}
$$

也就是：

$$
U_{L,\mathrm{ser}}\approx30.36\ \mathrm{mV}
$$

功率：

$$
P_\mathrm{ser}
=
\frac{U_{L,\mathrm{ser}}^2}{R_L}
$$

$$
P_\mathrm{ser}
=
\frac{(0.03036)^2}{100}
$$

$$
P_\mathrm{ser}\approx9.22\ \mathrm{\mu W}
$$

结果：

$$
P_\mathrm{ser}\approx9.22\ \mathrm{\mu W}
$$

### Task 5 总结：并联和串联怎么理解？

最终表：

| 连接方式 | 开路电压 | 等效内阻 | $100\ \Omega$ 负载功率 | 理解 |
|---|---:|---:|---:|---|
| 并联 | $56.6\ \mathrm{mV}$ | $2.5\ \Omega$ | $30.5\ \mathrm{\mu W}$ | 电压低，但内阻很小，适合低阻负载 |
| 串联 | $4.188\ \mathrm{V}$ | $13.69\ \mathrm{k\Omega}$ | $9.22\ \mathrm{\mu W}$ | 电压高，但内阻巨大，接 $100\ \Omega$ 时大部分电压掉在内阻上 |

这里最容易误解的是：串联开路电压很高，看起来更好，但一接 $100\ \Omega$ 负载，电压几乎全掉在内部电阻上，所以负载功率反而更低。

### Practicality

这个系统实际意义不太好：

- 要把几十个微型 TEG 精确贴在散热片和墙之间，机械装配很麻烦。
- 每个 TEG 都要良好热接触，平整度和导热膏都会影响结果。
- 单个 µTEG 价格约 $100$ 到 $200$ 欧，70 多个就是几千到一万多欧。
- 最后输出只有几十微瓦，性价比很差。

所以这个例子的主要价值是理解热阻分压和串并联负载匹配，而不是说这是一个现实中划算的方案。

## 本章易错点

- 外部温差不等于 TEG 温差。一定要先用热阻分压算 $\Delta T_\mathrm{TEG}$。
- 热电发电的最大功率不是开路，也不是短路，而是负载电阻和内阻匹配。
- 串联会增加电压，但也会增加内阻。
- 并联不会增加电压，但会降低内阻。
- 输出功率和温差平方成正比：$P\propto(\Delta T)^2$。
- $ZT$ 是材料/器件性能指标，不是效率本身。
- 微型 TEG 的热电腿很短，不是因为理论上更好，而是受到微加工工艺限制。
- DC-DC 的启动电压很重要。温差太小时，即使理论上有一点功率，也可能根本启动不了。
