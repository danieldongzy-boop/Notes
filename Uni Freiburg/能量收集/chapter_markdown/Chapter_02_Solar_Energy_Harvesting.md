# Chapter 2 - Solar Energy Harvesting: 太阳能先看光，再看电池

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_2_Solar Energy Harvesting_SS_2026.pdf`
- Exercise: `Exercise 2_Photovoltaics_SOLVED_SS_2026.pdf`
- Exercise information: Solems solar cell datasheet PDFs

## 这一章在讲什么

太阳能收集分两步：

1. 到达太阳能电池表面的光有多少？
2. 电池能把这些光变成多少电功率？

作业也是这两个方向：先算不同角度下的辐照度，再算太阳能电池的短路电流、开路电压、填充因子和效率。

## 作业重点公式

### 光子能量

$$
E_\mathrm{photon} = hf = \frac{hc}{\lambda}
$$

说人话：同样的光功率下，波长越长，单个光子能量越低，光子数量越多。作业里用它把入射光功率换成光子流，再换成电流。

### 入射到倾斜模块上的直射光

课件给出的核心关系是：

$$
S_m = S_i \sin(\alpha+\beta)
$$

- $S_i$：垂直于太阳光方向的辐照度
- $\alpha$：太阳高度角
- $\beta$：太阳能板相对地平线的角度

当 $\alpha+\beta=90^\circ$ 时，光线正对太阳能板，直射辐照度最大。

作业例子：

$$
850 \cdot \sin(45^\circ+45^\circ)=850 \ \mathrm{W/m^2}
$$

如果板子只有 $15^\circ$：

$$
850 \cdot \sin(45^\circ+15^\circ)=736 \ \mathrm{W/m^2}
$$

课件中也常用一个经验扩散光修正：

$$
I_G \approx 1.1 I_D
$$

所以夏天那题会得到约 $935 \ \mathrm{W/m^2}$ 和 $810 \ \mathrm{W/m^2}$。

### 冬天阴天的扩散光

作业里把阴天辐照度分成：

$$
I_\mathrm{total}=I_\mathrm{direct}+I_\mathrm{diffuse}
$$

扩散光用近似：

$$
I_\mathrm{diffuse}=I_\mathrm{cloud}\frac{180^\circ-\beta}{180^\circ}
$$

说人话：板子越平，能“看见”的天空越多，扩散光越多；板子越竖，扩散光少一些。

### 短路电流

理想量子效率 $QE=1$ 时：

$$
I_{SC} = q \cdot \frac{P_\mathrm{in}}{E_\mathrm{photon}}
$$

也就是：

$$
I_{SC} = QE \cdot q \cdot P_\mathrm{in}\frac{\lambda}{hc}
$$

其中：

$$
P_\mathrm{in}=H \cdot A
$$

说人话：入射光功率除以单个光子的能量，得到每秒多少个光子；每个光子理想情况下产生一个电子-空穴对，所以乘电子电荷得到电流。

### 太阳能电池 I-V 方程

无光时是二极管：

$$
I = I_0\left(e^{qV/(nkT)}-1\right)
$$

有光并把发电方向取正：

$$
I = I_L - I_0\left(e^{qV/(nkT)}-1\right)
$$

- $I_0$：暗电流
- $I_L$：光生电流，通常近似等于 $I_{SC}$
- $n$：理想因子

### 开路电压

开路时 $I=0$：

$$
V_{OC}=\frac{nkT}{q}\ln\left(\frac{I_L}{I_0}+1\right)
$$

说人话：光越强，$I_L$ 越大，$V_{OC}$ 增加；但因为是对数关系，光强翻倍不会让电压翻倍。

### 填充因子 FF

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}=\frac{V_{MP}I_{MP}}{V_{OC}I_{SC}}
$$

常用近似：

$$
v_{OC}=\frac{qV_{OC}}{nkT}
$$

$$
FF \approx \frac{v_{OC}-\ln(v_{OC}+0.72)}{v_{OC}+1}
$$

说人话：FF 表示 I-V 曲线能不能接近一个“方形”。越接近方形，最大功率越接近 $V_{OC}I_{SC}$。

### 效率

$$
\eta = \frac{P_\mathrm{max}}{P_\mathrm{in}}
=\frac{V_{OC}I_{SC}FF}{P_\mathrm{in}}
$$

作业中的硅电池题算出大约 $31.9\%$，接近硅单结电池理论上限。

### 串联电阻对 FF 的影响

先定义特征电阻：

$$
R_{CH}\approx \frac{V_{OC}}{I_{SC}}
$$

再定义归一化串联电阻：

$$
r_S=\frac{R_S}{R_{CH}}
$$

课件/作业用的近似：

$$
FF_S \approx FF_0\left(1-1.1r_S+\frac{r_S^2}{5.4}\right)
$$

说人话：串联电阻会吃掉一部分功率，让 I-V 曲线变“软”，FF 下降。作业里 $R_S=0.01 \ \Omega$，损失约 $1.6\%$。

## 室内光伏题怎么做

数据表给了不同照明下的：

- $V_{OC}$
- $I_{SC}$
- 最大功率点 $V_{MP}, I_{MP}$

直接算：

$$
P_{MP}=V_{MP}I_{MP}
$$

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}
$$

$$
\eta=\frac{P_{MP}}{P_\mathrm{in}}
$$

室内光伏的重点不是效率有多高，而是光谱和照度是否匹配。`lux` 是按人眼敏感度定义的，不等于太阳能电池真正关心的光谱功率。

## 太阳位置 Bonus 公式

作业 Bonus 用到这些：

$$
HRA = 15^\circ (LST-12)
$$

$$
\delta = 23.45^\circ \sin\left(\frac{360^\circ(d-81)}{365}\right)
$$

$$
\alpha=\sin^{-1}\left(\sin\delta\sin\varphi+\cos\delta\cos\varphi\cos(HRA)\right)
$$

说人话：

- $HRA$ 表示现在离太阳正午差多少角度。
- $\delta$ 表示季节导致的太阳赤纬。
- $\alpha$ 是太阳高度角。

## 易错点

- 太阳能板最佳角度不是固定一个数字，而是要让光线尽量垂直打到板上。
- $V_{OC}$ 和 $I_{SC}$ 不能直接相乘当输出功率，中间要乘 $FF$。
- 面积换算小心：$5 \ \mathrm{cm} \times 5 \ \mathrm{cm}=25 \ \mathrm{cm^2}=2.5\times10^{-3} \ \mathrm{m^2}$。
- 室内光伏不能只看太阳光效率，室内光谱、低照度、数据表条件更重要。

