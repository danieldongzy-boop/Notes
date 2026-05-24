# Chapter 3: Thermoelectric Energy Harvesting

> **Lecture**: Micro Energy Harvesting, SoSe 2026  
> **Institution**: IMTEK – Lehrstuhl für Konstruktion von Mikrosystemen, Universität Freiburg  
> **Instructors**: Prof. Dr. Peter Woias, Dr. Suman Kundu, Dr. Frank Goldschmidtböing

---

## 目录

1. [热电发电机 (TEG) 基本原理](#1-热电发电机-teg-基本原理)
2. [塞贝克效应 (Seebeck Effect)](#2-塞贝克效应-seebeck-effect)
3. [热电偶对 (Thermoelectric Unicouple)](#3-热电偶对-thermoelectric-unicouple)
4. [宏观 TEG 设计](#4-宏观-teg-设计)
5. [TEG 数据手册参数](#5-teg-数据手册参数)
6. [TEG 与 Peltier 元件的区别](#6-teg-与-peltier-元件的区别)
7. [微型热电发电机 (µTEG)](#7-微型热电发电机-µteg)
8. [µTEG 制造工艺](#8-µteg-制造工艺)
9. [热电材料](#9-热电材料)
10. [热电优值 (Figure of Merit, ZT)](#10-热电优值-figure-of-merit-zt)
11. [热电效率](#11-热电效率)
12. [功率生成——等效电路模型](#12-功率生成等效电路模型)
13. [TEG 建模——热界面](#13-teg-建模热界面)
14. [TEG 功率输出计算](#14-teg-功率输出计算)
15. [升压变换器与功率损耗](#15-升压变换器与功率损耗)
16. [应用领域](#16-应用领域)
17. [总结](#17-总结)

---

## 1. 热电发电机 (TEG) 基本原理

### 1.1 工作原理

- TEG 连接在**热源 (heat source)** 和**冷源 (heat sink)** 之间
- TEG 将**热能转换为电能**
- 转化的前提是：必须在器件两端建立温度差 $\Delta T$，从而驱动热流穿过器件

> 核心逻辑：**温度差 $\Delta T \rightarrow$ 热流 $\rightarrow$ 直流电压 $\Delta U$**

### 1.2 标准 TEG 组件

| 组件 | 功能 |
|------|------|
| **n 型和 p 型热电材料**（热腿, thermo-legs） | 热-电活性组件 |
| **互连层 (interconnects)** | thermo-legs 之间的电气连接 |
| **接触焊盘 (contact pads)** | 与用户应用的电气连接 |
| **陶瓷绝缘层 (ceramics insulation)** | 电气绝缘 + 机械稳定性 |

---

## 2. 塞贝克效应 (Seebeck Effect)

### 2.1 热扩散机制

- 在高温侧（热源），电子的平均速度更高
- 电子向低温侧（冷源）**扩散**
- 通过建立**反向电场**达到平衡态

$$v_{\text{热端}} > v_{\text{冷端}} \quad \Rightarrow \quad \text{电子扩散} \quad \Rightarrow \quad \text{反向电场建立} \quad \Rightarrow \quad \text{平衡}$$

### 2.2 塞贝克系数 / 塞贝克电压

- **典型值**：几十微伏每开尔文（µV/K）
- 金属的塞贝克系数较小，**半导体**的塞贝克系数较大
- 两种标度并存：
  - **旧标度**：以铂 (Pt) 为参考材料，定义其塞贝克系数为 $0\ \mu\text{V/K}$
  - **新标度**：使用塞贝克系数的绝对值（铂约为 $-5\ \mu\text{V/K}$）

### 2.3 热电功率 (Thermopower)

- p 型和 n 型材料中电场方向**相反**
  - p 型：$+S$（正塞贝克系数）
  - n 型：$-S$（负塞贝克系数）
- 大小取决于温度差和材料参数

**定义**：$S$（或 $\alpha$）为材料的**塞贝克系数**（或热电功率, thermopower），单位：$\text{V/K}$

$$\Delta U = \Delta U_p + \Delta U_n = (S_p - S_n) \cdot \Delta T = S \cdot \Delta T$$

其中：
- $S_p$：p 型材料的塞贝克系数
- $S_n$：n 型材料的塞贝克系数（负值）
- $S = S_p - S_n$：有效塞贝克系数

---

## 3. 热电偶对 (Thermoelectric Unicouple)

### 3.1 定义

- 每个 TEG 的**基本单元 (unit cell)**
- n 型和 p 型材料**并联排列**，实现简单的单向热流
- 通过将 thermo-legs **串联连接**来累加热电电压

### 3.2 典型参数

- 典型热电电压：$\Delta U = 200 - 500\ \mu\text{V/K}$
- 为获得可用输出电压，需要**大量 thermo-legs 串联**

$$\Delta U = S \cdot \Delta T \quad \text{（单个 unicouple）}$$

---

## 4. 宏观 TEG 设计

### 4.1 典型参数

| 参数 | 典型值 |
|------|--------|
| 热电偶对数量 | 20 – 150 对 |
| 尺寸 | $1 \times 1\ \text{cm}^2$ … $6 \times 6\ \text{cm}^2$ |
| 高度 | 0.3 … 1.5 cm |
| 电压 | 10 … 100 mV/K |

### 4.2 结构

- 上下为刚玉载体 (Korundträger)
- 中间为铜片连接的 p/n 热电偶阵列

---

## 5. TEG 数据手册参数

### 5.1 典型宏观 TEG 示例：Thermalforce TEG 049-150-30

**命名规则**：TEG XXX-XXX-XX（热电偶对数-热端温度-冷端温度）

**关键参数**（$\Delta T = 120\ \text{K}$，$T_{\text{hot}} = 150°\text{C}$，$T_{\text{cold}} = 30°\text{C}$）：

| 参数 | 符号 | 数值 |
|------|------|------|
| 开路电压 | $U_{\text{open}}$ | 2.054 V |
| 负载电压 | $U_{\text{load}}$ | 1.027 V |
| 内阻 @300K | $R_i$ | 0.570 $\Omega$ |
| 短路电流 | $I_{\text{short}}$ | 2.551 A |
| 负载电流 | $I_{\text{load}}$ | 1.275 A |
| 负载功率 | $P_{\text{load}}$ | 1.310 W |
| 热电功率 (Seebeck) | $S$ | 0.016 V/K |
| 热导率 | $K$ | 0.805 W/K |
| 热阻 | $R_{th}$ | 0.190 K/W |
| 效率 | $\eta$ | 5.263% (热端) / 4.256% (冷端) |
| 热端散热 | $Q_{\text{hot}}$ | 30.8 W |
| 冷端散热 | $Q_{\text{cold}}$ | 29.6 W |
| 尺寸 | | 25 × 25 × 3.7 mm |

### 5.2 温度对关键参数的影响趋势

| 参数 | 趋势 | 对功率的影响 |
|------|------|-------------|
| 内阻 $R_g$ | 随温度升高而增大 | 功率损耗 |
| 热阻 $R_{th}$ | 随温度变化 | 增益或损耗 |
| 塞贝克系数 $S$ | 随温度升高而增大 | 功率增益 |

### 5.3 机械参数（TEG 049-150-30）

| 参数 | 数值 |
|------|------|
| 热电偶数量 | 049 |
| 高度公差 | $\Delta H \pm 0.25\ \text{mm}$ |
| 长度公差 | $0.2\ \text{mm}$ |
| 重量 | 12 g |
| 最高温度 | 150 °C |
| 最大剪切力 | 125 N/cm² |
| 最大振动 | 55 Hz, 2 m/s² |
| 最大拉力 | 195 N/cm² |
| 陶瓷板 | BK-96, Al₂O₃ 96% |
| 陶瓷热导率 | 15 W/mK, 高度 1 mm |
| 参数公差 | ±6% |

### 5.4 应用要求

- 柔性安装概念（适应高度变化 $\Delta H$）
- 过温、冲击、力保护
- 建议**主动冷却**

---

## 6. TEG 与 Peltier 元件的区别

| 特性 | TEC (Peltier Cooler) | TEG (Generator) |
|------|---------------------|-----------------|
| 优化目标 | 最大冷却性能 / 最大热输运 | 最大输出电压 / 最大转换效率 |
| 热电腿数量 | 较少 | 较多 |
| 热电腿截面积 | 较大 | 较小 |

---

## 7. 微型热电发电机 (µTEG)

### 7.1 概述

- 功率范围：**µW 到 mW**
- 代表产品：
  - **Seiko Thermic** 手表（1998 年小批量生产）
  - **Seiko 微型 TEG**（1994 年开发）
  - **MicroPelt** µTEG
  - **RMT Ltd.** µTEG 和 µTEC

### 7.2 MicroPelt µTEG 规格

| 型号 | MPG-D651 | MPG-D751 |
|------|----------|----------|
| 热电偶对数 | 286 | 540 |
| 热阻 | 22 K/W | 12.5 K/W |
| 电阻 @23°C | 185 $\Omega$ | 300 $\Omega$ |
| 净塞贝克电压 @23°C | 75 mV/K | 140 mV/K |
| 厚度 | 1090 µm | 1090 µm |
| 顶部尺寸 | 2.5 × 2.5 mm | 3.388 × 3.364 mm |
| 底部尺寸 | 2.45 × 2.45 mm | 3.388 × 3.314 mm |
| 热电腿截面积 | | $35 \times 35\ \mu\text{m}^2$ |

### 7.3 MPG-D651 / D751 性能特性

- **功率 vs 负载电阻**：在 $\Delta T = 5\text{K}, 10\text{K}, 20\text{K}, 30\text{K}$ 下的特性曲线
- **电压 vs 电流（不同负载电阻）**：线性 I-V 特性
- 最大功率点出现在 $R_L = R_{g,\text{eff}}$

---

## 8. µTEG 制造工艺

### 8.1 MicroPelt 工艺（溅射沉积法）

| 步骤 | 工艺 |
|------|------|
| 1 | 衬底：Si / SiO₂ |
| 2 | 接触层沉积 (Contact layer deposition) |
| 3 | 接触层图形化 (Structuring) |
| 4 | 热电材料沉积（溅射, sputtering）：Wafer A → n 型，Wafer B → p 型 |
| 5 | 焊料层沉积 (Solder layer deposition) |
| 6 | 光刻胶图形化 thermo-legs |
| 7 | 各向同性和选择性刻蚀（极具挑战性） |
| 8 | 光刻胶去除 |
| 9 | Flip-Chip 键合工艺 |

### 8.2 greenTEG 工艺（电化学沉积法）

| 步骤 | 工艺 |
|------|------|
| 1 | 衬底：Si / SiO₂ + 牺牲层 (sacrificial layer) |
| 2 | 接触层——B-B 和 A-A 在屏面外连接 |
| 3 | 厚 SU-8 层（机械强度高、化学耐受性强） |
| 4 | 图形化 thermo-leg 模板 |
| 5 | 电化学沉积 p 型材料 + 接触（B 侧） |
| 6 | 电化学沉积 n 型材料 + 接触（A 侧） |
| 7 | 沉积顶部互连层 |
| 8 | 溶解牺牲层释放结构 |
| 9 | 沉积底部（此时为顶部）互连层 |
| 10 | 图形化底部接触层，移除 A-A 和 B-B 连接 |

### 8.3 RMT Ltd. 工艺（经典 pellet 法）

- 微型化、基于 pellet 的经典设计

### 8.4 三种方法对比

| 方法 | 制造商 | 技术特点 |
|------|--------|---------|
| 溅射沉积 | MicroPelt | 在 Si 衬底上溅射薄膜热电材料 |
| 电化学沉积 | greenTEG | 在 SU-8 模板中电沉积热电材料 |
| 微型 pellet | RMT Ltd. | 微型化经典体材料设计 |

---

## 9. 热电材料

### 9.1 高性能 TEG 的材料要求

| 要求 | 原因 |
|------|------|
| **大塞贝克系数** $S$ | 高 $\Delta U = S \cdot \Delta T$ |
| **大热阻 / 低热导率** $\kappa$ | 防止 $\Delta T$ 的热短路 |
| **大电导率 / 低电阻率** $\sigma$ | 低内阻 |

### 9.2 已确立的材料

- **Bi₂Te₃**：唯一**商业化可用**的热电材料
- 所有材料的 ZT 最大值约为 **1**
- 材料选择依据温度范围和应用需求

### 9.3 前沿研究材料

| 材料类别 | 状态 |
|----------|------|
| **Skutterudites** (方钴矿) | 研究中 |
| **Half-Heusler** (半赫斯勒) | 研究中 |
| **Clathrates** (笼合物) | 研究中 |

### 9.4 ZT 提升的瓶颈——矛盾性要求

- $S$、$\sigma$ 和 $\kappa$ 并非独立变量
- **低晶格热导率**（低 $\kappa$）与**高迁移率**（高 $\sigma$）不可兼得
- 需要窄带隙简并 p/n 型半导体
- 需要可调掺杂水平（不易实现）
- 需要机械稳定性 → 可选材料有限

---

## 10. 热电优值 (Figure of Merit, ZT)

### 10.1 定义

热电材料的**性能指标**，无量纲值。ZT 值越高，材料性能越好。ZT 具有强烈的**温度依赖性**。

$$ZT = \frac{S^2 \cdot \sigma}{\kappa} \cdot T$$

其中：

| 符号 | 含义 | 单位 |
|------|------|------|
| $S$ | 塞贝克系数 (Seebeck coefficient) | $\text{V/K}$ |
| $\sigma$ | 电导率 (electrical conductivity) | $\frac{1}{\Omega \cdot \text{m}}$ |
| $\kappa$ | 热导率 (thermal conductivity) | $\frac{\text{W}}{\text{m} \cdot \text{K}}$ |
| $T$ | 绝对温度 | $\text{K}$ |

### 10.2 ZT 的含义

- **高 $S$** → 高输出功率
- **高 $\sigma$** → 低内阻 → 高输出功率
- **低 $\kappa$** → 无 $\Delta T$ 热短路 → 高输出功率

### 10.3 功率因子 (Power Factor, PF)

$$PF = S^2 \cdot \sigma$$

$$ZT = \frac{PF}{\kappa} \cdot T$$

### 10.4 总热导率的组成

$$\kappa_{\text{ges}} = \kappa_e + \kappa_L$$

- $\kappa_e$：电子热导率
- $\kappa_L$：晶格热导率 (lattice thermal conductivity)

### 10.5 材料 ZT 现状

- 大多数材料的 ZT 最大值约为 **1**
- 仅有 Bi₂Te₃ 实现商业化
- 文献报道的部分新材料 ZT 可达 1.5–2（实验室阶段）

---

## 11. 热电效率

### 11.1 卡诺极限 (Carnot Limit)

热电的最大效率理论上受**卡诺效率**限制，在小温差下效率较低。

$$\eta_c = \frac{T_h - T_c}{T_h}$$

其中：
- $T_h$：热端温度
- $T_c$：冷端温度

**示例**：

| 场景 | 参数 | 卡诺效率 |
|------|------|---------|
| 室温应用 | $T_h = 310\ \text{K},\ T_c = 300\ \text{K}$ | $\eta_c = \frac{10}{310} = 3.2\%$ |
| 汽车应用 | $T_h = 600\ \text{K},\ T_c = 400\ \text{K}$ | $\eta_c = \frac{200}{600} \approx 33.3\%$ |

> 注：课件原文汽车应用示例写为 $\eta_c = \frac{200}{500} = 40\%$，按 $600\text{K}/400\text{K}$ 重新计算得 $\frac{200}{600}=33.3\%$。

### 11.2 TEG 器件效率极限

最大效率受材料 ZT 限制：

$$\eta = \frac{T_h - T_c}{T_h} \cdot \frac{\sqrt{ZT_m + 1} - 1}{\sqrt{ZT_m + 1} + (T_c / T_h)}$$

其中：

$$ZT_m = \frac{\int_{T_c}^{T_h} ZT \ dT}{T_h - T_c}$$

**示例**（$T_h = 310\ \text{K},\ T_c = 300\ \text{K},\ ZT = 1$）：

$$\eta < \sim 0.6\%$$

### 11.3 ZT 对效率的影响

| ZT | 效率趋势 |
|-----|---------|
| 1 | 基准值（室温 ~0.6%） |
| 1.5 | 显著提升 |
| 2 | 效率进一步提高 |
| 3 | 接近理想值 |
| 5 | 大幅跨越 |
| 10 | 接近卡诺极限 |

- 最佳效率（约 10%）在**航天应用**中实现（高 $\Delta T$）

---

## 12. 功率生成——等效电路模型

### 12.1 电气等效电路：带内阻的电压源

$$U_0 = m \cdot (S_p - S_n) \cdot (T_2 - T_1)$$

$$I_a = \frac{U_0}{R_{g,\text{eff}} + R_L}$$

其中：

| 符号 | 含义 |
|------|------|
| $U_0$ | 开路电压 (open circuit voltage) |
| $I_a$ | 输出电流 |
| $m$ | 热电偶对数量 |
| $T_{1,2}$ | 冷/热端温度 |
| $S_{p,n}$ | p/n 型材料的塞贝克系数 |
| $R_{g,\text{eff}}$ | TEG 内阻 |
| $R_L$ | 负载电阻 |

### 12.2 负载功率

$$P = U_L \cdot I_L = \left[ m \cdot (S_p - S_n) \cdot (T_2 - T_1) \right]^2 \cdot \frac{R_L}{(R_{g,\text{eff}} + R_L)^2}$$

### 12.3 最大输出功率条件（阻抗匹配）

对 $P(R_L)$ 求极值：

$$\frac{dP(R_L)}{dR_L} \stackrel{!}{=} 0 \quad \Rightarrow \quad R_L = R_{g,\text{eff}}$$

**最大功率**：

$$P_{\text{max}} = \frac{U_0^2}{4 \cdot R_{g,\text{eff}}} \quad (\text{当 } R_L = R_{g,\text{eff}})$$

### 12.4 影响输出功率的因素

| 因素 | 影响 | 方向 |
|------|------|------|
| 塞贝克系数 $S_p, S_n$ | 更高 → 更高输出功率 | ++ |
| 温度差 $\Delta T = T_2 - T_1$ | 更高 → 更高输出功率 | ++ |
| 热电偶对数 $m$ | 更多 → 更高输出电压 | ++ |
| 热电偶对数 $m$ | 更多 → 更高内阻 | - - |

**关键结论**：

- $P \sim (\Delta T)^2$
- 增加热电偶对数 $m$ 产生**设计冲突**（电压增大 vs 内阻增大）

---

## 13. TEG 建模——热界面

### 13.1 热界面的影响

TEG 与热/冷源之间的**接触热阻**会降低有效温度差 $\Delta T_{\text{TEG}}$，即降低热输入功率。

$$\Delta T_{\text{TEG}} = \frac{R_{th,\text{TEG}}}{R_{th,\text{TEG}} + R_{th,h} + R_{th,c}} \cdot (T_2 - T_1)$$

其中：
- $R_{th,\text{TEG}}$：TEG 热阻
- $R_{th,h}$：TEG 与热源之间的接触热阻
- $R_{th,c}$：TEG 与冷源之间的接触热阻

定义**热馈入因子 (thermal feed factor)**：

$$d = \frac{R_{th,\text{TEG}}}{R_{th,\text{TEG}} + R_{th,h} + R_{th,c}}$$

### 13.2 热 + 电界面综合模型

完整输出电功率表达式：

$$P_{el} = \left( \frac{R_{th,\text{TEG}}}{R_{th,\text{TEG}} + R_{th,h} + R_{th,c}} \right)^2 \cdot \frac{\left[ m \cdot S \cdot \Delta T \right]^2 \cdot R_L}{(R_{g,\text{eff}} + R_L)^2}$$

简写为：

$$P_{el} = d^2 \cdot \frac{(m \cdot S \cdot \Delta T)^2 \cdot R_L}{(R_{g,\text{eff}} + R_L)^2}$$

**关键结论**：实际功率与 $d^2$ 成正比，热界面显著影响性能。

### 13.3 热阻元件及其电气类比

#### 热势与热流类比

| 热学量 | 电气类比 |
|--------|---------|
| 温度 $T(t)$ | 电势 $e(t)$ |
| 热流 $\Phi(t)$ | 电流 $f(t)$ |

#### 热阻元件

**体积热阻 (Volumetric)**：

$$R_{th} = \frac{l}{\lambda \cdot A} \quad \left[ \frac{\text{K}}{\text{W}} \right]$$

其中：
- $\lambda$：热导率 $\left[ \frac{\text{W}}{\text{m} \cdot \text{K}} \right]$
- $l$：长度
- $A$：截面积

**热容 (Thermal Capacitance)**：

$$C = m \cdot c \quad \left[ \frac{\text{J}}{\text{K}} \right]$$

其中：
- $c$：比热容 $\left[ \frac{\text{J}}{\text{kg} \cdot \text{K}} \right]$

### 13.4 热阻的面定义 (Area-Specific)

适用于平面薄层和接触面：

$$R_{XH} = \frac{\gamma}{A} \quad ; \quad R_{XY} = \frac{\rho_{th}}{A}$$

其中：
- $\gamma$：比接触热阻 (specific contact resistance)
- $\rho_{th}$：比面热阻 (specific heat resistance)
- $A$：有效面积

**典型值**：

| 材料 | 厚度 | $\rho_{th}$ (K·cm²/W) |
|------|------|----------------------|
| Glimmer (云母) | 50 µm | 1.40 |
| Silicone (硅胶) | 300 µm | 2.46 |
| Al₂O₃ | 300 µm | 0.12 |
| Polyimide (聚酰亚胺) | 77 µm | 1.71 |
| Silicone-TCP | 100 µm | 1.64 |
| WL-Kleber (Epoxy) | 100 µm | 1.22 |

**接触比热阻** $\gamma$ (cm²·K/W)：

| 界面类型 | 有导热膏 | 无导热膏 |
|----------|---------|---------|
| 金属 - 金属 | 0.5 | 1 |
| 金属 - 阳极氧化铝 (Eloxal) | 1.4 | 2 |

### 13.5 空气对流的影响

- 散热器-空气界面热阻 $R_{HA}$ 可变
- 无强制对流（风速 $v \approx 0$）时，$R_{HA}$ 显著增大
- 强制对流可大幅降低 $R_{HA}$

**示例**：Fischer elektronik ICK S 25 × 25 × 18 散热器
- 低空气对流：$R_{HA} = 4.5\ \text{K/W}$
- 强制空气对流：$R_{HA} = 1.5\ \text{K/W}$

---

## 14. TEG 功率输出计算

### 14.1 计算示例参数

以 Thermalforce TEG 049-150-30 为例：

| 参数 | 值 |
|------|-----|
| TEG 面积 | 25 × 25 mm² |
| TEG 热阻 | 5.263 K/W |
| 散热器 (Fischer ICK S 25×25×18) | $R_{th,HS} = 4.5\ \text{K/W}$（低对流）/ $1.5\ \text{K/W}$（强制对流） |
| 导热膏 (TCP, Wacker P12) | 厚度 50 µm，热导率 $\lambda = 0.81\ \text{W/(m·K)}$ |
| 温差 | $\Delta T = T_2 - T_1 = 10\ \text{K}$ ($T_2 = 283\ \text{K},\ T_1 = 273\ \text{K}$) |

### 14.2 仅考虑热界面

**Case 1：低空气对流**

$$\begin{aligned}
R_{th,\text{TEG}} &= 5.263\ \text{K/W} \\
R_{th,\text{HS}} &= 4.5\ \text{K/W} \\
R_{th,\text{TCP}} &= 0.1\ \text{K/W}
\end{aligned}$$

$$\Rightarrow \Delta T_{\text{TEG}} = 0.528 \cdot (T_2 - T_1)$$

$$P_{\text{thermal}} = 0.278 \cdot P_{\text{max}}$$

热馈入因子 $d = 0.528$

**Case 2：强制空气对流**

$$\begin{aligned}
R_{th,\text{TEG}} &= 5.263\ \text{K/W} \\
R_{th,\text{HS}} &= 1.5\ \text{K/W} \\
R_{th,\text{TCP}} &= 0.1\ \text{K/W}
\end{aligned}$$

$$\Rightarrow \Delta T_{\text{TEG}} = 0.759 \cdot (T_2 - T_1)$$

$$P_{\text{thermal}} = 0.576 \cdot P_{\text{max}}$$

热馈入因子 $d = 0.759$

### 14.3 热 + 电界面综合计算

TEG 参数：
- 内阻 $R_{g,\text{eff}} = 0.57\ \Omega$
- 塞贝克系数 $m \cdot S = 0.016\ \text{V/K}$

**Case 1：低空气对流** ($d = 0.528$，$\Delta T = 10\ \text{K}$，$R_L = R_{g,\text{eff}}$)

$$P_{el} = d^2 \cdot \frac{(m \cdot S \cdot \Delta T)^2 \cdot R_L}{(R_{g,\text{eff}} + R_L)^2}$$

$$U_{0,\text{real}} = 84.4\ \text{mV} \quad ; \quad P_{\text{real}} = 3.1\ \text{mW}$$

**Case 2：强制空气对流** ($d = 0.759$，$\Delta T = 10\ \text{K}$，$R_L = R_{g,\text{eff}}$)

$$U_{0,\text{real}} = 121.4\ \text{mV} \quad ; \quad P_{\text{real}} = 6.4\ \text{mW}$$

**理论最大值**（$\Delta T = 10\ \text{K}$，无热界面损耗）：

$$U_{0,\text{max}} = m \cdot S \cdot \Delta T = 160\ \text{mV}$$

$$P_{\text{max}} = \frac{1}{4} \cdot \frac{U_{0,\text{max}}^2}{R_L} = 11.2\ \text{mW}$$

### 14.4 关键关系总结

$$\begin{aligned}
U_{0,\text{real}} &= d \cdot m \cdot S \cdot \Delta T \\
P_{\text{real}} &= d^2 \cdot P_{\text{max}}
\end{aligned}$$

- 输出电压 $U_{0,\text{real}} \sim d$
- 输出功率 $P_{\text{real}} \sim d^2$

---

## 15. 升压变换器与功率损耗

### 15.1 问题

- 低输出电压（~100 mV）不足以直接驱动电子系统
- 需要**低压升压变换器 (step-up converter)** 将 TEG 输出电压提升至可用水平（如 2 V）

### 15.2 升压变换器的功率损耗

- 在低输入电压下效率较低（典型 **≤ 25%**）
- 需要最低启动电压（目前大多约 **20 mV**，部分可达 **10 mV**）

### 15.3 完整功率表达（含 DC-DC 效率）

$$P_{el} = \left( \frac{R_{th,\text{TEG}}}{R_{th,\text{TEG}} + R_{th,h} + R_{th,c}} \right)^2 \cdot \frac{\left[ m \cdot S \cdot \Delta T \right]^2 \cdot R_L}{(R_{g,\text{eff}} + R_L)^2} \cdot \eta_{DC-DC}$$

其中 $\eta_{DC-DC}$ 为电子升压变换器效率。

> **后果**：在"极低温度梯度"下无法实现能量收集。

---

## 16. 应用领域

### 16.1 航天

- **RTG (Radioisotope Thermoelectric Generator)** 作为深空任务的电源（无太阳辐射环境）
- 放射性衰变作为热源
- 高可靠性（**40 年以上**）
- 示例：Mars 2020 Perseverance Rover + Ingenuity（NASA/JPL）

### 16.2 汽车

- 利用**废气热量**发电
- 可能的**交流发电机替代方案**

### 16.3 传感器与小型集成

- **无线传感器节点和网络**
- 独立于电源/电池运行
- 通过 MEMS 技术实现小型化
- 适用于**恶劣环境**

### 16.4 微型冷却

- 光纤通信系统中**激光波长稳定**
- 医疗和**航空航天应用**

### 16.5 冷却应用

| 应用 | 特点 |
|------|------|
| **冷却箱 (Cooling boxes)** | Peltier 元件最常见用途；效率低但设计简单、空间节省、成本低廉 |
| **实验室设备**（如 PCR 热循环仪） | 精确温控 ±0.25 K；TEG 坚固耐用、寿命长 |

---

## 17. 总结

1. **热电能量收集**利用**塞贝克效应**将热流转换为直流电压
2. **制造技术**涵盖从焊接 µTEG、溅射沉积到电化学沉积等多种方法
3. **热电效率**取决于材料的塞贝克系数 $S$、电导率 $\sigma$ 和热导率 $\kappa$，且由于矛盾性需求始终是一种**折中**
4. **TEG 输出功率**在内阻与负载**匹配**时最大，且随温度差增大而增大：$P \sim (\Delta T)^2$
5. 热源与冷源之间的**所有热界面**都必须纳入热电收集系统计算
6. 从冷源移除热量以维持温度梯度是设计热电收集系统的**最大挑战**

$$ZT = \frac{S^2 \cdot \sigma}{\kappa} \cdot T$$

---

> **笔记生成日期**：2026-05-24  
> **来源课件**：MicroEnergyHarvesting_Lecture_3_Thermoelectric Energy Harvesting_SS_2026.pdf (51 页)