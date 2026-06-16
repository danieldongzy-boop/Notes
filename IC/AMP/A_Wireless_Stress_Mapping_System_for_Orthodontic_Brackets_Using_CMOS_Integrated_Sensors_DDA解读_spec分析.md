# A Wireless Stress Mapping System for Orthodontic Brackets Using CMOS Integrated Sensors

## 1. 文章核心问题

这篇 JSSC 2013 论文做的是一个可无线供电、无线读出的正畸托槽应力映射系统。系统要被封装在牙齿托槽底座里，因此面积、厚度、功耗、读出时间和分辨率都受限。

论文的主线可以理解为：

- 在 0.35 um CMOS 中集成 24 个压阻式 FET stress sensors；
- 通过 DDA + SAR ADC + gain controller 对每个传感器进行可变增益读出；
- 用 13.56 MHz 感应耦合供电，并用 ASK 回传数据；
- 达到智能托槽需要的约 25 kPa 应力分辨率，实测最好到 11 kPa。

其中 DDA 是模拟前端的关键，因为传感器输出是小差分电压，同时传感器本身不希望被读出电路加载。

## 2. 系统架构速览

系统包括：

- 24 个 FET 型压阻应力传感器：10 个 NMOS，14 个 PMOS；
- MUX：选择某个 sensor 以及 bias direction；
- DDA：variable-gain differential difference amplifier；
- 10-bit SAR ADC；
- gain controller：根据 ADC 结果自动选择最大可用增益；
- digital control + 22-bit shift register；
- RF 部分：13.56 MHz 感应供电，847.5 kHz ASK 调制，13.56 kHz 数据频率。

传感器每次只激活一个，因此可以降低总功耗。每个 sensor 需要在 4 个 bias direction 下测量，用 DCS 方法抵消 offset、温度梯度等非机械应力贡献。

## 3. 为什么这里用 DDA

### 3.1 传感器接口需求

传感器是四晶体管桥式结构，输出是差分电压，但输出阻抗不低，且晶体管工作点容易被读出电路影响。论文明确提到：应避免从 sensor 抽取 cross currents，否则会改变 sensor operating point。

因此读出放大器需要：

- 高输入阻抗；
- 能接收差分 sensor signal；
- 能做闭环增益；
- 增益变化不能反过来改变 sensor 负载；
- offset 要低，噪声要接近 sensor 本底噪声；
- 功耗要小。

DDA 相比普通单输入差分 OTA/OPA 的优势，是它天然有两组差分输入：一组接 sensor，另一组接 feedback。这样 sensor 输入端和反馈网络分开，增益调整时反馈阻抗变化不会直接加载 sensor。

### 3.2 DDA 在本文中的连接方式

从 Fig. 12 看，DDA 输入端包括：

- `In+ / In-`：接传感器差分输出；
- `FB+ / FB-`：接反馈网络；
- 输出接 `R_L` 后进入 10-bit SAR ADC；
- gain controller 用 ADC 输出决定反馈 T-network 的开关配置。

直观表达为：

```text
sensor array -> DDA sensor input pair -> DDA output -> R_L -> SAR ADC
                         ^                         |
                         |                         v
                    feedback pair <- T-network <- gain controller
```

DDA 闭环工作时，反馈差分输入用于设定增益，sensor 差分输入保持高阻。这个分离是本文 DDA 方案最重要的点。

## 4. DDA 电路级解读

### 4.1 输入级与反馈级

Fig. 13 的 DDA 是一个带两组差分输入对的放大器：

- sensor input pair：`T_In+`, `T_In-`；
- feedback pair：`T_FB+`, `T_FB-`；
- 两组输入对尺寸都做得较大，`W/L = 100 um / 5 um`，主要是为了降低输入参考噪声；
- 其他晶体管 `T8-T10` 尺寸为 `80 um / 5 um`；
- 电流源晶体管 `T3-T7` 尺寸为 `32 um / 4 um`，每支约 `25 uA`。

论文强调：不管选什么增益，DDA 的总输入参考噪声都应当和 sensor 噪声处于同一量级，否则前端会成为系统瓶颈。

### 4.2 输出级与补偿

输出级为了获得较大输出摆幅，省掉了部分 cascode 结构。稳定性通过 Miller compensation 实现：

- `R_C = 23 kOhm`
- `C_C = 4.5 pF`

这一点说明作者更看重低电压供电下的输出范围和闭环稳定性，而不是追求极高输出阻抗。

### 4.3 DDA 关键设计指标

论文给出的 DDA 设计与实测参数如下：

| 项目 | 数值/说明 |
|---|---|
| DDA 类型 | variable-gain differential difference amplifier |
| 开环 DC 增益 | 92 dB |
| GBW | 2 MHz |
| 闭环增益范围 | 1 到 271，16 档数字选择 |
| 反馈网络 | resistive T-network |
| T-network 单位电阻 | `r = 109 kOhm` |
| 增益公式 | `A_CL = (R/r)^2 + 3(R/r) + 1` |
| `R/r` 取值 | 0 到 15 |
| 负载电阻 | `R_L = 436 kOhm` |
| ADC 输入电容 | 10 pF |
| 输出附加极点 | 36 kHz |
| 输入参考 offset | 38 到 270 uV，三颗 DDA 样本 |
| 输入共模下限 | 690 到 800 mV |
| 输入参考噪声积分带宽 | 1 Hz 到 36 kHz |
| 输入参考噪声 | 10.8 uV_rms |
| 最大增益输出噪声 | 2.1 mV_rms，约 0.6 LSB |
| DDA + ADC + GC 电流 | 290 uA at 3.3 V |

## 5. 可变增益与二叉树搜索

### 5.1 为什么需要自动增益

传感器信号幅度范围很大。小应力信号需要高增益提升分辨率；大应力信号若还用高增益会让 DDA 输出超出线性范围。

所以 gain controller 的目标不是固定最大增益，而是找：

> 在 DDA 输出仍在线性范围内的最大增益。

这相当于在分辨率和线性度之间自动折中。

### 5.2 16 档增益

由 Fig. 14(a) 可读出 16 档闭环增益：

```text
1, 5, 11, 19, 29, 41, 55, 71,
89, 109, 131, 155, 181, 209, 239, 271
```

这些增益来自：

```text
A_CL = (R/r)^2 + 3(R/r) + 1
R/r = 0, 1, 2, ..., 15
```

T-network 的好处是：如果用普通电阻分压，要覆盖 1 到 271 的增益，输出级看到的阻抗可能变化 271 倍；T-network 中只变化约 32 倍。因此它减轻了 DDA 输出负载变化，也更省面积、更利于匹配。

### 5.3 增益搜索流程

读出时先用最大增益 `271`。ADC 判断输出是否在 DDA 线性范围内：

- 输出低于 `79 LSB`，约 `255 mV`：over-range；
- 输出高于 `1024 - 79 LSB`，约 `3.045 V`：over-range；
- 中间区域：in-range。

若 over-range，则 gain controller 沿 Fig. 14(a) 的 binary search tree 降低增益，最多重复 6 次。每次 re-initialization 为 `100 us`，所以 DC stress signal 被等效搬移到 `10 kHz`。

找到理想增益后，系统会再次读出并平均，以抑制扰动。最终传输 22 bit：

- 10-bit sensor value；
- 5-bit sensor number；
- 2-bit bias direction；
- 1-bit error flag；
- 4-bit selected gain。

### 5.4 读出时间

- 若第一次 `A_CL = 271` 就 in-range，可直接平均，约 `200 us` 完成一次 readout；
- 若需要搜索，最长约 `600 us`；
- 表 I 给出的系统级采样时间是 `3.81 ms - 4.21 ms per sensor direction`；
- 全系统 cycle 时间为 `366 ms - 404 ms`。

## 6. DDA 噪声、线性度与瓶颈

### 6.1 噪声

sensor 本身在 1 Hz 到 36 kHz 内的输出噪声预测值：

- NMOS sensor：`8.1 uV_rms`；
- PMOS sensor：`8.4 uV_rms`。

DDA 输入参考噪声：

- `10.8 uV_rms`，略高于 sensor 噪声。

最大增益时 DDA 输出噪声：

- `2.1 mV_rms`。

但系统整体测试发现 ADC 输出标准差：

- DC supply：`0.9 LSB`；
- wireless supply：`1.9 LSB`；
- 等效 ADC 输入参考噪声分别为 `2.9 mV` 和 `6.1 mV`。

因此作者认为系统噪声瓶颈不是 DDA，而是标准单元 SAR ADC。这个判断很关键：DDA 已经基本够用，后续若优化分辨率，应优先换 ADC 或优化 ADC/供电噪声。

### 6.2 线性度

Fig. 16 显示 gain controller 会随着输入幅度增加逐级降低增益。在输入信号超过约 `400 mV` 前，DDA 输出 THD 保持在约 `< 2%`。

也就是说，自动增益控制让系统在小信号时保留分辨率，在大信号时防止 DDA 饱和或明显失真。

## 7. 系统 Spec 整理

来自 Table I：

| Spec                             | 数值                                        |
| -------------------------------- | ----------------------------------------- |
| Technology                       | 0.35 um CMOS & Au electroplating on Pyrex |
| System size                      | `2 x 2.5 x 0.73 mm^3`                     |
| Supply voltage                   | `3.3 V`，无线工作实测约 `3.19 V`                  |
| Power consumption                | `1.75 mW`，不含 RF interface                 |
| Communication approach           | inductive coupling with ASK               |
| Power link frequency             | `f_c = 13.56 MHz`                         |
| ASK modulation frequency         | `f_m = 847.5 kHz`                         |
| Sensor principle                 | 24 piezoresistive FET                     |
| Sensor composition               | 10 x NMOS, 14 x PMOS                      |
| NMOS sensitivity                 | `-783 uV/MPa` to `sigma_xy`               |
| PMOS sensitivity                 | `904 uV/MPa` to `sigma_xx`                |
| NMOS cross-sensitivity           | `11.4 uV/MPa` to `sigma_xx`               |
| PMOS cross-sensitivity           | `15.7 uV/MPa` to `sigma_xy`               |
| ADC                              | 10 bit                                    |
| Voltage resolution range         | `10 uV - 2.71 mV`，对应 `A_CL = 271 - 1`     |
| NMOS stress resolution range     | `13 kPa - 3.46 MPa`                       |
| PMOS stress resolution range     | `11 kPa - 3.00 MPa`                       |
| Linearity                        | `THD_% < 2%`                              |
| Sample time per sensor direction | `3.81 ms - 4.21 ms`                       |
| System cycle time                | `366 ms - 404 ms`                         |

论文目标分辨率来自应用需求：估计需要约 `25 kPa`。最终系统实测达到：

- NMOS：最大分辨率 `13 kPa`；
- PMOS：最大分辨率 `11 kPa`；

因此满足智能托槽应用需求。

## 8. DDA 设计取舍总结

### 优点

1. DDA 的 sensor input 与 feedback input 分离，避免反馈网络影响 sensor operating point。
2. 相比 3-opamp instrumentation amplifier，DDA 输入级更容易做 common-centroid 匹配，offset 表现更好。
3. 结合 DCS sensor bias rotation，可以不用 chopper，仍能抑制 offset 和温度梯度等低频误差。
4. 16 档自动增益扩大动态范围，小信号高分辨率，大信号不饱和。
5. T-network 反馈比普通电阻分压更适合大范围增益变化，输出负载变化小，面积也更友好。

### 局限

1. DDA 输入参考噪声 `10.8 uV_rms` 略高于 sensor 噪声，说明 DDA 不是完全透明的前端。
2. NMOS sensor common-mode 约 `721 mV`，而 DDA 输入共模下限样本间可到 `690-800 mV`，裕量并不大；因此论文必须加入 `R_CM` shifting resistor。
3. 最大增益输出噪声 `2.1 mV_rms` 虽低于 ADC/无线供电噪声，但已经不是特别小。
4. 系统最终噪声瓶颈在 ADC，DDA 做得更好也未必直接改善系统分辨率。

## 9. 对 IC 设计的启发

如果要复现或借鉴这篇文章的 DDA：

- 首先要明确 sensor 的 common-mode 范围，尤其是低端输入共模裕量；
- DDA 输入对尺寸需要按 sensor noise budget 来定，而不是只按带宽定；
- feedback 网络最好不要直接改变 sensor 端等效阻抗；
- 自动增益逻辑要和 ADC full-scale、DDA output swing、THD 上限一起定义；
- 若系统级噪声由 ADC 主导，继续堆 DDA 增益/噪声性能收益有限；
- 对低频应力/生物传感信号，DCS 或 current rotation 是 offset 抑制的好方法，可以降低 chopper 需求和纹波问题。

一句话总结：本文的 DDA 是一个为高阻、小信号、低功耗 sensor readout 定制的可变增益前端。它的价值不只在放大倍数，而在“高阻接入 + 反馈隔离 + 自动增益 + 与 DCS 配合抵消 offset”的整体读出策略。
