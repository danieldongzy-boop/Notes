# CDAC settling time 公式比较

> 目标：把你笔记里的 CDAC settling time 推导，和网上/论文里常见的几种 settling 公式放到同一个框架里比较。本文截图都来自资料原页渲染，不是手画图。

## 一句话结论

你的公式和网上常见公式不是互相矛盾，而是**建模层级不同**：

- 常见资料多把 DAC/CDAC 看成黑盒一阶系统，直接写 $V_{err}(t)=V_0e^{-t/\tau}$，然后要求误差小于 $1/2$ LSB。
- 你的笔记进一步从 top plate / bottom plate KCL 推出 $\tau$ 的来源：底板寄生、顶板寄生、开关电阻共同决定 settling。
- 你得到的 $t_{settle}=\tau\ln x$ 和论文里常见的 $N\tau\ln2$、$(N+1)\tau\ln2$ 本质都来自同一个式子，只是最大阶跃幅度 $V_0$、精度要求、阵列结构不同。

## 公式总览

| 类型 | 常见公式 | 适用场景 | 和你的区别 |
|---|---|---|---|
| 普通采样电容 settling | $t=-\tau\ln(E)$，或按 $1/2$ LSB 推出约 $t\approx (N+1)\tau\ln2$ | 输入采样电容、外部源阻抗、ADC tracking phase | 关注输入采样，不一定是 SAR 内部 CDAC bit cycling |
| SAR/CDAC 黑盒误差 | $V_{err}(t)=V_0e^{-t/\tau}$ | 只关心某次 DAC step 是否 settle 到精度内 | 没展开 $\tau$ 来自哪些寄生/开关 |
| redundancy 放宽 settling | 前几位只需较低 bit 精度，例如 3-bit/4-bit accurate settling | 非二进制/冗余 SAR | 通过数字冗余容忍 settling error，而不是严格每步 $1/2$ LSB |
| 你的 KCL 推导 | $\tau=RC_u(\alpha_P+\frac{\alpha_T}{1+\alpha_T})$，$t\ge\tau\ln x$ | split CDAC，考虑 top/bottom parasitic | 更像 transistor-level/CDAC-internal model |

## 截图资料

### 截图 1：普通 switched-capacitor ADC 的 settling time 公式

![Silicon Labs AN119 settling formula](source-silabs-settling-formula.png)

来源：[Silicon Labs AN119](https://www.silabs.com/documents/public/application-notes/AN119.pdf)。这类资料通常从一阶 RC 充电出发，关注 sampling capacitor 在 tracking phase 内能否 settle 到目标精度。

### 截图 2：SAR ADC 论文里的 settling error / redundancy 思路

![UM redundant SAR settling error](source-um-settling-error.png)

![UM redundant SAR redundancy time](source-um-redundancy-time.png)

来源：[A 10-bit SAR ADC With Two Redundant Decisions...](https://ime.um.edu.mo/wp-content/uploads/presentations/9777b0f6afb9a111dc187745bb7c0484.pdf)。这篇的重点不是展开 CDAC 寄生，而是说明 settling error 会导致错误比较，并用 redundancy 放宽 DAC settling requirement。

### 截图 3：高速 SAR 里 DAC settling 是 SAR loop delay 的一部分

![Stanford SAR loop delay](source-stanford-sar-loop-delay.png)

![Stanford pole-zero CDAC settling](source-stanford-pole-zero.png)

![Stanford time-domain DAC switching](source-stanford-time-domain.png)

来源：[Stanford thesis on high-speed SAR / two-CDAC pipelined SAR](https://stacks.stanford.edu/file/druid%3Ajc388fn7862/VaibhavT_thesis_final-augmented.pdf)。这份资料强调 SAR loop delay 由 DAC settling、comparator decision、SAR logic delay 组成，并讨论通过 CDAC / switch resistance / pole-zero cancellation 提高 DAC settling speed。

## 共同母公式

大多数 settling time 公式都能回到这个一阶残差模型：

$$
V_{err}(t)=V_0e^{-t/\tau}
$$

要求最终误差小于允许误差 $V_{tol}$：

$$
V_0e^{-t/\tau}\le V_{tol}
$$

两边取对数：

$$
t\ge \tau\ln\left(\frac{V_0}{V_{tol}}\right)
$$

所以所有差别都藏在三个量里：

1. $\tau$ 怎么定义；
2. 初始误差/阶跃 $V_0$ 多大；
3. 容许误差 $V_{tol}$ 取多少。

## 普通 $N\tau\ln2$ 或 $(N+1)\tau\ln2$ 怎么来的

如果要求 settle 到 $1/2$ LSB：

$$
V_{tol}=\frac{V_{FS}}{2^{N+1}}
$$

如果最坏初始阶跃大约是满量程：

$$
V_0\approx V_{FS}
$$

那么：

$$
t\ge\tau\ln\left(\frac{V_{FS}}{V_{FS}/2^{N+1}}\right)
=(N+1)\tau\ln2
$$

如果认为最坏 CDAC step 是 $V_{FS}/2$，则：

$$
t\ge\tau\ln\left(\frac{V_{FS}/2}{V_{FS}/2^{N+1}}\right)
=N\tau\ln2
$$

所以网上看到的 $N\tau\ln2$、$(N+1)\tau\ln2$，主要差在他们把最大 step 取成 $V_{FS}/2$ 还是 $V_{FS}$。

## 你的公式怎么来的

你笔记的电路模型是：

- $n$ 个单位电容 $C_u$；
- 顶板节点为 $V_{DAC}$；
- 第 $k$ 个底板节点为 $V_k$；
- 底板由参考 $V_{Rk}$ 通过开关电阻 $R$ 驱动；
- 顶板寄生 $C_T=n\alpha_TC_u$；
- 每个底板寄生 $C_P=\alpha_PC_u$。

### 1. 顶板 KCL

顶板浮动，因此单位电容电流和顶板寄生电流满足：

$$
\sum_{k=1}^{n}C_u(\dot V_{DAC}-\dot V_k)=-C_T\dot V_{DAC}
$$

整理：

$$
\sum_{k=1}^{n}\dot V_k=n(1+\alpha_T)\dot V_{DAC}
$$

积分：

$$
\sum_{k=1}^{n}V_k=n(1+\alpha_T)V_{DAC}-M
$$

这个式子说明：底板总变化通过电容耦合到顶板，但顶板寄生会稀释顶板变化。

### 2. 底板 KCL

每个底板节点通过 $R$ 被参考电压驱动，同时要给 $C_u$ 和底板寄生 $C_P$ 充放电：

$$
RC_u(\dot V_{DAC}-\dot V_k)=RC_P\dot V_k+(V_k-V_{Rk})
$$

对所有 $k$ 求和并代入顶板关系，得到一阶微分方程：

$$
\tau\dot V_{DAC}+V_{DAC}=\frac{1}{n(1+\alpha_T)}\left(M+\sum_{k=1}^{n}V_{Rk}\right)
$$

其中：

$$
\tau=RC_u\left(\alpha_P+\frac{\alpha_T}{1+\alpha_T}\right)
$$

这个 $\tau$ 很有意思：如果 $\alpha_P=0$ 且 $\alpha_T=0$，模型里 $\tau=0$，表示理想电容阵列在电荷重分布下瞬时到最终值。真正拖慢它的是寄生电容和有限开关电阻。

### 3. 指数响应

一阶方程解为：

$$
V_{DAC}(t)=V_{DAC}(\infty)+[V_{DAC}(0)-V_{DAC}(\infty)]e^{-t/\tau}
$$

也就是：

$$
\Delta V_{DAC}(t)=\Delta V_{DAC}(\infty)(1-e^{-t/\tau})
$$

残差误差：

$$
V_{err}(t)=\Delta V_{DAC}(\infty)e^{-t/\tau}
$$

### 4. 为什么得到 $t\ge\tau\ln x$

如果一次切换了 $x$ 个单位电容，且底板参考阶跃为 $\Delta V_X$，则最终顶板变化：

$$
\Delta V_{DAC}(\infty)=\frac{x}{n(1+\alpha_T)}\Delta V_X
$$

若这里 $\Delta V_X=V_{FS}/2$，而有效 $1/2$ LSB 为：

$$
V_{tol}=\frac{V_{FS}}{2n(1+\alpha_T)}
$$

代入母公式：

$$
\frac{x}{n(1+\alpha_T)}\frac{V_{FS}}{2}e^{-t/\tau}\le\frac{V_{FS}}{2n(1+\alpha_T)}
$$

公共项全部抵消：

$$
xe^{-t/\tau}\le1
$$

所以：

$$
t\ge\tau\ln x
$$

如果 split array 的最坏切换单位数是：

$$
x_{max}=2^{N-2}
$$

那么：

$$
t_{settle,min}=\tau\ln(2^{N-2})=\tau(N-2)\ln2
$$

## 和网上公式的具体差别

### 差别 1：$\tau$ 的定义

网上常见：

$$
\tau=R_{on}C_{eq}
$$

你的笔记：

$$
\tau=RC_u\left(\alpha_P+\frac{\alpha_T}{1+\alpha_T}\right)
$$

你的 $C_{eq}$ 实际上是：

$$
C_{eq}=C_u\left(\alpha_P+\frac{\alpha_T}{1+\alpha_T}\right)
$$

也就是说，你不是把整个 CDAC 总电容都放进时间常数，而是只把会被有限开关电阻充放电的寄生效应放进去了。

### 差别 2：最大阶跃 $V_0$

普通公式常用：

$$
V_0=V_{FS},\quad V_0=\frac{V_{FS}}{2}
$$

你的公式使用：

$$
V_0=\frac{x}{n(1+\alpha_T)}\frac{V_{FS}}{2}
$$

所以你的 settling time 直接和切换单位电容数 $x$ 相关。

### 差别 3：阵列结构

普通 binary CDAC 的 MSB step 可能对应 $x\approx2^{N-1}$ 或类似数量级，所以得到接近 $N\tau\ln2$。

你的 split array 假设里：

$$
x_{max}=2^{N-2}
$$

所以得到：

$$
(N-2)\tau\ln2
$$

这不是更松或更严的普适结论，而是由 split array 最大切换规模决定的。

### 差别 4：是否允许 redundancy

冗余 SAR 论文会说：前几步不必每一步都 settle 到完整 $N$ bit 精度，因为后面有数字校正空间。于是 settling requirement 可以从 $N$-bit accurate 变成 3-bit、4-bit accurate。

你的公式默认没有显式利用 redundancy，而是在每次切换后按 $1/2$ LSB 约束残差。

## 什么时候该用哪个公式

| 你在估什么 | 推荐公式 |
|---|---|
| 输入采样网络 settling | Silicon Labs / switched-capacitor ADC 那类 $t=\tau\ln(V_0/V_{tol})$ |
| 粗估 SAR CDAC 每步需要多久 | $t\approx N\tau\ln2$ 或 $(N+1)\tau\ln2$ |
| 比较不同 switching scheme 的速度 | $t\ge\tau\ln x$，因为 $x$ 直接体现切换电容数 |
| 做 CDAC parasitic-aware 分析 | 你的 $\tau=RC_u(\alpha_P+\alpha_T/(1+\alpha_T))$ |
| 有 redundancy / non-binary search | 按每一段实际需要的 bit accuracy 分段算 settling |

## 需要注意的限制

你的推导很适合解释 CDAC 内部寄生导致的 settling，但它没有包含这些效应：

- reference buffer 输出阻抗和动态压降；
- reference decap 和供电网络；
- 开关电阻随电压变化的非线性；
- comparator input parasitic 与 kickback；
- bottom plate switching 的具体时序重叠；
- differential CDAC 两边的 common-mode settling。

如果用于论文/报告，建议把它表述为：

> 在忽略 reference driver dynamics、开关非线性和 comparator kickback 的条件下，split CDAC 的一阶 settling time 可由 bottom/top parasitic KCL 推得。

## 参考来源

1. Silicon Labs, AN119: Calculating Settling Time for Switched Capacitor ADCs. <https://www.silabs.com/documents/public/application-notes/AN119.pdf>
2. C. C. Liu et al., A 10-bit SAR ADC With Two Redundant Decisions... <https://ime.um.edu.mo/wp-content/uploads/presentations/9777b0f6afb9a111dc187745bb7c0484.pdf>
3. V. Tripathi, Stanford thesis on high-speed SAR / two-CDAC pipelined SAR architecture. <https://stacks.stanford.edu/file/druid%3Ajc388fn7862/VaibhavT_thesis_final-augmented.pdf>
4. Journal of Semiconductors, A partial split capacitor switching scheme for SAR ADC. <https://www.jos.ac.cn/article/doi/10.1088/1674-4926/37/1/015004?pageType=en>
