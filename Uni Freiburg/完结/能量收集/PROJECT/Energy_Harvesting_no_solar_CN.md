# 无太阳能能量收集方案

## 设计边界

本项目不能使用 solar energy，因此能量收集只能来自动物自身或动物运动。对于 sheep-size animal，最现实的非太阳能来源是：

- 体热温差：thermoelectric generator, TEG
- 运动能量：kinetic electromagnetic generator

其它来源，例如 RF energy harvesting、风能、biofuel、普通 piezo vibration，在本项目里不适合作为主电源。

## 固定功耗约束

本项目已经确定使用 conventional GNSS，不采用 Snapshot GNSS，也不在本节修改 sensor、LoRa 或工作周期。附件中的固定选择为：

```text
Activity sensor: ADXL362
GNSS:            Quectel LC76G, active 15 s every minute
Radio:           Semtech SX1262
```

能量采集部分必须检查全天能量，而不能只检查一次操作是否低于 500 mJ buffer。

### LC76G

```text
LC76G active power = 33 mW
active time        = 15 s per minute
energy per minute  = 33 mW x 15 s = 495 mJ
```

加上每分钟 45 s 的 power-saving mode：

```text
E_GNSS_per_min = 495 mJ + 1.935 mJ = 496.935 mJ/min
E_GNSS_per_day = 496.935 mJ x 1440 = 715.5864 J/day
```

### ADXL362

```text
E_ADXL_per_min = 0.000144 mJ + 0.00118 mJ = 0.001324 mJ/min
E_ADXL_per_day = 0.001324 mJ x 1440 = 0.00191 J/day
```

### SX1262

严格按附件中的 1 ms Tx 和每分钟周期计算：

```text
E_LoRa_per_min = 0.138 mJ + 0.0295 mJ = 0.1675 mJ/min
E_LoRa_per_day = 0.1675 mJ x 1440 = 0.2412 J/day
```

如果实际 LoRa 只每几天发送一次，这一项会更低；但相对于 GNSS 的 715.6 J/day，已经不会改变结论。

### 固定负载总计

```text
E_total = 715.5864 + 0.00191 + 0.2412
        = 715.8295 J/day

P_average = 715.8295 J / 86400 s
          = 8.285 mW
```

这是下限，因为 MCU、flash、power-management quiescent current、电池充放电损耗和温度传感器还没有包含。

附件中的 `495 mJ < 500 mJ` 只证明 buffer 理论上能支撑一次 15 s GNSS 操作，不证明能量采集器能在下一分钟之前把这 495 mJ 补回来。若要每分钟重复一次，采集器必须连续提供至少 8.285 mW，还要另加系统损耗。

## 候选能量收集器

| 选项 | 器件/方案 | 可依据的输出 | 本项目判断 |
|---|---|---:|---|
| A | TECTEG `TEG2-126LDT` | 40 x 40 mm；模块两端 10 K 时匹配负载输出 0.2 V x 45 mA = 9 mW | 最适合理论方案；厂商明确定位 body/sensor low-DeltaT harvesting |
| B | Same Sky `SPG178-56` | 56 x 56 mm；额定 17.8 W at 270 K；低温差外推 5 K 时约 6.10 mW | 2 片、实际模块温差 5 K、70% 转换效率时约 8.55 mW usable |
| C | Same Sky `SPG179-80` | 80 x 80 mm；额定 27.3 W at 270 K；低温差外推 6 K 时约 13.48 mW | 单片在实际模块温差 6 K 时理论可满足负载 |
| D | TEC Microsystems `1MC06-048-15_TEG` | 山羊项圈野外平均 103-136 uW | 动物野外证据最强，但适合做实验基线，不是高功率理论主方案 |
| E | Kinetron `MSG32` 电磁运动发电机 | 0.69-10.04 J/day | 只作辅助，不作主电源 |
| F | TEC Microsystems `DX2625` 一体化采集器 | 0.5-20 mW，但要求热源与环境温差 15-70 K | 最小工作温差偏高，不如 `TEG2-126LDT` 适合本项目 |

## 论文案例：哪些数字能够迁移到项圈

不能把所有 wearable TEG 论文直接按面积搬到羊项圈。下面按证据强度排序。

| 案例 | TEG/材料 | 面积与条件 | 输出 | 对本项目的意义 |
|---|---|---|---:|---|
| Freiburg 2021 wildlife tracker | 商用 `1MC06-048-15_TEG`，2 个并联 | 山羊野外项圈；2 x 20.5 = 41 cm2 采热面积；TEG 实际温差 2.5 +/- 1.0 K | 平均 103/136 uW；夜间 157/217 uW；白天 65/78 uW | 唯一最接近本项目的系统级野外证据，应作为预算基线 |
| Freiburg 2020 thermal interface | Thermalforce `TEG-083-230-07`，主要用于热流/热阻实验 | Merino 羊毛和山羊毛实验台；插入毛层的 4 mm 圆柱热连接件 | 热接口热阻相对平板降低最多 38%，重量也降低 | 说明优化重点首先是毛皮热接口，不是盲目换更大 TEG |
| Yang et al. 2023 bracelet | 定制 287 对 Bi2Te3 柔性 FTEG，无商用型号 | 30 x 80 mm = 24 cm2；弯曲半径 30 mm；受控热源和冷凝管实验台 | 弯曲状态 4 K 时 167 mV、1.9 mA，论文给出的量级约 317 uW | 证明 24 cm2 定制器件在良好冷热端条件下可到数百 uW；不是毛皮上自然散热实测 |
| Miao et al. 2024 wearable TEG | 定制 Mg3Bi2/MgAgSb TEG，无商用型号 | 4.5 x 4.5 = 20.25 cm2；人体手臂 | 静止 126 uW = 6.22 uW/cm2；慢走测试 367 uW = 18.1 uW/cm2，但用 1.5 m/s 风扇模拟气流 | 静止值可作乐观人体参考；风扇值不能当作动物项圈全天平均值 |
| Bao et al. 2022 wearable TEG | 定制 Bi2Te3 冷却增强电极，无商用型号 | 人体志愿者室内坐姿；器件厚 3 mm | 最大 30.25 uW/cm2 | 展示了散热设计的潜力，但仍是裸露人体皮肤，不是羊毛接口 |

由 Freiburg 野外结果换成功率密度：

```text
Goat 1: 103 uW / 41 cm2 = 2.51 uW/cm2
Goat 2: 136 uW / 41 cm2 = 3.32 uW/cm2
Daytime: 65-78 uW / 41 cm2 = 1.59-1.90 uW/cm2
Night: 157-217 uW / 41 cm2 = 3.83-5.29 uW/cm2
```

因此项圈设计应采用：

```text
conservative design density = 2.0 uW/cm2
typical target density       = 2.5-3.3 uW/cm2
human/wind-assisted values   = 只用于说明上限，不用于能量预算
```

## 动物野外基线 TEG：1MC06-048-15_TEG

Freiburg 野外项圈使用的器件是：

```text
Manufacturer: TEC Microsystems
Model:        1MC06-048-15_TEG
Quantity:     2
Connection:   parallel
Package:      10 x 10 x 2.6 mm
```

厂商参数：

| 参数 | `1MC06-048-15_TEG` |
|---|---:|
| 电阻 | 4.1 ohm |
| 热阻 | 29.2 K/W |
| 开路电压系数 | 19.2 mV/K |
| 1 K 时最大功率点电流 | 2.33 mA |
| TEG 两端温差为 1 K 时的最大功率 | 22.37 uW |
| 陶瓷尺寸 | 10 x 10 mm |
| 高度 | 2.6 mm |

这里必须修正一个容易误解的写法：`22.37 uW` 是 **TEG 两端温差为 1 K 时**的最大功率，不是“每增加 1 K 就线性增加 22.37 uW”。在材料参数近似不变时：

```text
Pmax(DeltaT_TEG) = Pmax_at_1K x DeltaT_TEG^2
```

例如论文实测 TEG 平均温差约 2.5 K：

```text
one TEG: 22.37 x 2.5^2 = 139.8 uW raw maximum
two TEGs: 2 x 139.8 = 279.6 uW raw maximum
after converter, mismatch and system losses: field result about 103-136 uW average
```

这也解释了为什么夜间温差稍大，输出功率会明显提高。

注意：41 cm2 是动物侧 thermal heat connector 的总采热面积，不是两个 10 x 10 mm TEG 芯片的面积。重量主要来自热连接件、外侧散热器、外壳、防水和项圈固定结构。2020 论文估计两个热连接件和散热器约 120 g，还不包括电子、电池和项圈；2021 完整系统为 286 g。

## 为什么 Freiburg 野外系统选择小型 TEG

TEG 必须和动物侧、空气侧热阻匹配。论文用下面的简化条件比较器件：

```text
animal skin - ambient total temperature difference = 5 K
hot-side external thermal resistance Kh             = 35 K/W
cold-side external thermal resistance Kc             = 10 K/W
```

TEG 真正得到的温差为：

```text
DeltaT_TEG = 5 K x Rth_TEG / (Rth_TEG + Kh + Kc)
```

对 `1MC06-048-15_TEG`：

```text
DeltaT_TEG = 5 x 29.2 / (29.2 + 35 + 10) = 1.97 K
Voc        = 19.2 mV/K x 1.97 K = 37.8 mV
Vmpp       = Voc / 2 = 18.9 mV
Pmax       = 22.37 uW x 1.97^2 = 86.6 uW per TEG
```

不同 TEC Microsystems 型号在同一简化热环境下的计算：

| 型号 | 尺寸 | TEG 热阻 | 计算得到的 TEG 温差 | Vmpp | 单片 Pmax |
|---|---:|---:|---:|---:|---:|
| `1MC06-048-15_TEG` | 10 x 10 mm | 29.2 K/W | 1.97 K | 18.9 mV | 86.6 uW |
| `1MC06-048-12_TEG` | 10 x 10 mm | 23.4 K/W | 1.71 K | 16.4 mV | 81.8 uW |
| `1MC06-070-15_TEG` | 12 x 12 mm | 20.0 K/W | 1.54 K | 21.5 mV | 77.2 uW |
| `1MC06-096-15_TEG` | 12 x 16 mm | 14.6 K/W | 1.22 K | 23.5 mV | 67.1 uW |
| `1MC06-126-15_TEG` | 16 x 16 mm | 11.1 K/W | 0.99 K | 24.9 mV | 57.5 uW |

结论不是“更大 TEG 更差”，而是：在这组毛皮和自然对流热阻下，更大、更多热电偶的器件会分到更小的实际温差。`1MC06-048-15_TEG` 在功率和约 20 mV 最大功率点电压之间匹配最好，这正是 Freiburg 论文选择它的原因。

可做的 A/B 原型：

- 主样机：`1MC06-048-15_TEG`，直接复现论文基线。
- 对照样机：`1MC06-070-15_TEG`，电压略高，可能更容易配商用升压器，但按论文热模型功率略低。
- 不建议把普通大面积 TEC 制冷片作为首个样机；先测热阻和 1-5 K 下的 I-V 曲线再决定。

## 市售高功率 TEG 重新筛选

前面的 Freiburg 分析回答的是“已经在动物项圈上实测过什么”。如果这是理论报告，可以采用尺寸更大的市售低温差 TEG，并为冷热端建立明确的设计假设。

### TECTEG TEG2-126LDT

这是目前最贴合本项目描述的市售型号：

```text
Model: TEG2-126LDT
Application stated by manufacturer: body and sensor power harvesting
Size: 40 x 40 x 5.45 mm
Matched-load data at Th = 40 C, Tc = 30 C:
Vload = 0.2 V
Iload = 0.045 A
Rload = 4.5 ohm
Pload = 0.2 x 0.045 = 9 mW
```

厂商还给出：

| TEG 两端条件 | Vload | Iload | 计算功率 |
|---|---:|---:|---:|
| 40/30 C, DeltaT = 10 K | 0.2 V | 0.045 A | 9 mW |
| 60/30 C, DeltaT = 30 K | 0.6 V | 0.11 A | 66 mW |
| 80/30 C, DeltaT = 50 K | 1.1 V | 0.18 A | 198 mW |

10 K 数据是直接由厂商给出的低温差工作点，不是从高温额定值外推，因此比普通几瓦 TEG 的宣传数字更适合本报告。

厂商测试使用 40/30 C。理论报告可以假设 35/25 C 等相近平均温度下、同样 10 K 温差时输出近似，但这仍是需要验证的材料参数假设。产品页面没有给出该工作点的 heat flow，因此不能从现有数据证明动物热接口一定能维持这 10 K。

在材料参数近似不变时，用 `P proportional to DeltaT^2` 做 3-10 K 范围估算：

| 实际模块温差 | 单片理论 Pmpp | 70% 转换后 |
|---:|---:|---:|
| 3 K | 0.81 mW | 0.57 mW |
| 5 K | 2.25 mW | 1.58 mW |
| 8 K | 5.76 mW | 4.03 mW |
| 10 K | 9.00 mW | 6.30 mW |

因此：

```text
2 modules at actual DeltaT_TEG = 10 K:
Praw = 2 x 9 = 18 mW
Pusable = 18 x 0.70 = 12.6 mW > 8.285 mW load
```

如果全天温差变化，可以采用 4 片阵列和电池储能。例如理论日循环假设：夜间 12 h 的实际模块温差为 10 K，白天 12 h 为 5 K：

```text
average raw power per module
= 0.5 x 9.00 + 0.5 x 2.25
= 5.625 mW

4-module average raw power    = 22.50 mW
after 70% power conversion    = 15.75 mW
fixed system average demand   = 8.285 mW
theoretical power margin      = 7.465 mW
daily usable harvested energy = 15.75 mW x 86400 s = 1360.8 J/day
```

这个方案在数学上能够闭合，推荐作为理论报告主方案：`4 x TEG2-126LDT + low-voltage converter + rechargeable battery`。

### Same Sky SPG series

Same Sky（原 CUI Devices）提供可直接订购的 TEG。以下额定数据均在 `Th = 300 C, Tc = 30 C, DeltaT = 270 K` 下测得，不能直接当作体热输出。为了理论比较，按以下关系外推：

```text
P(DeltaT) approximately equals Prated x (DeltaT / 270 K)^2
```

| 型号 | 尺寸 | 厂商额定功率 | 3 K 外推 | 5 K 外推 | 6 K 外推 | 10 K 外推 |
|---|---:|---:|---:|---:|---:|---:|
| `SPG078-35` | 35 x 35 mm | 7.8 W | 0.96 mW | 2.67 mW | 3.85 mW | 10.70 mW |
| `SPG178-56` | 56 x 56 mm | 17.8 W | 2.20 mW | 6.10 mW | 8.79 mW | 24.42 mW |
| `SPG179-80` | 80 x 80 mm | 27.3 W | 3.37 mW | 9.36 mW | 13.48 mW | 37.45 mW |

几个可以写进理论报告的配置：

| 配置 | 实际模块温差假设 | Raw power | 70% 转换后 | 能否覆盖 8.285 mW |
|---|---:|---:|---:|---|
| 2 x `SPG178-56` | 5 K | 12.21 mW | 8.55 mW | 刚好覆盖，余量很小 |
| 2 x `SPG178-56` | 6 K | 17.58 mW | 12.31 mW | 可以，约 49% 余量 |
| 1 x `SPG179-80` | 6 K | 13.48 mW | 9.44 mW | 可以，约 14% 余量 |
| 2 x `SPG179-80` | 5 K | 18.72 mW | 13.11 mW | 可以，约 58% 余量 |

这些外推只适合作为 conceptual design。Same Sky 数据手册没有给出 3-10 K 的实测曲线，而且材料参数、接触电阻和负载匹配会随温度变化。

### 热流条件不能省略

大功率 TEG 的代价是需要很大的热流。以 `SPG179-80` 为例，厂商在 270 K 温差下给出 525 W heat flow。若先做线性热导近似：

```text
effective thermal conductance = 525 W / 270 K = 1.944 W/K

at actual DeltaT_TEG = 6 K:
required heat flow approximately 1.944 x 6 = 11.7 W
```

所以单片 `SPG179-80` 的电功率计算虽然闭合，但热机械设计必须从动物侧连续导入约 10 W 量级热流，并通过外侧散热器排出。理论报告应加入以下假设：

- 热端采用穿过毛层、接近皮肤的铝制 thermal connector。
- 冷端采用暴露于空气的低热阻鳍片散热器。
- 项圈或 harness 保持稳定接触压力。
- 可充电电池平衡昼夜和天气导致的温差变化。
- `DeltaT_TEG` 是两个陶瓷面的实测温差，不是 `body temperature - ambient temperature`。

如果不能建立这些热流和温差，大功率型号也只会得到很小的输出。

## Freiburg 小型 TEG 的面积和数量计算

Freiburg 基线是 **2 个 TEG + 2 个约 20.5 cm2 的采热结构**。所以 3 倍面积不是 3 个小芯片，而是约 6 个完整采热单元：

| TEG 数量 | 总采热面积 | 按两只山羊实测线性外推 | 每日能量 | 设计用途 |
|---:|---:|---:|---:|---|
| 2 | 41 cm2 | 103-136 uW | 8.90-11.75 J/day | 论文已验证基线 |
| 4 | 82 cm2 | 206-272 uW | 17.80-23.50 J/day | 中等面积原型 |
| 6 | 123 cm2 | 309-408 uW | 26.70-35.25 J/day | 300 uW 名义目标 |

但是线性外推没有考虑多个散热器互相遮挡、项圈曲率、接触压力、毛长差异和额外重量。因此建议把 6 单元方案写成：

```text
nominal target:      300 uW = 25.92 J/day
engineering budget:  200 uW = 17.28 J/day
stretch/night case:  400 uW = 34.56 J/day
```

也就是说，300 uW 是合理的 **目标值**，但在完成羊毛假体实验和动物原型之前，不应把它当作保证的全天平均值。

机械上优先采用 6 个接近论文尺寸的分布式采热单元，而不是 1 个 120 cm2 的刚性大块。这样更容易贴合项圈曲率，也可分别测量各单元输出。电气上不应在未验证极性和温差一致性时把 6 个单元直接全部并联；建议按 2 个一组做 3 个采集通道，储能侧再合并。

## 辅助采集器：Kinetic Generator

Kinefox 论文使用：

```text
Component: Kinetron MSG32
Type: electromagnetic micro-generator from automatic watch technology
Mass: 18 g
Diameter: 32 mm
Storage: lithium-ion capacitor
```

动物佩戴实验结果：

| Animal / mounting | Energy generated |
|---|---:|
| Exmoor pony | 0.69 J/day |
| Wisent | 2.38 J/day |
| Domestic dog cases | 2.26-10.04 J/day |
| Kinefox V2 dogs | about 1.10-2.25 J/day |

结论：`MSG32` 值得作为辅助源，也能提供活动相关信号，但其输出对动物和安装方向非常敏感，不能用 10.04 J/day 的最好案例做固定预算。建议基础预算只计 1 J/day，实测后再提高。

## 能量闭合检查

固定负载下限为 `715.83 J/day = 8.285 mW average`。首先将 Freiburg 小型 TEG 与它直接比较：

| Harvesting 情况 | 每日收入 | 覆盖固定负载 | 每日缺口 |
|---|---:|---:|---:|
| 2 TEG，Freiburg Goat 1 实测 | 8.90 J/day | 1.24% | 706.93 J/day |
| 2 TEG，Freiburg Goat 2 实测 | 11.75 J/day | 1.64% | 704.08 J/day |
| 6 TEG，工程预算 200 uW | 17.28 J/day | 2.41% | 698.55 J/day |
| 6 TEG，名义目标 300 uW | 25.92 J/day | 3.62% | 689.91 J/day |
| 6 TEG，乐观 400 uW + MSG32 最好案例 | 44.60 J/day | 6.23% | 671.23 J/day |

因此，`1MC06-048-15_TEG` 路线即使叠加 kinetic 仍缺少约 94% 的能量。这个结论只否定 Freiburg 小型模块方案，不再用于否定所有市售大功率 TEG。

### 市售大功率 TEG 的理论闭合

以 70% power-conversion efficiency 计算：

| 理论方案 | Raw average power | Usable power | Usable energy/day | 相对 715.83 J/day |
|---|---:|---:|---:|---:|
| 2 x `TEG2-126LDT`, DeltaT_TEG = 10 K | 18.00 mW | 12.60 mW | 1088.64 J/day | 闭合，52% 功率余量 |
| 4 x `TEG2-126LDT`, 12 h at 10 K + 12 h at 5 K | 22.50 mW average | 15.75 mW | 1360.80 J/day | 闭合，90% 功率余量 |
| 2 x `SPG178-56`, DeltaT_TEG = 6 K | 17.58 mW | 12.31 mW | 1063.25 J/day | 闭合，49% 功率余量 |
| 1 x `SPG179-80`, DeltaT_TEG = 6 K | 13.48 mW | 9.44 mW | 815.36 J/day | 闭合，14% 功率余量 |
| 2 x `SPG179-80`, DeltaT_TEG = 5 K | 18.72 mW | 13.11 mW | 1132.44 J/day | 闭合，58% 功率余量 |

因此市场上确实存在可以在理论计算中满足 8.285 mW 的商用 TEG。最适合报告的选择是 `4 x TEG2-126LDT`，因为它有厂商直接给出的 10 K 低温差数据，而且应用说明明确包括 body harvesting。

### 为什么 Freiburg 功率密度反推会得到巨大面积

按 Freiburg 动物项圈的功率密度反推所需采热面积：

```text
required average power = 8285 uW

at 2.0 uW/cm2 conservative:
A = 8285 / 2.0 = 4143 cm2 = 0.414 m2

at 2.5 uW/cm2 typical:
A = 8285 / 2.5 = 3314 cm2 = 0.331 m2

at 3.3 uW/cm2 optimistic animal average:
A = 8285 / 3.3 = 2511 cm2 = 0.251 m2
```

这相当于约 20-34 组 123 cm2 的六单元 TEG 系统，即约 120-204 个 `1MC06-048-15_TEG`。原因是 Freiburg 系统受毛皮接口、热流和超低压转换限制，不能用它的系统级功率密度代表所有更大 TEG 在理想 thermal boundary conditions 下的理论输出。

即使错误地采用人体慢走加风扇的 `18.1 uW/cm2`，仍需：

```text
8285 / 18.1 = 458 cm2
```

而这个功率密度来自裸露人体皮肤和 1.5 m/s 强制气流，不可能作为羊毛项圈的全天保证值。

## 推荐的理论能量采集架构

```text
Thermal mechanics:
4 distributed 40 x 40 mm thermal modules, total TEG face area 64 cm2
fur-side 4 mm rounded-pin thermal connector, spacing sufficient for wool penetration
external aluminum heatsink exposed to airflow

TEG:
4 x TECTEG TEG2-126LDT
electrical connection: two series modules per string, two strings in parallel (2S2P)
assumed module-surface temperature cycle: 10 K night / 5 K day
calculated average raw power: 22.5 mW

Power conversion:
low-voltage MPPT boost converter
assumed average efficiency: 70%
calculated usable average power: 15.75 mW

Auxiliary:
1 x Kinetron MSG32
not required for nominal energy closure; adds reserve energy

Storage:
rechargeable main battery for multi-day thermal deficits
LIC/supercapacitor for GNSS and LoRa pulse current

Control:
energy-aware scheduling based on storage voltage and recent harvested power
fixed conventional GNSS workload retained
```

在上述温差和 70% 转换效率假设下：

```text
TEG usable average power = 15.75 mW
fixed load lower bound   =  8.285 mW
power margin             =  7.465 mW
```

所以这套理论架构可以称为 energy autonomous。电池不是两年能量的主要来源，而是用来跨越白天、炎热天气、静止和接触变差时的能量缺口。

`TEG2-126LDT` 在 10 K 时的匹配负载电压约 0.2 V。2S2P 连接可将 string 工作电压提高到约 0.4 V，明显高于 Freiburg 小型 TEG 的约 20 mV 工作点，使 commercial MPPT/boost converter 的选择和效率假设更合理。具体 converter 型号仍需按 cold-start voltage、input impedance 和 2S2P I-V curve 选择。

## 理论报告需要声明的验证条件

报告不需要做成品，但应把下列内容列为 future experimental validation：

```text
1. Verify 5-10 K temperature difference directly across each TEG ceramic surface.
2. Verify that the fur-side connector can supply the required heat flow without harming the animal.
3. Measure the low-DeltaT I-V curves of the selected commercial module.
4. Verify at least 70% average converter efficiency with the 2S2P source.
5. Verify usable average harvested power above 10.8 mW,
   which gives about 30% margin over the current 8.285 mW lower-bound load.
```

## 最终判断

市场上存在理论上能够满足固定负载的商用 TEG。推荐主方案是 `4 x TECTEG TEG2-126LDT`：采用厂商 10 K 低温差实测点、白天 5 K/夜间 10 K 的理论循环和 70% 转换效率，可得到约 15.75 mW usable average，高于 8.285 mW 固定负载下限。

Same Sky `SPG178-56` 和 `SPG179-80` 也能形成可闭合的备选方案，但它们的 3-10 K 输出来自 270 K 额定数据的平方外推，证据弱于 `TEG2-126LDT` 的直接低温差数据。

因此报告可以写成 **conditionally feasible**，而不是“不可能”：电功率预算可以闭合，但成立条件是热机械结构确实能在 TEG 陶瓷两面维持 5-10 K 温差并传输数瓦到十瓦量级的热流。这个 thermal assumption 是整个方案最关键的风险。

## Sources and data notes

- Baeumker et al., "A Fully Featured Thermal Energy Harvesting Tracker for Wildlife", Energies 2021, DOI: https://doi.org/10.3390/en14196363. Local file: `energies-14-06363-v2.pdf`
- Baeumker et al., "Thermoelectric Harvesting Using Warm-Blooded Animals in Wildlife Tracking Applications", Energies 2020, DOI: https://doi.org/10.3390/en13112769. Local file: `tmp/pdfs/animal2020.pdf`
- Yang et al., "Flexible thermoelectric generator and energy management electronics powered by body heat", Microsystems & Nanoengineering 2023, DOI: https://doi.org/10.1038/s41378-023-00583-3
- Miao et al., "Comfortable wearable thermoelectric generator with high output power", Nature Communications 2024, DOI: https://doi.org/10.1038/s41467-024-52841-1
- Bao et al., "Wearable Thermoelectric Generator with Cooling-Enhanced Electrode Design for High-Efficient Human Body Heat Harvesting", ACS Applied Engineering Materials 2023, DOI: https://doi.org/10.1021/acsaenm.2c00167
- Gregersen et al., "A novel kinetic energy harvesting system for lifetime deployments of wildlife trackers", PLOS ONE 2023. Local file: `journal.pone.0285930.pdf`
- TEC Microsystems TEG product table: https://www.tec-microsystems.com/products/thermoelectric-generators/index.html
- TEC Microsystems DX2625: https://www.tec-microsystems.com/products/thermoelectric-generators/dx2625-mini-energy-harvester.html
- TECTEG TEG2-126LDT low-DeltaT module and measured output points: https://tecteg.com/low-dt-thermoelectric-harvesting-teg-power-module/
- Same Sky commercial TEG catalog: https://www.sameskydevices.com/catalog/thermal-management/thermoelectric-generators-(tegs)
- Same Sky SPG178-56 datasheet: https://www.sameskydevices.com/product/resource/spg178-56.pdf. Local copy: `tmp/pdfs/SPG178-56.pdf`
- Same Sky SPG179-80 datasheet: https://www.sameskydevices.com/product/resource/spg179-80.pdf. Local copy: `tmp/pdfs/SPG179-80.pdf`
- Kinetron MSG32 / Kinefox reference: https://doi.org/10.1371/journal.pone.0285930
