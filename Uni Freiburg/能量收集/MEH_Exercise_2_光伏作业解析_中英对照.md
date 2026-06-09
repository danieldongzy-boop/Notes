# Exercise 2 光伏作业逐步解析

> 原文件：`Exercise 2_Photovoltaics_SOLVED_SS_2026.pdf`

## Task 1：辐照度

### 1(a) 夏季最佳朝向

已知：

$$
I_D=850\,\mathrm{W/m^2},\qquad \alpha=45^\circ
$$

组件接收到的直接辐照度：

$$
S_m=S_i\sin(\alpha+\beta)
$$

最大值要求：

$$
\alpha+\beta=90^\circ
$$

因此：

$$
\boxed{\beta=45^\circ}
$$

$$
S_m=850\sin90^\circ
=\boxed{850\,\mathrm{W/m^2}}
$$

加入课件采用的 10% 漫射经验修正：

$$
S_G=1.1S_m
=\boxed{935\,\mathrm{W/m^2}}
$$

### 1(b) 夏季组件倾角为 $15^\circ$

$$
S_m=850\sin(45^\circ+15^\circ)
$$

$$
S_m\approx\boxed{736\,\mathrm{W/m^2}}
$$

$$
S_G\approx1.1\cdot736
=\boxed{810\,\mathrm{W/m^2}}
$$

### 冬季情况

已知：

$$
I_D=I_{\mathrm{diff}}=300\,\mathrm{W/m^2}
$$

$$
\alpha=23^\circ
$$

漫射分量按题目模型计算：

$$
S_{m,\mathrm{diff}}
=I_{\mathrm{diff}}
\frac{180^\circ-\beta}{180^\circ}
$$

#### 当 $\beta=15^\circ$

$$
S_{m,\mathrm{direct}}
=300\sin38^\circ
\approx185\,\mathrm{W/m^2}
$$

$$
S_{m,\mathrm{diff}}
=300\frac{165}{180}
=275\,\mathrm{W/m^2}
$$

$$
\boxed{S_{\mathrm{global}}=460\,\mathrm{W/m^2}}
$$

#### 当 $\beta=45^\circ$

$$
S_{m,\mathrm{direct}}
=300\sin68^\circ
\approx278\,\mathrm{W/m^2}
$$

$$
S_{m,\mathrm{diff}}
=300\frac{135}{180}
=225\,\mathrm{W/m^2}
$$

$$
\boxed{S_{\mathrm{global}}=503\,\mathrm{W/m^2}}
$$

较陡的组件冬季接收更多直接辐射，但接收的漫射辐射较少。

## Task 2：硅太阳电池

### 已知参数

$$
\lambda=589\,\mathrm{nm},\quad
I_G=1000\,\mathrm{W/m^2}
$$

$$
A=(0.05\,\mathrm m)^2
=2.5\times10^{-3}\,\mathrm{m^2}
$$

$$
n=1.1,\quad I_0=10^{-12}\,\mathrm A,\quad T=300\,\mathrm K,\quad QE=1
$$

### 2(a)-1 输入光功率

$$
P_{\mathrm{in}}=I_GA
=1000\cdot2.5\times10^{-3}
=\boxed{2.5\,\mathrm W}
$$

### 2(a)-2 短路电流

$$
SR(\lambda)=\frac{q\lambda}{hc}QE
$$

$$
I_{SC}=\frac{q\lambda}{hc}QE\,P_{\mathrm{in}}
$$

代入：

$$
I_{SC}\approx
\frac{
1.602\times10^{-19}\cdot589\times10^{-9}
}{
6.626\times10^{-34}\cdot2.998\times10^8
}
\cdot2.5
$$

$$
\boxed{I_{SC}\approx1.19\,\mathrm A}
$$

### 2(a)-3 开路电压

$$
V_{OC}=\frac{nkT}{q}
\ln\left(\frac{I_L}{I_0}+1\right)
$$

取 $I_L\approx I_{SC}$：

$$
\boxed{V_{OC}\approx0.79\,\mathrm V}
$$

### 2(a)-4 填充因子

$$
\nu_{OC}=\frac{qV_{OC}}{nkT}
\approx27.8
$$

$$
FF=
\frac{\nu_{OC}-\ln(\nu_{OC}+0.72)}
{\nu_{OC}+1}
$$

$$
\boxed{FF\approx0.849}
$$

### 2(a)-5 效率

$$
\eta=
\frac{V_{OC}I_{SC}FF}{P_{\mathrm{in}}}
$$

$$
\eta=
\frac{0.79\cdot1.19\cdot0.849}{2.5}
\approx\boxed{31.9\%}
$$

这个效率较高，是因为题目假设单色光、$QE=1$ 且载流子全部被收集。

### 2(b) 串联电阻造成的损失

$$
R_S=0.01\,\Omega
$$

特征电阻：

$$
R_{CH}\approx\frac{V_{OC}}{I_{SC}}
=\frac{0.79}{1.19}
\approx0.666\,\Omega
$$

$$
r_S=\frac{R_S}{R_{CH}}
\approx0.015
$$

原最大功率：

$$
P_{\max}=FFV_{OC}I_{SC}
\approx0.80\,\mathrm W
$$

修正后的填充因子：

$$
FF_S=FF_0(1-1.1r_S)+\frac{r_S^2}{5.4}
\approx0.835
$$

$$
P'_{\max}=0.835\cdot0.79\cdot1.19
\approx0.78\,\mathrm W
$$

$$
\frac{P'_{\max}}{P_{\max}}
=\frac{FF_S}{FF_0}
\approx98.4\%
$$

$$
\boxed{\text{功率损失}\approx1.6\%}
$$

## Task 3：室内光伏

电池面积：

$$
A=11\,\mathrm{cm^2}
=1.1\times10^{-3}\,\mathrm{m^2}
$$

### 3(a) 填充因子

$$
P_{MP}=V_{MP}I_{MP}
$$

$$
FF=\frac{P_{MP}}{V_{OC}I_{SC}}
$$

| 光照条件 | $P_{MP}$ | $FF$ |
|---|---:|---:|
| 200 lux | $0.0336\,mW$ | $0.57$ |
| 1000 lux | $0.186\,mW$ | $0.63$ |
| $200\,W/m^2$ | $6.30\,mW$ | $0.70$ |
| $1000\,W/m^2$ | $35.52\,mW$ | $0.65$ |

### 效率估算

室内情况按题解假设光效为：

$$
100\,\mathrm{lm/W}
$$

因为：

$$
1\,\mathrm{lux}=1\,\mathrm{lm/m^2}
$$

200 lux 对应的输入功率为：

$$
P_{\mathrm{in}}
=\frac{200}{100}\cdot1.1\times10^{-3}
=0.0022\,\mathrm W
$$

1000 lux 对应 $0.011\,\mathrm W$。

对于以 $\mathrm{W/m^2}$ 给出的情况：

$$
P_{\mathrm{in}}=IA
$$

| 光照条件 | $P_{\mathrm{in}}$ | 效率 |
|---|---:|---:|
| 200 lux | $2.2\,mW$ | $1.53\%$ |
| 1000 lux | $11\,mW$ | $1.69\%$ |
| $200\,W/m^2$ | $0.22\,W$ | $2.86\%$ |
| $1000\,W/m^2$ | $1.1\,W$ | $3.23\%$ |

注意：lux 换算依赖灯具光谱与光效，因此这里的效率只是题目假设下的估算。

### 3(b) 储能系统

题解建议使用带充电控制器的锂离子电池系统。电池电压匹配较方便，但必须考虑 DC-DC 和充电损耗。

### 3(c) 其他用途

因为：

$$
I_{SC}\propto\text{光照强度}
$$

太阳电池还可兼作光照传感器。

## Bonus Task 4：太阳位置

Toronto：

$$
\varphi=43.66135^\circ,\quad
\mathrm{Longitude}=-79.383087^\circ
$$

UTC-5：

$$
LSTM=-75^\circ
$$

11 月 12 日为第 $316$ 天。

### 时间方程

$$
B=\frac{360^\circ}{365}(316-81)
\approx231.8^\circ
$$

$$
EoT=
9.87\sin2B-7.53\cos B-1.5\sin B
\approx15.4\,\mathrm{min}
$$

$$
TC=4(-79.38+75)+15.4
\approx-2.1\,\mathrm{min}
$$

$$
LST=10+\frac{-2.1}{60}
\approx9.965
$$

### 时角

$$
HRA=15^\circ(9.965-12)
\approx\boxed{-30.5^\circ}
$$

### 赤纬

$$
\delta=
23.45^\circ\sin\left[
\frac{360^\circ}{365}(316-81)
\right]
\approx-18.42^\circ
$$

### 高度角

$$
\alpha=
\sin^{-1}\left(
\sin\delta\sin\varphi+
\cos\delta\cos\varphi\cos HRA
\right)
$$

$$
\boxed{\alpha\approx21.9^\circ}
$$

### 方位角

按课件采用的方位角定义：

$$
\boxed{\mathrm{Azimuth}\approx153.5^\circ}
$$

负时角说明此时位于上午。

## 最终结果

| 项目 | 结果 |
|---|---:|
| 夏季最佳倾角 | $45^\circ$ |
| 夏季最佳 global irradiance | $935\,W/m^2$ |
| 冬季 $\beta=15^\circ$ | $460\,W/m^2$ |
| 冬季 $\beta=45^\circ$ | $503\,W/m^2$ |
| $I_{SC}$ | $1.19\,A$ |
| $V_{OC}$ | $0.79\,V$ |
| FF | $0.849$ |
| 效率 | $31.9\%$ |
| 串联电阻功率损失 | $1.6\%$ |
| Toronto 时角 | $-30.5^\circ$ |
| Toronto 高度角 | $21.9^\circ$ |
| Toronto 方位角 | $153.5^\circ$ |

