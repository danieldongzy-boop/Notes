# Chapter 9 - Power Management: 有电不等于能用

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_9_Power Management_SS_2026.pdf`
- 本章没有单独对应的 exercise；相关公式会连接前面太阳、热电、振动和储能章节。

## 这一章在讲什么

能量收集器输出的电通常“不听话”：

- TEG：低电压、低电流、DC
- Solar cell：电压还可以、电流随光照变化、DC
- Piezo：高电压、低电流、AC
- Electromagnetic：低到中等电压、AC

负载却通常想要稳定电压，比如 $1.8 \ \mathrm{V}$、$3.3 \ \mathrm{V}$。所以 power management 的任务是把“不稳定的输入”变成“负载能用的输出”。

## 核心概念

### 效率

$$
\eta=\frac{P_\mathrm{out}}{P_\mathrm{in}}
$$

所以：

$$
P_\mathrm{in}=\frac{P_\mathrm{out}}{\eta}
$$

损耗：

$$
P_\mathrm{loss}=P_\mathrm{in}-P_\mathrm{out}
$$

说人话：如果负载要 $330 \ \mathrm{\mu W}$，转换效率只有 $34\%$，输入端就要接近 $971 \ \mathrm{\mu W}$。微能量系统里这差距很致命。

### 芯片自身功耗

管理芯片自己也耗电：

$$
P_\mathrm{self}=U_\mathrm{in}I_\mathrm{DD}
$$

课件例子里，输入 $0.9 \ \mathrm{V}$，芯片电流 $400 \ \mathrm{\mu A}$：

$$
P_\mathrm{self}=0.9\cdot400 \ \mathrm{\mu A}=360 \ \mathrm{\mu W}
$$

这已经和负载 $330 \ \mathrm{\mu W}$ 同量级。说人话：小功率系统里，电源管理芯片可能比你的传感器还费电。

### 冷启动电压

Cold-start voltage 是芯片从完全没电开始工作所需的最低输入电压。工作起来之后，芯片可能可以在更低电压下继续运行。

设计时要分清：

- start-up voltage：启动需要多少
- operating voltage：启动后最低能维持多少
- input power：输入功率够不够
- quiescent current：芯片自己偷走多少

## 电压转换

### Boost converter

升压转换器把低输入电压升到高输出电压。适合：

- 太阳能电池低光照
- TEG 低电压
- 小电池升压到 3.3 V

但在轻载时效率可能很差，尤其是输入功率只有微瓦到毫瓦时。

### Charge pump

电荷泵用电容和开关搬运电荷。课件给出近似：

$$
U_\mathrm{out}\approx \frac{C_p}{C_p+C_\mathrm{out}}2U_\mathrm{in}
$$

说人话：理想情况下可以倍压，但实际电容、开关和负载会让输出低于 $2U_\mathrm{in}$。

### Resonant ultra-low-voltage converter

谐振式超低压转换器可以从非常低的输入电压启动，适合 TEG 这类几十毫伏输出的源。但它们通常应用更专门，设计也更挑剔。

## 和前面章节的连接

### 太阳能

太阳能电池需要 maximum power point tracking, MPPT。

原因：光照和温度变了，最大功率点也变。如果负载直接接上去，可能把电池拉到不合适的工作点。

相关公式：

$$
P_{MP}=V_{MP}I_{MP}
$$

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}
$$

### 热电

TEG 输出电压低，经常需要超低压升压器。

相关检查：

$$
U_0=mS\Delta T
$$

$$
P_L=\frac{U_0^2R_L}{(R_g+R_L)^2}
$$

如果 $U_0$ 低于 converter start-up voltage，即使理论上有功率，也可能启动不了。

### 振动压电

压电输出是 AC，而且本身像电容。普通桥式整流会有损耗，也会错过最佳取能时刻。

课件提到两种改进：

- SECE: synchronous electric charge extraction
- SSHI: synchronized switch harvesting on inductor

说人话：它们都在“合适的时刻”把压电片上的电荷拿走，让电流和电压更接近有用的相位关系。

### 储能

电源管理通常还要控制储能器：

- 过压保护
- 欠压关断
- hysteresis switch
- 电池充电限制
- 电容缓冲

电容缓冲仍然用：

$$
E_\mathrm{use}=\frac{1}{2}C(U_\mathrm{on}^2-U_\mathrm{off}^2)
$$

## 选 power management 时的检查清单

1. 输入源是 AC 还是 DC？
2. 输入电压范围是多少？
3. 最低启动电压够不够？
4. 输入功率能不能覆盖负载、转换损耗和芯片自耗？
5. 输出电压是否匹配负载？
6. 是否需要 MPPT 或阻抗匹配？
7. 储能器是电容、超级电容还是电池？
8. 过充、过放、欠压、过压怎么处理？

## 易错点

- 不要只看 converter 的最高效率，要看你实际工作点下的效率。
- 数据表里的 start-up voltage 可能是在无负载条件下测的，实际负载下会更难启动。
- 微瓦级系统里，quiescent current 可能决定成败。
- Power management 不是最后随便加的模块，它会反过来影响发电器和储能器的选择。

