# Exercise 3 热电转换器作业逐步解析

> 原文件：`Exercise 3_Thermoelectric converters_SOLVED_SS_2026.pdf`

## Task 1：TEG

### 1(a) 所需热电偶数量

$m$ 个热电偶的电压：

$$
U=m(S_p-S_n)\Delta T
$$

因此：

$$
m=\frac{U}{(S_p-S_n)\Delta T}
$$

已知：

$$
U=2.5\,V,\qquad\Delta T=10\,K
$$

#### Nichrome 与 Constantan

$$
S_{\mathrm{NiCr}}=25\,\mu V/K
$$

$$
S_{\mathrm{Const}}=-35\,\mu V/K
$$

$$
\Delta S=25-(-35)=60\,\mu V/K
$$

单个热电偶电压：

$$
U_{\mathrm{pair}}=60\,\mu V/K\cdot10\,K
=0.6\,mV
$$

$$
m=\frac{2.5}{0.0006}
\approx4166.7
$$

必须向上取整：

$$
\boxed{m=4167}
$$

#### BiTe 材料组合

$$
S_n=-240\,\mu V/K,\qquad S_p=225\,\mu V/K
$$

$$
\Delta S=465\,\mu V/K
$$

$$
U_{\mathrm{pair}}=4.65\,mV
$$

$$
m=\frac{2.5}{0.00465}
\approx537.6
$$

$$
\boxed{m=538}
$$

半导体热电材料的 Seebeck coefficient 更大，因此需要的热电偶数量远少于金属组合。

### 1(b) 257 个热电偶的尺寸

49 个热电偶占用：

$$
A_{49}=25\cdot25=625\,mm^2
$$

每个热电偶平均占用：

$$
A_{\mathrm{pair}}=\frac{625}{49}
=12.755\,mm^2
$$

257 个热电偶需要：

$$
A_{257}=257\cdot12.755
\approx3278\,mm^2
$$

若保持正方形：

$$
L=\sqrt{3278}
\approx57.3\,mm
$$

$$
\boxed{L\approx58\,mm}
$$

### 1(c) 整机 ZT

已知：

$$
R_G=0.57\,\Omega,\quad
\alpha_G=0.016\,V/K
$$

$$
R_{th,G}=5.263\,K/W,\quad T=293\,K
$$

$$
ZT_G=\frac{\alpha_G^2R_{th,G}}{R_G}T
$$

$$
ZT_G=
\frac{0.016^2\cdot5.263}{0.57}\cdot293
\approx\boxed{0.69}
$$

### 1(d) 热电腿几何与有效面积

热电腿长度：

$$
L_{\mathrm{leg}}=3.7-2\cdot1.0
=1.7\,mm
$$

$$
R_{th,G}=
\frac{L_{\mathrm{leg}}}
{\kappa(2mA_{\mathrm{leg}})}
$$

整理得：

$$
A_{\mathrm{leg}}
=
\frac{L_{\mathrm{leg}}}
{R_{th,G}\kappa2m}
$$

代入 $\kappa=2\,W/(mK)$、$m=49$：

$$
\boxed{A_{\mathrm{leg}}\approx1.648\,mm^2}
$$

$$
\frac{L_{\mathrm{leg}}}{A_{\mathrm{leg}}}
\approx\boxed{1.03\,mm^{-1}}
$$

有效面积：

$$
A_{\mathrm{act}}=2\cdot49\cdot1.648
\approx161.5\,mm^2
$$

$$
\frac{A_{\mathrm{act}}}{A_{\mathrm{total}}}
=\frac{161.5}{625}
\approx\boxed{25.8\%}
$$

## Task 2：微型 TEG

### 已知参数

$$
A_G=3.388\cdot3.339
=11.3125\,mm^2
$$

$$
A_{\mathrm{leg}}=(35\,\mu m)^2
=1225\,\mu m^2
$$

$$
R_G=300\,\Omega,\quad
\rho=10^{-5}\,\Omega m
$$

器件有 540 个热电偶，即 1080 条热电腿。

### 热电腿长宽比

$$
R_G=\rho\frac{2mL_{\mathrm{leg}}}{A_{\mathrm{leg}}}
$$

$$
\frac{L_{\mathrm{leg}}}{A_{\mathrm{leg}}}
=\frac{R_G}{2m\rho}
$$

统一单位后：

$$
\boxed{\frac{L}{A}\approx27.78\,mm^{-1}}
$$

$$
L_{\mathrm{leg}}
=27.78\,mm^{-1}\cdot0.001225\,mm^2
\approx0.034\,mm
$$

$$
\boxed{L_{\mathrm{leg}}\approx34\,\mu m}
$$

### 有效面积比例

$$
A_{\mathrm{act}}
=1080\cdot0.001225
=1.323\,mm^2
$$

$$
\frac{A_{\mathrm{act}}}{A_G}
=\frac{1.323}{11.3125}
\approx\boxed{11.7\%}
$$

### 整机 ZT

$$
ZT=
\frac{(0.140)^2\cdot12.5}{300}\cdot293
\approx\boxed{0.239}
$$

相比宏观 TEG，微型器件的热电腿更短、$L/A$ 更大、内阻更高，整机 $ZT$ 也较低。

## Task 3：热电功率输出

已知：

$$
m=144,\quad S=400\,\mu V/K
$$

$$
R_g=10\,\Omega,\quad R_L=3\,\Omega
$$

$$
R_{th,G}=6.1\,K/W,\quad R_{th,HS}=4\,K/W
$$

$$
\Delta T_{\mathrm{external}}=15\,K
$$

### TEG 上的实际温差

$$
\Delta T_G=
\frac{6.1}{6.1+4}\cdot15
$$

$$
\boxed{\Delta T_G\approx9.059\,K}
$$

### 开路电压

$$
U_0=mS\Delta T_G
$$

$$
U_0=144\cdot0.0004\cdot9.059
\approx\boxed{0.522\,V}
$$

### 负载电压

$$
U_L=U_0\frac{R_L}{R_g+R_L}
$$

$$
U_L=0.522\frac{3}{13}
\approx\boxed{0.120\,V}
$$

### 负载功率

$$
P_L=\frac{U_L^2}{R_L}
$$

$$
P_L=\frac{0.120^2}{3}
\approx\boxed{4.8\,mW}
$$

### 变换器启动温差

启动电压为 $27\,mV$，在线性近似下：

$$
\Delta T_{\min}
=15\,K\cdot\frac{27\,mV}{120\,mV}
$$

$$
\boxed{\Delta T_{\min}\approx3.38\,K}
$$

这里默认变换器输入电阻在启动附近仍可近似为 $3\,\Omega$；真实冷启动特性应以数据手册为准。

## Task 4：TEG 优化

### 4(a) 热阻匹配所需热电偶数

单条热电腿热阻：

$$
R_{th,\mathrm{leg}}
=\frac{L}{\kappa A}
$$

$$
R_{th,\mathrm{leg}}
=
\frac{1.7\times10^{-3}}
{2\cdot1.65\times10^{-6}}
\approx515\,K/W
$$

所需并联热电腿数量：

$$
N_{\mathrm{leg}}=\frac{515}{4}
\approx128.75
$$

每个热电偶有两条腿：

$$
m\approx64.4
$$

向上取整：

$$
\boxed{m\approx65\text{ 个热电偶}}
$$

### 4(b) 有效面积比例

$$
A_{\mathrm{act}}=2\cdot65\cdot1.65
=214.5\,mm^2
$$

$$
\boxed{
\frac{A_{\mathrm{act}}}{625}
\approx34.3\%
}
$$

### 4(c) 144 个热电偶、25% 有效面积

$$
A_{\mathrm{act}}=0.25\cdot625
=156.25\,mm^2
$$

$$
A_{\mathrm{leg}}
=\frac{156.25}{2\cdot144}
\approx\boxed{0.54\,mm^2}
$$

正方形热电腿边长：

$$
w=\sqrt{0.54}
\approx\boxed{0.735\,mm}
$$

为满足 $R_{th,G}=4\,K/W$：

$$
L=R_{th,G}\kappa A_{\mathrm{leg}}2m
$$

$$
\boxed{L\approx1.24\,mm}
$$

### 4(d) 内部电阻

$$
R_g=\rho\frac{2mL}{A_{\mathrm{leg}}}
$$

$$
R_g=
10^{-5}
\frac{288\cdot1.24\times10^{-3}}
{0.54\times10^{-6}}
$$

$$
\boxed{R_g\approx6.61\,\Omega}
$$

## Task 5：墙面热电采集系统

外部温差：

$$
\Delta T=35.5-27.5=8\,K
$$

单个 D651：

$$
R_{th}=22\,K/W,\quad
\alpha=75\,mV/K,\quad
R_g=185\,\Omega
$$

### 可安装数量

面积除法给出约 74 个，但按器件边长实际排布：

$$
\left\lfloor\frac{25}{3.375}\right\rfloor
\cdot
\left\lfloor\frac{25}{2.5}\right\rfloor
=7\cdot10
=\boxed{70}
$$

边长排布更符合真实几何条件。下面沿用原题解的 74 个方案，以便与答案数值一致。

### TEG 上的温差

$$
R_{th,\mathrm{TEG,total}}
=\frac{22}{74}
=0.297\,K/W
$$

$$
\Delta T_G=
8
\frac{0.297}{0.297+2(0.05)+2.75}
\approx\boxed{0.755\,K}
$$

### 并联

$$
U_{0,p}=0.075\cdot0.755
\approx\boxed{56.6\,mV}
$$

$$
R_{g,p}=\frac{185}{74}
\approx2.50\,\Omega
$$

当 $R_L=100\,\Omega$：

$$
U_{L,p}=56.6\,mV
\frac{100}{102.5}
\approx55.2\,mV
$$

$$
\boxed{P_p\approx30.5\,\mu W}
$$

### 串联

$$
U_{0,s}=74\cdot56.6\,mV
\approx4.188\,V
$$

$$
R_{g,s}=74\cdot185
=13.69\,k\Omega
$$

$$
U_{L,s}=4.188
\frac{100}{13690+100}
\approx30.4\,mV
$$

$$
\boxed{P_s\approx9.22\,\mu W}
$$

对 $100\,\Omega$ 负载，并联方案更好，因为等效源电阻远低于串联方案。

### 实用性评价

- 70 到 74 个器件的对齐和接线非常困难；
- 很难保证所有器件具有一致、平整的热接触；
- 器件成本极高；
- 大部分外部温差损失在散热器和接触层；
- 最终功率仍只有几十微瓦。

因此该系统在技术上可行，但经济性和装配可行性很差。

