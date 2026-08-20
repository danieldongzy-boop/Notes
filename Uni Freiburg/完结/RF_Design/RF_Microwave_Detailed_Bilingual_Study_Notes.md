# RF & Microwave Devices and Circuits — 详细公式学习笔记 (Detailed Formula Study Notes)

> **来源 (Source):** `Skripte_Vorlesung-01bis12.pdf`, 496 pages  
> **授课 (Lecturer):** Prof. Dr. Rüdiger Quay / Dr.-Ing. Bersant Gashi  
> **学校 (University):** INATECH Universität Freiburg, Version 17.2  
> **课程 (Course):** RF and Microwave Devices and Circuits  
> **考试 (Exam):** 01.09.2026, Written 90 min, No Aid  
> **语言 (Language):** 中英双语 (Bilingual CN/EN)

---

# 目录 Table of Contents

1. [第一章：Maxwell 方程组与电磁场基础](#ch1)
2. [第二章：自由空间中的波动方程](#ch2)
3. [第三章：坡印廷矢量与电磁能量](#ch3)
4. [第四章：介质中的波传播与电介质](#ch4)
5. [第五章：导波传播与传输线理论](#ch5)
6. [第六章：反射系数与史密斯圆图](#ch6)
7. [第七章：S 参数与多端口网络](#ch7)
8. [第八章：Z / Y / h 参数体系](#ch8)
9. [第九章：波导结构与传输媒介](#ch9)
10. [第十章：微带线与真实无源结构](#ch10)
11. [第十一章：匹配理论与阻抗变换](#ch11)
12. [第十二章：四分之一波长变换与短截线](#ch12)
13. [第十三章：功分器、合成器与耦合器](#ch13)
14. [第十四章：损耗机制全面分析](#ch14)
15. [第十五章：趋肤效应与表面粗糙度](#ch15)
16. [第十六章：天线原理与特性参数](#ch16)
17. [第十七章：阵列天线与 MIMO](#ch17)
18. [第七讲：RF 半导体与有源器件基础](#lec7)
19. [第八讲：RF 半导体制造工艺](#lec8)
20. [第九讲：载流子输运、结与场效应晶体管](#lec9)
21. [第十讲：双极晶体管与 RF 功率半导体](#lec10)
22. [第十一讲：RF 增益、稳定性与放大器基础](#lec11)
23. [第十二讲：功率放大器、接收电路与 RF 系统](#lec12)
24. [Lectures 7-12 公式速查与易错点](#lec7-12-summary)
25. [附录：常数表、频段划分、单位换算](#appendix)

---

<h1 id="ch1">第一章：Maxwell 方程组与电磁场基础</h1>
<h2>Chapter 1: Maxwell's Equations and Electromagnetic Fundamentals</h2>

Maxwell 方程组是所有 RF 与微波分析的起点。本节详细展开四个方程的物理意义、推导脉络、以及本构关系的应用背景。
*Maxwell's Equations are the starting point for all RF and microwave analysis. This section details the physical meaning, derivation context, and application of constitutive relations.*

---

### 1.1 微分形式 Maxwell 方程组 (Differential Form)

在时变场的一般介质中，Maxwell 方程组写作：
*In general time-varying media, Maxwell's equations in differential form are:*

#### 高斯电场定律 (Gauss's Law – Electric)

$$
\boxed{\nabla \cdot \vec{D} = \rho}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 电位移矢量 $\vec{D}$ 的散度等于该点的自由电荷密度 $\rho$。电场从正电荷发出，终止于负电荷。*The divergence of electric displacement equals free charge density; E-field originates from positive and terminates on negative charges.* |
| **推导要点** Derivation | 由库仑定律与叠加原理积分得到，再通过散度定理转化为微分形式。*Derived from Coulomb's law + superposition, converted to differential form via divergence theorem.* |
| **参数** Parameters | $\vec{D}$: 电位移矢量 Electric displacement [C/m²]；$\rho$: 自由电荷体密度 Volume free charge density [C/m³] |
| **应用场景** Application | 静电学、半导体器件中空间电荷区的电场分布；RF 电路中电容器的场分析。*Electrostatics, space-charge region in semiconductors, capacitor field analysis in RF circuits.* |

#### 高斯磁定律 (Gauss's Law – Magnetic)

$$
\boxed{\nabla \cdot \vec{B} = 0}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 磁感应强度 $\vec{B}$ 的散度恒为零——不存在磁单极子（magnetic monopole）。磁场线总是闭合的。*Divergence of magnetic flux density is always zero — no magnetic monopoles exist; B-field lines are always closed loops.* |
| **推导要点** Derivation | 由 Biot-Savart 定律推导，$\nabla \cdot (\nabla \times \vec{A}) = 0$ 恒成立。*From Biot-Savart law; identity $\nabla \cdot (\nabla \times \vec{A}) = 0$ holds universally.* |
| **参数** Parameters | $\vec{B}$: 磁感应强度 / 磁通密度 Magnetic flux density [T 或 Wb/m²] |
| **应用场景** Application | 确保所有磁路分析和电磁仿真的解必须满足无散条件。*Ensures all magnetic circuit analysis and EM simulations satisfy the divergence-free condition.* |

#### 法拉第电磁感应定律 (Faraday's Law)

$$
\boxed{\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 随时间变化的磁场 $\vec{B}$ 产生旋转电场 $\vec{E}$。负号表示感应电场的方向符合楞次定律——感应电流的磁场总是阻碍原磁通的变化。*A time-varying magnetic field induces a circulating electric field. The minus sign reflects Lenz's Law — induced current's field opposes the change in flux.* |
| **推导要点** Derivation | 由实验 $\mathcal{E} = -\frac{d\Phi_B}{dt}$ 出发，利用斯托克斯定理 $\oint \vec{E}\cdot d\vec{l} = \int(\nabla\times\vec{E})\cdot d\vec{S}$ 得到微分形式。*From experimental law $\mathcal{E} = -d\Phi_B/dt$, using Stokes' theorem to derive differential form.* |
| **参数** Parameters | $\vec{E}$: 电场强度 Electric field intensity [V/m]；$\vec{B}$: 磁通密度 [T]；$\frac{\partial}{\partial t}$: 时间偏导 |
| **应用场景** Application | 变压器原理、电感耦合、环形天线接收、涡流检测、RFID 近场通信。*Transformer principle, inductive coupling, loop antenna reception, eddy current testing, RFID near-field communication.* |
| **典型数值** Typical Values | 在 1 GHz 的微波电路中，$\partial B/\partial t$ 项远大于直流情况，使感应效应不可忽略。*At 1 GHz microwave circuits, $\partial B/\partial t$ term is far larger than DC, making inductive effects non-negligible.* |

#### 安培-麦克斯韦定律 (Ampère–Maxwell Law)

$$
\boxed{\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 磁场 $\vec{H}$ 的旋度由两个源产生：(1) 传导电流密度 $\vec{J}$；(2) 位移电流密度 $\partial\vec{D}/\partial t$。位移电流是麦克斯韦的创造性贡献，它预言了电磁波的存在。*The curl of H-field has two sources: conduction current J and displacement current ∂D/∂t. Displacement current is Maxwell's creative contribution — it predicted electromagnetic waves.* |
| **推导要点** Derivation | 安培原定律 $\nabla\times\vec{H} = \vec{J}$ 在时变场中违反连续性方程 $\nabla\cdot\vec{J} = -\partial\rho/\partial t$，麦克斯韦加 $\partial\vec{D}/\partial t$ 后满足 $\nabla\cdot(\nabla\times\vec{H})=0$。*Original Ampere's law violated continuity; adding ∂D/∂t restores consistency.* |
| **参数** Parameters | $\vec{H}$: 磁场强度 Magnetic field intensity [A/m]；$\vec{J}$: 传导电流密度 Conduction current density [A/m²]；$\partial\vec{D}/\partial t$: 位移电流密度 Displacement current density [A/m²] |
| **应用场景** Application | 电容器中的交流电流连续性（极板间无传导电流但位移电流维持回路）；电磁波在真空中的传播；MMIC 中 MIM 电容的 RF 建模。*AC current continuity in capacitors (no conduction current between plates but displacement current closes loop); EM wave propagation in vacuum; MIM capacitor RF modeling in MMIC.* |

---

### 1.2 本构关系 (Constitutive Relations)

在均匀、各向同性（homogeneous, isotropic）介质中：
*In homogeneous, isotropic media:*

$$
\boxed{\vec{D} = \varepsilon_0 \varepsilon_r \vec{E} = \varepsilon \vec{E}}
\quad\quad
\boxed{\vec{B} = \mu_0 \mu_r \vec{H} = \mu \vec{H}}
\quad\quad
\boxed{\vec{J} = \sigma \vec{E}}
$$

| 参数 Parameter | 符号 Symbol | 数值 / 说明 Value / Description |
|---|---|---|
| 真空介电常数 Vacuum permittivity | $\varepsilon_0$ | $8.854 \times 10^{-12}$ F/m |
| 相对介电常数 Relative permittivity | $\varepsilon_r$ | 无量纲 dimensionless；空气≈1，GaAs≈12.9，FR4≈4.4，水≈80 |
| 真空磁导率 Vacuum permeability | $\mu_0$ | $4\pi \times 10^{-7} \approx 1.257 \times 10^{-6}$ H/m |
| 相对磁导率 Relative permeability | $\mu_r$ | 无量纲；非磁性材料≈1，铁氧体可 >1000 |
| 电导率 Conductivity | $\sigma$ | S/m；铜≈$5.8\times 10^7$，海水≈4，硅（本征）≈$4\times 10^{-4}$ |

**物理意义总结 (Physical Meaning Summary):**
- $\varepsilon$ 描述介质对电场的极化响应能力。高 $\varepsilon_r$ 意味着材料中电场被"削弱"（$\vec{E}$ 同 $\vec{D}$ 下的 $\vec{E}$ 更小），波的传播速度减慢。
  *$\varepsilon$ describes how a medium polarizes under E-field. High $\varepsilon_r$ means field is weakened, wave slows down.*
- $\mu$ 描述介质对磁场的磁化响应。大多数 RF 材料 $\mu_r \approx 1$。
  *$\mu$ describes magnetic response. Most RF materials have $\mu_r \approx 1$.*
- $\sigma$ 描述介质传导电流的能力。$\sigma=0$ 为理想介质（无损耗），$\sigma\to\infty$ 为理想导体。
  *$\sigma$ describes conduction capability. $\sigma=0$ is perfect dielectric (lossless), $\sigma\to\infty$ is perfect conductor.*

---

### 1.3 矢量算子补充 (Vector Operator Supplement)

纳布拉算子 $\nabla$ 的三种用法：
*The three uses of the Nabla operator $\nabla$:*

| 算子 Operator | 定义 Definition | 作用结果 Result | 比喻 Analogy |
|---|---|---|---|
| 梯度 Gradient $\nabla\phi$ | $\left(\frac{\partial\phi}{\partial x}, \frac{\partial\phi}{\partial y}, \frac{\partial\phi}{\partial z}\right)$ | 矢量，指向标量场增长最快的方向 Vector, points to direction of steepest increase of scalar field | 山坡的坡度方向 Direction of steepest slope |
| 散度 Divergence $\nabla\cdot\vec{A}$ | $\frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$ | 标量，描述该点是否为"源"（正值）/ "汇"（负值） Scalar, measures source (+) or sink (-) strength | 水龙头出水量 Rate of water outflow |
| 旋度 Curl $\nabla\times\vec{A}$ | 行列式 determinant $\begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \partial_x & \partial_y & \partial_z \\ A_x & A_y & A_z \end{vmatrix}$ | 矢量，描述局部旋转的轴方向与强度 Vector, describes axis and strength of local rotation | 漩涡的旋转方向和速度 Whirlpool rotation |

---

<h1 id="ch2">第二章：自由空间中的波动方程</h1>
<h2>Chapter 2: Wave Equation in Free Space</h2>

### 2.1 从 Maxwell 到波动方程 (From Maxwell to Wave Equation)

在无源真空中（$\rho=0, \vec{J}=0$），对法拉第定律取旋度：
*In source-free vacuum ($\rho=0, \vec{J}=0$), take curl of Faraday's law:*

$$
\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B})
$$

代入安培定律 $\nabla\times\vec{B} = \mu_0 \varepsilon_0 \frac{\partial\vec{E}}{\partial t}$，并使用矢量恒等式 $\nabla\times(\nabla\times\vec{E}) = \nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E}$，结合 $\nabla\cdot\vec{E}=0$（无自由电荷），得：
*Substituting Ampère's law and using vector identity, along with $\nabla\cdot\vec{E}=0$ (no free charge), we obtain:*

$$
\boxed{\nabla^2 \vec{E} - \mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2} = 0}
$$

同理对 $\vec{H}$：
*Similarly for $\vec{H}$:*

$$
\boxed{\nabla^2 \vec{H} - \mu_0 \varepsilon_0 \frac{\partial^2 \vec{H}}{\partial t^2} = 0}
$$

| 项目 Item                   | 说明 Explanation                                                                                                                                                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **物理含义** Physical Meaning | 电场 $\vec{E}$ 和磁场 $\vec{H}$ 各自满足标准的波动方程，形式为 $\nabla^2\psi - \frac{1}{v^2}\frac{\partial^2\psi}{\partial t^2}=0$。这表明电磁扰动以波的形式在空间中传播。*Both E and H satisfy standard wave equation; EM disturbances propagate as waves in space.* |
| **推导链** Derivation Chain  | Maxwell 方程组 → 取旋度 → 代入交叉耦合 → 消元 → 独立波动方程。*Maxwell → curl → substitute cross-coupling → eliminate → independent wave equations.*                                                                                               |
| **关键洞察** Key Insight      | 麦克斯韦在引入位移电流时就预言了电磁波——电场和磁场互相"生"对方，形成一个自持的传播过程。*Maxwell predicted EM waves upon adding displacement current: E and H mutually generate each other in a self-sustaining propagation.*                                           |

---

### 2.2 光速 (Speed of Light)

对比标准波动方程 $\nabla^2\psi - \frac{1}{v^2}\frac{\partial^2\psi}{\partial t^2}=0$，得：
*Comparing with standard wave equation:*

$$
\boxed{c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.998 \times 10^8 \; \text{m/s}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 电磁波在真空中的传播速度恒为 $c$，与频率无关（真空中无色散）。这是 Maxwell 最伟大的预言之一——光就是电磁波。*EM wave speed in vacuum equals c, independent of frequency (no dispersion). Maxwell's greatest prediction — light IS an electromagnetic wave.* |
| **历史意义** Historical | 麦克斯韦在 1865 年计算出的速度值与当时已知的光速测量值吻合，从而统一了光学与电磁学。*Maxwell's 1865 calculation matched measured speed of light, unifying optics and electromagnetism.* |
| **典型计算** Example | 使用 $\varepsilon_0=8.854\times10^{-12}$, $\mu_0=4\pi\times10^{-7}$：$c = 1/\sqrt{8.854\times10^{-12} \times 4\pi\times10^{-7}} \approx 2.998\times 10^8$ m/s。 |

---

### 2.3 时谐场解 (Time-Harmonic Solution)

对于沿 $+z$ 方向传播的时谐平面波：
*For a time-harmonic plane wave propagating in $+z$ direction:*

#### 实数表示 (Real Form):
$$
\vec{E}(z, t) = \vec{E}_0 \cos(\omega t - \beta z + \phi)
$$

#### 复数表示 (Complex / Phasor Form):
$$
\vec{E}(z, t) = \text{Re}\left\{ \vec{E}_0 \, e^{j(\omega t - \beta z)} \right\}
$$

其中通常将时间因子 $e^{j\omega t}$ 隐去，只保留空间部分 $\vec{E}_0 e^{-j\beta z}$，这称为**相量（phasor）**表示法。
*Usually the time factor $e^{j\omega t}$ is suppressed, leaving the spatial part — this is the **phasor** representation.*

| 参数 Parameter | 符号 Symbol | 公式 Formula | 单位 Unit |
|---|---|---|---|
| 角频率 Angular frequency | $\omega$ | $\omega = 2\pi f$ | rad/s |
| 频率 Frequency | $f$ | $f = \frac{\omega}{2\pi}$ | Hz |
| 相位常数 Phase constant | $\beta$ | $\beta = \frac{2\pi}{\lambda}$ | rad/m |
| 波长 Wavelength | $\lambda$ | $\lambda = \frac{c}{f} = \frac{2\pi}{\beta}$ | m |
| 周期 Period | $T$ | $T = \frac{1}{f} = \frac{2\pi}{\omega}$ | s |

**数值感 (Numerical Sense):**

| 频率 Frequency | 波长 Wavelength $\lambda_0$ (真空中 in vacuum) |
|---|---|
| 1 MHz | 300 m |
| 100 MHz | 3 m |
| 1 GHz | 30 cm |
| 10 GHz | 3 cm |
| 100 GHz | 3 mm |
| 400 GHz | 0.75 mm |

**重要概念——波长与电路尺寸 (Key Concept — Wavelength vs. Circuit Size):**
- 当电路尺寸 $l \ll \lambda$ 时（$l < \lambda/10$），可以用**集总参数**元件（lumped elements：R/L/C）建模。
  *When circuit size $l \ll \lambda$ ($l < \lambda/10$), use lumped element models (R/L/C).*
- 当 $l \gtrsim \lambda/10$ 时，必须使用**分布参数**模型（distributed model），波的性质占主导。
  *When $l \gtrsim \lambda/10$, must use distributed models — wave behavior dominates.*
- 例如 10 GHz 时 $\lambda=3$ cm，所以几毫米的微带线段就必须用传输线理论处理。
  *At 10 GHz, $\lambda=3$ cm, so mm-scale microstrip sections already require transmission line treatment.*

---

<h1 id="ch3">第三章：坡印廷矢量与电磁能量</h1>
<h2>Chapter 3: Poynting Vector and Electromagnetic Energy</h2>

### 3.1 瞬时坡印廷矢量 (Instantaneous Poynting Vector)

$$
\boxed{\vec{S}(t) = \vec{E}(t) \times \vec{H}(t)} \quad [\text{W/m}^2]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | $\vec{S}$ 的大小表示穿过单位面积的瞬时功率流，方向表示能量传播方向。满足右手定则：$\vec{E}$ × $\vec{H}$ → $\vec{S}$。*The magnitude of $\vec{S}$ is instantaneous power per unit area; direction is energy flow direction. Right-hand rule: $\vec{E}$ × $\vec{H}$ → $\vec{S}$.* |
| **推导要点** Derivation | 由 Maxwell 方程组出发，计算 $\nabla\cdot(\vec{E}\times\vec{H})$，结合电场能量密度 $\frac{1}{2}\varepsilon E^2$ 和磁场能量密度 $\frac{1}{2}\mu H^2$ 的变化率，导出坡印廷定理（Poynting theorem）。*From Maxwell's equations, compute $\nabla\cdot(\vec{E}\times\vec{H})$, combine with time derivatives of energy densities.* |
| **应用场景** Application | 天线辐射方向图计算（远场 $\vec{S}$ 空间分布）；PCB 走线的功率流分布可视化；电磁兼容（EMC）近场探测。*Antenna radiation pattern (far-field $\vec{S}$ distribution); PCB trace power flow visualization; EMC near-field probing.* |

### 3.2 时谐场中的时间平均坡印廷矢量 (Time-Averaged Poynting Vector)

对于时谐场（phasor 域），瞬时功率在一个周期内振荡，通常我们关心平均值：
*For time-harmonic fields, instantaneous power oscillates within a period — we typically care about the average:*

$$
\boxed{\vec{S}_{avg} = \frac{1}{2} \text{Re}\left\{ \vec{E} \times \vec{H}^* \right\}} \quad [\text{W/m}^2]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **因子 1/2** Factor 1/2 | 来自 $\cos^2$ 的时间平均 $\frac{1}{T}\int_0^T \cos^2(\omega t)dt = 1/2$。*From time average of $\cos^2$: $\frac{1}{T}\int_0^T \cos^2(\omega t)dt = 1/2$.* |
| **$\vec{H}^*$** | $\vec{H}$ 的复共轭。$\text{Re}\{\vec{E}\times\vec{H}^*\}$ 只取有功功率（resistive power）。虚部对应无功功率（reactive power, 来回振荡）。*Complex conjugate of $\vec{H}$. $\text{Re}\{\vec{E}\times\vec{H}^*\}$ gives active/real power only. Imaginary part corresponds to reactive power.* |
| **重要推论** Key Corollary | 对于 TEM 波：$H = E/\eta$，$\vec{E}\perp\vec{H}$，故 $|\vec{S}_{avg}| = \frac{1}{2}|E|^2/\eta = \frac{1}{2}|H|^2\eta$。*For TEM wave: $H = E/\eta$, $\vec{E}\perp\vec{H}$, so $|\vec{S}_{avg}| = \frac{1}{2}|E|^2/\eta = \frac{1}{2}|H|^2\eta$.* |

### 3.3 自由空间的特征阻抗 (Intrinsic Impedance of Free Space)

$$
\boxed{\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = \frac{|\vec{E}|}{|\vec{H}|} \approx 377 \, \Omega}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 真空中平面波的电场幅度与磁场幅度之比为常数 377 Ω。这不是"电路阻抗"而是介质的本征属性。*Ratio of E to H field amplitudes for plane wave in vacuum is constant 377 Ω. This is not "circuit impedance" but an intrinsic medium property.* |
| **类比** Analogy | 类似声学中的"声阻抗"$Z = \rho c$（介质密度 × 声速），电磁学中 $\eta = \sqrt{\mu/\varepsilon}$。*Analogous to acoustic impedance $Z = \rho c$; in EM $\eta = \sqrt{\mu/\varepsilon}$.* |
| **介质推广** General to Media | $\eta = \sqrt{\mu/\varepsilon} = \eta_0 \sqrt{\mu_r/\varepsilon_r}$。对于大多数 RF 基板材料 $\mu_r=1$，则 $\eta = \eta_0/\sqrt{\varepsilon_r}$。例如 FR4 ($\varepsilon_r=4.4$): $\eta \approx 377/\sqrt{4.4} \approx 180$ Ω。*For most RF substrates $\mu_r=1$, so $\eta = \eta_0/\sqrt{\varepsilon_r}$. E.g. FR4 ($\varepsilon_r=4.4$): $\eta \approx 180$ Ω.* |

---

<h1 id="ch4">第四章：介质中的波传播与电介质</h1>
<h2>Chapter 4: Wave Propagation in Media and Dielectrics</h2>

### 4.1 折射率 (Refractive Index)

$$
\boxed{n = \sqrt{\varepsilon_r \mu_r} \approx \sqrt{\varepsilon_r}} \quad (\text{对非磁性介质 for non-magnetic media, } \mu_r=1)
$$

| 项目 Item                   | 说明 Explanation                                                                                                                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **物理含义** Physical Meaning | 折射率描述光/电磁波在介质中的速度减慢程度：$v_p = c/n$。$n$ 越大，波走得越慢。*Refractive index describes how much slower light/EM waves travel in a medium: $v_p = c/n$. Higher n → slower wave.*                                      |
| **来源** Origin             | $\eta = \sqrt{\mu/\varepsilon} = \sqrt{\mu_0\mu_r/\varepsilon_0\varepsilon_r} = \eta_0 \sqrt{\mu_r/\varepsilon_r}$。非磁性材料中 $\eta=\eta_0/n$。*From intrinsic impedance; for non-magnetic: $\eta=\eta_0/n$.* |

### 4.2 介质中的波长 (Wavelength in a Medium)

$$
\boxed{\lambda = \frac{\lambda_0}{\sqrt{\varepsilon_{eff}}} = \frac{c}{f\sqrt{\varepsilon_{eff}}}}
$$

| 说明 Explanation                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 介质中的波长比真空中更短。例如 GaAs ($\varepsilon_r=12.9$) 中 10 GHz 的波长从 3 cm 缩短至 $3/\sqrt{12.9} \approx 0.83$ cm。这对 MMIC 设计至关重要——片上结构的物理尺寸直接由介质波长决定。*Wavelength is shorter in media. E.g. 10 GHz in GaAs: 3 cm → $3/\sqrt{12.9} \approx 0.83$ cm. Critical for MMIC design — on-chip structures are sized by medium wavelength.* |

### 4.3 有效介电常数 (Effective Permittivity) — 微带线

微带线（microstrip）的独特之处在于场一部分在介质基底中、一部分在空气中。因此引入**有效介电常数** $\varepsilon_{eff}$：
*Microstrip is unique — part of the field is in substrate, part in air. Hence the **effective permittivity**:*

$$
\boxed{\varepsilon_{eff} = 1 + q(\varepsilon_r - 1)}
$$

$$
\boxed{q = \frac{\varepsilon_{eff} - 1}{\varepsilon_r - 1}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **$q$ (填充因子 Fill Factor)** | 场在介质中的比例，$0<q<1$。$q \to 1$ 表示几乎所有场在介质中（极宽微带线）；$q \to 0.5$ 表示一半一半（极窄微带线）。*Fraction of field in dielectric. $q \to 1$: almost all field in dielectric (very wide line); $q \to 0.5$: about half-half (very narrow line).* |
| **物理含义** Physical Meaning | $\varepsilon_{eff}$ 是介于 1（空气）和 $\varepsilon_r$（纯介质）之间的一个等效值。波沿微带线传播时，"感受"到的介电常数就是这个中间值。*$\varepsilon_{eff}$ is an equivalent value between 1 (air) and $\varepsilon_r$ (pure dielectric). The wave "feels" this intermediate value as it propagates.* |
| **微带线近似公式** Approximate Formula | $\varepsilon_{eff} = \frac{\varepsilon_r+1}{2} + \frac{\varepsilon_r-1}{2} \cdot \frac{1}{\sqrt{1+12h/w}}$。当 $w/h \to 0$ (窄线): $\varepsilon_{eff} \to (\varepsilon_r+1)/2$。当 $w/h \to \infty$ (宽线): $\varepsilon_{eff} \to \varepsilon_r$。*As $w/h \to 0$ (narrow): $\varepsilon_{eff} \to (\varepsilon_r+1)/2$. As $w/h \to \infty$ (wide): $\varepsilon_{eff} \to \varepsilon_r$.* |
| **示例** Example (GaAs, $h=100$ µm, $w=10$ µm, $w/h=0.1$, $\varepsilon_r=13$) | $q=0.55$ → $\varepsilon_{eff} = 1 + 0.55(13-1) = 7.6$；线阻抗 $Z_{01} \approx 260$ Ω（场仿真结果）。若 $w/h=2$ 则 $q=0.7$ → $\varepsilon_{eff}=9.4$，$Z_{01} \approx 80$ Ω。*For $w/h=0.1$: $Z_{01}\approx 260$ Ω. For $w/h=2$: $Z_{01}\approx 80$ Ω.* |

### 4.4 斯奈尔定律与全内反射 (Snell's Law & Total Internal Reflection)

#### 斯奈尔折射定律 (Snell's Law of Refraction):
$$
\boxed{n_1 \sin \theta_1 = n_2 \sin \theta_2}
$$

#### 临界角 (Critical Angle):
$$
\boxed{\sin \theta_c = \frac{n_2}{n_1}} \quad (n_1 > n_2)
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 当波从光密介质 ($n_1$) 进入光疏介质 ($n_2$)，入射角 $\theta_1 > \theta_c$ 时发生全内反射（TIR），能量全部反射回 $n_1$ 中。*When wave enters from optically dense ($n_1$) to rare ($n_2$) medium and $\theta_1 > \theta_c$, total internal reflection occurs — all energy reflected.* |
| **在RF中的应用** RF Applications | 介质波导（dielectric waveguide）就是利用全内反射原理在无金属化的情况下导引电磁波——基片集成波导（SIW）是典型代表。*Dielectric waveguides use TIR to guide EM waves without metallization — Substrate Integrated Waveguide (SIW) is a prime example.* |

### 4.5 介质损耗正切 (Loss Tangent)

复杂情况下，介质的介电常数为复数：
*In lossy cases, permittivity is complex:*

$$
\varepsilon = \varepsilon' - j\varepsilon'' = \varepsilon_0\varepsilon_r(1 - j\tan\delta)
$$

$$
\boxed{\tan \delta = \frac{\varepsilon''}{\varepsilon'}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | $\tan\delta$ 量化了介质将电磁能转化为热能的比率。$\tan\delta \ll 1$ 为低损耗介质，$\tan\delta \to 0$ 为理想介质。*$\tan\delta$ quantifies dielectric's conversion of EM energy to heat. Low value = low loss.* |
| **典型值** Typical Values | Teflon (PTFE): ~0.0002；FR4: ~0.02；GaAs (半绝缘): ~0.0006；硅 (高阻): ~0.005。*PTFE: ~0.0002; FR4: ~0.02; GaAs (SI): ~0.0006; Si (HR): ~0.005.* |

---

<h1 id="ch5">第五章：导波传播与传输线理论</h1>
<h2>Chapter 5: Guided Wave Propagation and Transmission Line Theory</h2>

### 5.1 自由传播 vs. 导波传播 (Free vs. Guided Propagation)

| 传播方式 Mode | 特征 Characteristic |
|---|---|
| **自由传播** Free Propagation | 产生 TEM 波（横电磁波）：$\vec{E}$ 和 $\vec{H}$ 均垂直于传播方向。如：自由空间中的平面波。*Produces TEM waves: both $\vec{E}$ and $\vec{H}$ perpendicular to propagation direction. E.g. plane wave in free space.* |
| **沿导体传播** Guided Propagation | 沿导体传播时引入了纵向（沿传播方向）的场分量。这不是纯 TEM 模式，需要传输线理论。*Introduces longitudinal field components along conductors. Not pure TEM; needs transmission line theory.* |

### 5.2 分布参数模型 (Distributed / Lumped Element Model)

传输线（transmission line）用单位长度的四个分布参数建模：
*A transmission line is modeled by four per-unit-length distributed parameters:*

| 参数 Parameter | 符号 Symbol | 单位 Unit | 物理含义 Physical Meaning |
|---|---|---|---|
| 单位长度电阻 Resistance per unit length | $R'$ | Ω/m | 导体欧姆损耗 Conductor ohmic loss |
| 单位长度电感 Inductance per unit length | $L'$ | H/m | 导体的磁能存储 Magnetic energy storage of conductors |
| 单位长度电导 Conductance per unit length | $G'$ | S/m | 介质漏电损耗 Dielectric leakage loss (substrate conductivity) |
| 单位长度电容 Capacitance per unit length | $C'$ | F/m | 导体间的电能存储 Electric energy storage between conductors |

**为何需要分布参数？(Why Distributed Model?)**
- 集总参数假设：元件尺寸 $\ll \lambda$，电压电流在空间上不变。*Lumped: component size $\ll \lambda$, V and I are spatially uniform.*
- 当 $l \gtrsim \lambda/10$ 时，传输线各点的电压电流都不同，必须用分布参数。*When $l \gtrsim \lambda/10$, V and I vary along the line — distributed model required.*

### 5.3 电报方程 (Telegrapher's Equations)

对长度为 $dz$ 的传输线微分段应用基尔霍夫定律：
*Applying Kirchhoff's laws to a differential segment $dz$:*

$$
\boxed{\frac{\partial v(z,t)}{\partial z} = -R'\, i(z,t) - L'\, \frac{\partial i(z,t)}{\partial t}}
$$

$$
\boxed{\frac{\partial i(z,t)}{\partial z} = -G'\, v(z,t) - C'\, \frac{\partial v(z,t)}{\partial t}}
$$

对**无损耗线（lossless line）**$R'=G'=0$：
*For lossless line:*

$$
\frac{\partial v}{\partial z} = -L' \frac{\partial i}{\partial t}, \quad \frac{\partial i}{\partial z} = -C' \frac{\partial v}{\partial t}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理图像** Physical Picture | 电压沿线的减小是因为串联阻抗上的压降（$R$+$L$）；电流沿线的减小是因为并联导纳的分流（$G$+$C$）。*V decreases along line due to series impedance drop; I decreases due to shunt admittance leakage.* |
| **历史背景** Historical | "Telegrapher's Equations" 的名称源于 19 世纪横跨大西洋的电报电缆分析——这是第一个真正需要分布参数模型的工程问题。*Named after 19th-century transatlantic telegraph cable analysis — the first engineering problem requiring distributed models.* |

### 5.4 传播常数 (Propagation Constant)

在频域中，电压和电流的解形式为 $V(z) = V^+ e^{-\gamma z} + V^- e^{+\gamma z}$，其中：
*In frequency domain, solutions are $V(z) = V^+ e^{-\gamma z} + V^- e^{+\gamma z}$, where:*

$$
\boxed{\gamma = \alpha + j\beta = \sqrt{(R' + j\omega L')(G' + j\omega C')}} \quad [\text{1/m}]
$$

| 参数 Parameter | 含义 Meaning                | 单位 Unit |
| ------------ | ------------------------- | ------- |
| $\gamma$     | 传播常数 Propagation constant | 1/m     |
| $\alpha$     | 衰减常数 Attenuation constant | Np/m    |
| $\beta$      | 相位常数 Phase constant       | rad/m   |

**无损耗线特例 (Lossless Line Special Case) $R'=G'=0$:**
$$
\gamma = j\beta = j\omega\sqrt{L'C'}, \quad \alpha = 0
$$
此时波在传播过程中幅度不衰减，只有相位变化。*Wave amplitude doesn't decay, only phase changes.*

**低损耗近似 (Low-Loss Approximation)** — 当 $R' \ll \omega L'$ 且 $G' \ll \omega C'$ 时：
$$
\alpha \approx \frac{R'}{2Z_0} + \frac{G'Z_0}{2}, \quad \beta \approx \omega\sqrt{L'C'}
$$

### 5.5 特性阻抗 (Characteristic Impedance)

$$
\boxed{Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}}} \quad [\Omega]
$$

**无损耗线特例 (Lossless):**
$$
\boxed{Z_0 = \sqrt{\frac{L'}{C'}}} \quad [\Omega]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 特性阻抗是传输线本身的"内在"属性，不是可以测量的集中电阻。它等于前行波电压与前行波电流的比值：$Z_0 = V^+/I^+$。*Intrinsic property of the line, not a lumped resistor. It equals the ratio of forward wave voltage to current.* |
| **在RF中的标准值** Standard RF Values | 绝大多数 RF 同轴线和微带线设计为 $Z_0 = 50$ Ω。有线电视系统用 75 Ω。100 Ω 差分对用于高速数字。*Most RF coax and microstrip: $Z_0=50$ Ω. CATV: 75 Ω. 100 Ω differential for high-speed digital.* |
| **典型微带线 $Z_0$** Typical Microstrip $Z_0$ | GaAs ($\varepsilon_r=13$, $w/h=0.1$, $q=0.55$): $Z_{01} \approx 260$ Ω。GaAs ($w/h=2$, $q=0.7$): $Z_{01} \approx 80$ Ω。通过 Hammerstad 公式可精确计算。*GaAs thin line: ~260 Ω; wider line: ~80 Ω. Exact values via Hammerstad formula.* |

### 5.6 相速度与导波长 (Phase Velocity and Guided Wavelength)

$$
\boxed{v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{L'C'}} = \frac{c}{\sqrt{\varepsilon_{eff}}}} \quad [\text{m/s}]
$$

$$
\boxed{\lambda_g = \frac{2\pi}{\beta} = \frac{v_p}{f} = \frac{\lambda_0}{\sqrt{\varepsilon_{eff}}}} \quad [\text{m}]
$$

| 项目 Item                      | 说明 Explanation                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **物理含义** Physical Meaning    | $v_p$ 是恒定相位点的移动速度。$\lambda_g$ 是波在传输线中的实际空间周期。两者都由 $\varepsilon_{eff}$ 和 $f$ 决定。*$v_p$ is speed of constant-phase point. $\lambda_g$ is actual spatial period on the line. Both determined by $\varepsilon_{eff}$ and $f$.*           |
| **设计意义** Design Significance | 微带线设计中使用 $\lambda_g$ 而非 $\lambda_0$！例如一个 $\lambda_g/4$ 变换器在 GaAs 基板上远短于真空中的 $\lambda_0/4$。*Use $\lambda_g$ not $\lambda_0$ for microstrip design! A $\lambda_g/4$ transformer on GaAs is much shorter than $\lambda_0/4$ in vacuum.* |

### 5.7 通解 (General Voltage/Current Solution)

$$
A(x, \omega) = A_0 \cdot e^{-\gamma x} \cdot e^{j\omega t}
$$

分离前行与反向波：
*Separating forward and backward waves:*

$$
V(z) = V^+ e^{-\gamma z} + V^- e^{+\gamma z}
$$
$$
I(z) = \frac{1}{Z_0}\left(V^+ e^{-\gamma z} - V^- e^{+\gamma z}\right)
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **$V^+ e^{-\gamma z}$** | 沿 +z 方向传播的前行波，幅度随距离以 $e^{-\alpha z}$ 衰减。*Forward wave in +z direction, amplitude decays as $e^{-\alpha z}$.* |
| **$V^- e^{+\gamma z}$** | 沿 -z 方向传播的反向波（由负载失配引起的反射）。*Backward wave in -z direction (reflection due to load mismatch).* |
| **电流中的负号** Minus Sign in Current | 反向波电流与反向波电压方向相反（相对于 +z 方向），故减号。*Backward current opposes backward voltage relative to +z, hence the minus sign.* |

---

<h1 id="ch6">第六章：反射系数与史密斯圆图</h1>
<h2>Chapter 6: Reflection Coefficient and Smith Chart</h2>

### 6.1 电压反射系数 (Voltage Reflection Coefficient)

$$
\boxed{\Gamma = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | $\Gamma$ 是一个复数，$|\Gamma|$ 表示反射电压波幅度与前向电压波幅度之比（0→1）。$\angle\Gamma$ 表示反射波的相位移动。*A complex number; $|\Gamma|$ is ratio of reflected to forward wave amplitude (0→1). $\angle\Gamma$ is phase shift of reflected wave.* |
| **推导** Derivation | 在负载 $z=0$ 处：$V(0) = V^+ + V^- = Z_L I(0)$ 且 $I(0) = (V^+ - V^-)/Z_0$。消去 $I(0)$ 解得。*At load: $V(0)=V^++V^-=Z_L I(0)$ and $I(0)=(V^+-V^-)/Z_0$. Solve for $\Gamma$.* |
| **极端情况** Extreme Cases | $Z_L \to \infty$ (开路 Open): $\Gamma=+1$，全反射、同相。$Z_L=0$ (短路 Short): $\Gamma=-1$，全反射、180° 反相。$Z_L=Z_0$ (匹配 Matched): $\Gamma=0$，零反射。*Open: $\Gamma=+1$, total reflection in phase. Short: $\Gamma=-1$, 180° out of phase. Matched: $\Gamma=0$, no reflection.* |

### 6.2 归一化阻抗形式 (Normalized Impedance Form)

令 $z_L = Z_L / Z_0$：
*Let $z_L = Z_L / Z_0$:*

$$
\boxed{\Gamma = \frac{z_L - 1}{z_L + 1}}
$$

$$
\boxed{z_L = \frac{1 + \Gamma}{1 - \Gamma}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **为什么归一化？** Why Normalize? | 归一化使所有阻抗相对于系统阻抗 $Z_0$ (通常 50 Ω) 表达，消除了绝对值，让史密斯圆图成为通用工具。*Normalization expresses all impedances relative to system $Z_0$ (typically 50 Ω), making the Smith Chart universally applicable.* |
| **映射关系** Mapping | $z$ 复平面右半平面（$\text{Re}\{z\}>0$，即所有无源阻抗）被映射到 $\Gamma$ 复平面的单位圆内部（$|\Gamma|\le 1$）。这是共形映射（conformal mapping），保角。*Right-half z-plane (all passive impedances) maps to interior of unit circle in $\Gamma$-plane — a conformal (angle-preserving) mapping.* |

### 6.3 电压驻波比 (VSWR — Voltage Standing Wave Ratio)

$$
\boxed{\text{VSWR} = \frac{V_{max}}{V_{min}} = \frac{1 + |\Gamma|}{1 - |\Gamma|}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 传输线上由于前向波与反射波干涉形成的驻波模式中，最大电压与最小电压之比。纯行波：VSWR=1（完美匹配）；纯驻波：VSWR→∞（全反射）。*Ratio of max to min voltage in standing wave pattern. Pure traveling wave: VSWR=1 (perfect match). Pure standing wave: VSWR→∞ (total reflection).* |
| **取值范围** Range | $1 \le \text{VSWR} < \infty$。工程中通常要求 VSWR < 2 (即 $|\Gamma| < 0.33$)，对应回波损耗 > 9.5 dB。*Typically VSWR < 2 ($|\Gamma| < 0.33$, return loss > 9.5 dB).* |

### 6.4 回波损耗 (Return Loss)

$$
\boxed{\text{RL} = -20 \log_{10} |\Gamma|} \quad [\text{dB}]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **为什么是负号？** Why Minus? | 回波损耗定义为正值（"损耗"多大），而 $|\Gamma|\le 1$ → $20\log_{10}|\Gamma| \le 0$ → 加负号得正值。*Defined as positive value representing "how much loss". Since $|\Gamma|\le 1$, $20\log_{10}|\Gamma|\le 0$, the minus sign makes it positive.* |
| **典型值** Typical | −10 dB 回波损耗意味着 $|\Gamma|=0.316$，约 10% 功率被反射，VSWR≈1.92。−20 dB 回波损耗 ≈ $|\Gamma|=0.1$，1% 反射。天线通常要求 < −10 dB。*-10 dB RL → $|\Gamma|=0.316$, ~10% power reflected. -20 dB → $|\Gamma|=0.1$, 1% reflected. Antennas typically require < -10 dB.* |

### 6.5 传送到负载的功率 (Power Delivered to Load)

$$
P_L = P_{inc} - P_{ref} = P_{inc}(1 - |\Gamma|^2)
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **匹配效率** Matching Efficiency | 效率因子 $1-|\Gamma|^2$ 表示前向功率中真正被负载吸收的比例。即使 $|\Gamma|=0.1$，也有 $1-0.01 = 99\%$ 被吸收。*Efficiency factor $1-|\Gamma|^2$ is fraction of forward power absorbed by load. Even $|\Gamma|=0.1$, $1-0.01=99\%$ absorbed.* |

### 6.6 史密斯圆图概论 (Smith Chart Overview)

史密斯圆图是 $\Gamma$ 复平面单位圆上的归一化阻抗/导纳网格图。
*The Smith Chart is a normalized impedance/admittance grid on the unit circle of the $\Gamma$-plane.*

| 关键操作 Key Operation | 史密斯圆图规则 Smith Chart Rule |
|---|---|
| **串联电感** Series Inductor | 沿等电阻圆顺时针移动 Move clockwise along constant-resistance circle |
| **串联电容** Series Capacitor | 沿等电阻圆逆时针移动 Move counter-clockwise along constant-resistance circle |
| **并联电感** Shunt Inductor | 转到导纳图，沿等电导圆逆时针移动 Convert to admittance, move counter-clockwise along constant-conductance circle |
| **并联电容** Shunt Capacitor | 转到导纳图，沿等电导圆顺时针移动 Convert to admittance, move clockwise along constant-conductance circle |
| **传输线段** Transmission Line Section | 沿 $|\Gamma|$ 常数圆向**信号源方向**（顺时针）旋转 Rotate clockwise along constant-$|\Gamma|$ circle toward generator |
| **电阻匹配** Resistive Matching | 沿等电抗圆移动至实轴 Move along constant-reactance circle to real axis |

**实用记忆 (Practical Memory):**
- **顺时针 → 向信号源（长度增加）；逆时针 → 向负载。** *Clockwise → toward generator (longer line); Counter-clockwise → toward load.*
- 旋转 $360°$ 对应 $\lambda/2$ 的电长度（因为 $\Gamma(z) = \Gamma_L e^{-j2\beta z}$，相位变化 $2\beta z$）。*Full 360° rotation corresponds to $\lambda/2$ electrical length.*
- 圆图中心（$\Gamma=0$）对应完美匹配 $Z=Z_0$。*Center ($\Gamma=0$) is perfect match $Z=Z_0$.*
- 最左点（$\Gamma=-1$）对应短路 $Z=0$；最右点（$\Gamma=+1$）对应开路 $Z=\infty$。*Leftmost ($\Gamma=-1$) is short $Z=0$; Rightmost ($\Gamma=+1$) is open $Z=\infty$.*

---

<h1 id="ch7">第七章：S 参数与多端口网络</h1>
<h2>Chapter 7: S-Parameters and Multi-Port Networks</h2>

### 7.1 S 参数定义 (S-Parameter Definition) — 二端口网络

S 参数用**功率波**（power waves）描述网络，而非传统的电压/电流：
*S-parameters describe networks using **power waves**, not traditional voltage/current:*

$$
\begin{bmatrix} b_1 \\ b_2 \end{bmatrix}
=
\begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix}
\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}
$$

| 变量 Variable | 定义 Definition |
|---|---|
| $a_i = \frac{V_i + Z_0 I_i}{2\sqrt{Z_0}}$ | 第 $i$ 端口的入射功率波 Incident power wave at port $i$ |
| $b_i = \frac{V_i - Z_0 I_i}{2\sqrt{Z_0}}$ | 第 $i$ 端口的反射功率波 Reflected power wave at port $i$ |

| S 参数 S-Parameter | 含义 Meaning                                  | 测量条件 Measurement Condition                   |
| ---------------- | ------------------------------------------- | -------------------------------------------- |
| $S_{11}$         | 输入反射系数 Input reflection coefficient         | 输出端口接匹配负载 $Z_0$ Output terminated with $Z_0$ |
| $S_{21}$         | 正向传输系数（增益）Forward transmission (gain)       | 输出端口接匹配负载 Output terminated with $Z_0$       |
| $S_{12}$         | 反向传输系数（隔离度）Reverse transmission (isolation) | 输入端口接匹配负载 Input terminated with $Z_0$        |
| $S_{22}$         | 输出反射系数 Output reflection coefficient        | 输入端口接匹配负载 Input terminated with $Z_0$        |

| 项目 Item                          | 说明 Explanation                                                                                                                                                                                                                                        |        |                     |        |            |        |                          |        |                  |        |                 |        |                         |        |                  |        |     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | ------ | ---------- | ------ | ------------------------ | ------ | ---------------- | ------ | --------------- | ------ | ----------------------- | ------ | ---------------- | ------ | --- |
| **物理含义** Physical Meaning        | S 参数完全描述了一个线性时不变网络在所有频率上的行为。它们对 50 Ω 参考阻抗定义。*S-parameters completely describe a linear time-invariant network at all frequencies, referenced to 50 Ω.*                                                                                                |        |                     |        |            |        |                          |        |                  |        |                 |        |                         |        |                  |        |     |
| **为什么用 S 参数？** Why S-Parameters? | 在高频下，开路和短路条件难以实现（寄生效应），但 50 Ω 匹配负载容易做到。S 参数就是在 50 Ω 匹配条件下测量的，因此是微波频段的"自然"参数。*At high frequencies, open/short conditions are hard to realize (parasitics), but 50 Ω matched loads are easy. S-parameters are thus the "natural" microwave parameters.* |        |                     |        |            |        |                          |        |                  |        |                 |        |                         |        |                  |        |     |
| **与低频参数对比** vs. Low-Frequency    | Z 参数（开路）、Y 参数（短路）、h 参数（混合）在低频易于测量，但在微波频段 S 参数为首选。*Z (open), Y (short), h (hybrid) are easy at low freq; S-parameters are preferred at microwave.*                                                                                                     |        |                     |        |            |        |                          |        |                  |        |                 |        |                         |        |                  |        |     |
| **dB 转换** dB Conversion          | $                                                                                                                                                                                                                                                     | S_{ij} | _{dB} = 20\log_{10} | S_{ij} | $。注意功率增益 $ | S_{21} | ^2$ 在 dB 中为 $10\log_{10} | S_{21} | ^2 = 20\log_{10} | S_{21} | $。*Power gain $ | S_{21} | ^2$ in dB: $10\log_{10} | S_{21} | ^2 = 20\log_{10} | S_{21} | $.* |
| **典型值** Typical                  | 良好放大器: $S_{11}<-10$ dB, $S_{22}<-10$ dB, $S_{21}>10$ dB, $S_{12}<-20$ dB。*Good amplifier: $S_{11}<-10$ dB, $S_{22}<-10$ dB, $S_{21}>10$ dB, $S_{12}<-20$ dB.*                                                                                         |        |                     |        |            |        |                          |        |                  |        |                 |        |                         |        |                  |        |     |

### 7.2 级联网络的链矩阵 (Chain / ABCD Matrix for Cascading)

当多个二端口网络级联时，S 参数矩阵不能直接相乘（不满足级联乘法），需要用 **ABCD 矩阵（链矩阵 / Chain Matrix）**：
*When cascading two-ports, S-matrices don't directly multiply — use ABCD (chain) matrix:*

$$
\begin{bmatrix} V_1 \\ I_1 \end{bmatrix}
=
\begin{bmatrix} A & B \\ C & D \end{bmatrix}
\begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}
$$

级联时：$[ABCD]_{total} = [ABCD]_1 \times [ABCD]_2 \times ...$（直接矩阵乘法 *direct matrix multiplication*）。

在 **dB 域**中这变得更加方便，因为乘法转化为加法：
*In dB domain, this becomes even more convenient — multiplication becomes addition:*

$$
P_{total}[\text{dB}] = P_1[\text{dB}] + P_2[\text{dB}]
$$

| 项目 Item                   | 说明 Explanation                                                                                                                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **物理含义** Physical Meaning | 链矩阵让你可以把每个子模块（滤波器、放大器、衰减器）的行为编码为一个 2×2 矩阵，通过矩阵连乘得到整体系统的二端口特性。*Each sub-block (filter, amplifier, attenuator) is encoded as a 2×2 matrix; overall system = product of all matrices.*                |
| **应用** Application        | MMIC 设计中，各无源结构（微带线、MIM 电容、电感）的 S 矩阵通过链矩阵级联，预测整体匹配网络的频率响应。*In MMIC design, S-matrices of passive structures (microstrip, MIM caps, inductors) are cascaded via ABCD to predict frequency response.* |

### 7.3 S 参数测量 (S-Parameter Measurement Setup)

测量 S 参数需要**矢量网络分析仪（VNA / NWA — Vector Network Analyzer）**：
*S-parameters are measured with a Vector Network Analyzer (VNA):*

| 设备 Device                  | 用途 Purpose                                                            |
| -------------------------- | --------------------------------------------------------------------- |
| Network Analyzer (NWA)     | 测量 S 参数的幅值和相位 Measures magnitude and phase of S-parameters            |
| Parameter Analyzer (DC)    | 提供 DC 偏置并提供 IV 特性 Provides DC bias and IV characteristics             |
| Test-Set                   | 包含混频器将 RF 下变频到中频 Mixer for RF frequency down-conversion               |
| Wafer Prober with Bias Tee | 在晶圆级别接触 MMIC，同时注入 DC 偏置 RF 信号 On-wafer probing with DC bias injection |

---

<h1 id="ch8">第八章：Z / Y / h 参数体系</h1>
<h2>Chapter 8: Z / Y / h Parameter Systems (Multi-parameter Comparison)</h2>

### 8.1 四种参数体系对比 (Four Parameter System Comparison)

| 参数体系 Parameter System | 定义式 Definition | 测量条件 Measurement Condition | 主要用途 Primary Use |
|---|---|---|---|
| **Z 参数 Impedance** $Z_{ij}$ | $\begin{bmatrix}V_1\\V_2\end{bmatrix} = \begin{bmatrix}Z_{11}&Z_{12}\\Z_{21}&Z_{22}\end{bmatrix}\begin{bmatrix}I_1\\I_2\end{bmatrix}$ | 开路 Open circuit | FET/BJT 小信号建模 FET/BJT small-signal modeling |
| **Y 参数 Admittance** $Y_{ij}$ | $\begin{bmatrix}I_1\\I_2\end{bmatrix} = \begin{bmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{bmatrix}\begin{bmatrix}V_1\\V_2\end{bmatrix}$ | 短路 Short circuit | FET 建模（Y 参数自然对应 FET 的跨导模型）FET modeling (Y naturally matches FET transconductance model) |
| **h 参数 Hybrid** $h_{ij}$ | $\begin{bmatrix}V_1\\I_2\end{bmatrix} = \begin{bmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{bmatrix}\begin{bmatrix}I_1\\V_2\end{bmatrix}$ | 混合条件 Mixed | 提取截止频率 $f_T$, $f_{max}$ Extraction of cut-off frequencies |
| **S 参数 Scattering** $S_{ij}$ | $\begin{bmatrix}b_1\\b_2\end{bmatrix} = \begin{bmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}$ | 50 Ω 匹配负载 50 Ω matched load | **通用 RF 测量与设计** Universal RF measurement & design |

### 8.2 各参数体系的优势与应用 (Advantages and Applications)

| 体系 System | 优势 Advantage | 局限 Limitation |
|---|---|---|
| **Z 参数** | 直观的阻抗表示。并联网络用 Z 参数不方便（用导纳 Y 更好）。*Intuitive impedance representation.* | 微波频率下难以实现理想开路（寄生电容使开路变成低阻抗）。*Hard to achieve ideal open at microwave (parasitic C makes open = low Z).* |
| **Y 参数** | FET 的自然描述——栅极为电压控制的电流源。导纳在并联网络中直接相加。*Natural for FET: gate is voltage-controlled current source. Admittances add for parallel networks.* | 微波下理想短路难以实现（寄生电感使短路变成高阻抗）。*Hard to achieve ideal short at microwave (parasitic L makes short = high Z).* |
| **h 参数** | 混合参数适合提取晶体管的特征频率 $f_T$（电流增益=1 的频率）和 $f_{max}$（最大振荡频率）。*Hybrid parameters ideal for extracting transistor $f_T$ (unity current gain frequency) and $f_{max}$ (maximum oscillation frequency).* | 低频实用，微波频段转用 S 参数后转换。*Practical at low freq; convert from S-parameters at microwave.* |
| **S 参数** | 微波频率下的首选——参考 50 Ω 负载在物理上易于实现。功率波概念自然对应能量传输。*The preferred choice at microwave — 50 Ω reference load is physically easy to realize. Power wave concept naturally matches energy transfer.* | 不是所有电路拓扑都能直接从 S 参数直观理解（有时需转到 Z/Y）。*Not all circuit topologies are intuitive from S-parameters directly (sometimes need Z/Y conversion).* |

### 8.3 史密斯圆图上的 Z 和 Y (Z and Y on Smith Chart)

- **阻抗表示 Z**：图中直接读出归一化阻抗 $z = r + jx$。串联元件沿等电阻圆移动。*Read normalized impedance $z = r + jx$. Series elements move along constant-r circles.*
- **导纳表示 Y**：$y = 1/z = g + jb$。史密斯圆图旋转 180° 即为导纳图。并联元件沿等电导圆移动。*$y = 1/z = g + jb$. Rotating Smith Chart by 180° gives admittance chart. Shunt elements move along constant-g circles.*
- **参考阻抗 $Z_0$**：圆图中心始终对应 $Z = Z_0$ （即归一化 $z=1$）。所有映射基于这个 $Z_0$。*Chart center always corresponds to $Z = Z_0$ (normalized $z=1$). All mappings based on this $Z_0$.*

---

<h1 id="ch9">第九章：波导结构与传输媒介</h1>
<h2>Chapter 9: Waveguide Structures and Transmission Media</h2>

### 9.1 常见传输线媒介分类 (Classification of Transmission Media)

| 类型 Type | 结构 Structure | 频率范围 Freq Range | 典型应用 Application |
|---|---|---|---|
| **同轴电缆** Coaxial Cable | 内导体 + 介质 + 外屏蔽层 Inner conductor + dielectric + outer shield | DC ~ 18 GHz (标准) | 实验室互连、测试测量 Lab interconnect, test & measurement |
| **金属波导** Metallic Waveguide | 中空矩形/圆形金属管 Hollow rectangular/circular metal tube | 微波 ~ 亚毫米波 Microwave ~ sub-mm | 高功率传输、雷达馈线 High-power transmission, radar feed |
| **微带线** Microstrip | 介质基板上的导体带 + 接地面 Conductor strip on dielectric + ground plane | DC ~ 毫米波 DC ~ mm-wave | MMIC、PCB RF 电路 MMIC, PCB RF circuits |
| **共面波导** Coplanar Waveguide (CPW) | 信号线 + 两侧共面地 Signal line + coplanar grounds on same side | DC ~ 亚毫米波 DC ~ sub-mm | MMIC（便于并联接地）MMIC (easy shunt grounding) |
| **介质波导 / SIW** Dielectric Waveguide / SIW | 介质基片中的金属化通孔阵列 Metallized via arrays in dielectric substrate | 微波 ~ 毫米波 Microwave ~ mm-wave | 集成滤波器、天线馈电 Integrated filters, antenna feeds |
| **片上天线** On-Chip Antenna | MMIC 内的金属贴片 Metal patch within MMIC | >100 GHz | 400 GHz 发射机 400 GHz transmitter |

### 9.2 同轴电缆特性阻抗 (Coaxial Cable Characteristic Impedance)

$$
\boxed{Z_0 = \frac{60}{\sqrt{\varepsilon_r}} \ln\left( \frac{b}{a} \right)} \quad [\Omega]
$$

| 参数 Parameter | 含义 Meaning |
|---|---|
| $a$ | 内导体半径 Radius of inner conductor |
| $b$ | 外导体内半径 Inner radius of outer conductor |
| $\varepsilon_r$ | 填充介质的相对介电常数 Relative permittivity of filling dielectric |

| 项目 Item | 说明 Explanation |
|---|---|
| **推导思路** Derivation | 同轴线支持 TEM 模式。单位长度电容 $C' = 2\pi\varepsilon/\ln(b/a)$，单位长度电感 $L' = (\mu/2\pi)\ln(b/a)$，代入 $Z_0 = \sqrt{L'/C'}$ 得上述公式。*Coax supports TEM mode. $C' = 2\pi\varepsilon/\ln(b/a)$, $L' = (\mu/2\pi)\ln(b/a)$ → $Z_0 = \sqrt{L'/C'}$.* |
| **典型半刚性电缆** Typical Semi-Rigid | PTFE 填充 $\varepsilon_r=2.08$, $2b=5.46$ mm, $2a=1.64$ mm → $Z_0 \approx 50$ Ω。可用频率上限 18 GHz（更高频需更小尺寸以避免高次模）。*Useful up to 18 GHz; higher frequencies require smaller dimensions to avoid higher-order modes.* |

### 9.3 金属波导 (Metallic Waveguide)

| 项目 Item | 说明 Explanation |
|---|---|
| **工作原理** Principle | 电磁波在金属管壁间反射传播。不是 TEM（两者横向场必须同时为零才满足金属边界条件），而是 TE 或 TM 模式——至少有一个场分量在传播方向上有分量。*EM waves reflect between metal walls. Not TEM — at least one field component has longitudinal part. TE or TM modes.* |
| **截止频率** Cut-Off Frequency | 每个模式都有一个截止频率 $f_c$，低于该频率的模式不能传播（渐逝衰减）。波导尺寸决定 $f_c$。*Each mode has a cut-off frequency; below it, mode is evanescent. Waveguide dimensions determine $f_c$.* |
| **应用** Application | 高功率雷达、卫星通信馈线、粒子加速器 RF 腔。*High-power radar, satellite comm feed lines, particle accelerator RF cavities.* |

### 9.4 总结：关键概念对比 (Summary: Key Concept Comparison)

| 概念 Concept | 自由传播 Free | 导波传播 Guided |
|---|---|---|
| 波类型 Wave Type | TEM | TEM（同轴/微带近似）或 TE/TM（波导） |
| 纵向场分量 Longitudinal Field | 无 None ($E_z=H_z=0$) | 有 (微带准 TEM) 或 TE/TM 模式 |
| 阻抗描述 Impedance Description | $\eta = \sqrt{\mu/\varepsilon}$ | $Z_0 = \sqrt{L'/C'}$（非本征，由几何决定） |
| 链矩阵 Chain Matrix | — | 允许任意子模块级联 Allows arbitrary sub-block cascading |

---

<h1 id="ch10">第十章：微带线与真实无源结构</h1>
<h2>Chapter 10: Microstrip Lines and Real Passive Structures</h2>

### 10.1 微带线的重要性 (Importance of Microstrip)

微带线是 MMIC 设计中最重要的一种传输线。因为它**平面化**——只需一层金属化+一层接地层，可以在芯片上集成。
*Microstrip is the most important transmission line in MMIC design — it's planar, requiring only one metallization + one ground, enabling on-chip integration.*

### 10.2 微带线阻抗公式 — Hammerstad 修正 (Microstrip Impedance — Hammerstad Formulas)

基于 Wheeler 的工作，Hammerstad 提出了实用的微带线特性阻抗近似公式：
*Based on Wheeler's work, Hammerstad proposed practical approximate formulas:*

#### 窄微带线 (Narrow Strip, $w/h \le 1$):

$$
\boxed{Z_0 = \frac{60}{\sqrt{\varepsilon_{eff}}} \ln\left( \frac{8h}{w} + \frac{w}{4h} \right)} \quad [\Omega]
$$

#### 宽微带线 (Wide Strip, $w/h \ge 1$):

$$
\boxed{Z_0 = \frac{120\pi}{\sqrt{\varepsilon_{eff}} \left[ \frac{w}{h} + 1.393 + 0.667 \ln\left( \frac{w}{h} + 1.444 \right) \right]}} \quad [\Omega]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **参数 $w/h$** | 微带线宽度 $w$ 与介质厚度 $h$ 的比值。决定场分布和阻抗。*Width-to-height ratio determines field distribution and impedance.* |
| **趋势** Trend | $w/h$ 越大 → $Z_0$ 越低（宽线 = 低阻抗）。$w/h$ 越小 → $Z_0$ 越高（窄线 = 高阻抗）。*Larger $w/h$ → lower $Z_0$ (wide=low Z). Smaller $w/h$ → higher $Z_0$ (narrow=high Z).* |
| **设计意义** Design | 微带线 + MIM 电容 → 片上匹配网络。不同宽度的微带线段提供不同的特性阻抗，与并联电容一起实现阻抗变换。*Microstrip lines of varying impedance + MIM capacitors → on-chip matching network.* |

### 10.3 设计元素清单 (Design Element Inventory)

| 设计元素 Design Element | 功能 Function |
|---|---|
| **微带线** Microstrip | 传输 + 阻抗变换 Transmission + impedance transformation |
| **开路/短路短截线** Open/Short Stub | 并联电抗（容性或感性） Shunt reactance (capacitive or inductive) for matching |
| **MIM 电容** Metal-Insulator-Metal Capacitor | DC 阻断、并联匹配元件 DC blocking, shunt matching element |
| **螺旋电感** Spiral Inductor | 串联匹配、稳定性（栅极退化） Series matching, stabilization (gate degeneration) |
| **Wilkinson 功分器** Wilkinson Divider | 等功率分配/合成 Equal power split/combine |
| **Lange 耦合器** Lange Coupler | 3 dB 定向耦合器 3 dB directional coupler |
| **空气桥 / 过孔** Air Bridges / Via Holes | 跨接、接地、低电感互连 Cross-connection, grounding, low-inductance interconnect |
| **偏置 Tee** Bias Tee | DC 偏置注入 + RF 阻断 DC bias injection + RF blocking |

### 10.4 布局工程注意事项 (Layout Engineering Considerations)

| 规则 Rule | 说明 Explanation |
|---|---|
| **元件独立性** Element Independence | 所有无源元件的链矩阵必须是独立的——参考平面（reference plane）必须清晰定义，元件之间需要足够的间距避免耦合。*Chain matrices of all passive elements must be independent — clear reference planes, sufficient spacing to avoid coupling.* |
| **EM 验证** EM Verification | 使用额外的 EM 仿真（如 Momentum、HFSS、CST）验证各元件链矩阵的准确性——尤其是当元件间距较近时。*Use additional EM simulation to verify chain matrix accuracy — especially with closely-spaced elements.* |

---

<h1 id="ch11">第十一章：匹配理论与阻抗变换</h1>
<h2>Chapter 11: Matching Theory and Impedance Transformation</h2>

### 11.1 为什么需要匹配？(Why Matching?)

| 不匹配的后果 Consequence of Mismatch | 物理机制 Physical Mechanism |
|---|---|
| **功率浪费** Power Waste | 反射波携带功率返回信号源，不被负载吸收 *Reflected wave carries power back to source, not absorbed by load* |
| **驻波** Standing Waves | 前向与反射波干涉产生驻波——线上某些点电压是其他点的数倍 *Interference of forward and reflected waves creates standing waves — voltage peaks several times higher than elsewhere* |
| **有源器件振荡** Active Oscillation | 反射波在信号源与负载之间来回弹跳（zig-zag），在某些频率满足振荡条件（幅度+相位） *Reflected waves bounce between source and load, potentially satisfying oscillation conditions (amplitude + phase)* |

### 11.2 共轭匹配 (Conjugate Matching) — 最大功率传输

$$
\boxed{Z_L = Z_G^*} \quad \text{即} \quad R_L = R_G,\; X_L = -X_G
$$

$$
\boxed{\Gamma_L = \Gamma_G^*}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **深层原理** Principle | 当源阻抗 $Z_G = R_G + jX_G$ 时，负载必须提供 $-jX_G$ 来"抵消"源的电抗部分，同时 $R_L = R_G$ 使电阻部分匹配。这时传送到负载的功率最大：$P_{max} = |V_G|^2/(8R_G)$。*Load must cancel source's reactance and match resistance for maximum power transfer.* |
| **与"阻抗匹配"的区别** vs. "Impedance Match" | 共轭匹配（$Z_L=Z_G^*$）使功率传输最大；而 $Z_L=Z_0$（无反射匹配）使反射为零。两者在一般电路中不同，只有源阻抗为纯电阻 $Z_0$ 时两者一致。*Conjugate matching maximizes power; $Z_L=Z_0$ minimizes reflection. They differ unless source is purely resistive.* |
| **黄金法则** Golden Rule | 这是整个 RF 放大器设计的核心原则。输入匹配网络的目标就是将一个任意负载阻抗变换到与源阻抗的共轭。*This is the core principle of RF amplifier design. The input matching network transforms an arbitrary load to the conjugate of the source.* |

### 11.3 匹配网络类型 (Matching Network Types)

| 网络类型 Network Type | 元素 Elements | 适用场景 Application |
|---|---|---|
| **LC 梯形网络** LC Ladder | 串联 L/C + 并联 L/C Series L/C + shunt L/C | 低频 ~ 几 GHz 的窄带匹配 Narrow-band matching up to a few GHz |
| **传输线 + 短截线** Line + Stub | 微带线 + 开路/短路短截线 Microstrip + open/short stub | 微波频段的片上匹配 On-chip matching at microwave frequencies |
| **阻抗 + 导纳描述** Impedance / Admittance | 串联元件用阻抗描述；并联元件用导纳描述 Series: impedance. Shunt: admittance | Smith Chart 上交替使用 Z 和 Y 图 Alternate Z and Y on Smith Chart |

---

<h1 id="ch12">第十二章：四分之一波长变换与短截线</h1>
<h2>Chapter 12: Quarter-Wave Transformer and Stubs</h2>

### 12.1 四分之一波长变换器 (Quarter-Wave Transformer)

在 $Z_0$ 系统与负载 $Z_L$ 之间插入一段长度为 $\lambda/4$、特性阻抗为 $Z_T$ 的传输线：
*A $\lambda/4$ line with $Z_T$ inserted between $Z_0$ system and load $Z_L$:*

$$
\boxed{Z_T = \sqrt{Z_0 \cdot Z_L}} \quad [\Omega]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **推导** Derivation | 传输线输入阻抗公式：$Z_{in} = Z_T \frac{Z_L + jZ_T\tan(\beta l)}{Z_T + jZ_L\tan(\beta l)}$。当 $l=\lambda/4$ 时 $\beta l = \pi/2$，$\tan(\beta l)\to\infty$，得 $Z_{in} = Z_T^2/Z_L$。令 $Z_{in}=Z_0$ 解得 $Z_T = \sqrt{Z_0 Z_L}$。*When $\beta l = \pi/2$, $Z_{in} = Z_T^2/Z_L$. Set $Z_{in}=Z_0$ → $Z_T = \sqrt{Z_0 Z_L}$.* |
| **窄带特性** Narrow-Band | $\lambda/4$ 变换器仅在一个频率（及其奇数谐波）上理想工作。偏离中心频率时失配增大。带宽与阻抗变换比有关——变换比越大，带宽越窄。*Works ideally at one frequency + odd harmonics. Mismatch increases away from center. Larger impedance ratio → narrower bandwidth.* |
| **史密斯圆图对应** Smith Chart | 四分之一波长变换在史密斯圆图上是 180° 旋转（因为相位变化 $2\beta l = 2\cdot\pi/2 = \pi = 180°$）。*Quarter-wave transform = 180° rotation on Smith Chart (phase $2\beta l = 2\pi/2 = \pi$).* |

### 12.2 短截线 (Stubs) — 波长相关行为

短截线的等效电抗由其长度相对于波长决定：
*Stub equivalent reactance is determined by its length relative to wavelength:*

| 短截线类型 Stub Type | 长度条件 $l < \lambda/4$ | 长度条件 $l > \lambda/4$ | 输入阻抗公式 Input Impedance |
|---|---|---|---|
| **短路短截线** Short Stub | 感性 Inductive | 容性 Capacitive | $Z_{in} = jZ_0\tan(\beta l)$ |
| **开路短截线** Open Stub | 容性 Capacitive | 感性 Inductive | $Z_{in} = -jZ_0\cot(\beta l)$ |

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 短截线利用终端的全反射（短路 → $\Gamma=-1$ 或开路 → $\Gamma=+1$）在输入端产生一个纯电抗。改变长度即可调节电抗值。*Stubs use total reflection at termination to produce a pure reactance at input. Varying length tunes the reactance value.* |
| **设计用途** Design Use | 短截线实现并联电抗——与传输线主路并联，在史密斯圆图上提供所需的电纳移动（$+jB$ 或 $-jB$），将不匹配的阻抗"拖"到圆心（匹配点）。*Stubs provide shunt reactance — move impedance along constant-conductance circles on Smith Chart towards match.* |

### 12.3 四分之一波长变换器的其他用途 (Other Uses of $\lambda/4$ Lines)

| 用途 Use | 说明 Explanation |
|---|---|
| **偏置 Tee** Bias Tee | $\lambda/4$ 线一端短路 → 在中心频率对 RF 信号呈现开路（高阻），允许 DC 偏置注入而不影响 RF。*Quarter-wave line shorted at one end → open circuit for RF at center frequency; allows DC bias injection.* |
| **谐波终端** Harmonic Termination | 在特定谐波频率（$2f_0$, $3f_0$）上利用 $\lambda/4$ 或其整数倍提供短路/开路，实现谐波控制（如 F 类功放）。*Provide short/open at specific harmonics for waveform engineering (e.g. class-F PA).* |
| **Wilkinson 功分器臂** Wilkinson Arms | 两条 $\lambda/4$ 线将 50 Ω 输入变换为 100 Ω（每个端口），实现等分功率和无反射。*Two $\lambda/4$ arms transform 50 Ω input to 100 Ω each for equal split and no reflection.* |

---

<h1 id="ch13">第十三章：功分器、合成器与耦合器</h1>
<h2>Chapter 13: Dividers, Combiners, and Couplers</h2>

### 13.1 Wilkinson 功分器 (Wilkinson Power Divider)

| 项目 Item | 说明 Explanation |
|---|---|
| **结构** Structure | 输入端 → 两条 $\lambda/4$ 臂 ($Z_{arm} = \sqrt{2}Z_0$) → 两个输出端口，输出端口之间用一个隔离电阻 $R = 2Z_0$ 桥接。*Input → two $\lambda/4$ arms ($Z_{arm} = \sqrt{2}Z_0$) → two outputs; isolation resistor $R=2Z_0$ across outputs.* |
| **标准值** Standard Values ($Z_0=50$ Ω) | $Z_{arm} = 70.7$ Ω；$R = 100$ Ω |
| **功率分配** Power Split | $S_{21} = S_{31} = -3$ dB（每个端口一半功率）。$S_{23} \ll 1$（输出端口间高隔离）。$S_{11} \approx 0$（输入端匹配）。*Half power each port. High isolation between outputs. Input matched.* |
| **工作原理** Principle | $\lambda/4$ 线实现阻抗变换（50 Ω → 100 Ω → 两个 100 Ω 并联 = 50 Ω）。隔离电阻 $R$ 消耗偶模-奇模分析中的奇模功率（反射差模信号被电阻吸收）。*Quarter-wave transforms 50 Ω → 100 Ω each. Resistor absorbs odd-mode power (differential reflection signals).* |
| **主要目的** Main Purpose | $\lambda/4$ 变换引起阻抗变换，使两个组件/过渡之间的失配最小化。通常会有反射，可能与前向信号产生破坏性干涉——通过增加终端电阻来避免。*Induce impedance transformation to minimize mismatch. Reflections are absorbed by termination resistor to avoid destructive interference.* |

### 13.2 设计元素总览 (Design Element Overview)

| 元素 Element | 功能 Function | S 参数特征 S-Parameter Feature |
|---|---|---|
| **短截线** Stub | 匹配 Matching | $S_{11}$ 频率选择性 Frequency-selective |
| **合成器** Combiner | 多路信号合成 Multi-path signal combination | 功率相加 Power addition |
| **Lange 耦合器** Lange Coupler | 3 dB 定向耦合 Directional coupling | $S_{31}$ 与 $S_{41}$ 幅度相等、相位差 90° Equal amplitude, 90° phase |
| **MIM 电容** MIM Cap | DC 阻断 Blocking | 低频高阻、高频低阻 High Z at low f, low Z at high f |
| **电感** Inductor | 稳定性 Stability | 串联反馈退化 Series feedback degeneration |
| **空气桥 / 过孔** Air Bridge / Via | 接地 / 跨接 Ground / Jumper | 低寄生电感 Low parasitic L |

---

<h1 id="ch14">第十四章：损耗机制全面分析</h1>
<h2>Chapter 14: Comprehensive Loss Mechanism Analysis</h2>

### 14.1 传播常数回顾 (Propagation Constant Review)

$$
\boxed{\gamma = \alpha + j\beta}
$$

$$
\boxed{\alpha = \alpha_C + \alpha_D + \alpha_G + \alpha_R}
$$

| 损耗类型 Loss Type | 符号 Symbol | 来源 Source | 频率依赖性 Freq Dependence |
|---|---|---|---|
| 金属导体损耗 Metallic Conductor Loss | $\alpha_C$ | 金属有限的电导率（焦耳热）Finite metal conductivity (Joule heating) | $\propto \sqrt{f}$ |
| 介质损耗 Dielectric Loss | $\alpha_D$ | 介质极化弛豫→热 Dielectric polarization relaxation → heat | $\propto f$ |
| 衬底并联电导损耗 Substrate Conductance Loss | $\alpha_G$ | 衬底有限电阻率 Finite substrate resistivity (parallel path) | $\propto f$ |
| 辐射损耗 Radiation Loss | $\alpha_R$ | 开放结构向空间辐射能量 Open structure radiating into space | 通常较小，高频增大 Small typically, increases at high f |

### 14.2 金属导体损耗公式 (Metallic Conductor Loss)

$$
\boxed{\alpha_C = \frac{R'}{2Z_0}} \quad [\text{Np/m}]
$$

转换为 dB/m：$\alpha_{C,\text{dB/m}} = \alpha_C \times 8.686$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 金属线的串联电阻 $R'$ 消耗前行波的功率。损耗与电阻成正比，与 $Z_0$ 成反比——高阻抗线导体损耗更低（因为电流更小）。*Series metal resistance dissipates forward wave power. Loss ∝ R', ∝ 1/Z₀ — higher Z₀ lines have lower conductor loss (less current).* |
| **简化思想** Simplified Thinking | 可以把 $\alpha_C$ 理解为信号每传播 1 米，辐射出的焦耳热占信号功率的比例。*Think of $\alpha_C$ as the fraction of signal power lost to Joule heating per meter.* |

### 14.3 介质损耗公式 (Dielectric Loss)

$$
\boxed{\alpha_D = 8.686 \cdot \frac{\omega C' Z_0}{2} \cdot \tan \delta} \quad [\text{dB/m}]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 介质分子在外加交变电场中不断翻转（极化弛豫），每次翻转都有能量损耗。$\tan\delta$ 越大 → 损耗越大。频率越高 → 翻转越频繁 → 损耗越大（$\propto f$）。*Dielectric molecules flip under AC E-field (polarization relaxation), losing energy each time. Higher $\tan\delta$ → more loss. Higher f → more flips → more loss ($\propto f$).* |
| **频率依赖性** Frequency | $\alpha_D \propto \omega \propto f$，与导体损耗的 $\sqrt{f}$ 不同。在高频时介质损耗可能成为主导。*$\alpha_D \propto f$, different from conductor's $\sqrt{f}$. At high f, dielectric loss may dominate.* |
| **典型材料损耗对比** Material Comparison | FR4 ($\tan\delta\approx0.02$) 不适合 1 GHz 以上；Rogers RO4003 ($\tan\delta\approx0.0027$) 适合到 Ku 波段；GaAs 半绝缘 ($\tan\delta\approx 0.0006$) 适合到毫米波。*FR4 unsuitable above 1 GHz; Rogers RO4003 good to Ku-band; GaAs SI good to mm-wave.* |

### 14.4 衬底并联电导损耗 (Substrate Parallel Conductance Loss)

$$
\boxed{\alpha_G = \frac{8.686 \cdot \omega G' Z_0}{2}} \quad [\text{dB/m}]
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 衬底不是完美绝缘体——有限的电导率 $G'$ 形成了一个并联漏电路径。对硅基 MMIC 尤其重要（硅的电阻率较低）。*Substrate isn't perfect insulator — finite $G'$ forms a parallel leakage path. Particularly important for Si-based MMIC (Si has lower resistivity).* |

### 14.5 损耗机制的频率依赖性总结 (Frequency Dependence Summary)

| 频率 Frequency | 主导损耗 Dominant Loss | 原因 Reason |
|---|---|---|
| < 1 GHz | $\alpha_C$ (导体) | 趋肤效应尚未严重；介质损耗小 *Skin effect not severe; dielectric loss small* |
| 1-10 GHz | $\alpha_C + \alpha_D$ (混合) | 两者可比 *Both comparable* |
| > 10 GHz | $\alpha_D$ (介质) 可能主导 | $\alpha_D \propto f$ 比 $\alpha_C \propto \sqrt{f}$ 增长更快 *$\alpha_D$ grows faster than $\alpha_C$* |

---

<h1 id="ch15">第十五章：趋肤效应与表面粗糙度</h1>
<h2>Chapter 15: Skin Effect and Surface Roughness</h2>

### 15.1 趋肤深度 (Skin Depth)

$$
\boxed{\delta_{skin} = \sqrt{\frac{\rho}{\pi f \mu_0 \mu_r}} = \sqrt{\frac{2\rho}{\omega \mu_0 \mu_r}}} \quad [\text{m}]
$$

| 参数 Parameter | 含义 Meaning | 典型值 Typical |
|---|---|---|
| $\rho = 1/\sigma$ | 金属电阻率 Metal resistivity | 铜 Cu: $1.72\times 10^{-8}$ Ω·m |
| $f$ | 频率 Frequency | — |
| $\mu_r$ | 相对磁导率 Relative permeability | 非磁性金属: 1; 镍 Ni: ~100-600 |

| 项目 Item | 说明 Explanation |
|---|---|
| **物理图像** Physical Picture | 交流电流集中在导体表面 $\delta_{skin}$ 的薄层中。频率越高，趋肤深度越浅，有效导电截面积越小，等效电阻越大。*AC current crowds into a thin surface layer $\delta_{skin}$. Higher f → shallower skin depth → smaller effective cross-section → higher resistance.* |
| **推导** Derivation | 在导体中 Maxwell 方程化简为扩散方程 $\nabla^2\vec{E} = j\omega\mu\sigma\vec{E}$，解得 $\vec{E}(z) = \vec{E}_0 e^{-z/\delta} e^{-jz/\delta}$。$\delta$ 为场幅衰减到 $1/e$ 的深度。*Solve diffusion equation in conductor; $\delta$ is where field amplitude decays to $1/e$.* |

**铜的趋肤深度速查表 (Skin Depth of Copper at Various Frequencies):**

| 频率 Frequency | 趋肤深度 Skin Depth |
|---|---|
| 1 MHz | ~66 µm |
| 100 MHz | ~6.6 µm |
| 1 GHz | ~2.1 µm |
| 10 GHz | ~0.66 µm |
| 100 GHz | ~0.21 µm |

### 15.2 趋肤效应对导体损耗的影响 (Skin Effect Impact on Conductor Loss)

由于趋肤效应，导体的等效串联电阻 $R' \propto \sqrt{f}$，因此：
*Due to skin effect, effective series resistance $R' \propto \sqrt{f}$, thus:*

$$
\boxed{\alpha_C \propto \sqrt{f}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **设计启示** Design Implication | 频率从 1 GHz 升到 10 GHz → 导体损耗增加约 $\sqrt{10} \approx 3.16$ 倍。*Going from 1 GHz to 10 GHz → conductor loss increases ~3.16×.* |

### 15.3 表面粗糙度修正 (Surface Roughness Correction)

实际加工的金属表面不是理想光滑的。表面微观峰谷用 RMS（Root Mean Square）粗糙度量化。粗糙度增加了电流路径的有效长度，从而增大损耗。
*Real fabricated metal surfaces aren't perfectly smooth. Microscopic peaks and valleys — quantified by RMS roughness — increase effective current path length, hence increase loss.*

$$
\boxed{\alpha_{Cond,RMS} = \alpha_{Cond} \left[ 1 + \frac{2}{\pi} \tan^{-1}\left( \frac{RMS}{\delta_{skin}} \right)^2 \right]}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **参数 $RMS/\delta_{skin}$** | 粗糙度与趋肤深度的比值。这是关键的无量纲参数。当 $RMS \ll \delta_{skin}$ 时，电流"看不见"粗糙度。当 $RMS \gtrsim \delta_{skin}$ 时，粗糙度显著增加损耗。*Critical dimensionless ratio. When $RMS \ll \delta_{skin}$, current "doesn't see" roughness. When $RMS \gtrsim \delta_{skin}$, roughness significantly increases loss.* |
| **毫米波意义** mm-Wave Implication | 在 100 GHz，$\delta_{skin}$ (铜) ≈ 0.21 µm。此时即使 RMS ~ 0.1 µm（常规加工可达），粗糙度也可能使损耗增加 50% 以上。工艺控制至关重要。*At 100 GHz, $\delta_{skin}$(Cu) ≈ 0.21 µm. Even RMS ~0.1 µm can increase loss >50%. Process control is critical.* |
| **$\tan^{-1}$ 项** | 反正切函数将无量纲比值映射到 $[0,\pi/2]$ 区间，保证了修正因子在 $[1, 2]$ 范围内（即粗糙度最多使损耗翻倍）。*$\tan^{-1}$ maps to $[0,\pi/2]$, ensuring correction factor is in $[1,2]$ — at most doubles the loss.* |

---

<h1 id="ch16">第十六章：天线原理与特性参数</h1>
<h2>Chapter 16: Antenna Principles and Characteristic Parameters</h2>

### 16.1 天线定义 (Antenna Definition)

**天线：** 一种结构，使电磁能量在自由空间与导波装置之间进行转换。
**Antenna:** A structure which enables the transfer of electromagnetic energy in free-space to and from a guiding device.

### 16.2 天线类型分类 (Antenna Type Classification)

| 类型 Type | 示例 Examples |
|---|---|
| **线天线** Wire Antennas | 偶极子 Dipole、环天线 Loop、螺旋天线 Helix |
| **孔径天线** Aperture Antennas | 角锥喇叭 Pyramidal horn、圆锥喇叭 Conical horn、矩形波导开口 Rectangular waveguide |
| **微带天线** Microstrip Antennas | 矩形/圆形贴片 + 接地面 Rectangular/circular patch + ground plane |
| **阵列/反射面/透镜** Arrays / Reflectors / Lenses | 相控阵 Phased array、抛物面 Parabolic dish、龙伯透镜 Luneburg lens |

### 16.3 赫兹偶极子 (Hertz Dipole) — 最小天线

赫兹偶极子是最基本的辐射单元——一段长度远小于波长的电流元。所有更复杂的天线都可以理解为赫兹偶极子阵列。
*The Hertz dipole is the most basic radiating element — a current element much shorter than wavelength. All more complex antennas can be understood as arrays of Hertz dipoles.*

### 16.4 方向性系数 (Directivity)

$$
\boxed{D = \frac{4\pi \cdot U_{max}}{P_{rad}}}
$$

| 参数 Parameter | 含义 Meaning | 单位 Unit |
|---|---|---|
| $U_{max}$ | 最大辐射方向上单位立体角的辐射功率 Radiated power per solid angle in direction of maximum radiation | W/sr |
| $P_{rad}$ | 总辐射功率 Total radiated power | W |
| $4\pi$ | 半径为 1 的球面面积 Surface area of sphere with radius 1 | sr |

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 方向性 $D$ 是比较天线在某个方向的辐射强度与全向均匀辐射（各向同性 isotropic）之比。$D = 1 (0 \text{ dBi})$ 表示全向均匀辐射天线（各向同性 radiator）。*$D$ compares radiation intensity in a given direction vs. uniform isotropic radiation. $D=1$ (0 dBi) = isotropic.* |
| **在波束立体角下的表示** Beam Solid Angle | 定义波束立体角 $\Omega_A$ 为 $U_{max}\Omega_A = P_{rad}$，则 $D = 4\pi/\Omega_A$。$\Omega_A$ 越小（波束越窄），$D$ 越大。*Define beam solid angle $\Omega_A$; narrower beam → larger D.* |
| **典型值** Typical | 半波偶极子: $D \approx 1.64$ (2.15 dBi)。小孔径天线: $D \approx 4-10$ (6-10 dBi)。大抛物面天线: $D \approx 10^4-10^6$ (40-60 dBi)。*Half-wave dipole: ~2.15 dBi. Small aperture: 6-10 dBi. Large parabolic: 40-60 dBi.* |

### 16.5 天线增益 (Antenna Gain)

$$
\boxed{G = \eta \cdot D} \quad \text{或} \quad G_{\text{dBi}} = 10\log_{10}(\eta D)
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 增益 $G$ 是方向性 $D$ 乘以天线效率 $\eta$。它考虑了天线内部的欧姆损耗、介质损耗和阻抗失配导致的功率损失。$G$ 总是 ≤ $D$。*Gain = Directivity × Efficiency. Accounts for ohmic, dielectric, and mismatch losses. $G \leq D$ always.* |
| **为什么用 dBi？** Why dBi? | "i"表示参考全向天线（isotropic）。dBi 是天线增益最常用的单位。*"i" indicates reference to isotropic antenna. dBi is the most common unit.* |

### 16.6 天线效率 (Antenna Efficiency)

$$
\boxed{\eta = \frac{P_{rad}}{P_{in}} = \frac{P_{rad}}{P_{rad} + P_{loss}}}
$$

| 参数 Parameter | 含义 Meaning |
|---|---|
| $P_{in}$ | 输入天线的总功率 Total power input to antenna |
| $P_{rad}$ | 辐射到空间的功率 Power radiated into space |
| $P_{loss}$ | 内部损耗的功率（欧姆 + 介质 + 失配）Internal losses (ohmic + dielectric + mismatch) |

| 项目 Item | 说明 Explanation |
|---|---|
| **效率的关键性** Importance of Efficiency | 对于片上毫米波天线，效率可能是最关键的指标——由于片上金属薄、衬底损耗大，$\eta$ 可以低至 10-30%。提升效率需要优化金属厚度和衬底选择。*For on-chip mm-wave antennas, efficiency may be the most critical metric — thin metal and high substrate loss can reduce $\eta$ to 10-30%.* |

### 16.7 Friis 传输方程 (Friis Transmission Equation)

$$
\boxed{\frac{P_R}{P_T} = G_T G_R \left( \frac{\lambda}{4\pi R} \right)^2}
$$

| 参数 Parameter | 含义 Meaning |
|---|---|
| $P_T, P_R$ | 发射/接收功率 Transmitted/received power |
| $G_T, G_R$ | 发射/接收天线增益 Transmit/receive antenna gains (linear, not dB) |
| $R$ | 天线间距 Distance between antennas |
| $\lambda$ | 自由空间波长 Free-space wavelength |
| $(\lambda/4\pi R)^2$ | 自由空间路径损耗 Free-space path loss |

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | 接收功率与 $1/R^2$ 成正比（自由空间）。$\lambda$ 越大 → 接收功率越大（天线有效孔径与 $\lambda^2$ 成正比）。*Received power ∝ $1/R^2$. Larger $\lambda$ → more received power (aperture ∝ $\lambda^2$).* |
| **对数形式** Log Form | $P_{R,\text{dBm}} = P_{T,\text{dBm}} + G_{T,\text{dBi}} + G_{R,\text{dBi}} - 20\log_{10}(4\pi R/\lambda)$。*dB form for link budget calculation.* |
| **应用** Application | 无线通信链路预算（Link Budget）、雷达方程（Radar Equation）的简化形式。*Wireless link budget; simplified form of radar equation.* |

### 16.8 有效孔径 (Effective Aperture)

$$
\boxed{A_{eff} = \frac{G \lambda^2}{4\pi} = \eta_{ap} \cdot A_{phys}}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **物理含义** Physical Meaning | $A_{eff}$ 是天线"捕捉"入射电磁波功率的有效截面积。它与增益成正比、与频率平方成反比。*$A_{eff}$ is the effective cross-section for capturing incident EM wave power. ∝ $G$, ∝ $1/f^2$.* |
| **孔径效率** Aperture Efficiency | $\eta_{ap} = A_{eff}/A_{phys} \le 1$，描述物理孔径的利用效率。均匀照射孔径的 $\eta_{ap}=1$；锥形照射（降低旁瓣）则 $\eta_{ap} < 1$。*Uniform illumination: $\eta_{ap}=1$. Tapered illumination (lower sidelobes): $\eta_{ap} < 1$.* |

### 16.9 远场方向图 (Far-Field Pattern / Antenna Diagram)

天线方向图是增益随空间角度 $(\theta,\phi)$ 变化的极坐标图：
*Antenna diagram is a polar plot of gain vs. spatial angle $(\theta,\phi)$:*

| 特征 Feature | 说明 Explanation |
|---|---|
| **主瓣** Main Lobe | 辐射最强的方向 Direction of maximum radiation |
| **旁瓣** Side Lobes | 主瓣两侧的次要辐射峰 Secondary peaks on sides of main lobe |
| **3 dB 波束宽度** 3 dB Beamwidth | 主瓣增益下降 3 dB（一半功率）的角宽度 Angular width at half-power (-3 dB) |
| **前后比** Front-to-Back Ratio | 前向增益与后向增益的比值 Ratio of forward to backward gain |

---

<h1 id="ch17">第十七章：阵列天线与 MIMO</h1>
<h2>Chapter 17: Array Antennas and MIMO</h2>

### 17.1 方向图乘法 (Pattern Multiplication)

对于由 $N$ 个相同辐射单元组成的阵列：
*For an array of $N$ identical radiating elements:*

$$
\boxed{E_{total}(\theta, \phi) = E_{single}(\theta, \phi) \cdot AF(\theta, \phi)}
$$

| 项目 Item | 说明 Explanation |
|---|---|
| **$E_{single}$** | 单个天线单元的远场辐射方向图（单元因子 Element Factor）*Far-field pattern of a single element* |
| **$AF$** | 阵列因子（Array Factor）— 仅取决于各单元的位置和激励幅度/相位 *Depends only on element positions and excitation amplitudes/phases* |
| **物理含义** Physical Meaning | 阵列的总方向图 = 单元方向图 × 阵列因子。这个"乘法法则"是阵列天线设计的基石。*Total pattern = Element pattern × Array factor. The "Multiplication Law" is the cornerstone of array design.* |
| **应用** Application | 相控阵雷达：通过改变各单元的相位差实现电子波束扫描（不机械转动天线）。*Phased-array radar: electronic beam steering by varying phase differences.* |

### 17.2 合成孔径雷达 (SAR — Synthetic Aperture Radar)

| 项目 Item | 说明 Explanation |
|---|---|
| **原理** Principle | 通过移动平台（卫星/飞机）在不同位置发射和接收信号，利用信号处理合成一个等效的大孔径天线。分辨率远高于物理孔径。*Moving platform synthesizes a large equivalent aperture via signal processing. Resolution far exceeds physical aperture.* |
| **应用** Application | 地球遥感（对地观测）、洪水监测、地形测绘。*Earth remote sensing, flood monitoring, terrain mapping.* |

### 17.3 MIMO 天线（5G 移动通信）(MIMO for 5G Mobile Communication)

| 项目 Item | 说明 Explanation |
|---|---|
| **原理** Principle | Multiple-Input Multiple-Output — 发射端和接收端各使用多根天线，利用多径传播创造多个并行的空间信道，大幅提高频谱效率。*Multiple antennas at both Tx and Rx exploit multipath to create parallel spatial channels, greatly improving spectral efficiency.* |
| **5G 关键** 5G Key | 大规模 MIMO (Massive MIMO) 使用数十至数百根天线，通过波束成形（beamforming）将能量集中到特定用户方向，减少干扰、提高信噪比。*Massive MIMO with tens to hundreds of antennas uses beamforming to focus energy on specific users.* |

---

<h1 id="lec7">第七讲：RF 半导体与有源器件基础</h1>
<h2>Lecture 7: RF Semiconductors and Active-Device Fundamentals</h2>

> 本讲从无源网络进入有源器件。核心问题是：如何用偏置控制载流子的产生与运动，并把直流功率转换为 RF 功率。  
> *This lecture moves from passive networks to active devices: bias controls carrier generation and transport, enabling DC-to-RF power conversion.*

### 7.1 有源器件、工作点与线性化 (Active Devices, Bias Point, and Linearization)

晶体管的非线性关系可写成 $i_D=f(v_{GS},v_{DS})$。在静态工作点 $Q$ 附近作 Taylor 展开：

$$
i_D \approx I_{D,Q}
+g_m v_{gs}
+g_{ds}v_{ds}
+\frac{1}{2}g_m'v_{gs}^{2}
+\frac{1}{6}g_m''v_{gs}^{3}+\cdots
$$

其中小信号参数为

$$
\boxed{g_m=\left.\frac{\partial I_D}{\partial V_{GS}}\right|_Q},\qquad
\boxed{g_{ds}=\left.\frac{\partial I_D}{\partial V_{DS}}\right|_Q},\qquad
r_o=\frac{1}{g_{ds}}
$$

| 工作方式 Mode | 条件 Condition | 模型 Model | 主要用途 Main Use |
|---|---|---|---|
| 小信号 Small-signal | RF 摆幅远小于偏置量 | 一阶线性化、S 参数 | LNA、小信号增益与稳定性 |
| 大信号 Large-signal | RF 摆幅与偏置相当 | 完整非线性模型、谐波平衡 | PA、混频器、振荡器 |

### 7.2 本征模型与外部寄生 (Intrinsic Model and Extrinsic Parasitics)

RF 小信号模型由本征晶体管和外部壳层组成：

| 区域 | 典型元件 | 物理来源 |
|---|---|---|
| 本征 Intrinsic | $g_m$, $g_{ds}$, $C_{gs}$, $C_{gd}$, $C_{ds}$ | 沟道电荷、跨导、输出电导 |
| 外部 Extrinsic | $R_g,R_s,R_d$, $L_g,L_s,L_d$, pad capacitances | 栅/源/漏金属、互连、焊盘和衬底 |

常见近似输入阻抗和 Miller 放大为

$$
Z_{in}\approx R_g+\frac{1}{j\omega(C_{gs}+C_{gd}(1-A_v))}
$$

因此 $C_{gd}$ 不只是一个小寄生，它同时提供输入输出反馈，会限制增益、带宽并影响稳定性。  
*The gate-drain capacitance is a feedback element; through the Miller effect it limits gain and bandwidth and can threaten stability.*

### 7.3 晶体、能带与材料选择 (Crystal, Energy Bands, and Material Choice)

电子允许能级形成价带与导带，两者间隔为禁带宽度 $E_g$：

$$
E_g=E_C-E_V
$$

本征载流子浓度的主要温度关系为

$$
\boxed{n_i=\sqrt{N_CN_V}\exp\left(-\frac{E_g}{2k_BT}\right)}
$$

| 材料参数 Material Metric | RF 影响 RF Impact |
|---|---|
| 迁移率 $\mu_n,\mu_p$ | 决定低场速度、导通电阻和跨导 |
| 饱和速度 $v_{sat}$ | 决定短沟道高速输运与渡越时间 |
| 禁带宽度 $E_g$ | 影响漏电、最高结温与击穿能力 |
| 临界电场 $E_{crit}$ | 决定可承受电压和功率密度 |
| 热导率 $\kappa$ | 决定结温和散热能力 |
| 介电常数 $\varepsilon_r$ | 影响结电容、场分布和器件尺寸 |

粗略功率器件材料优值可写成

$$
\mathrm{FOM}_{Baliga}\propto \varepsilon\mu E_{crit}^{3}
$$

Si 的优势是大尺寸高质量晶圆、成熟 CMOS 工艺和低成本；III-V 材料通常具有更高电子迁移率或饱和速度；GaN/SiC 依靠宽禁带和高临界电场适合高压高功率。  
*Silicon wins in manufacturability and integration; III-V materials offer superior transport; GaN and SiC excel at high voltage and power density.*

### 7.4 漂移输运与电导率 (Drift Transport and Conductivity)

低场下

$$
\boxed{v_d=\mu E},\qquad
\boxed{J=q(n\mu_n+p\mu_p)E=\sigma E}
$$

$$
\boxed{\rho=\frac{1}{\sigma}=\frac{1}{q(n\mu_n+p\mu_p)}}
$$

高场时速度不再与电场成正比，而趋近 $v_{sat}$。一个常用经验模型是

$$
v(E)\approx\frac{\mu E}{1+\mu E/v_{sat}}
$$

器件速度的第一层直觉是

$$
\boxed{\tau_{tr}\approx\frac{L}{v}},\qquad
f\sim\frac{1}{2\pi\tau_{tr}}
$$

所以缩短栅长 $L_g$、提高载流子速度可以提升截止频率，但会同时加剧短沟道效应、隧穿、击穿和寄生影响。

### 7.5 异质结、应变与能带工程 (Heterojunctions, Strain, and Bandgap Engineering)

不同半导体组合时，晶格失配近似为

$$
\boxed{\epsilon_{misfit}=\frac{a_{layer}-a_{sub}}{a_{sub}}}
$$

薄层可通过弹性应变维持赝晶结构；超过临界厚度后会出现失配位错。异质结的导带和价带偏移满足

$$
\Delta E_C+\Delta E_V=\Delta E_g
$$

能带工程可实现载流子限制、调制掺杂和高迁移率二维电子气 (2DEG)，这是 HEMT 与 HBT 的物理基础。  
*Bandgap engineering confines carriers and separates dopants from the transport channel, enabling HEMTs and HBTs.*

### 7.6 衬底与外延 (Substrates and Epitaxy)

| 方法 Method | 特点 Characteristics | RF 应用 RF Use |
|---|---|---|
| Czochralski (CZ) | 从熔体拉制大尺寸单晶 | Si、GaAs 衬底 |
| CVD | 气相前驱体发生化学反应并沉积 | Si、介质与多晶层 |
| MOCVD | 金属有机源，产能高、适合量产 | GaAs、GaN、InP 异质结构 |
| MBE | 超高真空、原子束、界面控制精确 | 研究与高精度 III-V 外延 |

外延决定层厚、掺杂、界面陡峭度与缺陷密度；这些参数最后会反映到迁移率、击穿、电容、噪声与可靠性中。

---

<h1 id="lec8">第八讲：RF 半导体制造工艺</h1>
<h2>Lecture 8: RF Semiconductor Fabrication</h2>

### 8.1 从晶圆到芯片的工艺循环 (Wafer-to-Chip Process Loop)

一轮典型工艺不断重复：薄膜生长/沉积 -> 涂胶 -> 曝光 -> 显影 -> 刻蚀或注入 -> 去胶 -> 清洗 -> 退火 -> 测量。先进工艺可包含数百到上千步骤，完整制造周期可达数月。  
*Fabrication repeatedly combines deposition, lithography, etching or implantation, stripping, cleaning, annealing, and metrology.*

### 8.2 掺杂与离子注入 (Doping and Ion Implantation)

注入剂量与电流、时间和面积的关系为

$$
\boxed{Q_{dose}=\int J_{ion}(t)\,dt},\qquad [Q_{dose}]=\mathrm{cm^{-2}}
$$

注入能量主要控制平均投影深度 $R_p$，剂量控制掺杂总量。注入会破坏晶格，因此需要退火完成晶格修复与电激活。离子通道效应 (channeling) 可通过倾斜晶圆或预非晶化降低。

扩散的基本方程为

$$
\frac{\partial C}{\partial t}=D\frac{\partial^2C}{\partial x^2},\qquad
D=D_0\exp\left(-\frac{E_a}{k_BT}\right)
$$

### 8.3 光刻与分辨率 (Lithography and Resolution)

投影光刻的 Rayleigh 关系：

$$
\boxed{CD=k_1\frac{\lambda}{NA}},\qquad
\boxed{DOF=k_2\frac{\lambda}{NA^2}}
$$

减小曝光波长或增大数值孔径 $NA$ 可提高分辨率，但会缩小景深。EUV 使用约 $13.5\ \mathrm{nm}$ 波长；电子束光刻分辨率高但串行写入、吞吐量低，常用于掩模与原型。  
*Shorter wavelength and larger numerical aperture improve resolution, but a larger NA reduces depth of focus.*

### 8.4 刻蚀、沉积与金属化 (Etching, Deposition, and Metallization)

| 工艺 | 优势 | 限制 |
|---|---|---|
| 湿法刻蚀 Wet etch | 选择性高、成本低 | 多为各向同性，容易侧蚀 |
| 干法/RIE Dry etch | 各向异性、可形成陡直侧壁 | 等离子损伤、设备复杂 |
| Lift-off | 适合难刻蚀金属与 T-gate | 胶形貌和覆盖性要求高 |
| PVD/蒸发/溅射 | 金属沉积常用 | 台阶覆盖依方法而异 |
| CVD/ALD | 覆盖性和厚度控制好 | 温度、前驱体与速率限制 |

RF 器件尤其敏感于栅长、栅电阻、欧姆接触电阻、钝化层陷阱与互连电感。工艺偏差会同时改变直流工作点和 S 参数，因此版图寄生和工艺统计必须进入模型。

### 8.5 工艺总结 (Process Summary)

> 制造并非只负责“画出晶体管”。工艺定义了 $L_g$、接触电阻、寄生电容、缺陷与热路径，也就定义了器件的 $f_T$、$f_{max}$、噪声、击穿和可靠性。  
> *Fabrication defines geometry, contacts, parasitics, defects, and thermal paths; consequently it defines RF speed, noise, breakdown, and reliability.*

---

<h1 id="lec9">第九讲：载流子输运、结与场效应晶体管</h1>
<h2>Lecture 9: Carrier Transport, Junctions, and Field-Effect Transistors</h2>

### 9.1 漂移、扩散与 Einstein 关系 (Drift, Diffusion, and Einstein Relation)

$$
J_n=q n\mu_nE+qD_n\nabla n
$$

$$
J_p=q p\mu_pE-qD_p\nabla p
$$

$$
\boxed{\frac{D_n}{\mu_n}=\frac{D_p}{\mu_p}=\frac{k_BT}{q}}
$$

掺杂提高载流子浓度并降低电阻率，但离化杂质散射会降低迁移率。因此“重掺杂”不等价于无限提高电导，RF 设计必须在接触电阻、迁移率、电容和击穿之间折中。  
*Doping increases carrier concentration but also increases impurity scattering; conductivity, capacitance, and breakdown must be traded together.*

### 9.2 纳米尺度限制 (Nanoscale Limits)

| 限制 Limit | 物理机制 Mechanism | 后果 Consequence |
|---|---|---|
| 量子限制 Quantum confinement | 尺寸接近 de Broglie 波长 | 能级离散、阈值变化 |
| 隧穿 Tunneling | 势垒过薄 | 栅漏电、关断泄漏 |
| 速度饱和 Velocity saturation | 高横向电场 | 电流不再服从平方律 |
| 冲击电离 Impact ionization | 载流子获得足够能量 | 雪崩击穿、可靠性下降 |
| 热载流子 Hot carriers | 高场载流子注入介质/界面 | 参数漂移与退化 |

击穿电压的直觉关系为 $V_{BR}\sim E_{crit}L_{drift}$；提高电压需要更长、更轻掺杂的漂移区，却会增加导通电阻。

### 9.3 PN 结、Schottky 结与 RF 二极管模型 (PN, Schottky, and RF-Diode Model)

理想二极管方程：

$$
\boxed{I=I_S\left(e^{qV/(nk_BT)}-1\right)}
$$

小信号结电导和动态电阻：

$$
g_d=\frac{dI}{dV}\approx\frac{I_D}{nV_T},\qquad
\boxed{r_d\approx\frac{nV_T}{I_D}},\quad V_T=\frac{k_BT}{q}
$$

结电容近似为

$$
\boxed{C_j(V)=\frac{C_{j0}}{(1-V/V_{bi})^m}}
$$

RF 等效电路通常包括串联电阻 $R_s$、结电容 $C_j$、动态电阻 $r_d$ 和封装寄生。其速度常由 $R_sC_j$ 时间常数限制：

$$
f_c\sim\frac{1}{2\pi R_sC_j}
$$

Schottky 结由金属-半导体接触形成，多数载流子导电、反向恢复快，适用于检波、混频和高速开关；PN 结通常有少数载流子存储。

### 9.4 MOS 电容与界面 (MOS Capacitor and Interfaces)

单位面积氧化层电容为

$$
\boxed{C_{ox}'=\frac{\varepsilon_{ox}}{t_{ox}}}
$$

p 型衬底 MOS 随栅压经历累积、耗尽和反型。强反型层形成 MOSFET 沟道。界面态和费米能级钉扎会改变阈值、电容、噪声和稳定性；钝化的目标是降低界面陷阱密度 $D_{it}$。

### 9.5 长沟道 MOSFET 基本关系 (Long-Channel MOSFET Relations)

在线性区 $V_{DS}<V_{GS}-V_{TH}$：

$$
I_D=\mu_nC_{ox}'\frac{W}{L}
\left[(V_{GS}-V_{TH})V_{DS}-\frac{V_{DS}^2}{2}\right]
$$

在饱和区：

$$
\boxed{I_D\approx\frac{1}{2}\mu_nC_{ox}'\frac{W}{L}(V_{GS}-V_{TH})^2(1+\lambda V_{DS})}
$$

$$
\boxed{g_m\approx\frac{2I_D}{V_{OV}}=\sqrt{2\mu_nC_{ox}'\frac{W}{L}I_D}},\qquad
r_o\approx\frac{1}{\lambda I_D}
$$

这里 $V_{OV}=V_{GS}-V_{TH}$。短沟道 RF MOSFET 会出现速度饱和，平方律只能提供定性直觉。

### 9.6 FET 小信号与大信号行为 (FET Small- and Large-Signal Behavior)

小信号截止频率的一阶近似：

$$
\boxed{f_T\approx\frac{g_m}{2\pi(C_{gs}+C_{gd})}}
$$

最大振荡频率 $f_{max}$ 还受 $R_g$、$g_{ds}$ 和反馈电容 $C_{gd}$ 限制，通常以功率增益降为 1 的频率定义。大信号输入会造成增益压缩：

$$
G(P_{in})=\frac{P_{out}}{P_{in}}
$$

当实际增益比小信号线性外推低 $1\ \mathrm{dB}$ 时，对应 $P_{1\mathrm{dB}}$。  
*At the 1-dB compression point, gain is 1 dB below the small-signal extrapolation.*

### 9.7 MOSFET、MESFET 与 HEMT (MOSFET, MESFET, and HEMT)

| 器件 | 栅结构 | 主要优势 | 主要限制 |
|---|---|---|---|
| MOSFET | 金属-氧化物-半导体 | 高集成度、低成本、CMOS 系统 | 氧化层与衬底损耗、击穿 |
| MESFET | Schottky 栅/半导体 | 结构直接、III-V 高速 | 栅漏电、栅正向摆幅有限 |
| HEMT/pHEMT | 异质结 + 2DEG | 高迁移率、高 $g_m$、低噪声 | 外延和工艺复杂 |
| GaN HEMT | 极化诱导 2DEG | 高压、高功率密度、高温 | 陷阱、动态导通电阻、热管理 |

设计时不能只比较 $f_T$；还要同时比较 $f_{max}$、噪声系数、输出功率、击穿、效率、线性度和工艺集成度。

---

<h1 id="lec10">第十讲：双极晶体管与 RF 功率半导体</h1>
<h2>Lecture 10: Bipolar Transistors and RF Power Semiconductors</h2>

### 10.1 BJT 的控制关系 (BJT Control Relations)

在正向有源区：

$$
\boxed{I_C\approx I_Se^{V_{BE}/V_T}},\qquad
\boxed{\beta=\frac{I_C}{I_B}},\qquad
\boxed{g_m=\frac{I_C}{V_T}}
$$

$$
r_\pi=\frac{\beta}{g_m},\qquad
r_o\approx\frac{V_A}{I_C}
$$

其中 $V_A$ 描述 Early 效应。BJT 是少数载流子注入器件，基区渡越时间、结电容和电荷存储决定 RF 速度。

### 10.2 $f_T$、$f_{max}$ 与渡越时间 (Cutoff Frequencies and Transit Time)

$$
\boxed{f_T=\frac{g_m}{2\pi(C_\pi+C_\mu)}\approx\frac{1}{2\pi\tau_F}}
$$

$f_T$ 是短路电流增益 $|h_{21}|$ 外推到 1 的频率；$f_{max}$ 是单向功率增益外推到 1 的频率。前者偏向本征输运，后者更敏感于基极/栅极电阻、输出电导和反馈电容。

### 10.3 HBT 与 SiGe HBT (Heterojunction Bipolar Transistor)

HBT 使用宽禁带发射极与窄禁带基区来抑制基区向发射极的反向空穴注入，从而在较高基区掺杂下仍保持高电流增益。高基区掺杂可降低基极电阻，改善 $f_{max}$。SiGe 基区还可通过 Ge 梯度形成准电场，加速载流子通过基区。  
*A wide-bandgap emitter suppresses back injection; a heavily doped base lowers base resistance, and a graded SiGe base accelerates transport.*

Gummel plot 用半对数坐标同时观察 $I_C$、$I_B$ 随 $V_{BE}$ 的变化，可识别理想因子、漏电、复合和电流增益退化。

### 10.4 FET、BJT/HBT 与 BiCMOS 对比 (Device and Integration Comparison)

| 项目 | FET | BJT/HBT |
|---|---|---|
| 控制量 | 栅电压 | 基极电流/$V_{BE}$ |
| 输入阻抗 | 通常较高 | 较低 |
| 跨导效率 | 约 $g_m/I_D\sim2/V_{OV}$ | $g_m/I_C=1/V_T$，通常更高 |
| 噪声/线性 | 依结构和偏置 | HBT 常有高 $g_m$ 与良好线性 |
| 集成 | CMOS 最强 | SiGe BiCMOS 兼顾 RF 与数字 |

BiCMOS 把高速低噪声 HBT 与高密度 CMOS 集成在同一平台，但工艺步骤和成本更高。

### 10.5 LDMOS 与 RF 功率器件 (LDMOS and RF Power Devices)

LDMOS 使用横向漂移区分担高电压，并通过多指布局减小栅电阻和分布寄生。功率器件的重要矛盾是：漂移区加长和减小掺杂可提高击穿电压，却会提高导通电阻。

热阻模型：

$$
\boxed{T_j=T_{case}+P_{diss}R_{\theta JC}}
$$

若包含多层热路径，可用热阻网络或温度依赖热阻进行计算。封装寄生、键合线电感、热界面和散热器都属于功率设计的一部分。

### 10.6 宽禁带半导体与极化 (Wide-Bandgap Semiconductors and Polarization)

| 材料 | 关键优势 | 常见 RF 器件 |
|---|---|---|
| Si | 成本、集成与成熟度 | RF CMOS、LDMOS |
| SiGe | 高性能 HBT + CMOS | SiGe BiCMOS |
| GaAs | 高迁移率、低噪声 | pHEMT、HBT |
| GaN | 高 $E_{crit}$、高功率密度 | GaN HEMT |
| SiC | 高击穿、高热导率 | 高压功率器件、GaN 衬底 |

AlGaN/GaN 中自发极化与压电极化形成界面片电荷，可在无需传统沟道掺杂的情况下产生 2DEG：

$$
\boxed{n_s\approx\frac{|\sigma_{pol}|}{q}}
$$

这同时带来高电流密度和高频能力，但表面/缓冲层陷阱会引起 current collapse、动态 $R_{on}$ 和记忆效应。

---

<h1 id="lec11">第十一讲：RF 增益、稳定性与放大器基础</h1>
<h2>Lecture 11: RF Gain, Stability, and Amplifier Fundamentals</h2>

### 11.1 基本增益量 (Basic Gain Quantities)

$$
A_v=\frac{V_{out}}{V_{in}},\qquad
A_i=\frac{I_{out}}{I_{in}},\qquad
G=\frac{P_{out}}{P_{in}},\qquad
g_m=\frac{\partial I_{out}}{\partial V_{in}}
$$

功率增益使用 $10\log_{10}$，电压/电流幅度比在阻抗相同且为实数时可使用 $20\log_{10}$。不同端口阻抗下不能直接把 $20\log|V_2/V_1|$ 当作功率增益。

### 11.2 源与负载失配下的换能增益 (Transducer Gain with Mismatch)

定义

$$
\Delta=S_{11}S_{22}-S_{12}S_{21}
$$

输入和输出反射系数为

$$
\Gamma_{in}=S_{11}+\frac{S_{12}S_{21}\Gamma_L}{1-S_{22}\Gamma_L}
$$

$$
\Gamma_{out}=S_{22}+\frac{S_{12}S_{21}\Gamma_S}{1-S_{11}\Gamma_S}
$$

换能功率增益：

$$
\boxed{
G_T=
\frac{(1-|\Gamma_S|^2)|S_{21}|^2(1-|\Gamma_L|^2)}
{|(1-S_{11}\Gamma_S)(1-S_{22}\Gamma_L)-S_{12}S_{21}\Gamma_S\Gamma_L|^2}}
$$

若器件近似单向 $S_{12}\approx0$：

$$
G_T\approx
\frac{1-|\Gamma_S|^2}{|1-S_{11}\Gamma_S|^2}
|S_{21}|^2
\frac{1-|\Gamma_L|^2}{|1-S_{22}\Gamma_L|^2}
$$

最大功率传输要求端口共轭匹配：$\Gamma_S=\Gamma_{in}^*$、$\Gamma_L=\Gamma_{out}^*$。双向器件需要联立求解，不能直接令 $\Gamma_S=S_{11}^*$、$\Gamma_L=S_{22}^*$。

### 11.3 稳定性判据 (Stability Criteria)

无条件稳定的 Rollett 条件为

$$
\boxed{K=\frac{1-|S_{11}|^2-|S_{22}|^2+|\Delta|^2}{2|S_{12}S_{21}|}>1}
$$

$$
\boxed{|\Delta|<1}
$$

也可使用 $\mu$ 判据：

$$
\boxed{\mu=\frac{1-|S_{11}|^2}{|S_{22}-\Delta S_{11}^*|+|S_{12}S_{21}|}>1}
$$

若不满足，则为条件稳定，必须在 Smith Chart 上画源/负载稳定圆，选择稳定区域内的匹配点。稳定性必须在完整工作带宽和带外频率检查，而不只是中心频率。

当 $K>1$ 且 $|\Delta|<1$，最大可用增益

$$
\boxed{MAG=\left|\frac{S_{21}}{S_{12}}\right|\left(K-\sqrt{K^2-1}\right)}
$$

若 $K<1$，常引用最大稳定增益

$$
\boxed{MSG=\left|\frac{S_{21}}{S_{12}}\right|}
$$

但 MSG 本身不代表该匹配在实际电路中一定安全。

### 11.4 功率波、dBm 与大信号效率 (Power Waves, dBm, and Efficiency)

对实数参考阻抗 $Z_0$：

$$
a=\frac{V+Z_0I}{2\sqrt{Z_0}},\qquad
b=\frac{V-Z_0I}{2\sqrt{Z_0}},\qquad
P=|a|^2-|b|^2
$$

$$
\boxed{P[\mathrm{dBm}]=10\log_{10}\frac{P}{1\ \mathrm{mW}}}
$$

$$
\boxed{P[\mathrm{W}]=10^{(P_{dBm}-30)/10}}
$$

漏极/集电极效率和功率附加效率：

$$
\boxed{\eta_D=\frac{P_{RF,out}}{P_{DC}}},\qquad
\boxed{PAE=\frac{P_{RF,out}-P_{RF,in}}{P_{DC}}}
$$

不要混淆增益和效率：高增益不必然高效率，高 PAE 也不必然高线性度。

### 11.5 非线性模型与谐波 (Nonlinear Models and Harmonics)

若

$$
y(t)=a_0+a_1x(t)+a_2x^2(t)+a_3x^3(t)+\cdots
$$

单音 $x=A\cos\omega_0t$ 会产生 DC、$2\omega_0$、$3\omega_0$ 等谐波。大信号电路需同时考虑非线性电流源和随电压变化的电荷/电容，常采用谐波平衡 (harmonic balance) 或时域仿真。

### 11.6 匹配、偏置与稳定化网络 (Matching, Biasing, and Stabilization)

典型 RF 放大器由输入匹配、晶体管、输出匹配、偏置网络和稳定化网络组成。Bias-T 的理想目标是让 DC 与 RF 走不同路径：

$$
|X_L|=\omega L\gg Z_0,\qquad
|X_C|=\frac{1}{\omega C}\ll Z_0
$$

实际中应使用多级去耦、四分之一波长高阻线、径向 stub 或合适的 RF choke，并检查元件自谐振。串/并联电阻、反馈和有损匹配可提升稳定性，但通常牺牲增益、噪声或效率。

### 11.7 小信号放大器设计流程 (Small-Signal Amplifier Workflow)

1. 选择偏置点并取得该偏置、温度和频率下的 S 参数/噪声参数。  
2. 检查 $K,|\Delta|$ 或 $\mu$，必要时先稳定化。  
3. 在增益、噪声、输入/输出回波损耗和带宽之间选择 $\Gamma_S,\Gamma_L$。  
4. 用分布或集总网络实现匹配，并加入偏置与去耦。  
5. 联合仿真版图、封装和元件 Q 值，验证带内外稳定性。  
6. 最后检查 P1dB、IIP3、噪声系数和工艺/温度角落。  

---

<h1 id="lec12">第十二讲：功率放大器、接收电路与 RF 系统</h1>
<h2>Lecture 12: Power Amplifiers, Receive Circuits, and RF Systems</h2>

### 12.1 功率放大器类别 (Power-Amplifier Classes)

| 类别 Class | 导通角 | 理想最大效率 | 特点 |
|---|---:|---:|---|
| A | $360^\circ$ | 电阻负载 25%，变压器/谐振负载 50% | 线性最好，静态功耗大 |
| B | $180^\circ$ | $\pi/4\approx78.5\%$ | 推挽恢复完整波形，有交越失真 |
| AB | $180^\circ$ 到 $360^\circ$ | 介于 A 与 B | 线性度和效率折中 |
| C | 小于 $180^\circ$ | 可高于 B | 强非线性，依靠谐振网络恢复基波 |
| D/开关类 | 开关工作 | 理想 100% | 受开关损耗、寄生与带宽限制 |

PA 的最佳负载不是简单的 $Z_0^*$，而是在给定偏置、频率与输入功率下通过负载牵引 (load-pull) 得到的最佳大信号阻抗。

### 12.2 Doherty 与动态负载调制 (Doherty and Load Modulation)

Doherty PA 由 carrier/main 与 peaking/auxiliary 放大器组成。低功率时仅主放工作；接近峰值时辅助放导通，通过四分之一波长阻抗反转器改变主放看到的等效负载，使其在功率回退区仍维持较高效率。  
*The peaking path modulates the carrier amplifier's effective load, improving backed-off efficiency for high-PAPR signals.*

设计关键包括功率分配、相位对齐、器件尺寸比、阻抗反转器带宽和辅助支路开启规律。DC/envelope modulation 则通过随包络改变电源电压提升回退效率。

### 12.3 两音测试、IM3 与截点 (Two-Tone Test, IM3, and Intercept Points)

输入 $f_1,f_2$ 经三阶非线性产生

$$
2f_1-f_2,\qquad 2f_2-f_1
$$

它们最危险，因为靠近有用信号、通常无法滤除。小信号区内，基波输出斜率为 $1\ \mathrm{dB/dB}$，IM3 斜率为 $3\ \mathrm{dB/dB}$。输入三阶截点可由单个工作点估算：

$$
\boxed{IIP3\approx P_{in}+\frac{\Delta_{IM3}}{2}}
$$

$$
\boxed{OIP3\approx P_{out}+\frac{\Delta_{IM3}}{2}},\qquad
OIP3\approx IIP3+G
$$

其中 $\Delta_{IM3}$ 是基波与 IM3 的 dB 间隔。截点是线性外推概念，并非器件可以实际工作的功率点。

### 12.4 ACPR、EVM 与效率折中 (ACPR, EVM, and Efficiency Tradeoff)

邻道功率比

$$
\boxed{ACPR=10\log_{10}\frac{P_{adjacent}}{P_{main}}}
$$

通常为负 dBc，越负表示邻道泄漏越小。EVM 衡量星座点相对理想值的 RMS 误差：

$$
\boxed{EVM_{rms}=\sqrt{\frac{\sum_k|S_k-\hat S_k|^2}{\sum_k|S_k|^2}}}
$$

现代调制具有高 PAPR，PA 必须功率回退以满足 ACPR/EVM，导致平均效率下降。Doherty、包络跟踪和数字预失真分别从负载、电源和信号线性化角度改善这一矛盾。

### 12.5 宽带与行波放大器 (Broadband and Traveling-Wave Amplifiers)

行波放大器把多个晶体管的输入电容和输出电容分别吸收到人工传输线中。若两条线相速度匹配，各级输出在前向端同相叠加，反向波被终端吸收。  
*Distributed amplification trades area and DC power for wide bandwidth by absorbing device capacitances into artificial transmission lines.*

主要限制是线路损耗、终端功耗、相速失配、器件增益随频率下降以及芯片面积。

### 12.6 混频器 (Mixers)

非线性或时变乘法产生和频与差频：

$$
\cos\omega_{RF}t\cos\omega_{LO}t
=\frac{1}{2}\cos(\omega_{RF}-\omega_{LO})t
+\frac{1}{2}\cos(\omega_{RF}+\omega_{LO})t
$$

$$
\boxed{f_{IF}=|f_{RF}-f_{LO}|}
$$

| 指标 | 定义/意义 |
|---|---|
| Conversion gain | $G_c=P_{IF}/P_{RF}$，有源混频器可大于 1 |
| Conversion loss | $L_c=P_{RF}/P_{IF}$，无源混频器常用 |
| Isolation | LO-RF、LO-IF、RF-IF 泄漏 |
| Linearity | P1dB、IIP3、杂散表 |
| Noise | SSB/DSB 噪声系数、$1/f$ 噪声上变频 |

镜像频率满足与目标 RF 相同的 IF 差频，因此接收机通常需要前置选择滤波或 I/Q 架构抑制镜像。

### 12.7 RF 噪声与噪声系数 (RF Noise and Noise Figure)

电阻可用噪声功率：

$$
\boxed{N=k_BT_0B}
$$

电压噪声谱密度：

$$
\boxed{\overline{v_n^2}=4k_BTRB}
$$

噪声因子与噪声系数：

$$
\boxed{F=\frac{SNR_{in}}{SNR_{out}}},\qquad
\boxed{NF=10\log_{10}F}
$$

级联系统 Friis 公式：

$$
\boxed{F_{tot}=F_1+\frac{F_2-1}{G_1}+\frac{F_3-1}{G_1G_2}+\cdots}
$$

所有 $F$ 和 $G$ 必须使用线性值。第一级 LNA 的噪声和增益决定整机噪声性能。

带源失配的四噪声参数形式：

$$
\boxed{F=F_{min}+\frac{4R_n}{Z_0}
\frac{|\Gamma_S-\Gamma_{opt}|^2}
{(1-|\Gamma_S|^2)|1+\Gamma_{opt}|^2}}
$$

最低噪声匹配 $\Gamma_S=\Gamma_{opt}$ 一般不等于最大增益匹配，因此 LNA 必须在 $NF$、增益、稳定性和输入回波损耗之间折中。

### 12.8 低频噪声与相位噪声 (Low-Frequency Noise and Phase Noise)

器件噪声常见组成：热噪声、散粒噪声和闪烁噪声：

$$
\overline{i_{shot}^2}=2qIB,qquad
S_{1/f}(f)\propto\frac{1}{f^\alpha}
$$

混频器和振荡器会把低频 $1/f$ 噪声转换到载波附近。振荡器相位噪声通常以载波偏移 $\Delta f$ 处的单边带功率密度表示，单位 dBc/Hz。

### 12.9 振荡条件与 Leeson 直觉 (Oscillation and Leeson Intuition)

Barkhausen 条件：

$$
\boxed{|A(j\omega_0)\beta(j\omega_0)|=1},\qquad
\boxed{\angle A\beta=2\pi n}
$$

起振时环路增益需略大于 1，振幅增长后由非线性把有效环路增益压回 1。Leeson 型近似显示高 Q、较高载波功率和较低器件噪声可改善相位噪声：

$$
\mathcal{L}(\Delta f)\approx10\log_{10}
\left[\frac{Fk_BT}{2P_s}
\left(1+\left(\frac{f_0}{2Q_L\Delta f}\right)^2\right)
\left(1+\frac{f_c}{|\Delta f|}\right)\right]
$$

倍频器把频率乘以 $N$，理想情况下相位噪声恶化约

$$
\boxed{\Delta\mathcal{L}\approx20\log_{10}N}
$$

### 12.10 收发机前端与集成 (Transceiver Front Ends and Integration)

接收链通常为：天线/双工器 -> 预选滤波 -> LNA -> mixer -> IF/baseband。发射链通常为：基带/IQ -> mixer/upconverter -> driver -> PA -> 滤波/双工器 -> 天线。

| 系统指标 | 主要受哪些模块影响 |
|---|---|
| 灵敏度 Sensitivity | $kTB$、总 NF、所需 SNR |
| 选择性 Selectivity | RF/IF 滤波器、线性度、相位噪声 |
| 最大输入 | LNA/mixer P1dB 与 IIP3 |
| 发射频谱 | PA 线性度、ACPR、LO 泄漏与滤波 |
| 功耗 | PA 平均效率、LNA/LO/数据转换器偏置 |

封装和 PCB 不是理想连接：焊盘、电感、键合线、走线、地回路与热阻必须与芯片协同仿真。SoC 集成度越高，模块间耦合、衬底噪声、供电隔离和热耦合越重要。

---

<h1 id="lec7-12-summary">Lectures 7-12 公式速查与易错点</h1>

### 核心公式速查 (Formula Quick Reference)

| 主题 | 公式 |
|---|---|
| 漂移速度 | $v_d=\mu E$，高场趋近 $v_{sat}$ |
| 电导率 | $\sigma=q(n\mu_n+p\mu_p)$ |
| Einstein 关系 | $D/\mu=k_BT/q$ |
| 二极管 | $I=I_S(e^{V/(nV_T)}-1)$ |
| MOSFET 跨导 | $g_m\approx2I_D/V_{OV}$ |
| BJT 跨导 | $g_m=I_C/V_T$ |
| 截止频率 | $f_T\approx g_m/[2\pi C_{in}]$ |
| 稳定性 | $K>1$ 且 $|\Delta|<1$，或 $\mu>1$ |
| PAE | $(P_{out}-P_{in})/P_{DC}$ |
| IIP3 | $P_{in}+\Delta_{IM3}/2$ |
| 热噪声 | $N=kTB$ |
| 噪声级联 | $F_{tot}=F_1+(F_2-1)/G_1+\cdots$ |
| 混频 | $f_{IF}=|f_{RF}-f_{LO}|$ |
| 振荡 | $|A\beta|=1,\ \angle A\beta=2\pi n$ |

### 最容易混淆的概念 (Common Pitfalls)

1. **$f_T$ vs. $f_{max}$：** $f_T$ 是电流增益边界，$f_{max}$ 是功率增益边界；两者不是器件可正常提供高增益的工作频率。  
2. **小信号共轭匹配 vs. PA 最佳负载：** 小信号共轭匹配用于线性功率传输；PA 的最佳阻抗来自大信号 load-pull。  
3. **增益 vs. 效率：** $G=P_{out}/P_{in}$；$\eta=P_{out}/P_{DC}$；PAE 还扣除 RF 输入功率。  
4. **稳定性中心频率 vs. 全频段稳定性：** 中心频率 $K>1$ 不足以保证电路不会在带外振荡。  
5. **NF 的 dB 值不能直接代入 Friis：** 必须先转换成线性噪声因子和线性增益。  
6. **$\Gamma_{opt}$ vs. 最大增益匹配：** 最低噪声阻抗通常不等于输入共轭匹配。  
7. **IIP3/OIP3 是外推点：** 它们不是实际可达到的无失真输出功率。  
8. **ACPR 符号：** 以 dBc 表示时通常是负值，数值越负越好。  
9. **Barkhausen 条件：** 它描述稳态振荡；可靠起振要求小信号环路增益初始大于 1。  
10. **材料高迁移率不等于器件全面更优：** 还必须比较 $E_{crit}$、热导率、寄生、工艺和成本。

### Lectures 7-12 学习检查清单 (Study Checklist)

- [ ] 能从偏置点写出晶体管小信号线性化参数；
- [ ] 能解释本征模型与 $R/L/C$ 外部寄生的来源；
- [ ] 能用迁移率、饱和速度、禁带、临界电场和热导率比较材料；
- [ ] 能说明注入、光刻、刻蚀、沉积和退火如何影响 RF 参数；
- [ ] 能区分 PN、Schottky、MOS、MOSFET、MESFET、HEMT、BJT 和 HBT；
- [ ] 能解释 LDMOS、GaN HEMT 和 SiGe HBT 的应用优势；
- [ ] 能由 S 参数计算 $\Delta$、$K$、MAG/MSG 和 $G_T$；
- [ ] 能区分 P1dB、IIP3/OIP3、ACPR、EVM、效率与 PAE；
- [ ] 能使用 Friis 公式计算级联 NF；
- [ ] 能说明 LNA 噪声匹配和增益匹配为何不同；
- [ ] 能写出混频频率关系与 Barkhausen 条件；
- [ ] 能从系统角度串联 LNA、mixer、LO、driver、PA、滤波器和天线。

---

<h1 id="appendix">附录</h1>
<h2>Appendix: Constants, Frequency Bands, Unit Conversions</h2>

### A.1 物理常数 (Physical Constants)

| 常数 Constant | 符号 Symbol | 数值 Value | 单位 Unit |
|---|---|---|---|
| 真空介电常数 Vacuum Permittivity | $\varepsilon_0$ | $8.8541878128 \times 10^{-12}$ | F/m |
| 真空磁导率 Vacuum Permeability | $\mu_0$ | $4\pi \times 10^{-7} \approx 1.2566 \times 10^{-6}$ | H/m |
| 真空光速 Speed of Light | $c$ | $2.99792458 \times 10^8$ | m/s |
| 真空特征阻抗 Free-Space Impedance | $\eta_0$ | $\approx 376.73$ | Ω |
| 电子电荷 Electron Charge | $e$ | $1.602176 \times 10^{-19}$ | C |
| 玻尔兹曼常数 Boltzmann Constant | $k_B$ | $1.380649 \times 10^{-23}$ | J/K |

### A.2 常见材料介电常数 (Common Material $\varepsilon_r$)

| 材料 Material | $\varepsilon_r$ | $\tan\delta$ (典型值 Typical) | 典型应用 Application |
|---|---|---|---|
| 真空/空气 Vacuum/Air | 1.0 | 0 | — |
| PTFE (Teflon) | 2.08 | 0.0002 | 半刚性同轴电缆 Semi-rigid coax |
| Rogers RO4003C | 3.38 | 0.0027 | 微波 PCB Microwave PCB |
| 聚酰亚胺 Polyimide | 3.5 | 0.004 | 柔性电路 Flexible circuits |
| FR4 | 4.2-4.8 | 0.02 | 低频数字 PCB Low-freq digital PCB |
| 硅 Si (高阻 High-Res) | 11.7 | 0.005 | Si 基 MMIC Si-based MMIC |
| 砷化镓 GaAs (半绝缘 SI) | 12.9 | 0.0006 | GaAs MMIC |
| 水 Water | ~80 | >0.1 (@ GHz) | — |

### A.3 频率频段划分 (Frequency Band Designations)

| 频段 Band | 频率范围 Freq Range | 典型应用 Typical Application |
|---|---|---|
| VLF | 3 - 30 kHz | 潜艇通信 Submarine communication |
| LF | 30 - 300 kHz | 导航 Navigation |
| MF | 300 kHz - 3 MHz | AM 广播 AM Radio |
| HF | 3 - 30 MHz | 短波广播、业余无线电 Shortwave, amateur radio |
| VHF | 30 - 300 MHz | FM 广播、电视 FM Radio, TV |
| UHF | 300 MHz - 3 GHz | 移动通信、WiFi、GPS、蓝牙 Mobile comm, WiFi, GPS, BT |
| **L-band** | 1 - 2 GHz | GPS、手机卫星 Mobile satellite |
| **S-band** | 2 - 4 GHz | WiFi (2.4G)、气象雷达 Weather radar |
| **C-band** | 4 - 8 GHz | 卫星通信下行 Satellite downlink |
| **X-band** | 8 - 12 GHz | 军用雷达、卫星上行 Military radar, satellite uplink |
| **Ku-band** | 12 - 18 GHz | 卫星广播 Satellite TV |
| **K-band** | 18 - 27 GHz | 卫星通信 Satellite comm |
| **Ka-band** | 27 - 40 GHz | 5G mm-Wave、卫星互联网 Satellite internet |
| **V-band** | 40 - 75 GHz | 点对点通信 Point-to-point |
| **W-band** | 75 - 110 GHz | 汽车雷达 (77 GHz) Automotive radar |
| **mm-Wave** | 30 - 300 GHz | 5G/6G、成像 Imaging |
| **Sub-THz** | 300 GHz - 1 THz | 研究用 Research (400 GHz 发射机 Transmitter) |

### A.4 单位换算 (Unit Conversions)

| 换算关系 Conversion | 公式 Formula |
|---|---|
| Neper → dB | $1 \text{ Np} = 8.686 \text{ dB}$ |
| dB → Neper | $1 \text{ dB} = 0.115 \text{ Np}$ |
| 功率比 → dB | $L_{dB} = 10 \log_{10}(P_2/P_1)$ |
| 电压比 → dB | $L_{dB} = 20 \log_{10}(V_2/V_1)$ |
| dBi → 线性增益 | $G = 10^{G_{dBi}/10}$ |
| dBm → mW | $P_{mW} = 10^{P_{dBm}/10}$ |
| 趋肤深度近似 (铜) | $\delta[\mu\text{m}] \approx 66 / \sqrt{f[\text{MHz}]}$ |

### A.5 反射系数与回波损耗/VSWR 对照 ($\Gamma$, RL, VSWR Lookup)

| $\|\Gamma\|$ | Return Loss [dB] | VSWR | 反射功率百分比 Reflected Power |
|---|---|---|---|
| 0 | ∞ | 1.00 | 0% |
| 0.1 | 20 | 1.22 | 1% |
| 0.2 | 14 | 1.50 | 4% |
| 0.316 | 10 | 1.92 | 10% |
| 0.5 | 6 | 3.00 | 25% |
| 0.707 | 3 | 5.83 | 50% |
| 1.0 | 0 | ∞ | 100% |

---

> **编辑日期 Date Compiled:** 2026-07-19  
> **用途 Purpose:** Obsidian 个人学习笔记 / Personal Study Notes  
> **备注 Note:** 本文档从 496 页、Lectures 1-12 完整课程讲义中提取、整理并双语化。建议在 Obsidian 中使用 `[[wikilinks]]` 交叉引用相关章节。考试时间: 2026 年 9 月 1 日，笔试 90 分钟，闭卷。*Extracted, organized, and bilingualized from the complete 496-page Lectures 1-12 script. Use Obsidian wikilinks for cross-referencing. Exam: 01 Sep 2026, 90 min written, closed book.*
