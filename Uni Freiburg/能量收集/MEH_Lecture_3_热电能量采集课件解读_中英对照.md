# Lecture 3 热电能量采集课件解读

> 原文件：`MicroEnergyHarvesting_Lecture_3_Thermoelectric Energy Harvesting_SS_2026.pdf`

## 1. 基本概念

热电发电器（thermoelectric generator, TEG）利用 Seebeck effect 将温差转换成直流电压。

```text
热源 → TEG 上的温度梯度 → 直流电压 → 负载或变换器
```

TEG 需要的是持续热流和器件两端的温差，而不仅是较高的绝对温度。

## 2. Seebeck effect

高温端载流子的平均能量更高，会向冷端扩散，形成电荷分离和反向电场。

材料的 Seebeck coefficient：

$$
S=\frac{\Delta U}{\Delta T}
$$

一个 p/n 热电偶：

$$
U_{\mathrm{pair}}=(S_p-S_n)\Delta T
$$

$m$ 个热电偶电气串联：

$$
U_0=m(S_p-S_n)\Delta T
$$

p 型和 n 型热电腿在热学上并联、电学上串联。

## 3. 标准 TEG 结构

宏观 TEG 通常包括：

- p 型和 n 型 BiTe 热电腿；
- 铜互连；
- 陶瓷基板；
- 焊料和接触层。

增加热电偶数量会提高电压，但也会改变内部电阻、热阻和有效面积比例。

## 4. TEG 与 Peltier 冷却

同一类器件可双向工作：

- TEG 模式：温差产生电压；
- TEC/Peltier 模式：输入电流搬运热量。

两种模式基于互易的热电效应，但实际器件可能针对发电或制冷分别优化。

## 5. 微型 TEG

微型 TEG 的热电腿通常只有几十微米长，特点是：

- 热容量小；
- 单位面积热电偶数量多；
- 内部电阻往往较高；
- 输出通常为 $\mu W$ 到 $mW$；
- 易于靠近芯片或微热源集成。

短热电腿可降低电阻，但也降低热阻，使外部温差只有很小一部分落在器件上。

## 6. 热电材料性能

理想热电材料需要：

- 大 Seebeck coefficient $S$；
- 高电导率 $\sigma$；
- 低热导率 $\kappa$。

无量纲优值：

$$
ZT=\frac{S^2\sigma}{\kappa}T
$$

也可写成：

$$
ZT=\frac{PF}{\kappa}T
$$

其中：

$$
PF=S^2\sigma
$$

这些要求彼此冲突。例如提高载流子浓度会提高 $\sigma$，但可能降低 $S$ 并增加电子热导率。

## 7. 整机 ZT

若已知 TEG 的总 Seebeck coefficient $\alpha_G$、内阻 $R_G$ 和热阻 $R_{th,G}$：

$$
ZT_G=\frac{\alpha_G^2R_{th,G}}{R_G}T
$$

这个表达式适合直接使用数据手册中的器件参数。

## 8. 热电转换效率

Carnot 上限：

$$
\eta_C=\frac{T_h-T_c}{T_h}
$$

热电器件效率：

$$
\eta=
\frac{T_h-T_c}{T_h}
\cdot
\frac{\sqrt{1+ZT_m}-1}
{\sqrt{1+ZT_m}+T_c/T_h}
$$

当温差很小时，Carnot 上限本身就很低，因此低品位余热采集通常更关注能否提供可用功率，而不是高转换效率。

## 9. 电气等效电路

TEG 可建模为理想电压源 $U_0$ 串联内部电阻 $R_g$。

$$
U_0=m(S_p-S_n)\Delta T_{\mathrm{TEG}}
$$

负载电流：

$$
I=\frac{U_0}{R_g+R_L}
$$

负载电压：

$$
U_L=U_0\frac{R_L}{R_g+R_L}
$$

负载功率：

$$
P_L=\frac{U_0^2R_L}{(R_g+R_L)^2}
$$

最大功率传输条件：

$$
R_L=R_g
$$

$$
P_{\max}=\frac{U_0^2}{4R_g}
$$

## 10. 温差与功率

由于：

$$
U_0\propto\Delta T
$$

因此理想情况下：

$$
P\propto(\Delta T)^2
$$

有效温差加倍，输出功率约变为四倍。

## 11. 热阻网络

外部温差不会全部落在 TEG 上。热端接触、TEG 和冷端散热器形成串联热阻：

$$
\Delta T_{\mathrm{TEG}}
=
\frac{R_{th,\mathrm{TEG}}}
{R_{th,h}+R_{th,\mathrm{TEG}}+R_{th,c}}
\Delta T_{\mathrm{external}}
$$

它与电阻分压完全类似。

负载功率可写成：

$$
P_L=
\left[
\frac{R_{th,\mathrm{TEG}}}
{R_{th,h}+R_{th,\mathrm{TEG}}+R_{th,c}}
\right]^2
\left[mS\Delta T_{\mathrm{external}}\right]^2
\frac{R_L}{(R_g+R_L)^2}
$$

该式把热学匹配和电学匹配清楚地分开。

## 12. 热阻与热电腿

一维均匀材料：

$$
R_{th}=\frac{L}{\kappa A}
$$

$N$ 条相同热电腿热学并联：

$$
R_{th,\mathrm{array}}
=\frac{R_{th,\mathrm{leg}}}{N}
$$

接触层的面热阻可写为：

$$
R_{\mathrm{contact}}=\frac{\rho_{th}}{A}
$$

热膏、陶瓷、焊料、墙面接触和散热器都应纳入热阻网络。

## 13. 热电腿的电阻

$$
R_g=\rho\frac{L_{\mathrm{total}}}{A_{\mathrm{leg}}}
$$

$m$ 个热电偶共有 $2m$ 条热电腿：

$$
L_{\mathrm{total}}=2mL_{\mathrm{leg}}
$$

所以：

$$
R_g=\rho\frac{2mL_{\mathrm{leg}}}{A_{\mathrm{leg}}}
$$

增加热电腿长度可提高热阻，但也会提高电阻，必须折中。

## 14. 热学匹配

工程上常希望：

$$
R_{th,\mathrm{TEG}}
\sim R_{th,\mathrm{environment}}
$$

- TEG 热阻过小：器件上的温降太小；
- TEG 热阻过大：热流太小；
- 最佳点取决于热源、散热器和目标负载。

## 15. 热电偶数量的设计冲突

增加热电偶数量会：

- 提高开路电压；
- 增加内部电阻；
- 增大有效导热面积；
- 降低器件热阻；
- 可能反而减小 $\Delta T_{\mathrm{TEG}}$。

因此不能只追求更高电压，必须以负载得到的实际功率为目标。

## 16. DC-DC 接口

低温差 TEG 常只能产生数毫伏到数十毫伏。变换器具有：

- 启动电压；
- 输入阻抗；
- 随电压和功率变化的效率；
- 与稳态工作不同的冷启动过程。

$$
P_{\mathrm{usable}}=P_L\eta_{\mathrm{DC-DC}}
$$

理论功率足够并不代表系统一定能启动。

## 17. 多个 TEG 的串并联

对于 $n$ 个相同器件：

### 串联

$$
U_{0,s}=nU_0,\qquad R_{g,s}=nR_g
$$

### 并联

$$
U_{0,p}=U_0,\qquad R_{g,p}=\frac{R_g}{n}
$$

串联适合高输入电阻和高启动电压需求；并联适合较低负载电阻。最终选择由负载和变换器决定。

## 18. 宏观与微型 TEG 对比

| 参数 | 宏观 TEG | 微型 TEG |
|---|---|---|
| 热电腿长度 | mm | 数十 $\mu m$ |
| 内部电阻 | 低到中等 | 通常较高 |
| 热阻 | 较高 | 通常较低 |
| 集成能力 | 较差 | 很好 |
| 常见功率 | $mW$ 到 $W$ | $\mu W$ 到 $mW$ |

## 19. 系统设计步骤

1. 确定热端和冷端；
2. 建立完整热阻网络；
3. 计算 $\Delta T_{\mathrm{TEG}}$；
4. 计算 $U_0$ 与 $R_g$；
5. 匹配负载或变换器输入；
6. 加入 DC-DC 效率和启动条件；
7. 检查机械接触和热膨胀；
8. 评估成本与装配可行性。

## 20. 高频易错点

- 直接把外部温差代入 Seebeck 公式；
- 忽略接触热阻和散热器热阻；
- 只按 $R_L=R_g$ 匹配而忽略实际变换器；
- 增加热电偶后不重新计算 $R_g$ 和 $R_{th}$；
- 混淆热导率与热阻；
- 在 Carnot 和 $ZT$ 公式中使用摄氏温度；
- 从功率求电压时写错，正确关系是 $U=\sqrt{PR}$。

## 21. 公式速记

$$
U_0=m(S_p-S_n)\Delta T_{\mathrm{TEG}}
$$

$$
ZT=\frac{S^2\sigma}{\kappa}T
$$

$$
R_{th}=\frac{L}{\kappa A}
$$

$$
P_L=\frac{U_0^2R_L}{(R_g+R_L)^2}
$$

$$
P_{\max}=\frac{U_0^2}{4R_g}
$$

