# Lecture 2 太阳能采集课件解读

> 原文件：`MicroEnergyHarvesting_Lecture_2_Solar Energy Harvesting_SS_2026.pdf`  
> 本文以中文讲解为主，仅保留必要英文关键词。

## 1. 本章主线

本章可以分成四部分：

1. 太阳辐射与太阳位置；
2. 组件倾角和可接收辐照度；
3. 光伏电池的物理机理与电气模型；
4. 实际能量采集系统，包括寄生损耗、室内光伏和储能。

核心逻辑是：**光源和几何条件决定入射能量，半导体物理决定电池输出，电源管理决定最终可用能量。**

## 2. 太阳辐射与 Air Mass

大气层外的太阳光谱称为 AM0。太阳光进入大气后会被吸收和散射，地面光伏测试通常采用 AM1.5 光谱。

直接辐照度（direct irradiance）的经验模型为：

$$
I_D=I_0\cdot0.7^{AM^{0.678}}
$$

其中 $I_0$ 是太阳常数。课件用下式粗略加入漫射辐射：

$$
I_G\approx1.1I_D
$$

这个 1.1 是经验系数，只适合快速估算，不能替代严格的天空漫射模型。

## 3. 光子能量与带隙

光子能量为：

$$
E_{\mathrm{ph}}=hf=\frac{hc}{\lambda}
$$

只有满足：

$$
E_{\mathrm{ph}}\ge E_g
$$

的光子才能跨越材料带隙并产生电子-空穴对。

- 光子能量低于带隙：基本无法被有效利用；
- 光子能量高于带隙：多余能量通常通过热化损失；
- 因此材料带隙决定可利用的光谱范围。

## 4. 太阳位置

太阳位置由日期、纬度和地方太阳时共同决定。

### 4.1 地方太阳时

当地标准时需要经度修正和时间方程（equation of time）修正：

$$
LST=LT+\frac{TC}{60}
$$

$$
TC=4(\mathrm{Longitude}-LSTM)+EoT
$$

$$
LSTM=15^\circ\Delta t_{\mathrm{UTC}}
$$

时角（hour angle）为：

$$
HRA=15^\circ(LST-12)
$$

- 上午：$HRA<0$；
- 正午：$HRA=0$；
- 下午：$HRA>0$。

### 4.2 太阳赤纬和高度角

太阳赤纬可近似为：

$$
\delta=23.45^\circ\sin\left[\frac{360^\circ}{365}(d-81)\right]
$$

太阳高度角为：

$$
\alpha=\sin^{-1}\left(
\sin\delta\sin\varphi+
\cos\delta\cos\varphi\cos HRA
\right)
$$

其中 $\varphi$ 为当地纬度。

## 5. 组件倾角与接收辐照度

若组件朝向太阳所在方位，太阳高度角为 $\alpha$，组件相对水平面的倾角为 $\beta$，则：

$$
S_m=S_i\sin(\alpha+\beta)
$$

接收直接辐射最大的条件是：

$$
\alpha+\beta=90^\circ
$$

也就是组件法线与太阳光方向一致。

对于任意方位，可写为：

$$
S_m=S_i\left[
\cos\alpha\sin\beta\cos(\psi-\Theta)
+\sin\alpha\cos\beta
\right]
$$

其中 $\psi$ 和 $\Theta$ 分别表示组件与太阳的方位角。

更一般地，可使用方向向量点积：

$$
S_m=S_i\cos\gamma=S_i\mathbf S\cdot\mathbf N
$$

固定组件不应只追求某一时刻的峰值，而应优化全年或目标季节的累计能量。

## 6. 直接辐射与漫射辐射

总辐射可写成：

$$
G=B+D
$$

课件采用的简化漫射模型为：

$$
D=I_{\mathrm{diff}}
\frac{180^\circ-\beta}{180^\circ}
$$

组件越陡，看到的天空范围越小，接收到的漫射分量通常越少。

## 7. Irradiance 与 Insolation

- 辐照度（irradiance）：瞬时功率密度，单位 $\mathrm{W/m^2}$；
- 辐照量（insolation）：一段时间内的累计能量，单位 $\mathrm{Wh/m^2}$ 或 $\mathrm{J/m^2}$。

$$
H=\int I(t)\,dt
$$

设计能量采集系统时，真正决定能量预算的是辐照量，而不是正午的单个峰值。

## 8. 光伏结的工作机理

光子在半导体中产生电子-空穴对。p-n 结耗尽区中的内建电场将载流子分离，并把它们输送到外部电路。

实际收集效率受到以下因素影响：

- 光吸收深度；
- 复合寿命；
- 扩散长度；
- 产生位置与耗尽区的距离；
- 表面和体材料缺陷。

开路时形成开路电压 $V_{OC}$；短路时输出短路电流 $I_{SC}$。

## 9. 量子效率与光谱响应

量子效率（quantum efficiency, QE）：

$$
QE(\lambda)=
\frac{\text{被收集的电子数}}
{\text{入射光子数}}
$$

外量子效率包含反射和透射损失；内量子效率不计这些光学损失。

光谱响应（spectral response）：

$$
SR(\lambda)=\frac{I_{SC}}{P_{\mathrm{in}}}
=\frac{q\lambda}{hc}QE(\lambda)
$$

单位为 $\mathrm{A/W}$。

## 10. 光伏电池 I-V 模型

理想受光二极管模型：

$$
I=I_L-I_0\left[
\exp\left(\frac{qV}{nkT}\right)-1
\right]
$$

其中：

- $I_L$：光生电流；
- $I_0$：暗饱和电流；
- $n$：理想因子；
- $T$：绝对温度。

短路电流近似为：

$$
I_{SC}\approx I_L
$$

开路电压为：

$$
V_{OC}=\frac{nkT}{q}
\ln\left(\frac{I_L}{I_0}+1\right)
$$

$I_{SC}$ 与光强近似线性，而 $V_{OC}$ 只随光强对数变化。

## 11. 最大功率点与填充因子

最大功率点（maximum power point, MPP）：

$$
P_{MP}=V_{MP}I_{MP}
$$

填充因子（fill factor, FF）：

$$
FF=\frac{V_{MP}I_{MP}}{V_{OC}I_{SC}}
$$

定义归一化开路电压：

$$
\nu_{OC}=\frac{qV_{OC}}{nkT}
$$

经验公式：

$$
FF\approx
\frac{\nu_{OC}-\ln(\nu_{OC}+0.72)}
{\nu_{OC}+1}
$$

FF 越高，I-V 曲线越接近矩形，电池质量通常越好。

## 12. 效率及其限制

$$
\eta=\frac{P_{MP}}{P_{\mathrm{in}}}
=\frac{V_{OC}I_{SC}FF}{P_{\mathrm{in}}}
$$

单结电池受到 Shockley-Queisser 极限约束，主要损失包括：

- 低于带隙的光子透射；
- 高于带隙的能量热化；
- 辐射与非辐射复合；
- 表面反射；
- 电阻和漏电损失。

## 13. 寄生电阻

特征电阻可近似为：

$$
R_{CH}\approx\frac{V_{OC}}{I_{SC}}
$$

串联电阻 $R_S$ 来自半导体体电阻、金属接触和电极；并联电阻 $R_{SH}$ 表示漏电通道。

完整模型：

$$
I=I_L-I_0
\left[
\exp\left(\frac{q(V+IR_S)}{nkT}\right)-1
\right]
-\frac{V+IR_S}{R_{SH}}
$$

- $R_S$ 过大：高电压区域功率下降，FF 降低；
- $R_{SH}$ 过小：短路附近漏电增大，FF 降低。

归一化串联电阻：

$$
r_S=\frac{R_S}{R_{CH}}
$$

小 $r_S$ 时：

$$
FF_S\approx FF_0(1-1.1r_S)+\frac{r_S^2}{5.4}
$$

## 14. 温度与低照度

硅电池近似有：

$$
\frac{dV_{OC}}{dT}\approx-2.2\,\mathrm{mV/K}
$$

温度升高时：

- $I_{SC}$ 略微增加；
- $V_{OC}$ 明显下降；
- FF 和最大功率下降。

低照度下，光生电流很小，因此漏电和 $R_{SH}$ 的影响更加突出。

## 15. 室内光伏

室内 LED、荧光灯和钠灯的光谱与 AM1.5 差别很大。Lux 是按人眼灵敏度加权的照度单位，不能在不知道光谱和光效时直接换算成 $\mathrm{W/m^2}$。

室内电池选择时应关注：

- 光谱匹配；
- 低照度下的 $V_{OC}$；
- 漏电和并联电阻；
- 串联电池数量；
- DC-DC 启动电压；
- 储能器件和充电损耗。

## 16. 系统设计流程

```text
光源 → 光伏电池 → MPPT/DC-DC → 储能 → 稳压负载
```

建议步骤：

1. 获取实际光照时间序列；
2. 考虑方向、遮挡和季节；
3. 使用对应光谱下的电池数据；
4. 计算日均采集能量；
5. 加入变换器、储能和线路损耗；
6. 检查最差季节和冷启动条件。

## 17. 高频易错点

- 混淆辐照度与辐照量；
- 直接把 lux 当作 $\mathrm{W/m^2}$；
- 计算输入功率时忘记组件面积；
- 认为所有光子能量都能转换成电能；
- 认为 $V_{OC}$ 与光强线性；
- 忽略 $R_S$、$R_{SH}$ 和变换器启动条件；
- 只优化正午角度而忽略全年能量。

## 18. 公式速记

$$
E_{\mathrm{ph}}=\frac{hc}{\lambda}
$$

$$
S_m=S_i\sin(\alpha+\beta)
$$

$$
SR=\frac{q\lambda}{hc}QE
$$

$$
V_{OC}=\frac{nkT}{q}\ln\left(\frac{I_L}{I_0}+1\right)
$$

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}
$$

$$
\eta=\frac{V_{OC}I_{SC}FF}{P_{\mathrm{in}}}
$$

