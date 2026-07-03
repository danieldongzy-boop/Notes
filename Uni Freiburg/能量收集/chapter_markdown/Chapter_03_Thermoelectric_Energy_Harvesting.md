# Chapter 3 - Thermoelectric Energy Harvesting: 热电发电就是温差、电阻和热阻

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_3_Thermoelectric Energy Harvesting_SS_2026.pdf`
- Exercise: `Exercise 3_Thermoelectric converters_SOLVED_SS_2026.pdf`

## 这一章在讲什么

热电发电器 TEG 利用 Seebeck effect：两种材料两端有温差，就会产生电压。真正设计时不能只看温差，还要看：

- 材料的 Seebeck 系数够不够大
- 热阻有没有把温差浪费在界面和散热片上
- 负载电阻有没有和 TEG 内阻匹配
- 输出电压够不够启动 DC-DC 转换器

## 作业重点公式

### Seebeck 电压

单个热电偶：

$$
\Delta U = (S_p-S_n)\Delta T
$$

$m$ 个热电偶串联：

$$
U_0=m(S_p-S_n)\Delta T
$$

说人话：热电偶电压很小，通常是几百 $\mathrm{\mu V/K}$，所以要很多对热电腿串起来。

作业第一题求热电偶数量：

$$
m=\frac{U_\mathrm{target}}{(S_p-S_n)\Delta T}
$$

### 热电材料性能 ZT

材料层面的定义：

$$
ZT=\frac{S^2\sigma}{\kappa}T
$$

- $S$ 大：同样温差产生更高电压
- $\sigma$ 大：电阻小，损耗少
- $\kappa$ 小：不容易把温差直接导没

说人话：好的热电材料要“导电好但导热差”，这本身就是矛盾，所以 ZT 很难做高。

### 用数据表估算器件 ZT

作业用的是整个 TEG 的等效参数：

$$
ZT \approx \frac{\alpha_\mathrm{gen}^2 R_{\mathrm{th,gen}}}{R_{\mathrm{el,gen}}}T
$$

- $\alpha_\mathrm{gen}$：整个发电器的 Seebeck 系数，单位 $\mathrm{V/K}$
- $R_{\mathrm{th,gen}}$：热阻，单位 $\mathrm{K/W}$
- $R_{\mathrm{el,gen}}$：电阻，单位 $\Omega$

### 热阻

一维导热：

$$
R_\mathrm{th}=\frac{L}{\kappa A}
$$

对于 TEG，热电腿通常并联导热：

$$
A_\mathrm{act}=2mA_\mathrm{leg}
$$

$$
R_{\mathrm{th,gen}}=\frac{L_\mathrm{leg}}{\kappa A_\mathrm{act}}
$$

### 电阻

热电腿串联导电：

$$
R_{\mathrm{el,gen}}=\rho \frac{2mL_\mathrm{leg}}{A_\mathrm{leg}}
$$

说人话：热路里腿越多越粗，热阻越低；电路里腿越长越细，电阻越高。几何设计会同时影响热和电。

### 热阻分压

外部温差不一定全落在 TEG 上：

$$
d=\frac{R_{\mathrm{th,TEG}}}{R_{\mathrm{th,TEG}}+R_{\mathrm{th,h}}+R_{\mathrm{th,c}}}
$$

$$
\Delta T_\mathrm{TEG}=d\Delta T_\mathrm{system}
$$

说人话：热阻就像电阻分压。界面、导热膏、散热片太差，会把可用温差吃掉。

### 负载功率

TEG 可以看成电压源 $U_0$ 加内阻 $R_g$：

$$
P_L=\frac{U_0^2R_L}{(R_g+R_L)^2}
$$

最大功率出现在：

$$
R_L=R_g
$$

此时：

$$
P_\mathrm{max}=\frac{U_0^2}{4R_g}
$$

如果考虑热阻分压和 DC-DC 效率：

$$
P_\mathrm{el}
=d^2\frac{(mS\Delta T_\mathrm{system})^2R_L}{(R_g+R_L)^2}\eta_\mathrm{DC-DC}
$$

注意是 $d^2$，因为功率和电压平方成正比。

## 作业怎么解

### 需要多少个热电偶

步骤：

1. 查材料组合的 $S_p-S_n$。
2. 算单对热电偶在给定 $\Delta T$ 下的电压。
3. 用目标电压除以单对电压。

作业结果：

- Nichrome-Constantan：约 4167 对
- BiTe/SbBiTe：约 538 对

结论：普通金属热电偶电压太低，半导体热电材料更适合发电。

### 从 49 对热电偶放大到 257 对

如果假设每对热电偶占用面积相同：

$$
A_{257}=A_{49}\frac{257}{49}
$$

边长：

$$
L=\sqrt{A}
$$

作业算出边长约 $58 \ \mathrm{mm}$。

### 微型 TEG 和宏观 TEG

微型 TEG 的腿很短，作业里约 $34 \ \mathrm{\mu m}$。这会带来：

- 电阻可能很高
- 热阻可能和宏观器件差很多
- 工艺上不能随便把腿做长

所以微型化不是简单把宏观 TEG 缩小。

### TEG + 散热片 + 负载

作业 Task 3 的解题顺序：

1. 先用热阻分压算真正落在 TEG 上的温差。
2. 用 Seebeck 公式算开路电压。
3. 用电阻分压算负载电压。
4. 用 $P=U_L^2/R_L$ 算负载功率。
5. 反推 DC-DC 启动所需的最小温差。

## 易错点

- 外部温差不等于 TEG 温差，一定要先看热阻分压。
- 热电发电最大功率不是短路，也不是开路，而是 $R_L=R_g$。
- 多个微型 TEG 并联/串联时，电压和内阻变化不同：串联加电压也加内阻，并联电压不变但内阻变小。
- 输出电压很低时，DC-DC 的启动电压和效率可能决定系统能不能工作。

