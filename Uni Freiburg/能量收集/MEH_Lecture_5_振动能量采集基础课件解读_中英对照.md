# Lecture 5 振动能量采集基础课件解读

> 原文件：`MicroEnergyHarvesting_Lecture_5_Vibrational Energy Harvesting_SS_2025.pdf`

## 1. 核心思想

振动采集器通常可抽象成质量-弹簧-阻尼系统（mass-spring-damper）。环境振动使基座运动，惯性质量相对基座振动，转换器把其中一部分机械阻尼转化为电能。

由于采集器质量受体积和成本限制，最重要的策略是利用共振放大相对位移。

## 2. 谐振子模型

$$
m\ddot x+c\dot x+kx=F(t)
$$

其中：

- $m$：惯性质量；
- $k$：弹簧刚度；
- $c$：黏性阻尼；
- $x$：质量相对基座的位移。

固有角频率：

$$
\omega_0=\sqrt{\frac{k}{m}}
$$

固有频率：

$$
f_0=\frac{\omega_0}{2\pi}
$$

## 3. 无阻尼自由振动

当 $c=0$、$F=0$：

$$
\ddot x+\omega_0^2x=0
$$

解为：

$$
x(t)=x_0\cos(\omega_0t+\phi)
$$

势能：

$$
W_p=\frac12kx^2
$$

动能：

$$
W_k=\frac12m\dot x^2
$$

总能量保持不变：

$$
W_{\mathrm{tot}}=\frac12kx_0^2
=\frac12m\omega_0^2x_0^2
$$

能量在弹簧势能和质量动能之间周期性交换。

## 4. 有阻尼自由振动

阻尼比：

$$
\zeta=\frac{c}{2m\omega_0}
$$

欠阻尼情况下：

$$
\omega_R=\omega_0\sqrt{1-\zeta^2}
$$

$$
x(t)=A e^{-\zeta\omega_0t}
\cos(\omega_Rt+\phi)
$$

振幅按 $e^{-\zeta\omega_0t}$ 衰减，而能量按更快的速率衰减：

$$
W(t)\propto e^{-2\zeta\omega_0t}
$$

## 5. 阻尼功率

阻尼力：

$$
F_d=-c\dot x
$$

瞬时耗散功率：

$$
P_d=F_d\dot x=-c\dot x^2
$$

负号表示机械能从振动系统中流出。

## 6. 受迫振动

正弦激励：

$$
F(t)=F_0\cos\omega t
$$

稳态位移幅值：

$$
X(\omega)=
\frac{F_0/m}
{\sqrt{(\omega_0^2-\omega^2)^2+(2\zeta\omega_0\omega)^2}}
$$

低阻尼、接近共振时：

$$
X_{\max}\approx
\frac{F_0}{2\zeta m\omega_0^2}
$$

## 7. 品质因数与带宽

品质因数（quality factor）：

$$
Q=\frac{1}{2\zeta}
=\frac{m\omega_0}{c}
$$

共振时位移放大倍数约为 $Q$。

带宽近似：

$$
\Delta\omega\approx\frac{\omega_0}{Q}
$$

高 $Q$ 能带来大振幅，但会使频带变窄，并提高对频率漂移的敏感性。

## 8. 共振时的能量和功率

稳态时平均输入功率等于平均阻尼损耗：

$$
\overline P_{\mathrm{in}}
=\overline P_{\mathrm{damp}}
$$

弹簧和质量之间可能交换很大的瞬时功率，但平均储能不会持续增加。

高 $Q$ 系统内部的瞬时力、位移和应力可能远高于输出的平均电功率，因此必须检查机械强度和最大行程。

## 9. 基座激励

若基座位移为：

$$
y(t)=Y\cos\omega t
$$

则加速度幅值：

$$
a_{\mathrm{vib}}=\omega^2Y
$$

等效惯性力幅值：

$$
F_0=ma_{\mathrm{vib}}
=m\omega^2Y
$$

这说明即使高频振动位移很小，也可能具有较大的加速度和可采集功率。

## 10. 寄生阻尼与采集阻尼

总阻尼：

$$
c_{\mathrm{tot}}=c_{\mathrm{diss}}+c_{\mathrm{harv}}
$$

- $c_{\mathrm{diss}}$：机械摩擦、材料损耗、空气阻尼等寄生损耗；
- $c_{\mathrm{harv}}$：由能量转换器产生的有效电阻尼。

只有 $c_{\mathrm{harv}}$ 对应的能量能够转化为电能。

## 11. 最佳阻尼匹配

共振时平均采集功率与下式成正比：

$$
\overline P_{\mathrm{el}}
\propto
\frac{c_{\mathrm{harv}}}
{(c_{\mathrm{harv}}+c_{\mathrm{diss}})^2}
$$

令：

$$
x=\frac{c_{\mathrm{harv}}}{c_{\mathrm{diss}}}
$$

最大化：

$$
\frac{x}{(1+x)^2}
$$

得到：

$$
\boxed{c_{\mathrm{harv}}=c_{\mathrm{diss}}}
$$

此时输入阻尼功率的一半被采集，另一半被寄生阻尼消耗。

## 12. 功率公式

对于基座加速度激励，稳态相对位移幅值可写成：

$$
X(\omega)=
\frac{m a_{\mathrm{vib}}}
{\sqrt{(k-m\omega^2)^2+
\omega^2(c_{\mathrm{harv}}+c_{\mathrm{diss}})^2}}
$$

平均采集功率：

$$
P_{\mathrm{el}}(\omega)
=\frac12c_{\mathrm{harv}}\omega^2X^2
$$

代入后：

$$
P_{\mathrm{el}}(\omega)
=
\frac{
\frac12c_{\mathrm{harv}}\omega^2m^2a_{\mathrm{vib}}^2
}{
(k-m\omega^2)^2+
\omega^2(c_{\mathrm{harv}}+c_{\mathrm{diss}})^2
}
$$

共振时：

$$
P_{\mathrm{el,res}}
=
\frac12
\frac{c_{\mathrm{harv}}}
{(c_{\mathrm{harv}}+c_{\mathrm{diss}})^2}
m^2a_{\mathrm{vib}}^2
$$

阻尼匹配后：

$$
\boxed{
P_{\mathrm{el,max}}
=\frac{m^2a_{\mathrm{vib}}^2}
{8c_{\mathrm{diss}}}
}
$$

又因为 $a_{\mathrm{vib}}=\omega_0^2Y$：

$$
P_{\mathrm{el,max}}
=\frac{m^2\omega_0^4Y^2}
{8c_{\mathrm{diss}}}
$$

## 13. 设计规律

功率随以下因素增加：

- 更大的惯性质量；
- 更大的振动加速度；
- 更低的寄生阻尼；
- 更准确的共振匹配。

实际限制包括：

- 最大位移；
- 弹簧应力和疲劳；
- 器件体积；
- 振动频率漂移；
- 共振带宽；
- 撞击和非线性；
- 整流与储能损失。

## 14. 选择振动源与设计参数

1. 测量振动频谱；
2. 找到 $\omega^4Y^2$ 较大的频率成分；
3. 将 $\omega_0$ 调到目标频率；
4. 在体积和应力允许范围内增大质量；
5. 减小 $c_{\mathrm{diss}}$；
6. 使 $c_{\mathrm{harv}}\approx c_{\mathrm{diss}}$；
7. 检查最大位移和结构稳定性；
8. 加入整流和储能损失。

## 15. 整流

大多数振动换能器产生交流电。普通桥式整流器会带来：

- 二极管压降；
- 导通损耗；
- 低电压下无法有效工作。

低电压采集器通常更适合同步整流或有源整流。

## 16. 高频易错点

- 混淆基座位移与质量相对位移；
- 在需要 $\omega$ 时直接代入频率 $f$；
- 忽略功率与加速度平方的关系；
- 只追求高 $Q$ 而忽略带宽和行程；
- 认为全部阻尼都能转化为电能；
- 忽略整流和储能损失；
- 只按标称共振频率设计，不考虑源频率变化。

## 17. 公式速记

$$
\omega_0=\sqrt{\frac{k}{m}}
$$

$$
\zeta=\frac{c}{2m\omega_0}
$$

$$
Q=\frac{1}{2\zeta}
$$

$$
F_0=ma_{\mathrm{vib}}
$$

$$
c_{\mathrm{harv,opt}}=c_{\mathrm{diss}}
$$

$$
P_{\mathrm{el,max}}
=\frac{m^2a_{\mathrm{vib}}^2}
{8c_{\mathrm{diss}}}
$$

