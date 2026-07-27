# Energy Harvesting — Practice Exam with Sample Solutions

# 能量采集（Energy Harvesting）— 模拟考试与参考答案

> **Course**: Energy Harvesting (MEH), Summer Semester 2013
> **Instructor**: Prof. Dr.-Ing. Peter Woias, Lehrstuhl Konstruktion von Mikrosystemen
> **Source**: MEH_Probeklausur_mitMusterlösung.pdf (SS 2011 Beispielaufgaben)
>
> **课程**：能量采集 (MEH)，2013 夏季学期
> **授课教师**：Prof. Dr.-Ing. Peter Woias，微系统设计教席
> **来源**：MEH_Probeklausur_mitMusterlösung.pdf（2011 夏季学期例题）

---

## Exam Rules & Instructions · 考试规则与说明

| Rule 规则 | Description 说明 |
|---|---|
| Allowed tools 允许工具 | Set square (三角板), permanent pens (非可擦除笔), provided formulary (提供的公式表), non-programmable calculator (不可编程计算器), student ID + identification document (学生证+身份证件) |
| Prohibited 禁止 | Pencils (铅笔), correction fluid (修正液), RED color pen (红色笔—仅供批改), any other materials (其他任何材料) |
| Important 重要 | Write name & matriculation number on every sheet (每页右上角写姓名和学号); Underline final results twice (最终结果双下划线); No programmable calculator (禁止可编程计算器) |

---

## Task 1: Harmonic Oscillator · 任务 1：谐振子

### 1a) General equation of the damped harmonic oscillator (without excitation)

### 1a) 有阻尼谐振子的一般方程（无外部激励）

> Give the general equation for the damped harmonic oscillator (without excitation). Which term describes which function? Name the damping coefficients.

**Equation 方程：**

$$m\ddot{z} + b\dot{z} + kz = 0$$

| Term 项 | Physical Meaning 物理含义 |
|---|---|
| $m\ddot{z}$ | Mass motion — kinetic energy / 质量运动 — 动能 |
| $b\dot{z}$ | Damping / loss term (sign always opposite to motion) / 阻尼项/损耗项（符号始终与运动方向相反） |
| $kz$ | Energy storage in the spring — potential energy / 弹簧中的能量储存 — 势能 |

- $b$ = damping coefficient / 阻尼系数
- $m$ = mass / 质量
- $k$ = spring constant / 弹簧常数

---

### 1b) Quality factor (Q-factor)

### 1b) 品质因数（Q 值）

> What does a low vs. high Q-factor mean for an oscillating system?

| Q-factor Q 值 | Behavior 行为 | Examples 示例 |
|---|---|---|
| **High 高** (e.g. $Q > 500$) | Low energy loss per period / 每周期能量损耗小 | Ion trap 离子阱, quartz oscillator 石英振荡器, frequency standards 频率基准, sapphire bearings 蓝宝石轴承（钟表"宝石"） |
| **Low 低** (e.g. $Q < 10$) | No oscillation in overdamped system; high energy loss / 过阻尼系统中无振荡；高能量损耗 | Shock absorber 减震器 |

---

### 1c) Three technical examples of harmonic oscillators

### 1c) 谐振子的三个技术实例

> Name three different technical examples that can be described by the harmonic oscillator and briefly explain their function.

| Example 实例 | Damping 阻尼 | Description 描述 |
|---|---|---|
| **Loudspeaker** 扬声器 | High 高 | Should behave as "static" as possible / 应尽可能"静态"地工作 |
| **Door damper** 门缓冲器 | High 高 | Asymptotically damped / 渐近阻尼 |
| **Electrical resonant circuit** 电谐振回路 | Low 低 | Should lose as little energy as possible in the resistor / 应尽可能减少电阻中的能量损失 |

---

### 1d) Resonance frequency shift for strongly damped systems

### 1d) 强阻尼系统的共振频率偏移

> How does the resonance frequency shift for strongly damped systems?

The resonance frequency becomes **lower**. For the **aperiodic boundary case** (临界阻尼) or **overdamped systems** (过阻尼), **no oscillation occurs at all**.

共振频率**降低**。对于**临界阻尼**或**过阻尼**系统，**完全不发生振荡**。

---

### 1e) Formula for resonance frequency

### 1e) 共振频率公式

$$\omega = \sqrt{\frac{k}{m}}$$

---

### 1f) Three damping cases

### 1f) 三种阻尼情形

> Name the three damping cases for the damped harmonic oscillator.

| Damping Case 阻尼情形 | Description 描述 |
|---|---|
| **Underdamped** 欠阻尼 | Oscillating system / 振荡系统 |
| **Critically damped** (aperiodic) 临界阻尼 | Aperiodic boundary case / 非周期边界情形 |
| **Overdamped** 过阻尼 | Creep case / 蠕变情形（无振荡） |

---

## Task 2: Vibration Harvester · 任务 2：振动能量采集器

### 2a) Three vibration transducer types (< 25 cm²) and power rating

### 2a) 三种振动换能器类型（< 25 cm²）及功率评估

> Name three different vibration transducer types (smaller than 25 cm²) and evaluate them according to their power capability.

| Transducer Type 换能器类型 | Power Capability 功率能力 |
|---|---|
| **Electrostatic / Electret** 静电/驻极体式 | $0.1 \sim 5\ \mu\text{W}$ |
| **Electrodynamic** 电动式 | $100\ \mu\text{W} \sim \text{several}\ 10\ \text{mW}$ |
| **Piezoelectric** 压电式 | $50\ \mu\text{W} \sim \text{several}\ \text{mW}$ |

---

### 2b) Sketch of piezoelectric bimorph generator

### 2b) 压电双晶片发电器示意图

> Sketch a piezoelectric bimorph generator and name the individual components.

Components (see script): Substrate beam (基底梁), two piezo beams (两个压电梁), electrodes (电极), mass at beam end (梁末端质量块)

---

### 2c) Sketch of electromagnetic vibration transducer

### 2c) 电磁振动换能器示意图

Components (see script): Spring (弹簧), mass (质量块), magnets (磁铁), coil (线圈)

---

### 2d) Typical harvestable power

### 2d) 典型的可采集功率

> How much power can typically be harvested with a vibration harvester?

Depending on the concept: between $1\ \mu\text{W}$ and several $10\ \text{mW}$, **typically $100 \sim 500\ \mu\text{W}$**.

---

### 2e) Power calculation of a piezo bimorph

### 2e) 压电双晶片功率计算

> Calculate the power of a piezo bimorph (see exercise, formula will be provided).

(Formula provided in exam / 公式在考试中给出)

---

### 2f) Electret / electrostatic transducers — technical feasibility

### 2f) 驻极体/静电换能器 — 技术可行性评估

> Microtechnically, electret/electrostatic transducers are the most demanding to fabricate. Evaluate their technical application possibilities based on script data.

- Output power is **extremely low** → very limited technical application possibilities
- At most suitable for operating a **quartz watch** or electronics up to **max. 10 µW**
- 输出功率**极低** → 技术应用可能性非常有限
- 最多适用于驱动**石英手表**或功耗不超过 **10 µW** 的电子设备

---

## Task 4: Thermoelectric Generator (TEG) · 任务 4：热电发电机

> **Given data 给定数据：**
> - Seebeck coefficient 塞贝克系数：$\alpha_g = 51\ \text{mV/K}$
> - Thermal resistance 热阻：$K_g = 5.6\ \text{K/W}$
> - Electrical resistance 电阻：$R_g = 6.6\ \Omega$
> - Dimensions 尺寸：$30 \times 30 \times 4.8\ \text{mm}^3$
> - 127 thermocouple pairs 对热电偶，单腿横截面积 $A_{tb} = 1 \times 1\ \text{mm}^2$

---

### 4a) Material selection and series connection

### 4a) 材料选择与串联连接

> The material pairs p/n-Bismuth Telluride (Bi₂Te₃) and Copper/Constantan both exhibit a Seebeck coefficient. Which is typically used and why are thermolegs electrically connected in series? Can Bi₂Te₃ be used for every temperature range? Name two other thermoelectric material pairs with typical applications.

**材料选择**：通常使用 **Bismuth Telluride (Bi₂Te₃ / 碲化铋)**，因其塞贝克系数远高于 Copper/Constantan（铜/康铜）。

**串联原因**：串联可提高总输出电压（以牺牲输出电流为代价）。塞贝克系数通常仅几 µV/K，必须串联才能获得可用电压。即便串联后，通常仍需额外的 DC-DC 转换器才能有效驱动电子设备，尤其在能量采集中常见的低温度差场景。

**Bi₂Te₃ 温度限制**：不适用于所有温度范围。

**其他热电材料对**：
| Material Pair 材料对 | Typical Application 典型应用 |
|---|---|
| Cu/Ni 铜/镍 | — |
| PbTe 碲化铅 | 高温应用 |

---

### 4b) Ratio of active area to total area

### 4b) 活性面积与总面积之比

$$\text{Total area 总面积} = 900\ \text{mm}^2$$

$$\text{Active area 活性面积} = 2 \times 127 \times 1\ \text{mm}^2 = 254\ \text{mm}^2$$

$$\text{Ratio 比率} = \frac{254}{900} \approx 0.282$$

---

### 4c) Thermoleg length

### 4c) 热电腿长度

> How long are the thermolegs and how thick is one ceramic substrate plate? Given: $\lambda_{\text{Bi}_2\text{Te}_3} = 2\ \text{W/K/m}$. Thermal resistance and thickness of electrical contacts and ceramic substrate are negligible.

Equation for thermal generator resistance 热阻方程：

$$l = 2 \cdot K_g \cdot A_{tb} \cdot \lambda$$

Rearranging for $l$ 求解 $l$：

$$l = 2.85\ \text{mm}$$

---

### 4d) Figure of merit ZT at T = 293 K

### 4d) 热电优值 ZT（T = 293 K）

$$ZT = \frac{\alpha_g^2}{R_g \cdot K_g} \cdot T$$

$$ZT = \frac{(51 \times 10^{-3})^2}{6.6 \times 5.6} \times 293 \approx 0.646$$

---

### System Design · 系统设计

> Additional data 补充数据：
> - Heat sink thermal resistance 散热器热阻: $K(v) = (20 - v \cdot 5\ \text{s/m})\ \text{K/W}$
> - Electrical load resistance 负载电阻: $R_L = 3\ \Omega$

---

### 4e) Feasibility at $v = 2.9\ \text{m/s}$

### 4e) 风速 2.9 m/s 下的可行性

> Can the TEG be used for maximum power at $v = 2.9\ \text{m/s}$? Justify.

$$K(2.9) = (20 - 2.9 \times 5)\ \text{K/W} = 5.5\ \text{K/W}$$

- **Thermal** 热匹配：Heat sink $K = 5.5\ \text{K/W}$ is nearly optimally matched to TEG $K_g = 5.6\ \text{K/W}$. ✅
- **Electrical** 电匹配：TEG resistance $R_g = 6.6\ \Omega$ is nearly **double** the load $R_L = 3\ \Omega$. ❌

**Conclusion 结论**：Optimal power **cannot** be achieved because the electrical resistance is mismatched. 无法获得最优功率，因为电阻不匹配。

---

### 4f) General matching principle

### 4f) 一般匹配原则

> How should the electrical and thermal resistances of the TEG be chosen in general, and specifically for $v = 2\ \text{m/s}$?

**General principle 一般原则**：Electrical and thermal resistances of the TEG should **match** the electrical load and heat sink thermal resistance respectively (i.e., be identical).

**Specific case at $v = 2\ \text{m/s}$**：
- $K(v=2) = (20 - 2 \times 5) = 10\ \text{K/W}$
- Target thermal resistance: $K_g = 10\ \text{K/W}$
- Target load resistance: $R_L = R_G = 5.6\ \Omega$

---

### 4g) Electrical power and energy for $\Delta T = 10\ \text{K}$

### 4g) $\Delta T = 10\ \text{K}$ 时的电功率和能量

> Calculate electrical power and voltage at the load for matched resistances from 4f), $\Delta T = 10\ \text{K}$, $\alpha_g = 30\ \text{mV/K}$. How much energy in one day?

$$P = (\alpha_g \cdot \Delta T)^2 \cdot \left(\frac{K_g}{K + K_g}\right)^2 \cdot \frac{R_L}{(R_G + R_L)^2}$$

$$P \approx 439\ \mu\text{W}$$

**Daily energy 日能量**：

$$E = P \cdot t = 439 \times 10^{-6} \times 3600 \times 24 \approx 109.7\ \text{J}$$

---

### 4h) Typical consumer at 250 µW

### 4h) 250 µW 可驱动的典型设备

> Name a typical electrical consumer that can be operated with 250 µW (pulsed operation included if sensible).

**Low-energy radio module** (低功耗无线模块) — measurement every few seconds included (每隔几秒进行一次测量).

Other systems with higher consumption but less frequent operation are also possible, provided a suitable **intermediate storage** (中间储能) is available.

---

## Task 5: Thermomechanic Energy Harvester · 任务 5：热机械能量采集器

> **Principle**: Micro heat engine from University of California. A Gadolinium (Gd) block with Curie temperature $T_C = 18\ \text{°C}$ oscillates between a heat source (33 °C) and heat sink (2 °C). Below $T_C$, Gd is **ferromagnetic** and attracted to the heat source → contact → heats up → becomes **paramagnetic** → elastic force pulls it back to sink → cools → becomes ferromagnetic again → cycle repeats.
>
> **原理**：加州大学的微型热机。钆 (Gd) 块居里温度 $T_C = 18\ \text{°C}$，在热源 (33 °C) 和热沉 (2 °C) 之间振荡。低于 $T_C$ 时呈**铁磁性**被热源吸引→接触→升温→变为**顺磁性**→弹性力拉回热沉→冷却→再次铁磁性→循环往复。

**Given data 给定数据**：

| Parameter 参数 | Value 值 |
|---|---|
| Gap source–sink 源-沉间距 | $0.75\ \text{mm}$ |
| Source/Sink surface 源/沉表面积 | $75\ \text{mm}^2$ |
| Gd block thickness Gd 块厚度 | $0.3\ \text{mm}$ |
| Gd block cross-section Gd 块截面 | $9\ \text{mm}^2$ |
| Contact thermal resistance 接触热阻 $R_{kontakt}$ | $900\ \text{mm}^2\text{K/W}$ |
| Beams are perfect thermal insulators 梁为理想绝热体 |
| Source & sink: constant temperature 恒温 |

| Material 材料 | Air 空气 | Gd 钆 |
|---|---|---|
| Thermal conductivity $\lambda$ (W/mK) 导热率 | $0.025$ | $10.6$ |
| Specific heat capacity $c$ (J/kg/K) 比热容 | $1012$ | $56$ |
| Density $\rho$ (kg/m³) 密度 | $1.20$ | $1290$ |

---

### 5a) Equivalent circuit diagram

### 5a) 等效电路图

> Draw the equivalent circuit diagram and explain the important parts.

1. $R_{kontakt} = \frac{900}{9} = 100\ \text{K/W}$
2. $R_{Gd} = \frac{1}{10.6} \times \frac{0.3}{9 \times 10^{-6}} \times 10^3 = 3.14\ \text{K/W}$
3. $C_{Gd} = 0.3 \times 9 \times 10^{-9} \times 7900 \times 230 = 4.91 \times 10^{-3}\ \text{J/K}$
4. Air conduction losses neglected (Gd conductivity $\gg$ air) / 忽略空气导热损失
5. $T_{Quelle} = 33\ \text{°C}$ (heat source 热源)
6. $T_{Senke} = 2\ \text{°C}$ (heat sink 热沉)

---

### 5b) Operating frequency

### 5b) 工作频率

> Calculate the operating frequency of the generator.

$$\tau = \left(R_{kontakt} + \frac{R_{Gd}}{2}\right) \cdot C_{Gd} = 0.499\ \text{s}$$

- $T_{up} = 18\ \text{°C}$, $T_{down} = 17\ \text{°C}$
- $T_{Quelle} = 33\ \text{°C}$, $T_{Senke} = 2\ \text{°C}$

**Heating phase 加热阶段**：

$$T(t) = T_{down}\ e^{-t/\tau} + T_{Quelle}\ (1 - e^{-t/\tau})$$

$$t_{up} = -\tau \cdot \ln\left(\frac{T_{up} - T_{Quelle}}{T_{down} - T_{Quelle}}\right) = 0.032\ \text{s}$$

**Cooling phase 冷却阶段**：

$$T(t) = T_{up}\ e^{-t/\tau} + T_{Senke}\ (1 - e^{-t/\tau})$$

$$t_{down} = -\tau \cdot \ln\left(\frac{T_{down} - T_{Senke}}{T_{up} - T_{Senke}}\right) = 0.032\ \text{s}$$

$$t_{total} = t_{up} + t_{down} = 0.064\ \text{s}$$

$$f = \frac{1}{t_{total}} = \frac{1}{0.064} \approx 15.53\ \text{Hz}$$

---

### 5c) Heat transferred to sink

### 5c) 传递到热沉的热量

> Calculate the heat transferred from the Gd block to the heat sink (air conduction losses neglected).

$$Q = C_{Gd} \cdot (T_{up} - T_{down}) \cdot f = 4.91 \times 10^{-3} \cdot (18 - 17) \cdot 15.53 = 76.25\ \text{mW}$$

---

### 5d) System efficiency

### 5d) 系统效率

> Calculate the efficiency if mechanical output power (due to periodic beam bending) is 3 mW.

$$\eta = \frac{P_{mech}}{P_{therm}} = \frac{3\ \text{mW}}{76.25\ \text{mW}} \approx 3.93\%$$

---

## Task 6: Energy Management · 任务 6：能量管理

### 6a) Two electrical energy storage methods

### 6a) 两种电能存储方式

> Name two different electrical energy storage possibilities in energy harvesting.

| Storage 存储方式 | Description 描述 |
|---|---|
| **Capacitor** 电容器 | Short-term storage / 短期存储 |
| **Battery / Accumulator** 电池/蓄电池 | Long-term storage / 长期存储 |
| **Inductor (Coil)** 电感（线圈） | — |

---

### 6b) Capacitor vs. Battery as intermediate storage

### 6b) 电容器 vs. 电池作为中间存储

> When would one use a capacitor and when a battery as intermediate storage in energy harvesting?

| Storage 存储 | When to Use 适用场景 | Reason 原因 |
|---|---|---|
| **Capacitor** 电容器 | Short-term storage only 仅短期存储 | Potentially larger leakage currents (exception: Supercaps) / 可能存在较大漏电流（超级电容除外） |
| **Battery** 电池 | Long-term energy storage 长期能量存储 | Only if effective charging is possible / 仅在有效充电可行时使用 |

---

### 6c) Problem when feeding into batteries

### 6c) 向电池馈电的问题

> What is a problem when feeding electrical energy into currently available batteries?

Effective charging can be **prevented by minimum required charging currents** that may not be directly available from the generator. 发电机可能无法直接提供电池所需的**最小充电电流**，从而阻碍有效充电。

---

### 6d) Deep discharge of Li-Ion batteries

### 6d) 锂离子电池的深度放电

> What happens when a Li-Ion battery is deeply discharged? Can it be "regenerated" like a NiCd battery?

**No.** A deeply discharged Li-Ion battery is **physically destroyed** and cannot be regenerated (unlike NiCd batteries).

**不能。** 深度放电的锂离子电池会**物理性损坏**，无法像镍镉电池那样"再生"。

---

### 6e) Faraday efficiency

### 6e) 法拉第效率

> Calculate the Faraday efficiency of a battery.

(Refer to formulary — assume typical efficiency and capacity values. / 参见公式表 — 假定额定效率和容量值。)

---

### 6f) Large leakage currents in power management

### 6f) 电源管理中的大漏电流

> Where do large leakage currents occur in the electrical part of power management and how can they be reduced?

| Location 位置 | Mitigation 缓解措施 |
|---|---|
| **Storage elements** 存储元件 | Select storage with low long-term self-discharge rate / 选用低自放电率的存储元件 |
| **Rectification** 整流环节 | Use **Schottky diodes** instead of standard diodes depending on application / 根据应用需求使用**肖特基二极管**替代普通二极管 |

---

### 6g) Block diagram of complete energy harvesting system

### 6g) 完整能量采集系统框图

> Draw a sketch of a complete energy harvesting system as a block diagram. Briefly explain the individual functions.

**Block Chain 模块链**（参见课程导论幻灯片）：

| Block 模块 | Function 功能 |
|---|---|
| **Generator** 发电机 | Converts ambient energy to electrical energy / 将环境能量转换为电能 |
| **Management** 管理电路 | Rectification, voltage regulation, MPPT / 整流、电压调节、最大功率点跟踪 |
| **Storage** 存储 | Intermediate energy buffering / 中间能量缓冲 |
| **Measurement / Sensing** 测量/传感 | Data acquisition / 数据采集 |
| **Wireless Transmission** 无线传输 | Data transmission / 数据传输 |

---

## Task 7: Evaluation (Bonus) · 任务 7：评价（加分题）

> Please evaluate the currently available energy harvesting technologies and briefly justify which system you see as closest to market maturity.

**自由论述题** — 请根据课程所学知识，评价当前可用的能量采集技术，并简要论述你认为哪种系统最接近市场成熟度。

> *(This is an open-ended evaluation question — the instructor only wants to read your personal assessment.)*  
> *(此为开放性评价题 — 教师仅希望了解你的个人判断。)*

---

## Summary Table · 总结表

| Task 任务 | Topic 主题 | Key Takeaway 核心要点 |
|---|---|---|
| 1 | Harmonic Oscillator 谐振子 | Damped oscillator equation, Q-factor, resonance, damping cases |
| 2 | Vibration Harvester 振动采集器 | Piezo/electrostatic/electrodynamic types, power 100–500 µW typical |
| 4 | TEG 热电发电机 | ZT = 0.646, impedance matching, ~439 µW at ΔT = 10 K |
| 5 | Thermomechanic Harvester 热机械采集器 | Gd Curie-temperature switching, f ≈ 15.5 Hz, η ≈ 3.93% |
| 6 | Energy Management 能量管理 | Capacitor vs. battery, Schottky diodes, Li-Ion deep-discharge destruction |

> **Note**: Task 3 is not present in the original PDF document.  
> **注**：原始 PDF 中未包含任务 3。