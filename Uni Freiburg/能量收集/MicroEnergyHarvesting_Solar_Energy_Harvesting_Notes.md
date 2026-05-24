# 微能量收集 - 太阳能收集讲座笔记

## 1. 太阳辐射基础

### 1.1 太阳基本数据
- **太阳光度**：$3.86 \times 10^{26} \text{ W}$（功率密度：$140 \text{ W/m}^3$）
- **太阳年龄**：约 45.7 亿年
- **预期寿命**：约 70 亿年

### 1.2 空气质量光谱 (Air Mass Spectra)
- **AM0**：地球大气层外的太阳辐射
- **AM1**：太阳垂直照射时的完美情况
- **AM1.5**：太阳能电池测试标准（$1000 \text{ W/m}^2$）
  - **AM1.5D**：仅直接辐射
  - **AM1.5G**：全球辐射（包括散射）

#### 空气质量计算公式
$$AM = \frac{1}{\cos(\theta)} + 0.50572 \cdot (96.07995 - \theta)^{-1.6364}$$

其中：
- $\theta$：天顶角（AM1.5对应 $48.2^\circ$）

更精确的公式：
$$AM(\theta) = \frac{-R \cdot \cos(\theta) + \sqrt{(R+H)^2 - R^2 \cdot \sin^2(\theta)}}{H}$$

其中：
- $R$：地球半径（6371 km）
- $H$：尺度高度（8.5 km）

### 1.3 太阳强度计算

#### 直接辐射强度
$$I_D = I_0 \cdot 0.7^{AM^{0.678}}$$

其中：
- $I_D$：垂直于辐射平面的强度（W/m²）
- $I_0$：太阳常数（AM0辐射）

#### 全球辐射强度
$$I_G = I_0 \cdot 1.1 \cdot \left[ (1 - 0.14 \cdot h) \cdot 0.7^{AM^{0.678}} + 0.14 \cdot h \right]$$

其中：
- $h$：海拔高度（km）

简化公式：
$$I_G = I_D \cdot 1.1$$

### 1.4 辐射单位与关系

#### 光子能量
$$E_Q = h \cdot f = \frac{hc}{\lambda}$$

其中：
- $h$：普朗克常数
- $f$：频率
- $c$：光速
- $\lambda$：波长

可见光光子能量范围：$2-5 \times 10^{-19} \text{ J}$

#### 辐射通量密度
- **光谱辐射度**：$F(\lambda) = \frac{\Phi}{\Delta\lambda \cdot A}$（W/(m²·nm)）
- **辐射度**：$E = \int_0^\infty F(\lambda) d\lambda$（W/m²）
- **辐射通量**：$L_{e,\Omega}$（W/(m²·sr)）

#### 累积辐射
- 欧洲南向45°倾斜：$1000-5000 \text{ Wh/m}^2/\text{天} = 3.6-18 \text{ MJ/m}^2/\text{天}$

## 2. 太阳位置与角度计算

### 2.1 时间校正
- **时差 (EoT)**：$\pm 15$ 分钟
- **经度差校正**：通常 $\pm 30$ 分钟（考虑夏令时）

#### 时角
$$HRA = 15^\circ \cdot (LST - 12)$$

其中：
- $LST$：地方太阳时

### 2.2 赤纬角
$$\delta = 23.45^\circ \cdot \sin\left( \frac{360}{365} \cdot (d - 81) \right)$$

其中：
- $d$：从年初开始的天数

### 2.3 太阳高度角
$$\alpha = \sin^{-1}\left[ \sin\delta \cdot \sin\varphi + \cos\delta \cdot \cos\varphi \cdot \cos(HRA) \right]$$

正午时：
$$\alpha = 90^\circ + \varphi - \delta \quad (\text{如果} \alpha > 90^\circ: 180^\circ - \alpha)$$

其中：
- $\varphi$：纬度

### 2.4 方位角
$$Azimuth^* = \cos^{-1}\left( \frac{\sin\delta \cdot \cos\varphi - \cos\delta \cdot \sin\varphi \cdot \cos(HRA)}{\cos\alpha} \right)$$

其中：
- 当 $HRA < 0$ 时使用此公式
- 当 $HRA > 0$ 时：$360^\circ - Azimuth$

## 3. 太阳能电池板倾斜与方向

### 3.1 倾斜表面辐射
- 水平表面辐射：$S_h = S_i \cdot \sin\alpha$
- 倾斜表面辐射：$S_m = S_i \cdot \sin(\alpha + \beta)$

关系：
$$S_m = S_h \cdot \frac{\sin(\alpha + \beta)}{\sin\alpha}$$

其中：
- $\beta$：电池板倾斜角

### 3.2 任意方向电池板
$$S_m = S_i \cdot \left[ \cos\alpha \cdot \sin\beta \cdot \cos(\psi - \Theta) + \sin\alpha \cdot \cos\beta \right]$$

其中：
- $\psi$：电池板方位角
- $\Theta$：太阳方位角

### 3.3 向量表示
$$S_m = S_i \cdot \cos\gamma = S_i \cdot \boldsymbol{S} \cdot \boldsymbol{N}$$

### 3.4 最佳倾斜角
- 通常由纬度决定
- 季节性应用可能需要不同角度

## 4. 太阳辐射测量与计算

### 4.1 辐射与辐照度
- **太阳辐照度**：瞬时测量（W/m²）
- **太阳辐照量**：特定时间段内的总太阳能量（kWh/m²/天）

### 4.2 测量仪器
- **总日射表**：测量全球辐射（水平表面）
- **直接日射表**：仅测量直接辐射（跟踪太阳）
- **日照记录仪**：测量超过阈值（200 mW/cm²）的日照时数

### 4.3 使用TMY数据计算
典型气象年（TMY）数据集包含：
- 水平表面全球辐射 $I_G$
- 跟踪光束辐射 $I_D$

#### 漫射辐射
$$I_{Diff} = I_G - I_D \cdot \sin\alpha$$

#### 总辐照量
$$G = B + D$$

其中：
- $B$：直接部分
- $D$：漫射部分

$$B = I_D \cdot \left[ \sin\delta \sin\varphi \cos\beta - \sin\delta \cos\varphi \sin\beta \cos\psi + \cos\delta \cos\varphi \cos\beta \cos(HRA) + \cos\delta \sin\varphi \sin\beta \cos\psi \cos(HRA) + \cos\delta \sin\psi \sin(HRA) \sin\beta \right]$$

$$D = I_{Diff} \cdot \frac{180 - \beta}{180}$$

## 5. 光伏电池工作原理

### 5.1 工作模式

#### 平衡条件
- 无光照，无电压，无电流

#### 开路条件
- 产生额外载流子
- 开路电压 $V_{OC}$ 产生反向电场

#### 短路条件
- 短路电流 $I_{SC}$ 流过外部连接
- $I_{SC}$ 与辐照度成正比

### 5.2 收集概率与量子效率

#### 量子效率 (QE)
$$QE = \frac{\text{收集的电子数}}{\text{入射光子数}}$$

- **外部量子效率**：包括反射和透射
- **内部量子效率**：排除反射和透射

#### 光谱响应 (SR)
$$SR(\lambda) = \frac{I_{SC}}{P_{in}} = \frac{q\lambda}{hc} \cdot QE \quad (\text{A/W})$$

其中：
- $q$：电子电荷
- $\lambda$：波长
- $h$：普朗克常数
- $c$：光速

## 6. 光伏电池特性曲线

### 6.1 二极管方程（无光照）
$$I = I_0 \cdot \left( e^{\frac{qV}{nkT}} - 1 \right)$$

其中：
- $n$：理想因子
- $I_0$：反向饱和电流

### 6.2 光照条件下的电流方程
$$I = I_0 \cdot \left( e^{\frac{qV}{nkT}} - 1 \right) - I_L$$

或（作为电源）：
$$I = I_L - I_0 \cdot \left( e^{\frac{qV}{nkT}} - 1 \right)$$

其中：
- $I_L$：光生电流

### 6.3 关键参数

#### 短路电流 $I_{SC}$
- $I_{SC} = I_L$（除非串联电阻非常高）
- 随带隙增加而减小

#### 开路电压 $V_{OC}$
$$V_{OC} = \frac{nkT}{q} \ln\left( \frac{I_L}{I_0} + 1 \right)$$

或：
$$V_{OC} = \frac{kT}{q} \ln\left( \frac{(N_A + \Delta n) \cdot \Delta n}{n_i^2} \right)$$

其中：
- $N_A$：掺杂浓度
- $\Delta n$：过剩载流子
- $n_i$：本征载流子浓度

- $V_{OC}$ 与器件中的复合量成正比
- 随带隙增加而增加

### 6.4 填充因子 (Fill Factor)
$$FF = \frac{P_{MP}}{V_{OC} \cdot I_{SC}} = \frac{V_{MP} \cdot I_{MP}}{V_{OC} \cdot I_{SC}}$$

最大功率点电压：
$$V_{MP} = V_{OC} - \frac{nkT}{q} \ln\left( \frac{qV_{MP}}{nkT} + 1 \right)$$

经验公式：
$$FF = \frac{\upsilon_{OC} - \ln(\upsilon_{OC} + 0.72)}{\upsilon_{OC} + 1}$$

其中：
$$\upsilon_{OC} = \frac{q}{nkT} V_{OC}$$

- 最高FF值约0.85，某些电池接近0.90

### 6.5 太阳能电池效率
$$\eta = \frac{P_{max}}{P_{in}} = \frac{V_{OC} \cdot I_{SC} \cdot FF}{P_{in}}$$

其中：
- $P_{in}$ 通常基于AM1.5辐射（1000 W/m²）

#### 理论极限
- **Shockley-Queisser极限**（单p-n结）：33.7% @ 1.34 eV
- Si（1.1 eV）的SQ极限：32%
- 无限带隙的理论极限：86.8%

## 7. 太阳能电池中的电阻

### 7.1 特征电阻
$$R_{CH} = \frac{V_{MP}}{I_{MP}} \approx \frac{V_{OC}}{I_{SC}}$$

典型范围：mΩ量级

### 7.2 串联电阻 $R_S$
- 发射极和基区的体电阻
- 金属与Si之间的接触电阻
- 金属电极的电阻
- 典型值：0.5-1.3 Ω/cm²

### 7.3 并联电阻 $R_{SH}$
- 由制造缺陷引起的漏电流
- 典型值：>1000 Ω/cm²

### 7.4 包含电阻的电流方程
$$I = I_L - I_0 \cdot \left( e^{\frac{q(V+IR_S)}{nkT}} - 1 \right) - \frac{V + IR_S}{R_{SH}}$$

简化形式：
- 仅串联电阻：$I = I_L - I_0 \cdot \left( e^{\frac{q(V+IR_S)}{nkT}} - 1 \right)$
- 仅并联电阻：$I = I_L - I_0 \cdot \left( e^{\frac{qV}{nkT}} - 1 \right) - \frac{V}{R_{SH}}$

### 7.5 电阻对填充因子的影响
#### 串联电阻影响
$$FF_S = FF_0 \cdot \left( 1 - 1.1r_S + \frac{r_S^2}{5.4} \right)$$

#### 并联电阻影响
$$FF_{SH} = FF_0 \cdot \left( 1 - \frac{V_{OC} + 0.7}{V_{OC}} \cdot \frac{FF_0}{r_{SH}} \right)$$

#### 综合影响
$$FF = FF_0 \cdot \frac{1 - 1.1r_S + \frac{r_S^2}{5.4}}{1 - \frac{V_{OC} + 0.7}{V_{OC}} \cdot \frac{FF_0}{r_{SH}} \cdot \left( 1 - 1.1r_S + \frac{r_S^2}{5.4} \right)}$$

其中：
- $r_S = \frac{R_S}{R_{CH}}$
- $r_{SH} = \frac{R_{SH}}{R_{CH}}$

适用条件：$r_S < 0.4$；$r_{SH} > 0.4$；$\upsilon_{OC} > 10$

## 8. 其他影响因素

### 8.1 温度影响
- 温度升高降低 $E_C$ → $n_i$ 增加
- $V_{OC}$ 随温度升高而降低
- $I_{SC}$ 轻微增加

#### Si电池的温度系数
- $\frac{dV_{OC}}{dT} \approx -2.2 \text{ mV/K}$
- $I_{SC}$：每K增加0.06%
- $FF$：每K降低1.5%
- $P_{MP}$：每K降低0.4-0.5%

### 8.2 理想因子 $n$
- 通常假设为1
- 取决于复合机制

| 复合类型 | $n$ | 描述 |
|---------|-----|------|
| SRH，带间（低注入） | 1 | 复合受少数载流子限制 |
| SRH，带间（高注入） | 2 | 复合受两种载流子限制 |
| Auger | 2/3 | 复合需要两个多数载流子和一个少数载流子 |
| 耗尽区（结） | 2 | 两个载流子限制复合 |

### 8.3 光强影响
- 改变太阳数
- 1 sun @ AM1.5：1000 W/m²
- 低光强下：$R_{SH}$ 影响显著！

## 9. 商业太阳能电池类型

### 9.1 第一代技术（成熟技术）
| 电池类型 | 效率 | 优势 |
|---------|------|------|
| 单晶硅 | 25.6% | 地球丰富，常见 |
| 多晶硅 | 21.3% | 地球丰富，常见 |
| CIGS (CuInGaSe₂) | 21.7% | 柔性基板 |
| CdTe电池 | 21.5% | 柔性基板 |

### 9.2 第二代技术（新兴技术）
| 电池类型 | 效率 | 特点 |
|---------|------|------|
| 染料敏化TiO₂ | 11.9% | 颜色可调 |
| 薄膜硅 | 11.4% | 柔性模块 |
| 有机电池 | 11.5% | 柔性，半透明 |
| GaAs电池 | 28.8% | 高效率，柔性模块 |

### 9.3 第三代技术
| 电池类型 | 效率 | 特点 |
|---------|------|------|
| 钙钛矿电池 | 21.0% | 溶液处理 |

## 10. 太阳能能量收集应用

### 10.1 HydroWatch气象节点
- 使用NiMH电池，支持涓流充电
- 移除输入调节器可显著提高效率
- 30分钟日照 → 120 mWh/天（66%效率下79.2 mWh/天）

### 10.2 a-Si薄膜电池功率计算
$$P_{max} = \int F(\lambda) \cdot QE(\lambda) d\lambda \quad (\text{W/m}^2)$$

其中：
- $F(\lambda)$：光谱辐射度
- $QE(\lambda)$：量子效率

#### 量子效率拟合
$$fit(\lambda) = -1.433 \times 10^{-6} \lambda^2 + 0.0154\lambda - 3.335$$

#### 最大功率
$$P_{max} = \int_{280nm}^{800nm} F(\lambda) \cdot QE(\lambda) d\lambda = 188 \text{ W/m}^2$$

### 10.3 室内太阳能电池 (IPV)
#### 光谱不匹配
- 室内光源光谱 ≠ AM1.5
- 透过窗户的阳光功率降低，光谱偏移

#### 可用辐射水平
| 条件 | 功率密度 (W/m²) |
|------|----------------|
| 室外正午，直射阳光 | 700-1200 |
| 室外正午，弱云 | 150-500 |
| 室外正午，强云 | 20-50 |
| 室内玻璃后正午 | 500-900 |
| 室内玻璃后正午，弱云 | 50-200 |
| 室内玻璃后正午，强云 | 5-50 |
| 室内仅人工光 | 2-10 |
| 室内仅荧光灯 | 1-3 |

## 11. 太阳能电池选择考虑因素

1. **应用地点**：室内或室外？→ 相关光谱（AM1.5、人工光等）
2. **应用地点辐照度**：直接辐射、漫射光、昼夜、季节变化等
3. **其他边界条件**：温度、振动、污染、湿度等

---

*笔记基于"Micro Energy Harvesting Chapter 2: Solar Energy Harvesting"讲座内容整理，包含所有核心概念、公式和关键理论。*

*文件生成时间：2026-05-24*