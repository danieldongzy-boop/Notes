---
title: CIM 入门综述：从模拟信号链 IC 到 SRAM-CIM
tags:
  - CIM
  - SRAM-CIM
  - compute-in-memory
  - analog-IC
created: 2026-07-08
---

# CIM 入门综述：从模拟信号链 IC 到 SRAM-CIM

## 0. 先给一个直觉

Compute-in-Memory，常写作 CIM 或 IMC，核心目标不是“发明一种更快的乘法器”，而是减少数据搬运。传统数字系统里，权重/激活从存储器搬到计算单元，算完再搬回去。对 DNN、搜索、图计算这类数据密集任务，能量和延迟常常花在搬数据上，而不是花在乘加本身上。

从模拟信号链 IC 的视角看，CIM 很像把一部分“信号处理链”折叠进存储阵列里：

- 存储单元提供权重，类似可配置的增益/开关/电导。
- 输入激活通过 WL、BL、SL、电压、电流、脉宽或电荷注入阵列。
- 阵列天然完成并行加和，尤其适合向量-矩阵乘法，也就是 VMM/MAC。
- 外围电路负责感测、量化、移位累加、校准和数据流调度。

所以 CIM 的难点也非常像混合信号系统设计：阵列线性度、噪声、失配、动态范围、ADC 代价、PVT、IR drop、读扰动、校准、算法容错。只是这里的“前端传感器”变成了存储阵列，“被测信号”变成了乘加结果。

## 1. CIM 为什么重要

Von Neumann 架构把存储和计算分开，通用性很好，但在大规模数据搬运时效率低。SRAM-IMC survey 中提到，数据传输能量可能比算术操作高出两个数量级量级；这正是 DNN 推理、缓存内搜索、数据库比较、模式匹配等任务被 CIM 吸引的原因。

CIM 的典型收益来自三件事：

1. **并行性**：一行或多行同时激活，多个列方向同时产生部分和。
2. **近数据/存内计算**：减少从 SRAM/DRAM/非易失存储到 ALU/MAC array 的往返。
3. **物理加和**：电流、电荷或电压在 bitline / capacitor / sense path 上自然叠加，阵列可以用物理定律完成 accumulation。

但 CIM 不等于免费午餐。它把传统数字 MAC 的确定性，换成了阵列、电路、算法共同承担误差和复杂度。尤其是 analog CIM，乘加本体可能很省能量，但 DAC/ADC、校准、阵列外围和数据重排会决定最终系统是否真的划算。

## 2. CIM 的大分类

### 2.1 按存储介质分

| 类型 | 优点 | 主要问题 | 适合初学关注点 |
|---|---|---|---|
| SRAM-CIM | CMOS 兼容、速度快、工艺成熟、耐久性高、适合片上缓存/边缘 AI | 面积密度低，6T 读扰动，多 bit 模拟精度难，ADC/SA 外围开销大 | 最适合从传统 IC 转入 CIM 的入口 |
| DRAM-CIM | 密度高，可利用大容量主存/近存储计算 | refresh、破坏性读、工艺/接口限制 | 系统和架构导向更多 |
| RRAM/ReRAM-CIM | 非易失、高密度、天然电导乘法，适合 crossbar VMM | 写入变异、漂移、耐久、forming、精度和可靠性 | 理解 analog VMM 的经典平台 |
| PCM/MRAM/FeFET 等 | 各有非易失/密度/速度优势 | 材料和器件成熟度、变异性、集成难度 | 偏器件-电路协同 |

对你现在的背景，建议优先从 **SRAM-CIM** 开始。原因很简单：它离现有 CMOS/ADC/SA/存储编译器/SoC flow 最近，能最快把你已有的模拟链路能力迁移过来。

### 2.2 按计算域分

| 类型 | 核心做法 | 优点 | 代价 |
|---|---|---|---|
| Digital CIM, DCIM | 在 bitcell、sense path 或 column peripheral 中做逻辑/位串行运算 | 精度高、可验证性强、PVT 鲁棒、随工艺缩放较友好 | 并行 MAC 密度和能效不如模拟方案，周期数可能多 |
| Analog CIM, ACIM | 用电流、电荷、电压、时间等模拟量完成乘加 | 能效和面积潜力高，适合低/中精度 VMM | ADC/DAC、噪声、失配、线性度、动态范围、校准 |
| Mixed/Hybrid CIM | 模拟负责低位/局部累加，数字负责高位/校正/累加 | 在精度、能效和鲁棒性间折中 | 架构和验证复杂度更高 |

2024 年的一篇 SRAM-CIM review 将 SRAM CIM 重点分为 DCIM、ACIM 和 hybrid CIM，并指出 DCIM 偏高精度和工艺缩放，ACIM 偏功耗/面积效率，hybrid 试图把两者优势结合起来。

## 3. CIM 最常见的计算：VMM/MAC

神经网络中的线性层或卷积最终都可以展开为：

```text
y_j = sum_i x_i * w_ij
```

在 SRAM-CIM 中，可以把 `w_ij` 存在 bitcell 里，把 `x_i` 映射成 WL 上的电压、脉宽、时间窗口或数字激活信号。列方向 bitline 汇聚所有 `i` 的贡献，得到 `y_j` 的模拟或数字部分和。

对应到电路：

- **乘法**：由输入激活与存储权重共同决定某个 bitcell 是否向列贡献电流/电荷/逻辑结果。
- **加法**：由 BL/局部 BL/电容节点/计数器完成列方向 accumulation。
- **量化**：由 SA、ADC、TDC、counter 或多周期比较完成。
- **多 bit**：通过 bit slicing、time slicing、multi-level input、multi-row activation、shift-and-add 实现。

这就是为什么 CIM 论文里经常看到关键词：MAC、VMM、MVM、XNOR-popcount、bit-serial、charge sharing、current summation、SAR ADC、ADC sharing、near-memory accumulation。

## 4. SRAM-CIM 重点入门

### 4.1 SRAM-CIM 的基本形态

传统 SRAM macro 由 bitcell array、WL driver、precharge、BL/BLB、sense amplifier、write driver、decoder、IO mux 构成。SRAM-CIM 在这个基础上做三类改造：

1. **改 bitcell**：从 6T 扩展到 8T、10T、12T、4+2T 等，让读路径和存储节点隔离，或增加计算端口。
2. **改 bitline/sense path**：让多行同时激活，在 BL 上形成电流/电荷/电压叠加，再通过 SA/ADC 判断。
3. **改外围数字逻辑**：在 column peripheral 或 near-memory block 中加入 XNOR、AND、popcount、adder tree、shift-add、累加寄存器。

SRAM-CIM 的关键问题是：如何在不破坏 SRAM 可靠性的前提下，让多个 bitcell 同时参与计算。

### 4.2 6T、8T、10T：为什么 bitcell 这么重要

**6T SRAM** 面积最小、最接近 foundry 标准 bitcell，但它的读路径直接耦合内部存储节点。多行同时打开时，BL/BLB 上的扰动和 cell ratio 问题会放大，容易出现 read disturb、read noise margin 降低和 sensing failure。

**8T SRAM** 增加独立读端口，把读路径与存储节点隔离，CIM 操作更安全。代价是面积变大，阵列密度下降。很多 SRAM-CIM 原型喜欢 8T 或 10T，因为它给模拟读出和多行激活留出更大的电路余量。

**10T/12T 或定制 bitcell** 可以进一步支持差分计算、XNOR、signed weight、局部乘法或更高鲁棒性，但面积和版图复杂度更高，也更难直接用标准 SRAM compiler。

一个实用判断：

- 追求产品化和兼容性：尽量靠近 6T/8T 标准 SRAM。
- 追求论文指标和功能展示：定制 bitcell 更灵活。
- 追求高精度 analog MAC：通常需要更强的读隔离、校准和外围支持。

### 4.3 Digital SRAM-CIM

DCIM 尽量保持数字确定性。常见路线包括：

- **bitwise logic in SRAM**：通过同时激活多行，在 SA 或外围实现 AND/OR/XOR/XNOR。
- **XNOR-popcount**：特别适合 BNN/TNN。权重和激活二值化后，乘法变成 XNOR，累加变成 popcount。
- **bit-serial MAC**：多 bit 乘法拆成多轮 bit-level 操作，再在数字外围 shift-and-add。
- **compute cache**：把 LLC/cache macro 加入简单逻辑，让部分数据并行操作在缓存内完成。

DCIM 的优势：

- 精度和功能更容易验证。
- PVT、噪声、失配压力较小。
- 更容易接入数字 EDA flow。
- 对中高精度整数推理更友好。

DCIM 的劣势：

- 多 bit MAC 往往需要多个周期。
- 数字外围和路由可能吃掉面积/能耗。
- 阵列内部“物理加和”的优势不如 ACIM 明显。

从学习角度，DCIM 是理解 SRAM-CIM 架构和数据流的好入口；从模拟 IC 迁移角度，ACIM 更能发挥你的原有经验。

### 4.4 Analog SRAM-CIM

ACIM 用模拟物理量完成乘加。常见实现方式有三类：

#### 4.4.1 Current-domain CIM

输入激活控制 WL 电压、脉宽或选择信号，存储权重决定 cell 是否导通，多个 cell 的电流在 BL 上叠加：

```text
I_BL ~= sum_i f(x_i, w_ij)
```

优点是直观、速度快、并行度高。问题是大列电流、IR drop、BL 电容、device mismatch、输入相关非线性、动态范围和 sensing margin。列越长、同时激活行越多，越容易遇到功耗和线性度问题。

#### 4.4.2 Charge-domain CIM

把输入或权重转换成电荷注入，再在电容节点上累加/共享。对模拟信号链工程师来说，这一路线很像 switched-capacitor MAC：

- 预充电或采样输入。
- 根据权重选择是否向电容贡献电荷。
- 多个 cell 或多个周期累加。
- 最后用 ADC/比较器读出。

优点是能量可控、适合低电压和中等精度，很多设计可以借鉴 ADC/CDAC/SC filter 的直觉。挑战是 kT/C noise、charge injection、clock feedthrough、电容 mismatch、leakage、时钟相位和版图寄生。

#### 4.4.3 Time-domain CIM

把输入映射为脉宽、延迟或时间窗口，计算结果通过时间积分、计数或 TDC 读出。它可以减少传统幅度型 ADC 的压力，但把问题转移到时钟、延迟线、抖动、PVT 漂移和 TDC/counter 上。

### 4.5 SRAM-CIM 里的“模拟信号链”

如果把 SRAM-CIM macro 当成一个混合信号链，可以这样拆：

```text
数字输入/激活
  -> 输入编码/DAC/脉宽调制/WL driver
  -> SRAM bitcell array 乘法与列累加
  -> BL/局部 BL 模拟节点
  -> SA/ADC/TDC/比较器
  -> 数字校正、shift-add、累加、激活函数
```

你熟悉的传统模拟信号链经验会直接用在这些地方：

- **动态范围规划**：最大激活行数、权重 bit 数、输入 bit 数、列长度决定 BL swing/ADC range。
- **噪声预算**：thermal noise、mismatch、supply noise、digital coupling、quantization noise。
- **线性度**：cell current vs WL/BL voltage、BL discharge 非线性、charge sharing 非理想。
- **采样与时序**：precharge、evaluate、sample、reset、multi-cycle accumulation。
- **ADC 选择**：flash 快但面积功耗高；SAR 折中常见；single-slope/计数型适合高并行但慢；SA-based quantizer 适合低 bit。
- **校准**：offset cancellation、reference tracking、dummy column、background calibration、algorithm-aware retraining。

一个常见误区是只看“阵列 MAC 很省电”。真正的设计闭环要看：

```text
总能耗 = 阵列计算 + WL/BL 切换 + ADC/DAC/SA + 数字累加 + SRAM 访问/搬运 + 控制开销
```

在低精度任务中，阵列和简单 SA 可能很占优；一旦要求 6-8 bit 以上有效精度，ADC 和校准成本会迅速变成主角。

### 4.6 多 bit 与 signed 计算

实际网络不会永远是 1 bit。SRAM-CIM 常用以下技巧支持多 bit：

- **Bit slicing**：把多 bit 权重拆到多个 bitcell/多个阵列 bit-plane。
- **Input slicing**：把多 bit activation 分多周期送入。
- **Shift-and-add**：每个 bit-plane 的结果按权重位宽移位累加。
- **Differential columns**：正负权重分别存储，输出相减实现 signed weight。
- **Offset/bias correction**：对二值/无符号阵列输出做数字域修正。
- **Partial sum hierarchy**：local BL -> global BL -> ADC -> digital accumulator。

这里的系统问题是数据流而不只是电路：权重如何排布，卷积如何展开，partial sum 存在哪里，ADC 多少列共享一次，输出带宽够不够，数字后处理是否抵消了 CIM 的收益。

### 4.7 评价指标

读 CIM 论文时，建议同时看这些指标：

- **TOPS/W**：能效，但要确认是否只算 macro、是否包含 ADC/DAC、是否包含稀疏/零跳过。
- **TOPS/mm²**：面积效率，注意 bitcell 类型和外围面积。
- **计算精度**：bit-width、ENOB、MAC precision、是否支持 signed。
- **模型精度损失**：CIFAR/ImageNet/keyword spotting 等任务上 top-1 drop。
- **工艺节点和电压**：先进节点、低 VDD 往往带来不同稳定性问题。
- **阵列大小**：小 macro 指标漂亮，大阵列会遇到 BL 电容、IR drop、yield 和校准问题。
- **是否可编程**：固定 CNN 加速器与通用 CIM macro 是不同问题。
- **是否包含系统开销**：片上 SRAM、NoC、DMA、controller、activation buffer、batch norm/activation。

## 5. SRAM-CIM 的核心挑战

### 5.1 读稳定性和扰动

多行同时激活会改变传统 SRAM 的读假设。6T cell 尤其敏感，因为读路径会影响内部节点。解决方案包括降低 WL 电压、限制 simultaneous row count、使用 8T/10T、采用分段 BL、增强 sensing margin、算法上限制并行度。

### 5.2 ADC/DAC 外围开销

ACIM 的阵列本身可能非常高效，但每列一个高精度 ADC 通常不可承受。常见折中包括：

- 多列共享 ADC。
- 使用低 bit ADC 加多周期累加。
- 用 SA 做 1-3 bit 量化。
- 把一部分计算移到数字域。
- 算法训练时注入硬件噪声，让网络适应低精度。

### 5.3 模拟非理想

包括 offset、mismatch、nonlinearity、BL coupling、supply droop、temperature drift、process corner、charge leakage、clock jitter。对 CIM 来说，这些不是“后端小误差”，而会直接变成 MAC 误差。

### 5.4 数据映射和架构瓶颈

CIM macro 只解决了局部 VMM。真实系统还要处理：

- 卷积层 im2col 或 weight-stationary 映射。
- activation/partial sum buffer。
- 多 macro 之间的数据交换。
- transformer 中 attention、softmax、normalization 等非 MAC 操作。
- 稀疏性、batch size、编译器调度。

因此，一个好 SRAM-CIM 设计通常是 circuit + architecture + algorithm co-design，而不是单点电路优化。

## 6. 与 RRAM/PCM analog CIM 的区别

RRAM/PCM crossbar 常被看作 analog CIM 的代表，因为电导天然表示权重，欧姆定律和基尔霍夫电流定律直接实现 VMM。相比之下，SRAM-CIM 的权重本质上是数字存储，模拟计算通常来自读路径、电流/电荷累加和外围转换。

SRAM-CIM 的优势：

- CMOS 工艺成熟，不需要新型存储器件。
- 写入快、耐久高、变异小。
- 适合片上缓存和边缘 AI accelerator。
- 工程导入风险较低。

SRAM-CIM 的短板：

- bitcell 面积大，权重密度低。
- 非易失性缺失，断电后权重需重载。
- analog 多 bit 精度不如理想 crossbar 直观。

所以：SRAM-CIM 更像“用成熟 CMOS SRAM 做高效低/中精度计算”；RRAM/PCM-CIM 更像“用器件电导阵列做高密度 analog VMM”。两条路线都重要，但工程风险和研究问题不一样。

## 7. 给模拟信号链 IC 工程师的迁移地图

你已有的传统模拟 IC 能力，在 CIM 中可以这样对应：

| 传统模拟链路能力 | CIM 中的对应问题 |
|---|---|
| ADC/SAR/CDAC/比较器 | column ADC、低 bit 量化、SA-based ADC、reference ladder |
| switched-capacitor | charge-domain MAC、采样累加、kT/C 与 charge injection |
| 电流镜/跨导/电流积分 | current-domain BL accumulation、linear range、headroom |
| 噪声/失配分析 | MAC error budget、ENOB、CSNR、model accuracy drop |
| 时钟和采样 | precharge/evaluate/sample/reset，多周期 bit slicing |
| 版图寄生 | BL/WL RC、coupling、IR drop、matching、array edge effect |
| 校准 | offset/background calibration、reference tracking、algorithm-aware compensation |
| 系统建模 | circuit nonideality -> quantization/noise model -> DNN accuracy |

建议你不要一开始就陷入器件材料或 AI 模型细节。更高效的路径是：

1. 先理解 SRAM macro 和 bitcell 读写稳定性。
2. 再理解 DCIM/ACIM 的基本数据流。
3. 然后重点看 column ADC/SA/bitline compute。
4. 最后补 algorithm-aware training 和 mapping。

## 8. 一个入门学习路线

### 第一阶段：概念和分类

- CIM/IMC/PIM 的区别。
- VMM/MAC 为什么适合 CIM。
- SRAM、DRAM、RRAM/PCM 各自的 CIM 路线。
- DCIM、ACIM、hybrid CIM 的 trade-off。

### 第二阶段：SRAM-CIM 电路

- 6T/8T/10T SRAM bitcell。
- 多行激活与 read disturb。
- BL current/charge accumulation。
- SA、ADC、TDC、counter、popcount。
- bit slicing 和 shift-add。

### 第三阶段：系统和算法

- CNN/MLP/Transformer 的算子映射。
- weight stationary / output stationary / row stationary。
- quantization-aware training。
- hardware-aware noise injection。
- macro 到 accelerator 的数据搬运。

### 第四阶段：读论文时做拆解

每读一篇 SRAM-CIM 论文，建议固定回答：

- 用的是 6T、8T 还是定制 cell？
- 计算在 bitcell、BL、SA 还是外围数字逻辑里？
- 是 current、charge、voltage、time 还是 digital？
- 支持几 bit input/weight/output？
- ADC/DAC 是否计入能耗和面积？
- 阵列多大？是否多 macro？
- 模型精度损失多少？
- 这个设计最怕的 nonideality 是什么？

## 9. 关键术语速查

- **CIM / IMC**：compute/in-memory computing，在存储阵列内部或附近完成计算。
- **PIM**：processing-in-memory，更宽泛，常包括近存储处理器、DRAM/HBM 内逻辑等。
- **MVM/VMM**：matrix-vector multiplication / vector-matrix multiplication。
- **MAC**：multiply-accumulate。
- **BNN/TNN**：binary/ternary neural network。
- **XNOR-popcount**：二值网络常用计算形式。
- **Bit slicing**：把多 bit 数值拆成多个 bit-plane。
- **SA**：sense amplifier。
- **ADC sharing**：多个列共享一个 ADC，降低面积功耗。
- **CSNR**：compute signal-to-noise ratio，用于刻画 analog CIM 计算信号与噪声/误差的关系。
- **Read disturb**：读操作扰动 SRAM 内部存储节点。

## 10. 推荐阅读

1. Kentaro Yoshioka 等，*A Review of SRAM-based Compute-in-Memory Circuits*，2024。适合作为 SRAM-CIM 主线综述，覆盖 DCIM、ACIM、hybrid CIM。  
   https://arxiv.org/html/2411.06079v2

2. Sparsh Mittal 等，*A survey of SRAM-based in-memory computing techniques and applications*，Journal of Systems Architecture, 2021。覆盖 SRAM-IMC 的逻辑、搜索、算术和 ML 应用。  
   https://www.sciencedirect.com/science/article/abs/pii/S1383762121001909

3. *A full spectrum of computing-in-memory technologies*，Nature Electronics review。适合建立 CIM 分类框架，不只局限于 SRAM。  
   https://discovery.ucl.ac.uk/10185844/1/Manuscript_Nature_Electronics.pdf

4. *Trends in Analog and Digital Intensive Compute-in-SRAM Designs*，AICAS 2021。短而集中，适合理解 analog vs digitally intensive compute-in-SRAM。  
   https://sites.utexas.edu/CRL/wp-content/uploads/sites/4417/2021/07/AICAS_2021_Trends_in-CISRAM.pdf

## 11. 下一步可以拆成的 Obsidian 子笔记

- `SRAM-CIM：6T 8T 10T bitcell 对比`
- `SRAM-CIM：current-domain MAC`
- `SRAM-CIM：charge-domain MAC 与 switched-capacitor 类比`
- `SRAM-CIM：column ADC 和 SA 设计`
- `SRAM-CIM：bit slicing 与 signed MAC`
- `CIM 论文阅读模板`
- `CIM 指标：TOPS/W TOPS/mm2 ENOB CSNR`

如果只抓一条主线：**SRAM-CIM = SRAM array + 多行并行 + bitline/SA/ADC 计算 + 数字后处理 + 算法容错**。你从模拟信号链 IC 转过来，最值得发挥的地方是 ACIM 的信号预算、ADC/SA、噪声失配建模和校准。
