# Signale und Systeme：往年考试整理

> 基于 WS22/23、WS23/24、WS24 三份考试/回忆资料整理。题目和分值可能有遗漏或记忆误差；公式按常见连续时间与离散时间傅里叶、拉普拉斯、Z 变换约定整理。
>
> Based on three exam papers/memory protocols from WS22/23, WS23/24 and WS24. Some recalled questions may be incomplete; formulas follow the standard CT/DT Fourier, Laplace and Z-transform conventions.

## 0. 考试概况 / Exam overview

| 学期 / Term | 形式 / Format | 反复出现的主题 / Recurring topics |
|---|---|---|
| WS22/23 | 约 120 min；计算器限制；含判断题 | 系统性质、RC/CR、卷积、傅里叶、采样混叠、Z 变换、DFT、Leakage |
| WS23/24 | 约 100 分 | 拉普拉斯、周期信号、卷积、真假题、Z 平面、DFT、音频链路、频谱分析 |
| WS24 | 120 min / 120 P；给公式表；仅普通计算器 | 系统性质、周期信号、二阶模拟滤波器、卷积、Z 平面、Nyquist、DFT、音频/Leakage |

---

## 1. 线性时不变系统 / Linear Time-Invariant Systems

### 1.1 三个基本判据 / Three basic tests

系统写作 (y(t)=S\{x(t)\}) 或 (y[n]=S\{x[n]\})。

**线性 Linearity**：

$$
S\{a x_1+b x_2\}=aS\{x_1\}+bS\{x_2\}.
$$

必须同时满足齐次性和叠加性。平方、绝对值、最大值、与输入相乘等通常是非线性的。

**时不变 Time invariance**：

若输入延迟 (n_0) 或 (t_0)，输出必须同样延迟：

$$
S\{x(t-t_0)\}=y(t-t_0),
\qquad
S\{x[n-n_0]\}=y[n-n_0].
$$

显式出现 (t)、(n)、$$\sin(\omega t)$$ 等系数时，通常是时变系统。

**因果 Causality**：输出只依赖当前和过去输入，不依赖未来输入：

$$
y[n]=\sum_{k\ge0}b_kx[n-k]
$$

是因果的；出现 (x[n+1]) 则非因果。

### 1.2 记忆性与稳定性 / Memory and stability

- 无记忆 memoryless：(y[n]) 只依赖 (x[n])。
- 有记忆 with memory：出现延迟、积分、卷积或过去输出。
- 连续时间 BIBO 稳定：$$\int|h(t)|dt<\infty$$。
- 离散时间 BIBO 稳定：$$\sum_n|h[n]|<\infty$$。
- 因果有理 LTI 系统：所有极点必须在单位圆内才稳定。

串联结论：两个线性系统串联仍线性；两个时不变系统串联仍时不变。但“两个非线性系统串联一定非线性”并非严格普遍命题，需看具体系统是否发生特殊抵消。

---

## 2. 连续时间电路、拉普拉斯与滤波器 / CT circuits, Laplace and filters

### 2.1 一阶 RC 低通 / First-order RC low-pass

若输出取电容两端：

$$
RC\frac{dy(t)}{dt}+y(t)=x(t),
\qquad
H(s)=\frac{Y(s)}{X(s)}=\frac1{RCs+1}.
$$

单位阶跃输入 (x(t)=U_0u(t))：

$$
y(t)=U_0\left(1-e^{-t/(RC)}\right)u(t).
$$

极点：$$s=-1/(RC)$$。当 (R,C>0) 时在左半平面，系统稳定。

### 2.2 CR 高通 / CR high-pass

若电容串联、电阻接地且输出取电阻两端：

$$
H(s)=\frac{RCs}{1+RCs}.
$$

直流 (s=0) 时增益为 0，因此是高通。

### 2.3 二阶电路 / Second-order circuit

典型形式：

$$
G(s)=\frac1{LCs^2+RCs+1}.
$$

分母最高次幂为 2，所以是二阶系统。高频渐近斜率：每个分母中的 (s) 因子贡献约 (-20\,mathrm{dB/dec})，二阶低通约 (-40\,mathrm{dB/dec})。

### 2.4 Fourier 是 Laplace 的特例 / Fourier as a special case of Laplace

双边拉普拉斯：

$$
X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}dt.
$$

令 (s=\sigma+j\omega)：

$$
X(s)=\int x(t)e^{-\sigma t}e^{-j\omega t}dt.
$$

当 $$\sigma=0$$，即沿虚轴取值：

$$
X(j\omega)=\int x(t)e^{-j\omega t}dt,
$$

因此 Fourier transform 是 Laplace transform 在 (s=j\omega) 轴上的特殊情况，前提是虚轴位于 ROC 内。

---

## 3. 连续时间卷积 / Continuous-time convolution

$$
y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau.
$$

标准步骤 / Standard procedure:

1. 选择翻转的信号，通常画 (h(-\tau))。
2. 平移为 (h(t-\tau))。
3. 找到两个非零区间的重叠范围。
4. 按不同 (t) 区间写积分上下限。
5. 必要时计算积分。

### 两个矩形 / Two rectangles

例如：

$$
x(t)=a\,\mathrm{rect}\left(t-\frac12\right),
\qquad
h(t)=b\,\mathrm{rect}\left(\frac{t-4}{2}\right).
$$

支持区间分别为 ([0,1]) 和 ([3,5])。卷积是重叠长度乘 (ab)：

$$
y(t)=
\begin{cases}
0,&t<3,\\
ab(t-3),&3\le t<4,\\
ab,&4\le t<5,\\
ab(6-t),&5\le t<6,\\
0,&t\ge6.
\end{cases}
$$

不同宽度矩形卷积为梯形；相同宽度矩形卷积为三角形。

---

## 4. 傅里叶变换与真假题 / Fourier-transform facts

### 4.1 高频考点 / High-frequency facts

| 命题 / Statement | 判断 / Answer | 理由 / Reason |
|---|---|---|
| 短矩形时域信号变成窄带频谱 / Short time rectangle gives narrow spectrum | 错 False | 时间越短，频谱越宽 |
| 三角形时域对应 $$\mathrm{si}^2$$ 频域 / Triangle corresponds to sinc-squared | 对 True | 三角形是矩形卷积 |
| 频域矩形对应时域 sinc | 对 True | rectangle-sinc transform pair |
| 连续时间 Fourier 变换是 (2\pi) 周期 | 错 False | DTFT 才对离散频率 (2\pi) 周期 |
| 时域左移导致下降相位 | 错 False | 左移 (x(t+t_0)\leftrightarrow X(j\omega)e^{+j\omega t_0})，相位上升 |
| 奇函数在 0 Hz 有非零分量 | 错 False | $$X(0)=\int x(t)dt=0$$ |
| 频域常数对应时域 Dirac | 对 True | (1\leftrightarrow\delta(t))，比例取决于归一化 |
| 频域实偶对应时域实偶 | 对 True | Fourier 对称性 |
| Fourier transform 是非线性的 | 错 False | Fourier transform 是线性的 |
| 时域卷积对应频域乘法 | 对 True | (x*h\leftrightarrow XH) |
| 时域采样会在频域产生以采样频率为间隔的 replicas | 对 True | Sampling creates spectral images |

### 4.2 平移与对称性 / Shift and symmetry

$$
x(t-t_0)\leftrightarrow X(j\omega)e^{-j\omega t_0}
$$

表示右移，频率相位下降；

$$
x(t+t_0)\leftrightarrow X(j\omega)e^{+j\omega t_0}
$$

表示左移，频率相位上升。

实信号满足共轭对称：

$$
X(-j\omega)=X^*(j\omega).
$$

实偶时域信号的频谱为实偶；实奇时域信号的频谱为虚奇。

---

## 5. 周期信号与傅里叶级数 / Periodic signals and Fourier series

若基本周期为 (T_0)，则：

$$
\omega_0=\frac{2\pi}{T_0},
\qquad
f_0=\frac1{T_0}.
$$

平均值或直流分量：

$$
a_0=\frac1{T_0}\int_{t_0}^{t_0+T_0}x(t)dt.
$$

复指数级数：

$$
x(t)=\sum_{k=-\infty}^{\infty}a_ke^{jk\omega_0t},
\qquad
a_k=\frac1{T_0}\int_{t_0}^{t_0+T_0}x(t)e^{-jk\omega_0t}dt.
$$

考试常见操作：先从图读出 (T_0)，画周期延拓，再分段积分求 (a_0)、(a_n)。常数项与其他部分可利用线性分别计算。

---

## 6. 采样、混叠与重建 / Sampling, aliasing and reconstruction

### 6.1 基本采样定理 / Sampling theorem

若信号最高频率为 (f_{max})，无混叠采样要求：

$$
f_s>2f_{max}.
$$

等价地，Nyquist 频率为 (f_s/2)。超过该范围的频率会折叠到基带。

正弦信号采样：

$$
x[n]=\sin\left(2\pi\frac{f_0}{f_s}n\right).
$$

离散角频率只在 (2\pi) 意义下等价：

$$
\omega_0\equiv\omega_0+2\pi k.
$$

混叠频率可用：

$$
f_{alias}=|f_0-kf_s|
$$

选择落入 ([0,f_s/2]) 的结果。

### 6.2 带通信号采样 / Bandpass sampling

对于带通信号，不一定要求 (f_s>2f_{\max})，但必须选择采样率使频谱复制不重叠。考试中通常要求写出频带边界与 replicas 的不重叠不等式，而不是只写普通 Nyquist 结论。

### 6.3 重建链路 / Audio conversion chain

麦克风到扬声器的典型顺序：

$$
\boxed{
\text{Microphone}\rightarrow\text{Analog LPF}\rightarrow\text{Sample/Hold}\rightarrow\text{A/D}\rightarrow\text{DSP}\rightarrow\text{D/A}\rightarrow\text{Analog reconstruction LPF}\rightarrow\text{Loudspeaker}
}
$$

抗混叠低通在 ADC 前；重建低通在 DAC 后。

---

## 7. Z 变换、极点零点与数字滤波器 / Z-transform, poles and zeros

### 7.1 基本关系 / Basic relations

因果序列：

$$
X(z)=\sum_{n=0}^{\infty}x[n]z^{-n}.
$$

延迟：

$$
x[n-k]\leftrightarrow z^{-k}X(z).
$$

卷积：

$$
x[n]*h[n]\leftrightarrow X(z)H(z).
$$

标准系统函数：

$$
H(z)=\frac{\sum_{k=0}^{N}b_kz^{-k}}
{1+\sum_{k=1}^{M}a_kz^{-k}}.
$$

分子根是零点，分母根是极点。

### 7.2 ROC、因果与稳定 / ROC, causality and stability

- 因果右边序列：ROC 在最外层极点之外。
- 反因果左边序列：ROC 在最内层极点之内。
- 稳定要求 ROC 包含单位圆 (|z|=1)。
- 对因果有理系统，所有极点必须满足 (|p_i|<1)。

### 7.3 常见例题形式 / Typical example

若：

$$
H(z)=\frac{z^2}{z^2-z+0.5},
$$

则零点为 (z=0)（二重），极点为：

$$
p=\frac{1\pm j}{2}=0.5\pm0.5j.
$$

极点模为 (1/\sqrt2<1)，因果 ROC 为 (|z|>1/\sqrt2)，系统稳定。单位圆上的幅值可先算 (H(1))、(H(-1))，再结合共轭对称性草图。

---

## 8. DFT、DTFT 与频率分辨率 / DFT, DTFT and resolution

### 8.1 DFT 定义 / DFT definition

$$
X[m]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi mn/N},
\qquad m=0,\ldots,N-1.
$$

频率分辨率：

$$
\boxed{\Delta f=\frac{f_s}{N}}.
$$

第 (m) 个 bin：

$$
f_m=m\Delta f.
$$

当 (m>N/2) 时，通常解释为负频率：

$$
f_m=(m-N)\Delta f.
$$

### 8.2 DFT 与 DTFT / Difference

- DTFT：离散时间信号的连续频率函数，关于 (omega) 连续且 (2\pi) 周期。
- DFT：对有限 (N) 点序列在 (N) 个离散频率点上的采样，适合计算机实现。

DFT 频域逐点相乘对应时域 (N) 点循环卷积；线性卷积需零填充到至少 (L+K-1) 点。

### 8.3 典型四点 DFT / Typical four-point DFT

$$
x[n]=[0,1,0,-1]
\Rightarrow
X[m]=[0,-2j,0,2j].
$$

幅值为 ([0,2,0,2])，相位在非零点分别为 (-\pi/2)、(+\pi/2)。

---

## 9. Leakage、窗口与 Zero Padding / Leakage, windows and zero padding

### 9.1 Leakage 是什么？ / What is leakage?

有限时间截断相当于时域乘以窗口。时域乘法对应频域卷积，因此一个理想谱线会扩散到邻近频率 bin，称为 spectral leakage。

### 9.2 什么时候没有 leakage？ / When is leakage absent?

当观测窗内包含整数个周期，并且周期边界连续拼接时，矩形窗可以不产生（理想情况下的）泄漏。否则会产生边界不连续和 leakage。

### 9.3 Zero padding 能否减少 leakage？

不能真正减少 leakage，也不能提升真实频率分辨率。Zero padding 只增加频率采样点，使频谱曲线看起来更平滑、更容易估计峰值位置。

### 9.4 矩形窗优点 / Rectangular window advantage

矩形窗主瓣最窄，频率分辨能力较好；代价是旁瓣较高、泄漏抑制差。其他窗通常用更宽主瓣换取更低旁瓣。

---

## 10. 群延迟、理想滤波器与系统辨识 / Group delay, ideal filters and identification

### 10.1 群延迟 / Group delay

$$
\tau_g(\omega)=-\frac{d\phi(\omega)}{d\omega}.
$$

音频信号中希望通带内群延迟尽量平坦，否则不同频率分量延迟不同，会导致波形失真。

### 10.2 冲激响应与阶跃响应 / Impulse and step response

$$
y_\sigma(t)=u(t)*h(t)=\int_{-\infty}^{t}h(\tau)d\tau,
$$

所以：

$$
\boxed{h(t)=\frac{d}{dt}y_\sigma(t)}.
$$

离散时间中，冲激响应可由阶跃响应的一阶差分得到：

$$
h[n]=y_u[n]-y_u[n-1].
$$

### 10.3 为什么理想滤波器不可实现？ / Why ideal filters are unrealizable

理想砖墙频响的时域冲激响应通常是无限长 sinc，并且常常是非因果的；实际实时系统不能提前知道未来输入，也不能实现无限延伸的精确响应。因此只能用 FIR/IIR 近似。

### 10.4 LTI 系统辨识激励 / Excitations for LTI identification

常见三种：

1. 单位冲激 / impulse；
2. 阶跃 / step；
3. 白噪声、伪随机二进制序列 PRBS 或扫频 chirp。

---

## 11. 模拟到数字滤波器设计 / Analog-to-digital filter design

### 11.1 双线性变换 / Bilinear transform

$$
s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}.
$$

它满足：

- 左半 (s) 平面映射到单位圆内；
- 虚轴映射到单位圆；
- 稳定模拟滤波器映射为稳定数字滤波器；
- 不发生 impulse-invariance 那样的频谱混叠；
- 但有频率扭曲。

频率预畸变：

$$
\boxed{\Omega=\frac{2}{T}\tan\frac{\omega}{2}}.
$$

### 11.2 Butterworth 设计 / Butterworth design

$$
|H_C(j\Omega)|^2
=
\frac1{1+(\Omega/\Omega_C)^{2N}}.
$$

常用阶数公式：

$$
N\ge
\frac{\ln\left[
\dfrac{1/A_s^2-1}{1/A_p^2-1}
\right]}
{2\ln(\Omega_s/\Omega_p)}.
$$

若要通带边缘恰好为 (-3$$ dB，则二阶或任意阶 Butterworth 的通带边缘设置为：

$$
\Omega_C=\Omega_p.
$$

若题目要求阻带边缘恰好达到指定衰减，则按阻带等式求 (Omega_C)：

$$
\Omega_C=
\frac{\Omega_s}{(1/A_s^2-1)^{1/(2N)}}.
$$

### 11.3 IIR 相对 FIR / IIR versus FIR

IIR 优点：相同频率选择性通常需要更低阶数、较少乘法器和存储器、计算量和功耗较低。缺点：存在反馈、需检查稳定性，通常难以实现严格线性相位。

---

## 12. 相关、卷积与延迟测量 / Correlation, convolution and delay measurement

### 12.1 自相关 / Autocorrelation

$$
\phi_{xx}[m]=\sum_n x[n]x[n+m].
$$

用途：检测周期、估计基频、分析能量。周期信号的自相关通常在 (m=0,\pm N,\pm2N$$ 附近有峰值。

### 12.2 互相关 / Cross-correlation

本课程常用约定：

$$
\phi_{xy}[m]=\sum_n x[n]y[n+m].
$$

互相关峰值给出两个信号最匹配的延迟。若 (y[n]=x[n-n_0])，按此约定峰值在 (m=n_0)。其他教材使用 (y[n-m]) 时，峰值符号可能相反。

### 12.3 回波距离 / Echo distance

采样频率为 (f_s)，互相关峰值延迟为 (m_0)，介质声速为 (c)。往返测距：

$$
\boxed{d=\frac{c}{2}\frac{m_0}{f_s}}.
$$

例如 (f_s=10\text{ kHz})、(m_0=11)、水中 (c=1500\text{ m/s})：

$$
d=\frac{1500}{2}\frac{11}{10000}=0.825\text{ m}.
$$

---

## 13. 高频公式速查 / Formula sheet

$$
\begin{aligned}
&y(t)=x(t)*h(t),\\
&Y(j\omega)=X(j\omega)H(j\omega),\\
&\omega_0=2\pi f_0,\\
&f_s>2f_{max},\\
&\Delta f=f_s/N,\\
&H(z)=Y(z)/X(z),\\
&\text{stable causal rational DT system: }|p_i|<1,\\
&s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}},\\
&\Omega=\frac{2}{T}\tan(\omega/2),\\
&\tau_g(\omega)=-d\phi/d\omega,\\
&h(t)=d y_\sigma(t)/dt.
\end{aligned}
$$

## 14. 考前优先级 / Recommended revision order

1. 系统性质真假判断：线性、因果、时不变、稳定、记忆。
2. 连续时间卷积：矩形脉冲重叠区间和积分上下限。
3. 拉普拉斯电路：RC/CR、一阶二阶滤波器、极点稳定性、终值。
4. Z 变换：差分方程、(H(z))、ROC、极点零点、频率响应。
5. DFT/DTFT、频率分辨率、负频率、DFT 与循环卷积。
6. 采样和混叠：Nyquist、频谱 replicas、带通采样。
7. Leakage、窗口、zero padding、群延迟和音频链路。

