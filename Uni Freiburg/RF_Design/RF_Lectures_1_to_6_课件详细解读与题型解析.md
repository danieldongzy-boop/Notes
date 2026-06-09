# RF and Microwave Devices and Circuits

## Lectures 1–6 课件详细解读与题型解析

> 原始资料：`Script-Lectures-1-to-6.pdf`  
> 课程：RF- and Microwave Devices and Circuits  
> 说明：本文以中文讲解为主，仅保留必要英文术语。公式统一使用 Obsidian 支持的 `$...$` 与 `$$...$$`。

---

## 0. 如何使用这份笔记

这 233 页课件的主线不是“背很多器件名称”，而是建立一套从电磁场到高频电路的思维链：

1. 为什么频率升高后，普通集总电路方法会失效；
2. 电磁波如何由 Maxwell 方程产生并传播；
3. 为什么高频系统使用功率波和 S 参数，而不直接测电压、电流；
4. 传输线如何改变负载阻抗；
5. 如何用 Smith Chart 做阻抗匹配；
6. 开路枝节、短路枝节、四分之一波长线、功分器和耦合器如何工作；
7. 传输线中的能量最后如何变成自由空间辐射，即天线。

建议按下面的顺序学习：

- 第一遍：理解物理图像，不追求公式推导细节；
- 第二遍：掌握公式中每个量的含义和适用条件；
- 第三遍：练习“归一化、求反射系数、沿线移动、加入电抗、反归一化”；
- 第四遍：把 S 参数、匹配网络、功率和天线增益串成完整系统。

---

# 第一讲：RF 与微波技术为什么不同

## 1.1 RF、Microwave 与毫米波

RF 是射频，英文为 **Radio Frequency**。Microwave 是微波。二者并没有绝对统一的分界，工程上更重要的是判断：

> 电路尺寸是否已经能够和信号波长相比。

真空中的波长为

$$
\lambda_0=\frac{c_0}{f}
$$

其中：

- $\lambda_0$：真空波长；
- $c_0\approx 3\times10^8\ \mathrm{m/s}$：真空光速；
- $f$：频率。

例如：

| 频率 | 真空波长 | 直观意义 |
|---|---:|---|
| $1\ \mathrm{GHz}$ | $30\ \mathrm{cm}$ | PCB 走线已可能不可忽略 |
| $10\ \mathrm{GHz}$ | $3\ \mathrm{cm}$ | 毫米级结构就会产生明显相位差 |
| $100\ \mathrm{GHz}$ | $3\ \mathrm{mm}$ | 芯片互连也必须按传输线处理 |
| $1\ \mathrm{THz}$ | $0.3\ \mathrm{mm}$ | 接近亚毫米波范围 |

介质中的相速度通常低于真空光速，因此导波波长更短：

$$
\lambda_g=\frac{v_p}{f}
$$

对于近似均匀介质，

$$
v_p\approx\frac{c_0}{\sqrt{\varepsilon_r}}
$$

所以

$$
\lambda_g\approx\frac{\lambda_0}{\sqrt{\varepsilon_r}}
$$

微带线的场同时存在于空气和基板中，实际应使用有效介电常数 $\varepsilon_{\mathrm{eff}}$：

$$
\lambda_g\approx\frac{\lambda_0}{\sqrt{\varepsilon_{\mathrm{eff}}}}
$$

### 核心理解

同一段物理长度 $l$，在不同频率下对应不同电长度：

$$
\theta=\beta l=\frac{2\pi l}{\lambda_g}
$$

低频时 $\theta\ll1$，整段导线上的电压几乎同时变化，可以当作理想连接线。

高频时 $\theta$ 不再很小，走线不同位置具有不同相位，导线本身成为电路元件。

---

## 1.2 集总模型何时失效

集总参数模型 **lumped-element model** 假设：

- 元件内部没有显著传播延迟；
- 节点上所有位置具有同一电压；
- 连接线是理想短路；
- 电场和磁场可分别集中在电容与电感中。

常用经验判断是：

$$
l<\frac{\lambda_g}{10}
$$

这不是严格定律，而是工程近似。如果结构接近或超过 $\lambda_g/10$，通常需要考虑分布参数模型 **distributed model**。

### 为什么 Kirchhoff 定律在高频下不能直接照搬

Kirchhoff 定律本身来自 Maxwell 方程的低频近似。高频时：

- 电压和电流随位置变化；
- 电流变化会产生磁场；
- 电荷变化会产生电场；
- 场会以有限速度传播；
- 开路处仍可能有电场和位移电流；
- 导线可能辐射能量。

因此，高频电路不能只问“这个节点电压是多少”，还要问：

- 波向哪个方向传播？
- 相位走了多少？
- 在不连续处反射了多少？
- 结构储存、损耗或辐射了多少能量？

---

## 1.3 RF 技术的应用背景

课件用移动通信、雷达、卫星、传感、数据通信和毫米波器件说明 RF 技术的应用。

这些系统虽然用途不同，但都可以抽象为：

$$
\text{信号源}\rightarrow\text{放大与调制}\rightarrow
\text{传输网络}\rightarrow\text{天线}\rightarrow
\text{传播信道}\rightarrow\text{接收机}
$$

在高频系统中，每个模块之间都存在阻抗接口。工程上最常见的参考阻抗是

$$
Z_0=50\ \Omega
$$

使用 $50\ \Omega$ 的原因不是自然定律，而是功率承受能力、损耗、制造和历史标准之间的折中。

---

## 1.4 第一讲题型：判断是否需要传输线模型

### 题目模板

某 PCB 上有一段长度为 $l$ 的走线，工作频率为 $f$，有效介电常数为 $\varepsilon_{\mathrm{eff}}$。判断能否按理想导线处理。

### 解题步骤

**步骤 1：计算真空波长**

$$
\lambda_0=\frac{c_0}{f}
$$

**步骤 2：计算导波波长**

$$
\lambda_g=\frac{\lambda_0}{\sqrt{\varepsilon_{\mathrm{eff}}}}
$$

**步骤 3：计算长度比例**

$$
\frac{l}{\lambda_g}
$$

**步骤 4：判断**

- 若 $l/\lambda_g\ll0.1$，通常可以先使用集总模型；
- 若 $l/\lambda_g\ge0.1$，应采用传输线模型；
- 对相位精度、宽带或高动态范围系统，即使比例更小也可能需要传输线模型。

### 常见错误

- 错把真空波长直接当作 PCB 上的波长；
- 忘记单位换算；
- 只看频率，不看结构尺寸；
- 把 $\lambda/10$ 当成绝对边界。

---

# 第二讲：Maxwell 方程、波与介质

## 2.1 四个 Maxwell 方程

Maxwell 方程是整门课程的物理基础。

### Gauss 电场定律

$$
\nabla\cdot\mathbf{D}=\rho
$$

含义：电荷是电位移通量的源。

积分形式为

$$
\oint_S\mathbf{D}\cdot d\mathbf{S}=Q_{\mathrm{enc}}
$$

### Gauss 磁场定律

$$
\nabla\cdot\mathbf{B}=0
$$

含义：不存在独立磁荷，磁力线总是闭合的。

### Faraday 电磁感应定律

$$
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}
$$

含义：随时间变化的磁场产生旋转电场。

### Ampère-Maxwell 定律

$$
\nabla\times\mathbf{H}
=\mathbf{J}+\frac{\partial\mathbf{D}}{\partial t}
$$

含义：传导电流和随时间变化的电场都能产生磁场。

其中 $\partial\mathbf{D}/\partial t$ 称为位移电流密度 **displacement current density**。

### 材料关系

在线性、各向同性介质中：

$$
\mathbf{D}=\varepsilon\mathbf{E}
$$

$$
\mathbf{B}=\mu\mathbf{H}
$$

$$
\mathbf{J}=\sigma\mathbf{E}
$$

参数含义：

- $\varepsilon$：介电常数 **permittivity**；
- $\mu$：磁导率 **permeability**；
- $\sigma$：电导率 **conductivity**。

---

## 2.2 电磁波为什么能离开导体传播

变化的电流 $\mathbf{J}$ 产生磁场；变化的磁场又根据 Faraday 定律产生电场；变化的电场再通过位移电流产生磁场。

因此，离开最初的激励源后，变化的 $\mathbf{E}$ 和 $\mathbf{H}$ 可以相互维持并向外传播。

在均匀、无源、无损介质中，电场满足波动方程：

$$
\nabla^2\mathbf{E}
-\mu\varepsilon
\frac{\partial^2\mathbf{E}}{\partial t^2}=0
$$

磁场同样满足：

$$
\nabla^2\mathbf{H}
-\mu\varepsilon
\frac{\partial^2\mathbf{H}}{\partial t^2}=0
$$

由此得到传播速度：

$$
v_p=\frac{1}{\sqrt{\mu\varepsilon}}
$$

在真空中：

$$
c_0=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

---

## 2.3 平面波、传播常数与波阻抗

沿 $+z$ 方向传播的时谐平面波可写成：

$$
\mathbf{E}(z)=\mathbf{E}_0e^{-\gamma z}
$$

传播常数为

$$
\gamma=\alpha+j\beta
$$

其中：

- $\alpha$：衰减常数 **attenuation constant**，单位通常为 $\mathrm{Np/m}$；
- $\beta$：相位常数 **phase constant**，单位为 $\mathrm{rad/m}$。

因此

$$
e^{-\gamma z}=e^{-\alpha z}e^{-j\beta z}
$$

前一项表示幅度衰减，后一项表示相位延迟。

波长与相位常数关系：

$$
\beta=\frac{2\pi}{\lambda}
$$

相速度：

$$
v_p=\frac{\omega}{\beta}
$$

介质波阻抗 **wave impedance** 为

$$
\eta=\frac{E}{H}
$$

无损介质中：

$$
\eta=\sqrt{\frac{\mu}{\varepsilon}}
$$

真空波阻抗约为：

$$
\eta_0\approx377\ \Omega
$$

注意：$377\ \Omega$ 是自由空间平面波中 $E/H$ 的比值，不是射频仪器的 $50\ \Omega$ 端口阻抗。

---

## 2.4 Poynting 向量与功率流

瞬时 Poynting 向量为

$$
\mathbf{S}(t)=\mathbf{E}(t)\times\mathbf{H}(t)
$$

它表示单位面积上的瞬时功率流密度，单位为 $\mathrm{W/m^2}$。

使用相量时，平均功率密度为

$$
\mathbf{S}_{\mathrm{avg}}
=\frac{1}{2}\operatorname{Re}
\left\{\mathbf{E}\times\mathbf{H}^*\right\}
$$

穿过表面 $A$ 的平均功率：

$$
P=\iint_A\mathbf{S}_{\mathrm{avg}}\cdot d\mathbf{A}
$$

### 物理意义

在传输线中，能量并不是简单地“装在铜线里面向前流”。主要功率流位于导体周围的电磁场中，方向由 $\mathbf{E}\times\mathbf{H}$ 决定。

这解释了：

- 为什么改变介质会改变传输特性；
- 为什么金属表面粗糙度会增加损耗；
- 为什么结构不连续会产生反射和辐射；
- 为什么天线可以把导波转换成自由空间波。

---

## 2.5 边界条件

边界条件决定电磁波在材料交界处如何反射、透射和形成导波模式。

在两种介质界面上：

$$
\hat{\mathbf n}\times
\left(\mathbf E_2-\mathbf E_1\right)=0
$$

表示切向电场连续。

$$
\hat{\mathbf n}\times
\left(\mathbf H_2-\mathbf H_1\right)=\mathbf J_s
$$

表示切向磁场的跳变由表面电流密度 $\mathbf J_s$ 决定。

$$
\hat{\mathbf n}\cdot
\left(\mathbf D_2-\mathbf D_1\right)=\rho_s
$$

表示法向电位移的跳变由表面电荷密度 $\rho_s$ 决定。

$$
\hat{\mathbf n}\cdot
\left(\mathbf B_2-\mathbf B_1\right)=0
$$

表示法向磁通密度连续。

对理想导体 **PEC**：

- 导体内部 $\mathbf E=0$；
- 表面切向电场为零；
- 电流集中在表面；
- 入射波会产生反射。

---

## 2.6 TEM、TE 与 TM 模式

假设传播方向为 $z$。

### TEM 模式

$$
E_z=0,\qquad H_z=0
$$

电场和磁场都完全横向。双导体传输线可以支持 TEM 或准 TEM 模式，例如同轴线、双线和近似微带线。

### TE 模式

$$
E_z=0,\qquad H_z\ne0
$$

称为横电模式 **Transverse Electric**。

### TM 模式

$$
H_z=0,\qquad E_z\ne0
$$

称为横磁模式 **Transverse Magnetic**。

空心单导体波导不能支持真正的 TEM 模式，因为 TEM 模式需要至少两个导体建立电势差。

TE 和 TM 模式通常具有截止频率 **cutoff frequency**。低于截止频率时，波不能以传播模式传输，只形成快速衰减的倏逝场。

---

## 2.7 时域与频域

正弦稳态信号：

$$
x(t)=A\cos\left(\omega t+\varphi\right)
$$

可以用相量表示：

$$
\tilde X=Ae^{j\varphi}
$$

在频域中，

$$
\frac{d}{dt}\longrightarrow j\omega
$$

因此微分方程可以转化为代数方程。这是 RF 分析大量使用频域方法的原因。

### 必须注意

频域结果同时包含：

- 幅度；
- 相位；
- 频率响应；
- 群延迟；
- 谐振与带宽。

只看幅度而忽略相位，在匹配、功分、耦合和阵列天线问题中通常会得到错误结论。

---

## 2.8 第二讲题型：波长、相位和传播延迟

### 已知

频率 $f$、传播长度 $l$、相对介电常数或有效介电常数。

### 步骤

1. 求传播速度：

$$
v_p=\frac{c_0}{\sqrt{\varepsilon_{\mathrm{eff}}}}
$$

2. 求导波波长：

$$
\lambda_g=\frac{v_p}{f}
$$

3. 求相位常数：

$$
\beta=\frac{2\pi}{\lambda_g}
$$

4. 求相移：

$$
\theta=\beta l
$$

5. 求传播延迟：

$$
t_d=\frac{l}{v_p}
$$

### 检查方法

- 长度为 $\lambda_g/4$ 时，相移应为 $90^\circ$；
- 长度为 $\lambda_g/2$ 时，相移应为 $180^\circ$；
- 长度为 $\lambda_g$ 时，相移应为 $360^\circ$。

---

# 第三讲：RF 参数与测量

## 3.1 为什么高频不用直接的开路、短路测量

低频二端口可以用 Z、Y、h 等参数描述，但这些参数的测量条件在高频下很难实现。

例如 Z 参数要求某些端口开路。高频“开路”本身具有寄生电容，还可能辐射。

Y 参数要求某些端口短路。高频“短路”具有寄生电感，不再是理想零阻抗。

此外，高频下直接测量瞬时端口电压和电流也非常困难。因此使用容易产生、传输和测量的入射波与反射波。

---

## 3.2 二端口网络

二端口网络 **two-port network** 把器件内部细节封装起来，只研究端口变量。

常见表示法包括：

- Z 参数：阻抗参数；
- Y 参数：导纳参数；
- ABCD 参数：链参数；
- S 参数：散射参数。

### ABCD 参数的优势

级联网络可以直接相乘：

$$
\begin{bmatrix}
V_1\\
I_1
\end{bmatrix}
=
\begin{bmatrix}
A&B\\
C&D
\end{bmatrix}
\begin{bmatrix}
V_2\\
I_2
\end{bmatrix}
$$

若两个网络依次级联：

$$
\mathbf T_{\mathrm{total}}
=\mathbf T_1\mathbf T_2
$$

所以传输线、匹配段和级联滤波器常用 ABCD 参数分析。

---

## 3.3 功率波与 S 参数

对参考阻抗为实数 $Z_0$ 的端口，可将入射波和反射波写成：

$$
a=\frac{V+Z_0I}{2\sqrt{Z_0}}
$$

$$
b=\frac{V-Z_0I}{2\sqrt{Z_0}}
$$

在合适归一化下，$|a|^2$ 与入射功率成正比，$|b|^2$ 与反射或输出功率成正比。

二端口 S 参数定义：

$$
\begin{bmatrix}
b_1\\
b_2
\end{bmatrix}
=
\begin{bmatrix}
S_{11}&S_{12}\\
S_{21}&S_{22}
\end{bmatrix}
\begin{bmatrix}
a_1\\
a_2
\end{bmatrix}
$$

各参数含义：

- $S_{11}$：端口 1 输入反射系数；
- $S_{21}$：从端口 1 到端口 2 的正向传输；
- $S_{12}$：从端口 2 到端口 1 的反向传输；
- $S_{22}$：端口 2 输出反射系数。

测量 $S_{11}$ 与 $S_{21}$ 时，端口 2 必须接匹配负载，因此 $a_2=0$：

$$
S_{11}=\left.\frac{b_1}{a_1}\right|_{a_2=0}
$$

$$
S_{21}=\left.\frac{b_2}{a_1}\right|_{a_2=0}
$$

---

## 3.4 S 参数的 dB 表示

幅度比转为 dB：

$$
S_{ij,\mathrm{dB}}=20\log_{10}|S_{ij}|
$$

因为功率与波幅平方成正比：

$$
10\log_{10}|S_{ij}|^2
=20\log_{10}|S_{ij}|
$$

### 例子

若

$$
|S_{21}|=0.5
$$

则

$$
S_{21,\mathrm{dB}}
=20\log_{10}(0.5)
\approx-6.02\ \mathrm{dB}
$$

这表示输出波功率约为输入波功率的 $25\%$，不是 $50\%$。

---

## 3.5 回波损耗、插入损耗和驻波比

### 回波损耗

$$
RL=-20\log_{10}|\Gamma|
$$

对输入端：

$$
RL=-20\log_{10}|S_{11}|
$$

$RL$ 越大，匹配越好。

### 插入损耗

对无增益的无源二端口，常写为：

$$
IL=-20\log_{10}|S_{21}|
$$

$IL$ 越小，传输损耗越低。

### 电压驻波比

$$
VSWR=\frac{1+|\Gamma|}{1-|\Gamma|}
$$

反算：

$$
|\Gamma|=\frac{VSWR-1}{VSWR+1}
$$

匹配时：

$$
\Gamma=0,\qquad VSWR=1
$$

完全反射时：

$$
|\Gamma|=1,\qquad VSWR\rightarrow\infty
$$

---

## 3.6 无源、互易与无损网络

### 互易网络

若网络由线性、无源、非磁偏置结构构成，通常满足互易性：

$$
S_{21}=S_{12}
$$

### 无损网络

无损网络的 S 矩阵满足酉条件：

$$
\mathbf S^\mathrm H\mathbf S=\mathbf I
$$

对二端口的一列：

$$
|S_{11}|^2+|S_{21}|^2=1
$$

它表示输入功率只能被反射或传输，不能凭空消失。

### 匹配网络

若端口 1 完全匹配：

$$
S_{11}=0
$$

若两个端口都匹配：

$$
S_{11}=S_{22}=0
$$

---

## 3.7 网络分析仪测量思路

矢量网络分析仪 **VNA, Vector Network Analyzer** 测量复数 S 参数，即同时测量幅度和相位。

基本流程：

1. 信号源产生扫频信号；
2. 定向耦合结构分离入射波和反射波；
3. 接收机测量各波的幅度与相位；
4. 通过校准把系统误差参考面移动到待测器件端口；
5. 输出 S 参数随频率的变化。

常见校准件：

- Open：开路；
- Short：短路；
- Load：匹配负载；
- Through：直通。

校准的本质不是“让仪器归零”，而是建立误差模型并消除方向性、跟踪误差和源/负载失配等影响。

---

## 3.8 第三讲题型：由 S 参数计算功率

若端口 2 匹配，向端口 1 提供入射功率 $P_{\mathrm{in}}$：

反射功率：

$$
P_{\mathrm{refl}}=|S_{11}|^2P_{\mathrm{in}}
$$

传输到端口 2 的功率：

$$
P_{\mathrm{out}}=|S_{21}|^2P_{\mathrm{in}}
$$

若器件无源，则耗散或其他端口流失的功率为：

$$
P_{\mathrm{loss}}
=P_{\mathrm{in}}
-P_{\mathrm{refl}}
-P_{\mathrm{out}}
$$

### 解题注意

- S 参数通常是波幅比，计算功率时必须平方；
- dB 转线性幅度使用 $10^{S_{\mathrm{dB}}/20}$；
- dB 转功率比使用 $10^{P_{\mathrm{dB}}/10}$；
- 必须确认未激励端口是否匹配。

---

# 第四讲：导波传播、传输线与 Smith Chart

## 4.1 传输线的分布参数模型

一小段长度 $\Delta z$ 的传输线包含：

- 串联电阻 $R\Delta z$；
- 串联电感 $L\Delta z$；
- 并联电导 $G\Delta z$；
- 并联电容 $C\Delta z$。

其中 $R,L,G,C$ 都是单位长度参数。

Telegrapher 方程为：

$$
\frac{\partial V}{\partial z}
=-RI-L\frac{\partial I}{\partial t}
$$

$$
\frac{\partial I}{\partial z}
=-GV-C\frac{\partial V}{\partial t}
$$

正弦稳态下：

$$
\frac{dV}{dz}=-(R+j\omega L)I
$$

$$
\frac{dI}{dz}=-(G+j\omega C)V
$$

传播常数：

$$
\gamma
=\sqrt{(R+j\omega L)(G+j\omega C)}
$$

特性阻抗：

$$
Z_0
=\sqrt{\frac{R+j\omega L}{G+j\omega C}}
$$

对于无损线 $R=G=0$：

$$
Z_0=\sqrt{\frac{L}{C}}
$$

$$
\gamma=j\beta
$$

$$
\beta=\omega\sqrt{LC}
$$

$$
v_p=\frac{1}{\sqrt{LC}}
$$

---

## 4.2 入射波与反射波

传输线电压可以写成：

$$
V(z)=V^+e^{-\gamma z}+V^-e^{\gamma z}
$$

电流为：

$$
I(z)=\frac{V^+}{Z_0}e^{-\gamma z}
-\frac{V^-}{Z_0}e^{\gamma z}
$$

反射波电流前的负号来自反向传播方向。

负载反射系数：

$$
\Gamma_L
=\frac{V^-}{V^+}
=\frac{Z_L-Z_0}{Z_L+Z_0}
$$

特殊情况：

- $Z_L=Z_0$：$\Gamma_L=0$，无反射；
- $Z_L=0$：$\Gamma_L=-1$，短路；
- $Z_L\rightarrow\infty$：$\Gamma_L=+1$，开路。

反射系数是复数：

$$
\Gamma=|\Gamma|e^{j\varphi}
$$

$|\Gamma|$ 决定反射强度，$\varphi$ 决定反射波相位。

---

## 4.3 输入阻抗

距负载长度为 $l$ 的无损传输线输入阻抗：

$$
Z_{\mathrm{in}}
=Z_0\cdot
\frac{Z_L+jZ_0\tan(\beta l)}
{Z_0+jZ_L\tan(\beta l)}
$$

这条公式是传输线题目的核心。

### 半波长重复

当 $l=\lambda_g/2$：

$$
\tan(\beta l)=\tan(\pi)=0
$$

所以

$$
Z_{\mathrm{in}}=Z_L
$$

阻抗每隔半个导波波长重复一次。

### 四分之一波长变换

当 $l=\lambda_g/4$：

$$
\beta l=\frac{\pi}{2}
$$

得到

$$
Z_{\mathrm{in}}=\frac{Z_0^2}{Z_L}
$$

开路与短路因此会互相转换：

$$
Z_L\rightarrow\infty
\quad\Rightarrow\quad
Z_{\mathrm{in}}\rightarrow0
$$

$$
Z_L=0
\quad\Rightarrow\quad
Z_{\mathrm{in}}\rightarrow\infty
$$

---

## 4.4 驻波

入射波与反射波叠加后形成驻波。

最大电压：

$$
|V|_{\max}=|V^+|(1+|\Gamma|)
$$

最小电压：

$$
|V|_{\min}=|V^+|(1-|\Gamma|)
$$

所以：

$$
VSWR
=\frac{|V|_{\max}}{|V|_{\min}}
=\frac{1+|\Gamma|}{1-|\Gamma|}
$$

相邻电压最大值之间的距离为 $\lambda_g/2$，最大值到相邻最小值的距离为 $\lambda_g/4$。

---

## 4.5 Smith Chart 的数学基础

先将阻抗归一化：

$$
z=\frac{Z}{Z_0}=r+jx
$$

反射系数：

$$
\Gamma=\frac{z-1}{z+1}
$$

反算归一化阻抗：

$$
z=\frac{1+\Gamma}{1-\Gamma}
$$

Smith Chart 实际上是反射系数复平面，只是叠加了等电阻圆和等电抗圆。

### 图上的关键点

- 中心：$z=1$，即 $Z=Z_0$，完全匹配；
- 最左端：$z=0$，短路；
- 最右端：$z\rightarrow\infty$，开路；
- 上半平面：感性电抗 $x>0$；
- 下半平面：容性电抗 $x<0$；
- 外圆：$|\Gamma|=1$，纯无功负载。

---

## 4.6 阻抗图与导纳图

归一化导纳：

$$
y=\frac{Y}{Y_0}=\frac{1}{z}
$$

从阻抗点转换到导纳点，相当于绕 Smith Chart 中心旋转 $180^\circ$。

这一操作在并联元件和并联枝节匹配中非常重要：

- 串联元件适合在阻抗图上处理；
- 并联元件适合在导纳图上处理。

不要把“沿传输线旋转”和“阻抗导纳互换”混为一谈。两者在图上都可能表现为旋转，但物理意义不同。

---

## 4.7 沿传输线移动

反射系数沿无损线变化：

$$
\Gamma(l)=\Gamma_Le^{-j2\beta l}
$$

因此：

- $|\Gamma|$ 不变；
- 只改变相位；
- 在 Smith Chart 上沿等 $|\Gamma|$ 圆移动；
- 向发生器方向移动通常为顺时针；
- 向负载方向移动通常为逆时针。

为什么指数中是 $2\beta l$？

因为反射波相对入射波经历了往返相位差。物理长度为 $\lambda_g/4$ 时：

$$
2\beta l
=2\cdot\frac{2\pi}{\lambda_g}
\cdot\frac{\lambda_g}{4}
=\pi
$$

所以在 Smith Chart 上转过 $180^\circ$。

---

## 4.8 Smith Chart 标准解题流程

### 已知负载 $Z_L$ 和参考阻抗 $Z_0$

**步骤 1：归一化**

$$
z_L=\frac{Z_L}{Z_0}
$$

**步骤 2：在图上找点**

找到等电阻圆 $r$ 与等电抗弧 $x$ 的交点。

**步骤 3：读取反射系数**

由点到中心的距离得到 $|\Gamma|$，角度得到相位。

**步骤 4：若沿线移动**

沿等 $|\Gamma|$ 圆，根据方向和电长度旋转。

**步骤 5：若加入串联元件**

保持归一化电阻 $r$ 不变，改变电抗 $x$。

**步骤 6：若加入并联元件**

先转换成导纳 $y=1/z$，保持电导 $g$ 不变，改变电纳 $b$。

**步骤 7：反归一化**

$$
Z=Z_0z
$$

或

$$
Y=Y_0y
$$

---

## 4.9 传输线损耗

总衰减通常由导体损耗、介质损耗和辐射损耗组成：

$$
\alpha
=\alpha_c+\alpha_d+\alpha_r
$$

### 趋肤效应

趋肤深度：

$$
\delta
=\sqrt{\frac{2}{\omega\mu\sigma}}
=\sqrt{\frac{\rho}{\pi f\mu}}
$$

频率升高时，$\delta$ 变小，电流集中在导体表面，等效导电截面积减小，交流电阻增大。

理想光滑导体的导体损耗通常近似随 $\sqrt f$ 增加。

### 表面粗糙度

当表面起伏尺寸与趋肤深度可比时，电流路径变长，实际损耗高于理想光滑导体模型。

### 介质损耗

介质损耗常用损耗角正切 $\tan\delta_d$ 描述。频率越高，介质损耗通常越明显。

注意区分：

- $\delta$：趋肤深度；
- $\tan\delta_d$：介质损耗角正切。

---

# 第五讲：实际无源结构与阻抗匹配

## 5.1 实际 RF 无源结构

课件列出的实际设计元件包括：

- 开路或短路枝节 **stub**；
- 合路器与功分器 **combiner/divider**；
- 耦合器 **coupler**；
- 隔直电容 **DC-blocking capacitor**；
- 稳定或馈电电感；
- 空气桥 **air bridge**；
- 接地通孔 **via hole**；
- 微带线 **microstrip**；
- 共面波导 **coplanar waveguide**。

这些结构在低频原理图上可能只显示为简单符号，但在高频版图中，尺寸、拐角、接地、间距和过渡都会改变电磁特性。

---

## 5.2 微带线与共面波导

### 微带线

微带线由顶层信号导体、介质基板和背面接地平面组成。

特点：

- 场一部分位于空气，一部分位于介质；
- 传播模式近似为准 TEM；
- 易于制造和连接元件；
- 存在色散、导体损耗、介质损耗和辐射。

### 共面波导

共面波导的中心信号线和两侧地线位于同一平面。

特点：

- 便于并联接地；
- 适合 MMIC 和探针测量；
- 不一定需要大量穿过基板的接地通孔；
- 地线不连续和槽线模式必须认真控制。

选择哪一种结构，不只取决于特性阻抗，还取决于：

- 工艺层结构；
- 基板厚度与介电常数；
- 元件接地方式；
- 功率与损耗；
- 可制造尺寸；
- 是否需要探针测试。

---

## 5.3 开路与短路枝节

无损短路传输线的输入阻抗：

$$
Z_{\mathrm{in,short}}
=jZ_0\tan(\beta l)
$$

无损开路传输线的输入阻抗：

$$
Z_{\mathrm{in,open}}
=-jZ_0\cot(\beta l)
$$

当长度较短时：

- 短路枝节通常表现为感性；
- 开路枝节通常表现为容性。

但这种等效只在指定频率附近成立。频率变化后，$\beta l$ 变化，等效电抗也随之变化。

### 四分之一波长枝节

长度为 $\lambda_g/4$ 时：

- 开路枝节输入端表现为短路；
- 短路枝节输入端表现为开路。

可用于：

- 偏置网络 **bias tee**；
- RF 接地；
- 谐波开路或短路；
- 阻抗匹配；
- 滤波和谐振。

---

## 5.4 四分之一波长阻抗变换器

设源侧阻抗为 $Z_S$，负载为纯电阻 $Z_L$，中间加入长度为 $\lambda_g/4$、特性阻抗为 $Z_t$ 的传输线。

四分之一波长线的输入阻抗：

$$
Z_{\mathrm{in}}=\frac{Z_t^2}{Z_L}
$$

为了匹配 $Z_S$：

$$
Z_S=\frac{Z_t^2}{Z_L}
$$

所以：

$$
Z_t=\sqrt{Z_SZ_L}
$$

### 解题步骤

1. 确认两端阻抗是实数，或已在中心频率处变换成实数；
2. 用几何平均求 $Z_t$；
3. 计算中心频率下的导波波长；
4. 取物理长度 $l=\lambda_g/4$；
5. 检查工艺是否能实现该特性阻抗；
6. 检查所需带宽。

### 局限

四分之一波长匹配是窄带方法。频率偏离设计中心后，电长度不再是 $90^\circ$，匹配性能下降。

---

## 5.5 单枝节匹配

单枝节匹配 **single-stub matching** 的目标是：

1. 先沿主传输线移动到某个位置，使归一化导纳的实部变为 $1$；
2. 再并联一个纯电纳枝节，抵消剩余虚部。

若移动后：

$$
y=1+jb
$$

则枝节应提供：

$$
y_{\mathrm{stub}}=-jb
$$

总导纳为：

$$
y_{\mathrm{total}}
=1+jb-jb
=1
$$

于是实现匹配。

### 为什么通常会有两个解

等 $|\Gamma|$ 圆一般与 $g=1$ 圆有两个交点，因此常有两组“枝节位置 + 枝节长度”。

选择时考虑：

- 哪个枝节更短；
- 开路还是短路更容易制造；
- 是否容易接地；
- 带宽和损耗；
- 是否靠近不适合布线的位置。

---

## 5.6 功分器

简单 T 结可以分配功率，但不一定同时实现：

- 所有端口匹配；
- 输出端口隔离；
- 等幅同相；
- 无损。

这是多端口网络的基本限制。实际设计必须明确优先目标。

### Wilkinson 功分器

等分 Wilkinson 功分器由两段四分之一波长线和一个输出端口间的隔离电阻构成。

对于系统阻抗 $Z_0$：

$$
Z_{\lambda/4}=\sqrt2Z_0
$$

隔离电阻：

$$
R=2Z_0
$$

当 $Z_0=50\ \Omega$：

$$
Z_{\lambda/4}\approx70.7\ \Omega
$$

$$
R=100\ \Omega
$$

理想情况下：

- 输入端匹配；
- 两输出端等幅同相；
- 输出端之间隔离；
- 输出负载平衡时，隔离电阻几乎不耗散功率。

每个输出端的理想传输幅度：

$$
|S_{21}|=|S_{31}|=\frac{1}{\sqrt2}
$$

对应：

$$
20\log_{10}\frac{1}{\sqrt2}
\approx-3.01\ \mathrm{dB}
$$

这 $3\ \mathrm{dB}$ 主要来自功率被平均分成两路，不应直接称为耗散损耗。

---

## 5.7 定向耦合器

定向耦合器 **directional coupler** 通常有四个端口：

- 输入端；
- 直通端；
- 耦合端；
- 隔离端。

耦合度：

$$
C=-20\log_{10}|S_{\mathrm{coupled,input}}|
$$

隔离度：

$$
I=-20\log_{10}|S_{\mathrm{isolated,input}}|
$$

方向性：

$$
D=I-C
$$

方向性越高，越能准确区分正向波和反向波。VNA 测量反射波时需要这一能力。

---

## 5.8 第五讲综合匹配题流程

### 题目给定

- 负载阻抗 $Z_L$；
- 参考阻抗 $Z_0$；
- 工作频率 $f_0$；
- 匹配网络类型。

### 通用步骤

1. 归一化：

$$
z_L=\frac{Z_L}{Z_0}
$$

2. 判断负载是感性还是容性；
3. 选择串联或并联匹配路径；
4. 在 Smith Chart 上完成几何变换；
5. 读取归一化电抗或电纳；
6. 反归一化；
7. 将电抗转换成元件值：

$$
X_L=\omega L
$$

$$
X_C=-\frac{1}{\omega C}
$$

$$
B_C=\omega C
$$

$$
B_L=-\frac{1}{\omega L}
$$

8. 若使用枝节，再由所需电抗或电纳求电长度；
9. 使用 $\lambda_g$ 换算物理长度；
10. 最后检查 $S_{11}$、带宽、损耗和可制造性。

---

# 第六讲：天线基础与现代天线

## 6.1 天线的本质

天线完成两种模式之间的转换：

$$
\text{导波模式}
\longleftrightarrow
\text{自由空间辐射模式}
$$

发射时，传输线中的受约束电磁场在天线结构中形成时变电流和电荷分布，产生能够脱离结构传播的电磁波。

接收时，自由空间电磁波在天线上感应电压和电流，并把功率送入接收机。

根据互易原理，线性互易天线的发射方向图和接收方向图相同。

---

## 6.2 近场与远场

天线周围通常区分：

- 反应近场 **reactive near field**；
- 辐射近场 **radiating near field**；
- 远场 **far field**。

在远场中：

- $\mathbf E$ 与 $\mathbf H$ 近似互相垂直；
- 二者都垂直于传播方向；
- $E/H$ 接近介质波阻抗；
- 场幅度近似按 $1/r$ 衰减；
- 功率密度按 $1/r^2$ 衰减；
- 方向图与距离基本无关。

常用远场判据：

$$
r\gtrsim\frac{2D^2}{\lambda}
$$

其中 $D$ 是天线最大尺寸。

---

## 6.3 辐射方向图、波束宽度和旁瓣

辐射方向图 **radiation pattern** 表示辐射强度随方向的变化。

关键术语：

- 主瓣 **main lobe**：最大辐射方向附近的波束；
- 旁瓣 **side lobe**：非主方向上的局部峰值；
- 后瓣 **back lobe**：与主波束大致相反的辐射；
- 零点 **null**：辐射很弱或理论为零的方向；
- 半功率波束宽度 **HPBW**：功率降至最大值一半，即 $-3\ \mathrm{dB}$ 两点间的角宽。

波束越窄，通常方向性越高，但具体关系取决于二维方向图和天线结构。

---

## 6.4 辐射强度与方向性

远场功率密度为 $S_{\mathrm{avg}}$，辐射强度定义：

$$
U(\theta,\phi)=r^2S_{\mathrm{avg}}(r,\theta,\phi)
$$

总辐射功率：

$$
P_{\mathrm{rad}}
=\int_{4\pi}U(\theta,\phi)d\Omega
$$

平均辐射强度：

$$
U_{\mathrm{avg}}=\frac{P_{\mathrm{rad}}}{4\pi}
$$

方向性：

$$
D(\theta,\phi)
=\frac{U(\theta,\phi)}{U_{\mathrm{avg}}}
=\frac{4\pi U(\theta,\phi)}{P_{\mathrm{rad}}}
$$

最大方向性：

$$
D_0=\frac{4\pi U_{\max}}{P_{\mathrm{rad}}}
$$

方向性只描述功率在空间中的集中程度，不包含天线内部损耗。

---

## 6.5 天线效率与增益

天线增益：

$$
G=\eta_{\mathrm{ant}}D
$$

其中：

- $D$：方向性；
- $\eta_{\mathrm{ant}}$：天线效率；
- $G$：增益。

以 dB 表示：

$$
G_{\mathrm{dBi}}=10\log_{10}G
$$

dBi 表示相对于理想各向同性天线的增益。

必须区分：

- 高方向性不等于高效率；
- 高增益通常要求较高方向性和较低损耗；
- 阻抗失配还会进一步减少实际接受或辐射的功率。

若把失配也计入，可使用实现增益 **realized gain**：

$$
G_{\mathrm{realized}}
=(1-|\Gamma|^2)G
$$

---

## 6.6 有效孔径

接收天线从入射波中提取功率的能力可用有效孔径 **effective aperture** 表示：

$$
A_e=\frac{\lambda^2G}{4\pi}
$$

若入射功率密度为 $S$，理想极化和方向匹配下，可接收功率：

$$
P_r=SA_e
$$

该式说明：

- 增益越大，有效接收面积越大；
- 在相同增益下，波长越长，有效孔径越大；
- 物理面积和有效孔径不是同一个概念。

---

## 6.7 自由空间链路

自由空间中，发射天线距离 $r$ 处的功率密度：

$$
S=\frac{P_tG_t}{4\pi r^2}
$$

接收天线功率：

$$
P_r=SA_{e,r}
$$

代入有效孔径：

$$
P_r
=P_tG_tG_r
\left(\frac{\lambda}{4\pi r}\right)^2
$$

这就是自由空间 Friis 传输关系。

以 dB 表示：

$$
P_r[\mathrm{dBm}]
=P_t[\mathrm{dBm}]
+G_t[\mathrm{dBi}]
+G_r[\mathrm{dBi}]
-L_{\mathrm{FS}}[\mathrm{dB}]
$$

自由空间路径损耗：

$$
L_{\mathrm{FS}}
=20\log_{10}\left(\frac{4\pi r}{\lambda}\right)
$$

实际链路还要加入：

- 馈线损耗；
- 阻抗失配损耗；
- 极化失配；
- 指向误差；
- 大气和雨衰；
- 障碍物与多径。

---

## 6.8 极化

极化 **polarization** 描述固定空间点上电场矢量随时间的轨迹。

主要形式：

- 线极化；
- 圆极化；
- 椭圆极化。

若发射与接收天线极化不匹配，会产生极化损耗。

两线极化天线夹角为 $\psi$ 时，极化功率因子：

$$
PLF=|\hat{\mathbf e}_t\cdot\hat{\mathbf e}_r|^2
=\cos^2\psi
$$

当二者正交时，理想情况下：

$$
PLF=0
$$

---

## 6.9 阵列天线与波束控制

阵列天线由多个辐射单元组成。总方向图通常可理解为：

$$
\text{总方向图}
=\text{单元方向图}
\times\text{阵列因子}
$$

通过控制各单元的：

- 幅度；
- 相位；
- 间距；
- 排列方式；

可以控制主波束方向、波束宽度、旁瓣和零点。

相控阵 **phased array** 不需要机械旋转，而是通过改变单元相位实现电子扫描。

### 栅瓣

若阵元间距过大，不同方向可能同时满足相位叠加条件，出现强栅瓣 **grating lobes**。

常见设计经验是：

$$
d\le\frac{\lambda}{2}
$$

但扫描范围较大时，允许间距可能还要更小。

---

## 6.10 毫米波与片上天线

频率升高后，波长变短，天线尺寸也随之缩小，因此可以把天线集成到芯片或封装中。

但片上天线并不自动意味着高性能。主要挑战包括：

- 硅等基板损耗高；
- 金属层薄，导体损耗明显；
- 芯片尺寸和接地结构限制辐射；
- 封装会改变方向图和谐振频率；
- 天线与有源电路之间存在耦合；
- 测量校准困难。

因此现代天线设计往往是芯片、封装、天线和系统的联合设计。

---

## 6.11 第六讲链路预算题

### 已知

- 发射功率 $P_t$；
- 发射增益 $G_t$；
- 接收增益 $G_r$；
- 距离 $r$；
- 频率 $f$；
- 其他损耗 $L_{\mathrm{other}}$。

### 步骤

1. 计算波长：

$$
\lambda=\frac{c_0}{f}
$$

2. 计算自由空间路径损耗：

$$
L_{\mathrm{FS}}
=20\log_{10}
\left(\frac{4\pi r}{\lambda}\right)
$$

3. 在 dB 域相加减：

$$
P_r
=P_t+G_t+G_r
-L_{\mathrm{FS}}
-L_{\mathrm{other}}
$$

4. 与接收机灵敏度比较；
5. 计算链路余量：

$$
M=P_r-P_{\mathrm{sens}}
$$

### 常见错误

- $r$ 和 $\lambda$ 使用不同长度单位；
- 把 dBi 当作线性倍数直接相乘；
- 忘记馈线和失配损耗；
- 在非远场条件下直接套 Friis 公式；
- 忘记检查极化和天线方向。

---

# 课程知识总串联

## 7.1 从 Maxwell 方程到 S 参数

完整逻辑如下：

1. Maxwell 方程决定电磁场；
2. 材料和边界条件决定允许的传播模式；
3. 传播模式决定传输线的 $Z_0$、$\gamma$ 和场分布；
4. 负载与 $Z_0$ 不同会产生反射；
5. 反射和传输用功率波表示；
6. 功率波之间的线性关系就是 S 参数；
7. Smith Chart 把阻抗和反射系数建立可视化映射；
8. 匹配网络通过改变阻抗来减小 $S_{11}$；
9. 功分器和耦合器控制功率的方向、比例和相位；
10. 天线把导波转换为自由空间波。

---

## 7.2 高频题目的统一思维

遇到任何 RF 题目，先回答五个问题：

### 1. 参考阻抗是什么

通常为 $50\ \Omega$，但不能默认所有题目都如此。

### 2. 使用的是阻抗、电压波还是功率

三者公式不同，不能混用。

### 3. 当前量是线性值还是 dB

- 电压或波幅比：$20\log_{10}$；
- 功率比：$10\log_{10}$。

### 4. 使用真空波长还是导波波长

传输线物理长度一般必须使用 $\lambda_g$。

### 5. 端口和参考面在哪里

移动参考面会改变反射系数相位，也会改变看到的输入阻抗。

---

# 典型综合例题

## 例题 1：负载反射与功率

已知：

$$
Z_0=50\ \Omega
$$

$$
Z_L=100\ \Omega
$$

入射功率为 $10\ \mathrm{mW}$。

### 第一步：反射系数

$$
\Gamma_L
=\frac{Z_L-Z_0}{Z_L+Z_0}
=\frac{100-50}{100+50}
=\frac13
$$

### 第二步：回波损耗

$$
RL=-20\log_{10}\frac13
\approx9.54\ \mathrm{dB}
$$

### 第三步：反射功率

$$
P_{\mathrm{refl}}
=|\Gamma|^2P_{\mathrm{in}}
=\frac19\cdot10\ \mathrm{mW}
\approx1.11\ \mathrm{mW}
$$

### 第四步：送入负载的功率

若传输线无损：

$$
P_L=P_{\mathrm{in}}-P_{\mathrm{refl}}
\approx8.89\ \mathrm{mW}
$$

### 易错点

反射功率比例是 $|\Gamma|^2=1/9$，不是 $|\Gamma|=1/3$。

---

## 例题 2：四分之一波长匹配

用四分之一波长线把 $50\ \Omega$ 系统匹配到 $100\ \Omega$ 纯电阻负载。

所需变换线特性阻抗：

$$
Z_t=\sqrt{50\cdot100}
\approx70.71\ \Omega
$$

若中心频率为 $10\ \mathrm{GHz}$，有效介电常数为 $2.25$：

$$
\lambda_0
=\frac{3\times10^8}{10^{10}}
=30\ \mathrm{mm}
$$

$$
\lambda_g
=\frac{30}{\sqrt{2.25}}
=20\ \mathrm{mm}
$$

所以理想电长度对应的物理长度：

$$
l=\frac{\lambda_g}{4}=5\ \mathrm{mm}
$$

实际版图还需要考虑开路端效应、色散、金属厚度和过渡不连续。

---

## 例题 3：由 $S_{11}$ 求 VSWR

若：

$$
S_{11}=-10\ \mathrm{dB}
$$

先转换为线性幅度：

$$
|\Gamma|
=10^{-10/20}
\approx0.316
$$

然后：

$$
VSWR
=\frac{1+0.316}{1-0.316}
\approx1.92
$$

反射功率比例：

$$
|\Gamma|^2\approx0.1
$$

即约 $10\%$ 的入射功率被反射。

---

## 例题 4：Wilkinson 功分器

设计一个 $50\ \Omega$ 等分 Wilkinson 功分器。

### 四分之一波长支路线阻抗

$$
Z_t=\sqrt2\cdot50
\approx70.7\ \Omega
$$

### 输出隔离电阻

$$
R=2\cdot50=100\ \Omega
$$

### 理想传输

$$
S_{21}=S_{31}
=\frac{1}{\sqrt2}
$$

$$
20\log_{10}\frac{1}{\sqrt2}
\approx-3.01\ \mathrm{dB}
$$

如果仿真中每路为 $-3.4\ \mathrm{dB}$，额外的约 $0.4\ \mathrm{dB}$ 才主要来自实际损耗和不理想效应。

---

## 例题 5：自由空间链路

给定：

- $f=10\ \mathrm{GHz}$；
- $r=100\ \mathrm{m}$；
- $P_t=20\ \mathrm{dBm}$；
- $G_t=G_r=20\ \mathrm{dBi}$；
- 其他损耗共 $3\ \mathrm{dB}$。

波长：

$$
\lambda=\frac{3\times10^8}{10^{10}}
=0.03\ \mathrm{m}
$$

路径损耗：

$$
L_{\mathrm{FS}}
=20\log_{10}
\left(\frac{4\pi\cdot100}{0.03}\right)
\approx92.44\ \mathrm{dB}
$$

接收功率：

$$
P_r
=20+20+20-92.44-3
\approx-35.44\ \mathrm{dBm}
$$

---

# 高频考试速查表

## 波与传播

$$
\lambda=\frac{v_p}{f}
$$

$$
\beta=\frac{2\pi}{\lambda}
$$

$$
\theta=\beta l
$$

$$
\gamma=\alpha+j\beta
$$

## 反射与驻波

$$
\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0}
$$

$$
Z_L=Z_0\frac{1+\Gamma}{1-\Gamma}
$$

$$
VSWR=\frac{1+|\Gamma|}{1-|\Gamma|}
$$

$$
RL=-20\log_{10}|\Gamma|
$$

## 传输线

$$
Z_{\mathrm{in}}
=Z_0\cdot
\frac{Z_L+jZ_0\tan(\beta l)}
{Z_0+jZ_L\tan(\beta l)}
$$

$$
Z_{\mathrm{in},\lambda/4}
=\frac{Z_0^2}{Z_L}
$$

## S 参数功率

$$
P_{\mathrm{refl}}
=|S_{11}|^2P_{\mathrm{in}}
$$

$$
P_{\mathrm{out}}
=|S_{21}|^2P_{\mathrm{in}}
$$

## 天线

$$
G=\eta D
$$

$$
A_e=\frac{\lambda^2G}{4\pi}
$$

$$
P_r
=P_tG_tG_r
\left(\frac{\lambda}{4\pi r}\right)^2
$$

---

# 最容易混淆的概念

| 概念 A | 概念 B | 区别 |
|---|---|---|
| 特性阻抗 $Z_0$ | 输入阻抗 $Z_{\mathrm{in}}$ | $Z_0$ 是传输线自身属性，$Z_{\mathrm{in}}$ 还取决于负载和长度 |
| 波阻抗 $\eta$ | 端口参考阻抗 | $\eta=E/H$，端口阻抗用于定义电压、电流和功率波 |
| 反射系数 $|\Gamma|$ | 反射功率比例 | 后者为 $|\Gamma|^2$ |
| 回波损耗 | 插入损耗 | 前者描述反射，后者描述传输衰减 |
| 方向性 $D$ | 增益 $G$ | 增益包含效率 |
| 导波波长 $\lambda_g$ | 真空波长 $\lambda_0$ | 介质和结构会缩短导波波长 |
| 电长度 | 物理长度 | 电长度随频率和传播速度变化 |
| 阻抗图 | 导纳图 | 串联操作常用阻抗，并联操作常用导纳 |
| $-3\ \mathrm{dB}$ 功分 | $3\ \mathrm{dB}$ 损耗 | 理想二等分本来每路就是一半功率，不代表能量耗散 |

---

# 学习检查清单

完成本课件后，应当能够：

- 解释为什么高频下导线必须视为传输线；
- 从频率和介质参数计算导波波长、电长度和延迟；
- 说明 Maxwell 方程如何支持电磁波传播；
- 区分 TEM、TE 和 TM 模式；
- 使用 Poynting 向量解释功率流；
- 计算负载反射系数、回波损耗和 VSWR；
- 解释 $S_{11}$、$S_{21}$、$S_{12}$ 和 $S_{22}$；
- 根据 S 参数计算反射功率和传输功率；
- 使用传输线输入阻抗公式；
- 解释半波长重复和四分之一波长阻抗反转；
- 在 Smith Chart 中完成归一化、移动和反归一化；
- 区分串联匹配与并联匹配；
- 设计四分之一波长变换器和基本枝节匹配；
- 说明 Wilkinson 功分器的阻抗和隔离电阻；
- 区分天线方向性、效率、增益和实现增益；
- 完成基本自由空间链路预算；
- 识别毫米波片上天线的主要工程限制。
