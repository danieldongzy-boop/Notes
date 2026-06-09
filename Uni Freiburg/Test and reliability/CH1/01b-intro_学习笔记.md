---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 8860b6eee8db2334bfd5e1c30eb390f0_7c2a18f25ffd11f191b55254006c9bbf
    ReservedCode1: RpTKqSAmdDQLeeiKk+dT4mUhJCZk28AEUCR+ituGzAeGNrtO375BSRbLr8enRo7mykMfPre0sVCbH97O6nE5NbcMl4TPEnLHw2U/j8iDuOv/S3P+alqUPf+xAwbuDNdwsQlK8K8G+TeLZm5YC9RhejVDYndVjpd1xrWcVrv49INyC8wozCiJcf3t9Po=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 8860b6eee8db2334bfd5e1c30eb390f0_7c2a18f25ffd11f191b55254006c9bbf
    ReservedCode2: RpTKqSAmdDQLeeiKk+dT4mUhJCZk28AEUCR+ituGzAeGNrtO375BSRbLr8enRo7mykMfPre0sVCbH97O6nE5NbcMl4TPEnLHw2U/j8iDuOv/S3P+alqUPf+xAwbuDNdwsQlK8K8G+TeLZm5YC9RhejVDYndVjpd1xrWcVrv49INyC8wozCiJcf3t9Po=
---


# Chapter 1: Introduction to Circuit Testing — 学习笔记（中英对照）

> **Course**: Test and Reliability  
> **Instructor**: Prof. Dr. Ralf Wimmer, Dr. Tobias Seufert  
> **Semester**: Summer Term 2026  
> **University**: Universität Freiburg, Department of Computer Science  
> **Original Document**: `01b-intro_annot.pdf` (91 pages)

---

## 目录 / Table of Contents

1. [What is Testing? / 什么是测试？](#1-what-is-testing--什么是测试)
2. [Fault Coverage and Yield / 故障覆盖率与良率](#2-fault-coverage-and-yield--故障覆盖率与良率)
3. [Types of Tests / 测试类型](#3-types-of-tests--测试类型)
4. [Test Application Methods / 测试应用方法](#4-test-application-methods--测试应用方法)
5. [Fault Models / 故障模型](#5-fault-models--故障模型)
6. [Test Generation / 测试生成](#6-test-generation--测试生成)
7. [Fault Detection and Redundancy / 故障检测与冗余](#7-fault-detection-and-redundancy--故障检测与冗余)
8. [Fault Collapsing / 故障压缩](#8-fault-collapsing--故障压缩)

---

## 1. What is Testing? / 什么是测试？

### 1.1 基本概念 / Basic Concepts

| English (英文) | 中文 (Chinese) |
|---|---|
| Manufacturing processes of VLSI chips may introduce different kinds of defects (shorts, opens, etc.). | 超大规模集成电路（VLSI）芯片的制造过程可能引入各种缺陷（短路、断路等）。 |
| No 100% yield possible. | 不可能达到 100% 的良率。 |
| Failures may also occur during the lifetime of a circuit. | 故障也可能在电路的使用寿命期间发生。 |
| As a result, a circuit may be different from its design. | 因此，实际电路可能与其设计不同。 |
| **The goal of testing** is to identify the existence of such a difference. | **测试的目标**是识别这种差异的存在。 |
| **Formal verification** in contrast: prove that circuit has been designed correctly. Related to, but different from testing. | **形式化验证**则相反：证明电路设计正确。与测试相关但不同。 |

### 1.2 缺陷的影响 / Effects of Defects

| English Term (英文术语) | 中文翻译 | 说明 |
|---|---|---|
| **Catastrophic defects** | 灾难性缺陷 | 一旦尝试使用电路就会被检测到 |
| **Subtle defects** | 细微缺陷 | 需要非常特定的测试才能检测到 |
| **Latent defects** | 潜在缺陷 | 不会立即导致故障，但会随时间恶化 |
| **Transient faults** | 瞬态故障 | 出现后消失，不可重复；例如由辐射引起 |
| **Intermittent faults** | 间歇性故障 | 由某种未知激活条件触发 |

### 1.3 为什么要测试？ / Why Test?

- **测试成本高昂**：高达总制造成本的 **60%**
  - Test is expensive: up to **60%** of overall manufacturing cost
- 确切成本取决于质量要求；无法提供 100% 保证
  - Exact cost depends on quality requirements; no 100% guarantee
- 销售有缺陷的零件代价也很高：一个有缺陷的 IC 会使整块电路板/产品失效
  - Selling a defective part is expensive: a defective IC invalidates whole board/product

> **「十倍法则」/ "Rule of Ten"**：修复成本从组件 → 电路板 → 系统 → 现场，大致每次增加 10 倍。
> The cost of fixing increases roughly by 10 from component → board → system → field.

- 是否测试以及测试到什么程度，取决于哪种成本更高
- **安全关键系统**（影响人类生命）和**不可更换硬件**（如卫星）尤其需要严格测试
  - Safety-critical systems (affect human life) and non-replaceable hardware (e.g., satellites)

---

## 2. Fault Coverage and Yield / 故障覆盖率与良率

### 2.1 关键指标 / Key Metrics

| 术语 (Term) | 英文定义 | 中文定义 |
|---|---|---|
| **Process Yield** ( $Y$ ) | The fraction of manufactured parts that are defect-free | 制造零件中无缺陷的比例 |
| **Defect Level** (DL) | The fraction of bad parts that pass all the tests | 通过所有测试的不良零件比例 |
| **Fault Coverage** (FC) | Measure of the quality of a test | 测试质量的度量 |
| **DPM** / **PPM** | Defects Per Million / defective Parts Per Million | 每百万缺陷数 / 每百万不良零件数 |

### 2.2 缺陷 vs 故障 / Defects vs Faults

> **Defects** are actual physical effects that happen in a manufactured circuit.  
> **缺陷**是制造电路中发生的实际物理效应。

> **Faults** are used to model defects.  
> **故障**用于对缺陷进行建模。

- 并非每个缺陷都能用故障建模；并非每个故障都对应一个可能的缺陷
- Not every defect may be modeled by a fault; not every fault may correspond to a likely defect
- 故障是有效工具，因为不可能枚举所有可能的缺陷并确定其对电路的影响
- Faults are an effective tool since it is impossible to enumerate all possible defects

### 2.3 公式 / Formula

设：
- $M$ = 建模故障数量 / number of modeled faults
- $N$ = 测试检测到的建模故障数量 / number of modeled faults detected by a test

**故障覆盖率 / Fault Coverage**：

$$FC = \frac{N}{M}$$

假设所有故障等概率且独立：

**缺陷水平 / Defect Level**：

$$DL = 1 - Y^{(1-FC)}$$

- 如果 $Y = 100\%$，则 $DL = 0$，无需测试
- 存在改进的公式

### 2.4 良率随时间变化 / Yield in Time

- 首批硅片：良率约 **20–30%**
- 量产：良率约 **80–95%**
- 良率随时间提升，缺陷密度降低
- 良率永不为 100%；当良率接近 100% 时，设备可能用于下一代技术（良率再次降低）

---

## 3. Types of Tests / 测试类型

### 3.1 测试的基本原理 / Basic Principle

所有类型的测试都指定输入值并测量输出值：
- All types of tests specify input values and measure output values.

### 3.2 逻辑测试 / Logical Tests

| English | 中文 |
|---|---|
| Apply logical values on circuit inputs. Consider logical values on circuit outputs (0, 1 values). | 在电路输入端施加逻辑值。观察电路输出端的逻辑值（0、1 值）。 |
| Voltage levels: Logic-0 ≈ 0V, Logic-1 ≈ $V_{DD}$ | 电压电平：Logic-0 ≈ 0V，Logic-1 ≈ $V_{DD}$ |
| For defects that cause a change in the logical behavior of the circuit. | 适用于导致电路逻辑行为变化的缺陷。 |

**故障注入电路模型 / Fault-injected circuit module**：将制造电路建模为在无故障设计中注入故障，使用同一 HDL 语言表示。

### 3.3 电气测试 / Electrical Tests

| English | 中文 |
|---|---|
| Measure the values of electrical parameters such as voltage levels, current levels, or delays. | 测量电气参数的值，如电压电平、电流电平或延迟。 |
| **$I_{DDQ}$ testing**: applied to CMOS circuits, measures the quiescent power supply current drawn when the chip is not switching ("leak current"). | **$I_{DDQ}$ 测试**：应用于 CMOS 电路，测量芯片不切换时的静态电源电流（"漏电流"）。 |
| In a fault-free chip this current is very small. In the presence of a defect such as a short, the current may be significantly higher. | 在无故障芯片中此电流非常小。存在短路等缺陷时，电流可能显著增大。 |

其他测试类型：光学检测（optical inspection）、热力图（thermal maps）等。

### 3.4 测试用途 / Test Use

| 用途 | English | 中文 |
|---|---|---|
| **检测 / Detection** | Distinguish between good and bad circuits. Needed to avoid shipping or using bad circuits. | 区分好电路和坏电路。用于避免出货或使用坏电路。 |
| **诊断 / Diagnosis** | Identify the location of the defect. Needed to improve manufacturing process or for repair. | 识别缺陷位置。用于改进制造工艺或进行修复。 |

---

## 4. Test Application Methods / 测试应用方法

### 4.1 外部测试 — 自动测试设备 / External Test — ATE

| English | 中文 |
|---|---|
| Input and output values are stored in an external tester, so-called **Automatic Test Equipment (ATE)**. | 输入和输出值存储在外部测试器中，即**自动测试设备（ATE）**。 |
| The external tester applies input values and compares output values to stored values. | 外部测试器施加输入值并将输出值与存储值比较。 |
| ATE are expensive. Cost increases with memory required and maximum supported clock frequency. | ATE 昂贵，成本随所需存储量和最大支持时钟频率增加。 |

**结构图 / Architecture**：

```
ATE ──→ CUT (Circuit under Test) ──→ Outputs = Expected Outputs?
         ↑ 预计算的存储测试模式
```

### 4.2 内建自测试 / Built-In Self-Test (BIST)

| English | 中文 |
|---|---|
| Input values are generated by special hardware on-chip, e.g., a **linear feedback shift register** (pseudo-random number generator). | 输入值由片上专用硬件生成，如**线性反馈移位寄存器**（伪随机数发生器）。 |
| Output values are compressed on-chip into a **signature**. | 输出值在片上压缩为一个**签名**。 |
| The external tester sends a signal to start testing, receives the signature at the end, and compares to a fault-free signature. | 外部测试器发送信号启动测试，结束时接收签名，并与无故障签名比较。 |

**BIST 架构 / BIST Architecture**：

```
ATE ──→ CUT [TPG → Circuit → ORA] ──→ Result
              ↑ Initiate test
```

- **TPG** = Test Pattern Generator（测试模式生成器）
- **ORA** = Output Response Analyzer（输出响应分析器）

### 4.3 测试数据压缩 / Test Data Compression

| English | 中文 |
|---|---|
| Input values are stored in an external tester in a compressed form. | 输入值以压缩形式存储在外部测试器中。 |
| Reduces memory requirements of ATE, test time, energy, and circuit stress. | 减少 ATE 的内存需求、测试时间、能耗和电路应力。 |
| The circuit contains a decompression circuit that applies required tests. | 电路包含解压缩电路来施加所需测试。 |
| Output compression can be done similar to BIST. | 输出压缩可与 BIST 类似。 |

**压缩架构 / Compression Architecture**：

```
ATE (compressed data) → CUT [decompress → Circuit → compress] → Result
```

**BIST vs Compression vs External Test 对比图**：

```
BIST:             最少外部数据 ──── 最多片上硬件
Compression:      中等外部数据 ──── 中等片上硬件
External Test:    最多外部数据 ──── 最少片上硬件
```

### 4.4 可测试性设计 / Design-for-Testability (DFT)

| English | 中文 |
|---|---|
| Methods of designing or augmenting a circuit to reduce the cost of testing it. | 设计或增强电路以降低测试成本的方法。 |
| The cost of testing is estimated at up to **60%** of manufacturing cost of a VLSI chip. | 测试成本估计高达 VLSI 芯片制造成本的 **60%**。 |
| Cost determined by: cost of test generation, tester cost (test set size and test application time). | 成本由以下决定：测试生成成本、测试器成本（测试集大小和测试应用时间）。 |

### 4.5 电路类型 / Circuit Types

| 类型 | English | 中文 |
|---|---|---|
| 数字-组合 | Digital — combinational | 数字 — 组合电路 |
| 数字-同步时序（无扫描） | Digital — synchronous Sequential (without Scan) | 数字 — 同步时序（无扫描） |
| 数字-同步时序（带扫描） | Digital — synchronous Sequential with Scan | 数字 — 同步时序（带扫描） |
| 数字-异步 | Digital — asynchronous | 数字 — 异步 |
| 模拟 | Analog | 模拟 |
| 混合信号 | Mixed Signal | 混合信号 |
| 存储器/MEMS/传感器 | Memories; MEMS; Sensors | 存储器；MEMS；传感器 |

> **课程重点**：同步数字电路 / Focus on synchronous digital circuits

### 4.6 扫描链 / Scan Chains

```
正常模式 (Normal Mode):
  组合逻辑 (Combinational logic) ←→ FF FF FF FF FF FF

扫描模式 (Scan Mode):
  scan-in → FF → FF → FF → FF → FF → FF → scan-out
```

**扫描链的工作原理 / How Scan Chains Work**：

| 模式 | English | 中文 |
|---|---|---|
| **扫描模式激活** | The scan chain can be used to assign values to the state variables for every vector applied to the circuit. | 扫描链可用于为施加到电路的每个向量分配状态变量值。 |
| **正常模式激活** | Find a test for the combinational logic. Bring the circuit from its initial state to the target state using a transfer/synchronizing sequence. | 为组合逻辑找到测试。使用转移/同步序列将电路从初始状态带到目标状态。 |

> 同步序列的长度可能在存储容量上呈指数增长！  
> The length of synchronizing sequence might be exponential in size of memory!

**观察故障效应 / Observing the Fault Effect**：

- 如果故障传播到主输出，前述过程即足够
- 否则：在非扫描情况下，需添加将故障效应传播到主输出的序列
- 在扫描情况下，使用 scan-out 线读取触发器值

### 4.7 测试相关人员 / Who Needs to Know About Test?

| 角色 | English | 职责 |
|---|---|---|
| 项目经理 | Project Manager | 性能、质量（DPM）、良率、面积、功耗、成本、开发时间权衡 |
| 可测试性经理 | Testability Manager | 选择可制造性设计规则、DFT、工具、测试器硬件 |
| 高级设计师 | Designer (senior) | 根据目标决定 DFT 策略 |
| DFT 工程师 | DFT engineer | 设计 DFT 硬件 |
| 测试工程师（仿真） | Test engineer (simulation) | 运行故障仿真和 ATPG，为 DFT 生成数据 |
| 测试工程师（ATE） | Test engineer (ATE) | 编程测试器，准备探针卡，微调时序 |

---

## 5. Fault Models / 故障模型

### 5.1 功能方法 vs 结构方法 / Functional vs Structural Approach

| 方法 | English | 中文 |
|---|---|---|
| **功能方法** | Check whether functionality meets specification | 检查功能是否满足规格说明 |
| — | combinational circuit: essentially truth table | 组合电路：本质上是真值表 |
| — | sequential circuit: Mealy automaton | 时序电路：Mealy 自动机 |
| — | Infeasible for non-trivial ICs | 对非平凡 IC 不可行 |
| — | In practice: check "relevant" parts using hand-written tests | 实践中：使用基于设计者经验的手写测试检查"相关"部分 |
| **结构方法** | Prove absence of defects | 证明缺陷不存在 |
| — | Model defects as faults; generate tests that detect (a large fraction of) faults | 将缺陷建模为故障；生成检测（大部分）故障的测试 |
| — | Can be automated | 可自动化 |
| — | Quality of functional tests can be assessed using structural methods | 功能测试的质量可用结构方法评估 |

> **课程重点**：结构方法 / We focus on structural methods

### 5.2 故障模型概述 / Fault Models Overview

- 故障模型用于在更高抽象层次上表示缺陷
- 使测试生成问题变得可处理
- 基于经验观察：高层故障模型的测试能有效检测低层故障，也能有效检测实际缺陷
- Based on empirical observation: tests for fault models at a higher level are effective in detecting faults at a lower level, and effective in detecting defects

### 5.3 电路描述层次 / Circuit Description Levels

| 层次 | English | 描述 |
|---|---|---|
| **行为级** | Behavioral Level | 使用 HDL（VHDL、Verilog）描述数据流和控制流 |
| **功能级 (RTL)** | Functional Level | 使用寄存器、模块和互连结构表示电路 |
| **结构级** | Structural Level | 在逻辑门级别表示电路 |
| **开关级** | Switch-Level | 晶体管的描述 |
| **几何级** | Geometric Description | 布局级别描述 |

**示例 / Example**：半加器从行为级到结构级

```verilog
// 行为级 / Behavioral
c = a + b;

// 功能级 / Functional
wire a, b;
wire [1:0] c;
adder (c, a, b);

// 结构级 / Structural
module adder(c, a, b);
  input a, b; output [1:0] c;
  wire d,e,f,g;
  nand (d, a, b);
  nand (e, a, d);
  nand (f, d, b);
  nand (c[0], e, f);
  nand (c[1], d, d);
endmodule
```

### 5.4 行为级故障模型 / Behavioral Fault Models

- 变量 $R$ 始终为 1 或 0
- 函数调用始终返回 1 或 0
- 语句 `if(Y) then {B1} else {B2}` 可能出错：
  - 始终执行 $B_1$
  - 始终执行 $B_2$
  - 当 $Y$ 为 false 时执行 $B_1$，当 $Y$ 为 true 时执行 $B_2$

### 5.5 功能级故障模型 / Functional Fault Models

确保功能块实现其设计功能。例如**多路复用器（MUX）**：

- 当选择输入 $i$ 时，实际选择了另一个输入 $j$（代替 $i$ 或除 $i$ 之外）
- When an input $i$ is selected, another input $j$ is selected instead of or in addition to $i$

**基于真值表的模型 / Truth Table Based Models**：

- 功能块的真值表可能以任意方式变化，需要**穷举测试**
- $n$ 个输入需要 $2^n$ 个测试
- 如果输出 $i$ 仅依赖于 $n_i$ 个输入，可用 $2^{n_i}$ 个测试（**伪穷举测试 / pseudo-exhaustive testing**）

### 5.6 结构级故障模型 / Structural Fault Models

#### 5.6.1 固定型故障 / Stuck-At Fault Model

| 故障 | English | 说明 |
|---|---|---|
| **固定为 0** (s.a.0) | Stuck-at 0 | 线路固定在低电压电平 |
| **固定为 1** (s.a.1) | Stuck-at 1 | 线路固定在高电压电平 |

- 表示对电源线或地的短路，以及其他短路和断路
- **最常用的故障模型！** / This is the most commonly used fault model!

#### 5.6.2 扇出主干与分支 / Fanout Stems and Branches

在扇出点，故障可以发生在：
- **主干 (stem)** 上
- 各个**分支 (branch)** 上

每个位置都有 s.a.0 和 s.a.1 两种可能。

#### 5.6.3 单固定型故障 vs 多固定型故障 / Single vs Multiple Stuck-At Faults

| 类型 | English | 数量 |
|---|---|---|
| **单固定型故障** | Single stuck-at fault | 对 $L$ 条线的电路，有 $2L$ 个 |
| **多固定型故障** | Multiple stuck-at fault | $3^L - 1$ 个（每条线三种状态：无故障/s.a.0/s.a.1，减去全无故障的情况） |

**为什么考虑单故障？/ Why Consider Single Faults?**

- 对于周期性测试（足够频繁），可假设在一个故障发生后、下一个出现前完成测试
- 单固定型故障测试在检测多固定型故障和各种缺陷方面证明有效
- 比多故障更易处理
- 但对于实际缺陷机制不够精确：缺陷聚类、诊断时的问题

#### 5.6.4 n-检测模型 / n-Detection Model

- 通过 $n$ 个不同测试检测每个固定型故障 $n > 1$ 次
- 增强测试集检测缺陷的能力
- $n$ 可以独立于故障，也可以依赖具体故障（可变 n-检测 / variable n-detection）

### 5.7 桥接故障 / Bridging Faults

| English | 中文 |
|---|---|
| A bridging fault is an unwanted connection between two lines in the circuit. | 桥接故障是电路中两条线之间不期望的连接。 |
| Assuming zero resistance simplifies modeling. | 假设连接电阻为零可简化建模。 |
| A bridging fault can be modeled by a **wired-AND** or a **wired-OR** between shorted lines. | 桥接故障可建模为短路线路之间的**线与（wired-AND）**或**线或（wired-OR）**。 |

**线与 / Wired-AND**：0 是更强的值（AND corresponds to 0 being the stronger value）

**线或 / Wired-OR**：1 是更强的值（OR corresponds to 1 being the stronger value）

**四路模型 / 4-way Model**：每对线 $(g_1, g_2)$ 有四种故障，取决于哪条线更强、对什么值更强。

**桥接故障数量 / Number of Bridging Faults**：
- 对 $L$ 条线的电路：$L \cdot (L-1)$ 个
- 可通过布局信息限制为每条线的 $k$ 条最可能桥接线：总计 $k \cdot L$ 个故障

### 5.8 延迟故障 / Delay Faults

延迟故障模拟影响电路时序行为的缺陷，通常使电路比其指定运行速度更慢。

| 故障模型 | English | 说明 |
|---|---|---|
| **跳变故障** | Transition faults (gross delay faults) | 通过一条或多条线的传播延迟高于电路时钟周期 |
| **慢上升** | Slow-to-rise | 减慢线上的上升跳变 |
| **慢下降** | Slow-to-fall | 减慢线上的下降跳变 |
| **门延迟故障** | Gate delay faults | 一个或多个门的输入到输出传播延迟大于设计值 |
| **路径延迟故障** | Path delay faults | 一条或多条从输入到输出的路径传播上升/下降跳变缓慢 |

**跳变故障测试 / Testing for a Transition Fault $g: a \to \neg a$**：

1. 第一个测试模式需设置 $g = a$（比检测 $g$ s.a.$\neg a$ 更弱的要求）
2. 第二个测试模式需设置 $g = \neg a$，故障效应为 $g = \neg a / a$
3. 检测故障需传播 $g = \neg a / a$ 到输出，这需要 $g$ s.a.$a$ 的测试

> 所有延迟故障都需要**双模式测试**（two-pattern tests）。

### 5.9 开关级故障模型 / Switch-Level Fault Models

应用于 CMOS 电路中的晶体管

| 故障 | English | 说明 |
|---|---|---|
| **卡开故障** | Stuck-open fault | 晶体管永久不导通 |
| **卡开故障** | Stuck-on fault | 晶体管永久导通 |

**卡开故障检测示例 / Detecting a Stuck-Open Fault**：

- 对于 CMOS 电路，故障电路中的节点 $z$ 可能**保持其前一值**
- 检测需要确保前一值为正确值
- 示例测试：$\langle 00, 10 \rangle \Rightarrow z = \langle 1, 0/1 \rangle$

### 5.10 故障模型总结 / Summary of Fault Models

- 故障模型用于模拟物理缺陷的影响
- 为测试生成提供目标
- 不同故障模型产生不同的测试集，检测不同类型的缺陷
- 模型选择取决于测试生成可投入的时间和可使用的测试数量

---

## 6. Test Generation / 测试生成

### 6.1 测试生成流程 / Test Generation Process

| 步骤 | English |
|---|---|
| 1. 在行为级生成测试 | Generate tests at the behavioral level |
| 2. 在功能级仿真测试 | Simulate the tests at the functional level |
| 3. 为剩余故障生成额外测试 | Generate additional tests for the remaining faults |
| 4. 在结构级仿真 | Simulate at the structural level |
| 5. 为剩余故障生成额外测试 | Generate additional tests for the remaining faults |
| 6. 在开关级仿真 | Simulate at the switch level ... |

### 6.2 常用流程 / Commonly Used Process

1. 高层由设计者考虑，提供**功能测试序列**
2. 测试生成考虑**结构级**，可能加布局用于实际故障
3. 为（接近）**100% 的单固定型故障**生成测试
4. 补充测试集：
   - 延迟故障（跳变故障和/或路径延迟故障子集）
   - $I_{DDQ}$ 测试用于桥接故障

### 6.3 复杂度 / Complexity

- 单固定型故障的测试生成是 **NP-完全**问题
- 完整测试生成过程的复杂度（目前）与输入数量指数相关
- 实践中存在各种优化技术和启发式方法高效解决

### 6.4 电路模型 / Circuit Models

| 模型 | English | 说明 |
|---|---|---|
| 实际制造电路 | Actual manufactured circuits | 只能访问其输入和输出（可能无故障或有故障） |
| 无故障电路模型 | Fault-free circuit model | 已知内部细节的计算机表示，用于测试生成和故障仿真 |
| 故障注入电路模型 | Faulty circuit models | 注入建模故障的电路模型 |

---

## 7. Fault Detection and Redundancy / 故障检测与冗余

### 7.1 故障检测定义 / Fault Detection Definition

设组合电路 $N$ 的输出函数为 $Z(x)$，输入向量为 $t$，故障 $f$ 将 $N$ 变换为 $N_f$，输出函数为 $Z_f(x)$。

> **定义**：测试向量 $t$ 检测故障 $f$ **当且仅当** $Z_f(t) \neq Z(t)$。  
> **Definition**: A test vector $t$ detects a fault $f$ **iff** $Z_f(t) \neq Z(t)$.

测试 $t$ 满足：$Z(t) \oplus Z_f(t) = 1$

**多输出电路 / Multi-output circuit**：

$$Z(t) \oplus Z_f(t) = (z_1(t) \oplus z_{1f}(t)) + (z_2(t) \oplus z_{2f}(t)) + \cdots + (z_m(t) \oplus z_{mf}(t))$$

### 7.2 敏化 / Sensitization

| 术语 | English | 定义 |
|---|---|---|
| **激活故障** | Activate the fault | 为故障点分配不同的无故障值和故障值 |
| **传播故障** | Propagate the fault | 使故障点和输出之间至少一条路径上所有线具有不同的无故障值和故障值 |
| **敏化线** | Sensitized line | 在测试 $t$ 下，故障电路和无故障电路中值不同的线 |
| **敏化路径** | Sensitized path | 由敏化线组成的路径 |

### 7.3 敏化引理 / Sensitization Lemmas

#### 敏化引理 1 / Sensitization Lemma 1

设 $G$ 为门，反相为 $i$，控制值为 $c$。假设门 $G$ 的输出被测试 $t$ 敏化到故障 $f$：

1. $G$ 的所有敏化输入在无故障电路中具有相同的值 $a$
2. $G$ 的所有非敏化输入具有值 $\neg c$
3. $G$ 的输出在无故障电路中具有值 $a \oplus i$

**门属性表 / Gate Properties Table**：

| 门类型 | 反相 $i$ / Inversion | 控制值 $c$ / Controlling Value |
|---|---|---|
| AND | 0 | 0 |
| OR | 0 | 1 |
| Buffer | 0 | — |
| NAND | 1 | 0 |
| NOR | 1 | 1 |
| Inverter | 1 | — |

#### 敏化引理 2 / Sensitization Lemma 2

设线 $j$ 被测试 $t$ 敏化到故障 $l$ s.a.$v$，$p$ 为 $l$ 和 $j$ 之间一条敏化路径的反相奇偶性：

1. $j$ 在无故障电路中的值为 $\neg v \oplus p$
2. 如果 $l$ 和 $j$ 之间存在多条敏化路径，则所有路径具有相同的反相奇偶性

### 7.4 可检测性 / Detectability

| 术语 | English | 定义 |
|---|---|---|
| **可检测故障** | Detectable fault | 存在检测它的测试 $t$ |
| **不可检测故障** | Undetectable fault | $Z_f(x) = Z(x)$，不存在能检测它的测试 |

> 不可检测故障的存在可能使某可检测故障的测试失效。

### 7.5 冗余 / Redundancy

- 包含不可检测固定型故障的组合电路称为**冗余的**
- 冗余电路可通过移除至少一条线来简化
- A combinational circuit that contains an undetectable stuck-at fault is said to be **redundant**

**冗余故障的三个性质 / Three Properties of Redundant Faults**：

| 性质 | English | 说明 |
|---|---|---|
| 性质 1 | After removing a redundant fault $f$, a detectable fault $g$ may become redundant. | 移除冗余故障 $f$ 后，可检测故障 $g$ 可能变为冗余 |
| 性质 2 | After removing a redundant fault $f$, a redundant fault $g$ may become detectable. | 移除冗余故障 $f$ 后，冗余故障 $g$ 可能变为可检测 |
| 性质 3 | Two redundant faults $f$ and $g$ may be detectable if present simultaneously. | 两个冗余故障 $f$ 和 $g$ 同时存在时可能变为可检测 |

---

## 8. Fault Collapsing / 故障压缩

### 8.1 等价故障 / Equivalent Faults

> **定义**：两个故障 $f$ 和 $g$ **功能等价**当且仅当 $Z_f(x) = Z_g(x)$。  
> **Definition**: Two faults $f$ and $g$ are **functionally equivalent** iff $Z_f(x) = Z_g(x)$.

**对于 $n$ 输入 AND 门 / For an $n$-input AND gate**：

- 可定义 $2(n+1)$ 个单固定型故障
- 所有输入上的 s.a.0 故障和输出上的 s.a.0 故障是等价的
- **只需考虑输出 s.a.0 故障和所有 s.a.1 故障**，共 $n + 2$ 个

| 门类型 | 等价关系 / Equivalence |
|---|---|
| $n$-input AND | 所有输入 s.a.0 $\equiv$ 输出 s.a.0 |
| $n$-input NAND | 所有输入 s.a.0 $\equiv$ 输出 s.a.1 |
| $n$-input OR | 所有输入 s.a.1 $\equiv$ 输出 s.a.1 |
| $n$-input NOR | 所有输入 s.a.1 $\equiv$ 输出 s.a.0 |

- 对每个 $n$ 输入门，使用 $n + 2$ 个非等价故障
- 减少了需要考虑的单固定型故障数量

### 8.2 故障支配 / Fault Dominance

> **定义**：设 $T_g$ 为检测故障 $g$ 的所有测试集。故障 $f$ **支配**故障 $g$，如果每个检测 $g$ 的测试也检测 $f$，即 $T_g \subseteq T_f$。  
> **Definition**: A fault $f$ **dominates** a fault $g$ if every test that detects $g$ also detects $f$, i.e., $T_g \subseteq T_f$.

**AND 门示例**：输出 s.a.1 故障支配每个输入上的 s.a.1 故障（因为要检测输入 s.a.1 需将所有输入设为 1，此时也检测了输出 s.a.1）。

**实践中为何不用支配压缩？**

- 如果输入故障不可检测但输出故障可检测，移除输出故障后它可能保持未被检测

### 8.3 诊断支配 / Diagnostic Dominance

> 故障 $f$ **诊断支配**故障 $g$，如果对于每个测试 $t$ 和电路的每个输出 $z$，如果 $g$ 在 $z$ 上被检测到，则 $f$ 也在 $z$ 上被检测到。  
> A fault $f$ **diagnostically dominates** a fault $g$ if for every test $t$ and every output $z$, if $g$ is detected on $z$ then $f$ is also detected on $z$.

---

## 9. 关键公式汇总 / Key Formulas Summary

| 公式 | 含义 |
|---|---|
| $FC = \frac{N}{M}$ | 故障覆盖率 = 检测到的故障数 / 总建模故障数 |
| $DL = 1 - Y^{(1-FC)}$ | 缺陷水平（假设故障等概率独立） |
| $2L$ | 单固定型故障数量（$L$ 条线） |
| $3^L - 1$ | 多固定型故障数量（$L$ 条线） |
| $L \cdot (L-1)$ | 桥接故障数量 |
| $n + 2$ | $n$ 输入门的非等价故障数（等价故障压缩后） |
| $Z(t) \oplus Z_f(t) = 1$ | 测试 $t$ 检测故障 $f$ 的条件 |
| $\neg v \oplus p$ | 敏化引理 2：敏化线上的无故障值 |

---

## 10. 核心术语对照表 / Glossary of Key Terms

| English | 中文 | 缩写 |
|---|---|---|
| Automatic Test Equipment | 自动测试设备 | ATE |
| Built-In Self-Test | 内建自测试 | BIST |
| Circuit Under Test | 被测电路 | CUT |
| Design-for-Testability | 可测试性设计 | DFT |
| Defect Level | 缺陷水平 | DL |
| Defects Per Million | 每百万缺陷数 | DPM |
| Fault Coverage | 故障覆盖率 | FC |
| Linear Feedback Shift Register | 线性反馈移位寄存器 | LFSR |
| Output Response Analyzer | 输出响应分析器 | ORA |
| Process Yield | 工艺良率 | $Y$ |
| Stuck-at 0 / Stuck-at 1 | 固定为 0 / 固定为 1 | s.a.0 / s.a.1 |
| Test Pattern Generator | 测试模式生成器 | TPG |
| Very Large Scale Integration | 超大规模集成电路 | VLSI |
| Rule of Ten | 十倍法则 | — |
| Sensitized Path | 敏化路径 | — |
| Fault Collapsing | 故障压缩 | — |
| Bridging Fault | 桥接故障 | — |
| Transition Fault | 跳变故障 | — |
| Path Delay Fault | 路径延迟故障 | — |
| Stuck-open / Stuck-on | 卡开 / 卡闭 | — |

---

*笔记整理自 `01b-intro_annot.pdf`，共 91 页，覆盖 Chapter 1: Introduction to Circuit Testing 全部内容。*
*（内容由AI生成，仅供参考）*
