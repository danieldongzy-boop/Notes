# Test and Reliability CH1-CH8 完整学习笔记

> 范围：整理文件夹中的 CH1 至 CH8 课件内容。注意：`08-cellaware_annot.pdf` 封面写的是 Chapter 9；本笔记按文件夹顺序把它记作 CH8，并保留其正式主题 Cell-Aware Testing。
> 不包含：`ex*.pdf`、作业解析、exercise 解答。  
> 目标：用比较人话的方式，把概念、公式、算法和容易混淆的点串起来。

## 目录

- [[#0. 五章在讲什么|0. 五章在讲什么]]
- [[#CH1. Circuit Testing 基础与 Fault Collapsing|CH1. Circuit Testing 基础与 Fault Collapsing]]
  - [[#1.1 关键词中英文对照|1.1 关键词中英文对照]]
  - [[#1.2 Testing 到底在测什么|1.2 Testing 到底在测什么]]
  - [[#1.3 Yield、Defect Level 和 Fault Coverage|1.3 Yield、Defect Level 和 Fault Coverage]]
  - [[#1.4 测试方式：ATE、BIST、压缩和 DFT|1.4 测试方式：ATE、BIST、压缩和 DFT]]
  - [[#1.5 Fault Model：为什么需要故障模型|1.5 Fault Model：为什么需要故障模型]]
  - [[#1.6 Stuck-at Fault 固定型故障|1.6 Stuck-at Fault 固定型故障]]
  - [[#1.7 其他常见故障模型|1.7 其他常见故障模型]]
  - [[#1.8 什么叫检测到一个故障|1.8 什么叫检测到一个故障]]
  - [[#1.9 Sensitization 敏化|1.9 Sensitization 敏化]]
  - [[#1.10 Redundancy 冗余|1.10 Redundancy 冗余]]
  - [[#1.11 Fault Collapsing：为什么要压缩故障|1.11 Fault Collapsing：为什么要压缩故障]]
  - [[#1.12 Equivalent Fault Collapsing, EFC|1.12 Equivalent Fault Collapsing, EFC]]
  - [[#1.13 SIMPLE_EFC 的规则|1.13 SIMPLE_EFC 的规则]]
  - [[#1.14 Dominance Fault Collapsing, DFC|1.14 Dominance Fault Collapsing, DFC]]
  - [[#1.15 Checkpoint Theorem|1.15 Checkpoint Theorem]]
- [[#CH2. Fault Simulation 故障仿真|CH2. Fault Simulation 故障仿真]]
  - [[#2.1 关键词中英文对照|2.1 关键词中英文对照]]
  - [[#2.2 Fault Simulation 的输入和输出|2.2 Fault Simulation 的输入和输出]]
  - [[#2.3 最直接的方法为什么太慢|2.3 最直接的方法为什么太慢]]
  - [[#2.4 Event-Driven Simulation|2.4 Event-Driven Simulation]]
  - [[#2.5 Fault Dropping|2.5 Fault Dropping]]
  - [[#2.6 Parallel Fault Simulation|2.6 Parallel Fault Simulation]]
  - [[#2.7 Fault Insertion Mask|2.7 Fault Insertion Mask]]
  - [[#2.8 Parallel Fault Simulation 的优缺点|2.8 Parallel Fault Simulation 的优缺点]]
  - [[#2.9 Deductive Fault Simulation|2.9 Deductive Fault Simulation]]
  - [[#2.10 AND 门的 fault list 传播规则|2.10 AND 门的 fault list 传播规则]]
  - [[#2.11 Parallel 和 Deductive 的关系|2.11 Parallel 和 Deductive 的关系]]
  - [[#2.12 Sequential Circuits|2.12 Sequential Circuits]]
- [[#CH3. Combinational ATPG 组合电路测试生成|CH3. Combinational ATPG 组合电路测试生成]]
  - [[#3.1 关键词中英文对照|3.1 关键词中英文对照]]
  - [[#3.2 Test Generation Problem|3.2 Test Generation Problem]]
  - [[#3.3 Random Patterns 和 Fault Coverage Curve|3.3 Random Patterns 和 Fault Coverage Curve]]
  - [[#3.4 Deterministic ATPG 为什么难|3.4 Deterministic ATPG 为什么难]]
  - [[#3.5 3 值、5 值和 9 值逻辑|3.5 3 值、5 值和 9 值逻辑]]
  - [[#3.6 D-Algorithm 的核心思想|3.6 D-Algorithm 的核心思想]]
  - [[#3.7 D-Frontier 和 J-Frontier|3.7 D-Frontier 和 J-Frontier]]
  - [[#3.8 Implication|3.8 Implication]]
  - [[#3.9 Backtracking|3.9 Backtracking]]
  - [[#3.10 D-Algorithm 速记|3.10 D-Algorithm 速记]]
  - [[#3.11 加速技术|3.11 加速技术]]
  - [[#3.12 PODEM|3.12 PODEM]]
  - [[#3.13 Objective 和 Backtrace|3.13 Objective 和 Backtrace]]
  - [[#3.14 Controllability 和 Observability|3.14 Controllability 和 Observability]]
  - [[#3.15 ATPG 的整体流程|3.15 ATPG 的整体流程]]
  - [[#3.16 Unspecified Values 和 Test Compaction|3.16 Unspecified Values 和 Test Compaction]]
  - [[#3.17 Test Pattern Relaxation|3.17 Test Pattern Relaxation]]
  - [[#3.18 Test Power Consumption|3.18 Test Power Consumption]]
- [[#CH4. Boolean Satisfiability 与 SAT-based ATPG|CH4. Boolean Satisfiability 与 SAT-based ATPG]]
  - [[#4.1 关键词中英文对照|4.1 关键词中英文对照]]
  - [[#4.2 SAT 问题|4.2 SAT 问题]]
  - [[#4.3 Miter Circuit|4.3 Miter Circuit]]
  - [[#4.4 Tseitin Transformation|4.4 Tseitin Transformation]]
  - [[#4.5 Resolution 归结|4.5 Resolution 归结]]
  - [[#4.6 现代 SAT Solver 的主循环|4.6 现代 SAT Solver 的主循环]]
  - [[#4.7 Preprocessing|4.7 Preprocessing]]
  - [[#4.8 Decision Stack 和 Decision Level|4.8 Decision Stack 和 Decision Level]]
  - [[#4.9 VSIDS 决策启发式|4.9 VSIDS 决策启发式]]
  - [[#4.10 BCP 和 Watched Literals|4.10 BCP 和 Watched Literals]]
  - [[#4.11 Conflict Analysis、1UIP 和 Learned Clause|4.11 Conflict Analysis、1UIP 和 Learned Clause]]
  - [[#4.12 SAT for ATPG：怎么编码|4.12 SAT for ATPG：怎么编码]]
  - [[#4.13 Incremental Solving|4.13 Incremental Solving]]
  - [[#4.14 为什么需要 D-Chain|4.14 为什么需要 D-Chain]]
  - [[#4.15 Forward D-Chain|4.15 Forward D-Chain]]
  - [[#4.16 Backward D-Chain|4.16 Backward D-Chain]]
  - [[#4.17 Combined Backward/Forward D-Chains|4.17 Combined Backward/Forward D-Chains]]
  - [[#4.18 Good-Diff D-Chain|4.18 Good-Diff D-Chain]]
  - [[#4.19 Hybrid D-Chains|4.19 Hybrid D-Chains]]
- [[#CH5. Design-for-Testability 可测试性设计|CH5. Design-for-Testability 可测试性设计]]
  - [[#5.1 DFT 为什么存在|5.1 DFT 为什么存在]]
  - [[#5.2 DFT 与 SFT|5.2 DFT 与 SFT]]
  - [[#5.3 怎样衡量 Testability|5.3 怎样衡量 Testability]]
  - [[#5.4 Control Point 与 Observation Point|5.4 Control Point 与 Observation Point]]
  - [[#5.5 根据 Fault Simulation 选择测试点|5.5 根据 Fault Simulation 选择测试点]]
  - [[#5.6 多个故障与 Set Covering|5.6 多个故障与 Set Covering]]
  - [[#5.7 额外测试输入怎么接出去|5.7 额外测试输入怎么接出去]]
  - [[#5.8 额外测试输出怎么接出去|5.8 额外测试输出怎么接出去]]
  - [[#5.9 XOR Tree 与 Aliasing|5.9 XOR Tree 与 Aliasing]]
  - [[#5.10 Test Points 与 BIST|5.10 Test Points 与 BIST]]
  - [[#5.11 时序电路为什么更难测|5.11 时序电路为什么更难测]]
  - [[#5.12 Circuit Initialization|5.12 Circuit Initialization]]
  - [[#5.13 ILA 与同步序列生成|5.13 ILA 与同步序列生成]]
  - [[#5.14 Counter 的测试问题|5.14 Counter 的测试问题]]
  - [[#5.15 Sequential ATPG|5.15 Sequential ATPG]]
  - [[#5.16 Scan 的核心思想|5.16 Scan 的核心思想]]
  - [[#5.17 Scan Cell|5.17 Scan Cell]]
  - [[#5.18 Integrated Scan 与 Boundary Scan|5.18 Integrated Scan 与 Boundary Scan]]
  - [[#5.19 Full Scan 与 Partial Scan|5.19 Full Scan 与 Partial Scan]]
  - [[#5.20 CH5 考前压缩版|5.20 CH5 考前压缩版]]
- [[#CH6. BIST and Test Compression 芯片自己测自己|CH6. BIST and Test Compression 芯片自己测自己]]
  - [[#6.1 这一章到底在解决什么|6.1 这一章到底在解决什么]]
  - [[#6.2 On-line 和 Off-line BIST|6.2 On-line 和 Off-line BIST]]
  - [[#6.3 穷举、伪穷举与 test signal input|6.3 穷举、伪穷举与 test signal input]]
  - [[#6.4 Pseudo-random BIST 与 LFSR|6.4 Pseudo-random BIST 与 LFSR]]
  - [[#6.5 为什么随机测不全：WRP|6.5 为什么随机测不全：WRP]]
  - [[#6.6 混合模式 BIST：随机抓大头，确定性补尾巴|6.6 混合模式 BIST：随机抓大头，确定性补尾巴]]
  - [[#6.7 Output compaction：为什么只看一个 signature 也能判题|6.7 Output compaction：为什么只看一个 signature 也能判题]]
  - [[#6.8 Test compression：压缩的两端都要考虑|6.8 Test compression：压缩的两端都要考虑]]
  - [[#6.9 CH6 考前压缩卡|6.9 CH6 考前压缩卡]]
- [[#CH7. Software-Based Self-Test 用软件测硬件|CH7. Software-Based Self-Test 用软件测硬件]]
  - [[#7.0 按课件页码重新梳理|7.0 按课件页码重新梳理]]
  - [[#7.1 核心想法|7.1 核心想法]]
  - [[#7.2 Random-based SBIST：软件版 LBIST|7.2 Random-based SBIST：软件版 LBIST]]
  - [[#7.3 Pattern-based SBIST：软件版 MBIST|7.3 Pattern-based SBIST：软件版 MBIST]]
  - [[#7.4 为什么需要 constrained ATPG|7.4 为什么需要 constrained ATPG]]
  - [[#7.5 Test pattern retargeting：从总线事务到指令|7.5 Test pattern retargeting：从总线事务到指令]]
  - [[#7.6 Generic VCM、Startup SBST 与 Online SBST|7.6 Generic VCM、Startup SBST 与 Online SBST]]
  - [[#7.7 CH7 考前压缩卡|7.7 CH7 考前压缩卡]]
- [[#CH8. Cell-Aware Testing 让 fault model 更接近真实缺陷|CH8. Cell-Aware Testing 让 fault model 更接近真实缺陷]]
  - [[#8.0 按课件页码重新梳理|8.0 按课件页码重新梳理]]
  - [[#8.1 为什么 stuck-at / transition-delay 不够了|8.1 为什么 stuck-at / transition-delay 不够了]]
  - [[#8.2 Cell-aware 的一句话定义|8.2 Cell-aware 的一句话定义]]
  - [[#8.3 fault model 在这里长什么样|8.3 fault model 在这里长什么样]]
  - [[#8.4 怎么从物理缺陷生成模型|8.4 怎么从物理缺陷生成模型]]
  - [[#8.5 CAT 的优势与成本|8.5 CAT 的优势与成本]]
  - [[#8.6 Cell-aware SBST：把真实 cell 缺陷变成可运行软件测试|8.6 Cell-aware SBST：把真实 cell 缺陷变成可运行软件测试]]
  - [[#8.7 CH8 考前压缩卡|8.7 CH8 考前压缩卡]]
- [[#9. CH1-CH5 的核心关系回顾|9. CH1-CH5 的核心关系回顾]]
  - [[#9.1 从“测得出”到“怎么找”再到“让它好测”|9.1 从“测得出”到“怎么找”再到“让它好测”]]
  - [[#9.2 三个永远绕不开的动作|9.2 三个永远绕不开的动作]]
  - [[#9.3 公式和算法速记|9.3 公式和算法速记]]
  - [[#9.4 高频易错点|9.4 高频易错点]]
  - [[#9.5 考前压缩版|9.5 考前压缩版]]

## 0. 八章在讲什么

前五章是一条基础主线：定义故障、评估测试、生成测试，再通过 DFT 改造电路。后面三章把测试带到真实芯片系统中：让芯片自测、让软件自测、让故障模型更接近真实制造缺陷。

| Chapter | 英文主题                                              | 中文主题                   | 一句话                                     |
| ------- | ------------------------------------------------- | ---------------------- | --------------------------------------- |
| CH1     | Introduction to Circuit Testing, Fault Collapsing | 电路测试基础与故障压缩            | 为什么要测、测什么、怎么定义故障和覆盖率                    |
| CH2     | Fault Simulation                                  | 故障仿真                   | 给一组测试向量，算它们能测出哪些故障                      |
| CH3     | Test Generation for Single Stuck-At Faults        | 单固定故障的测试生成             | 自动找测试向量，让故障被激活、传播、观察                    |
| CH4     | Boolean Satisfiability                            | 布尔可满足性与 SAT-based ATPG | 把测试生成翻译成 SAT，让 SAT solver 搜索测试          |
| CH5     | Design-for-Testability                            | 可测试性设计                 | 如果原电路太难测，就加入测试点或 scan 结构改善可控制性和可观察性     |
| CH6     | BIST and Test Compression                         | 内建自测试与测试压缩             | 把出题、判题和压缩放到芯片里，以更少 ATE 数据实现 at-speed 测试 |
| CH7     | Software-Based Self-Test                          | 软件自测试                  | 用已有处理器和合法软件事务测试 IP / 处理器自身              |
| CH8*    | Cell-Aware Testing                                | 单元感知测试                 | 从 cell 内物理缺陷建立更真实的 ATPG 故障模型            |

整体关系可以这样记：

```text
CH1: 定义目标
  什么是 fault? 什么叫 detected? 什么叫 coverage?

CH2: 评估测试
  已有测试集 T，故障列表 F，算 T 检测了 F 里的哪些故障。

CH3: 生成测试
  针对某个 stuck-at fault，找一个输入向量让它被检测。

CH4: 用 SAT 生成测试
  把“好电路和坏电路输出不同”编码成 CNF，交给 SAT solver。

CH5: 改造电路使它好测
  加入 control point、observation point 或 scan，降低 ATPG 难度并提高覆盖率。

CH6: 芯片自己做测试
  LFSR 出伪随机模式，MISR 把响应压成 signature；必要时用确定性模式补 hard faults。

CH7: 软件也能做测试
  CPU 通过真实总线操作 CUT；VCM 确保 ATPG 生成的是合法、可执行的软件行为。

CH8: 模型要更像真实缺陷
  从 cell 的 SPICE 缺陷仿真出发，生成 cell-aware fault model，再交给 ATPG。
```

---

## CH1. Circuit Testing 基础与 Fault Collapsing

[[#目录|返回目录]]

### 1.1 关键词中英文对照

| English | 中文 | 人话解释 |
|---|---|---|
| Testing | 测试 | 看制造出来的电路和设计是否有可观察差异 |
| Formal Verification | 形式化验证 | 证明设计本身是否正确，不是检查制造缺陷 |
| Defect | 缺陷 | 真实物理问题，如短路、断路、颗粒污染 |
| Fault | 故障 | 用来建模 defect 的抽象逻辑错误 |
| Failure | 失效 | 电路在使用中表现出错误行为 |
| Process Yield | 工艺良率 | 制造出来的零件中本来就是好的比例 |
| Defect Level, DL | 缺陷水平 | 坏零件通过测试后被放行的比例 |
| Fault Coverage, FC | 故障覆盖率 | 测试集检测到的目标故障比例 |
| Automatic Test Equipment, ATE | 自动测试设备 | 外部测试机，负责输入测试向量并比对输出 |
| Built-In Self-Test, BIST | 内建自测试 | 芯片内部自己产生测试、压缩响应 |
| Design-for-Testability, DFT | 可测试性设计 | 在设计时加入结构，降低测试成本 |
| Scan Chain | 扫描链 | 把触发器串起来，使时序电路更像组合电路来测 |
| Fault Model | 故障模型 | 用可处理的抽象形式描述物理缺陷 |
| Stuck-at Fault | 固定型故障 | 某条线永久固定为 0 或 1 |
| Bridging Fault | 桥接故障 | 两条不该连的线短接在一起 |
| Delay Fault | 延迟故障 | 信号传播太慢，导致时序错误 |
| Transition Fault | 跳变故障 | 某条线的上升或下降跳变太慢 |
| Path Delay Fault | 路径延迟故障 | 某条输入到输出路径整体太慢 |
| Sensitization | 敏化 | 让故障影响沿路径传到输出 |
| Redundancy | 冗余 | 存在不可检测 stuck-at fault 的组合电路 |
| Equivalent Faults | 等价故障 | 任意测试都无法区分的故障 |
| Fault Dominance | 故障支配 | 测到一个更难的故障时，必然也测到另一个故障 |
| Fault Collapsing | 故障压缩 | 用代表故障替代一大堆等价或被支配的故障 |
| Checkpoint Theorem | 检查点定理 | 测 PI 和 fanout branch 上的故障即可覆盖所有 stuck-at 故障 |

### 1.2 Testing 到底在测什么

制造 VLSI 芯片时会出现物理缺陷，例如短路、断路、颗粒污染、腐蚀、过蚀等。测试不是要证明设计逻辑正确，而是要判断：

```text
真实制造出来的电路，是否和理想设计有可观察差异？
```

形式化验证关心的是“设计有没有写对”。测试关心的是“做出来的这颗芯片有没有坏”。

有些 defect 很明显，芯片一用就坏；有些很隐蔽，只在特定输入下才表现出来；还有一些 latent defect 一开始不出错，但会随时间恶化。测试不能给 100% 保证，但可以把出货坏件概率降到可接受水平。

### 1.3 Yield、Defect Level 和 Fault Coverage

核心量：

- $Y$：process yield，制造出来本来无缺陷的比例。
- $M$：建模出来的故障总数。
- $N$：被测试集检测到的故障数。
- $FC$：fault coverage。
- $DL$：defect level，坏零件逃过测试的比例。

故障覆盖率：

$$
FC = \frac{N}{M}
$$

在“故障等概率且独立”的简化假设下：

$$
DL = 1 - Y^{(1-FC)}
$$

人话理解：

- 良率 $Y$ 越高，本来坏的芯片越少。
- 覆盖率 $FC$ 越高，坏芯片越不容易逃过测试。
- 测试不是为了追求数学上的完美，而是在测试成本和出货风险之间折中。

### 1.4 测试方式：ATE、BIST、压缩和 DFT

所有测试本质上都做两件事：

```text
给输入 -> 看输出
```

区别在于输入从哪里来、输出在哪里比对。

| 方法 | 英文 | 核心思想 | 优点 | 代价 |
|---|---|---|---|---|
| 外部测试 | ATE | 测试机存储输入和期望输出 | 灵活、可控 | 测试机贵，存储和时间成本高 |
| 内建自测试 | BIST | 芯片内部生成测试并压缩输出 | 外部数据少 | 需要片上硬件 |
| 测试数据压缩 | Test Data Compression | ATE 存压缩数据，芯片内解压/压缩 | 降低 ATE 存储和测试时间 | 需要压缩/解压逻辑 |
| 可测试性设计 | DFT | 设计时加结构方便测试 | 降低测试难度 | 增加面积和设计复杂度 |

Scan chain 是 DFT 中很重要的一种。它把触发器串起来，让测试工具可以直接设置和观察内部状态。没有 scan 时，时序电路的状态要靠输入序列慢慢“带到”目标状态；有 scan 后，可以更直接地把时序问题转成组合逻辑测试问题。

### 1.5 Fault Model：为什么需要故障模型

真实 defect 太多太复杂，没法全部枚举。所以课程用 fault model 把物理问题抽象成可以自动处理的逻辑问题。

几个层次：

| Level | 中文 | 例子 |
|---|---|---|
| Behavioral level | 行为级 | HDL 中变量永远为 0/1，if 分支错误 |
| Functional level | 功能级 | MUX 选错输入 |
| Structural level | 结构级 | 逻辑门和连线上的 stuck-at fault |
| Switch level | 开关级 | CMOS 晶体管 stuck-open/stuck-on |
| Geometric level | 几何/版图级 | 布局导致的桥接、短路 |

课程后续主要关注 structural level，尤其是 single stuck-at fault。

### 1.6 Stuck-at Fault 固定型故障

一条线可能有两种 stuck-at fault：

```text
x/0: x stuck-at 0
x/1: x stuck-at 1
```

如果电路有 $L$ 条线：

```text
single stuck-at faults = 2L
multiple stuck-at faults = 3^L - 1
```

为什么 multiple 是 $3^L - 1$：

- 每条线有三种状态：无故障、s.a.0、s.a.1。
- 所有线都无故障的情况不算 fault，所以减 1。

课程先研究 single stuck-at fault，因为它更容易处理，而且经验上对很多真实缺陷也有不错的覆盖效果。

### 1.7 其他常见故障模型

**Bridging fault 桥接故障**

两条线意外短接。可以粗略建模成：

- wired-AND：0 是强值。
- wired-OR：1 是强值。

若电路有 $L$ 条线，潜在桥接数量约为：

$$
L(L-1)
$$

实际中通常结合 layout，只考虑每条线附近最可能桥接的 $k$ 条线，降到 $kL$。

**Delay fault 延迟故障**

缺陷不一定改变逻辑功能，但会让信号变慢。常见模型：

- transition fault：某条线 slow-to-rise 或 slow-to-fall。
- gate delay fault：某个门输入到输出的延迟过大。
- path delay fault：某条路径整体延迟过大。

所有 delay fault 通常需要 two-pattern test：

```text
第一个 pattern 建立初始值
第二个 pattern 触发跳变并观察是否及时到达输出
```

**Switch-level fault 开关级故障**

CMOS 晶体管可能 stuck-open 或 stuck-on。stuck-open 特别容易引入“记忆效应”：输出节点可能保留上一次的值，所以也常需要两个输入向量。

### 1.8 什么叫检测到一个故障

对组合电路 $N$，无故障输出函数为 $Z(x)$。故障 $f$ 注入后，电路变成 $N_f$，输出函数为 $Z_f(x)$。

测试向量 $t$ 检测故障 $f$ 当且仅当：

$$
Z_f(t) \neq Z(t)
$$

多输出电路中，只要有一个 primary output 不同，就算检测到：

$$
Z(t) \oplus Z_f(t)
= (z_1(t) \oplus z_{1f}(t)) + \cdots + (z_m(t) \oplus z_{mf}(t))
$$

检测一个 stuck-at fault 通常要三步：

1. 激活故障 activation：故障点的 good value 必须和 stuck-at value 相反。
2. 传播故障 propagation：故障差异不能被后续门遮住。
3. 观察故障 observation：差异必须到达 primary output。

### 1.9 Sensitization 敏化

如果某条线在 good circuit 和 faulty circuit 中取值不同，就说这条线被 sensitized。

让故障通过门时，要注意 controlling value：

| Gate | Controlling value | Non-controlling value |
|---|---:|---:|
| AND / NAND | 0 | 1 |
| OR / NOR | 1 | 0 |

人话：

- AND 门想传播某个输入上的差异，其他输入要设成 1。
- OR 门想传播某个输入上的差异，其他输入要设成 0。

因为 AND 的 0、OR 的 1 会直接决定输出，把故障差异遮住。

### 1.10 Redundancy 冗余

如果一个组合电路里存在不可检测的 stuck-at fault，这个电路称为 redundant。

不可检测的意思是：

```text
不存在任何输入向量能让 good circuit 和 faulty circuit 的输出不同。
```

冗余不是“没用”的同义词，但它说明某些结构对外部行为没有可观察影响。冗余会让测试生成更难，因为 ATPG 需要证明“找不到测试”。

### 1.11 Fault Collapsing：为什么要压缩故障

原始 fault list 很大。每个 fault 都做 ATPG 和 fault simulation，会非常慢。

Fault collapsing 的思想：

```text
如果很多故障在测试角度等价，或者一个故障被另一个故障覆盖，
那就只保留代表故障。
```

要求：压缩算法本身必须快。为了省时间做一个很慢的预处理，没有意义。

### 1.12 Equivalent Fault Collapsing, EFC

两个故障 $f$ 和 $g$ functionally equivalent，当且仅当：

$$
Z_f(x) = Z_g(x)
$$

也就是说，任意测试都无法区分它们。

对一个 $n$ 输入 AND 门：

- 所有输入 s.a.0 和输出 s.a.0 等价。
- 保留输出 s.a.0，再保留所有输入/输出相关的 s.a.1。
- 原本 $2(n+1)$ 个 fault，EFC 后变成 $n+2$ 个代表 fault。

类似地：

| Gate | 等价关系 |
|---|---|
| AND | input s.a.0 等价于 output s.a.0 |
| NAND | input s.a.0 等价于 output s.a.1 |
| OR | input s.a.1 等价于 output s.a.1 |
| NOR | input s.a.1 等价于 output s.a.0 |

在 fanout-free circuit 中，结构规则比较安全，因为每条信号只流向一个后继门。遇到 fanout 时，stem fault 和 branch fault 不能随便合并，因为 stem 会影响所有分支，branch 只影响一个分支。

### 1.13 SIMPLE_EFC 的规则

对 fanout-free 区域，常用近似规则：

1. primary output 保留 s.a.0 和 s.a.1。
2. fanout stem 保留 s.a.0 和 s.a.1。
3. AND/NAND 的 gate input 保留 s.a.1。
4. OR/NOR 的 gate input 保留 s.a.0。

这样做是线性时间，通常效果够好，但不保证全局最小。

重要实现细节：

```text
representative fault -> {original faults in this equivalence class}
```

如果不保存这个映射，后面算 uncollapsed fault coverage 会不准确。

### 1.14 Dominance Fault Collapsing, DFC

令 $T_f$ 是检测故障 $f$ 的所有测试向量集合。

如果：

$$
T_f \supseteq T_g
$$

则称 $f$ dominates $g$。意思是：每个能检测 $g$ 的测试，也一定能检测 $f$。

因此做 ATPG 时，可以删掉 dominating fault $f$，保留更难测的 dominated fault $g$。

方向容易反：

```text
T_f 更大 -> f 更容易被测到 -> f 是 dominating fault -> 可以删 f
T_g 更小 -> g 更难被测到 -> g 应该保留
```

DFC 比 EFC 更激进：

```text
2-input gate:
原始 6 faults -> EFC 后 4 faults -> DFC 后 3 faults

n-input elementary gate:
EFC + DFC 后约 n + 1 faults
```

但 DFC 实践中不如 EFC 常用，因为 coverage 报告可能 pessimistic。一个测试可能检测到了被删除的 dominating fault，却没有检测保留的 dominated fault，于是这个检测不会被计入 DFC coverage。

### 1.15 Checkpoint Theorem

Checkpoints 是：

1. primary inputs
2. fanout branches

Checkpoint theorem：

```text
如果测试集检测了所有 checkpoint 上的 stuck-at faults，
那么它也检测了电路中所有 single stuck-at faults。
```

数量关系：

$$
|CHKPT| \ge |EFC| \ge |DFC|
$$

Checkpoint set 通常不是最小的，但有完整性保证，规则也简单。

---

## CH2. Fault Simulation 故障仿真

[[#目录|返回目录]]

### 2.1 关键词中英文对照

| English                     | 中文     | 人话解释                                       |
| --------------------------- | ------ | ------------------------------------------ |
| Fault Simulation            | 故障仿真   | 算测试集能检测哪些故障                                |
| Serial Fault Simulation     | 串行故障仿真 | 一个故障一个故障地模拟，最直观也最慢                         |
| Event-Driven Simulation     | 事件驱动仿真 | 只重新计算值发生变化影响到的门                            |
| Fault Dropping              | 故障丢弃   | 故障一旦被测到，就从后续仿真中删掉                          |
| Parallel Fault Simulation   | 并行故障仿真 | 一个机器字里同时装 good circuit 和多个 faulty circuits |
| Parallel Pattern Simulation | 并行向量仿真 | 一个机器字里同时装多个测试向量                            |
| Fault Insertion Mask        | 故障注入掩码 | 指定哪些 bit 位置要被强制成 stuck-at 值                |
| Deductive Fault Simulation  | 演绎故障仿真 | 每条线维护一个“哪些故障会让它不同”的集合                      |
| Fault List                  | 故障列表   | 某条线或某个测试下相关的 fault 集合                      |
| Active Faults               | 活跃故障   | 当前测试下已经造成内部差异的故障                           |

### 2.2 Fault Simulation 的输入和输出

输入：

- 测试集 $T = \{t_1, t_2, \ldots, t_n\}$
- 故障列表 $F = \{f_1, f_2, \ldots, f_m\}$
- 无故障电路 $N$

输出：

```text
T 检测到了 F 中哪些 fault
```

用途：

1. 测试生成之后，计算 fault coverage。
2. 测试生成过程中，判断新生成的 pattern 还能顺便检测哪些 fault。

### 2.3 最直接的方法为什么太慢

串行方法：

1. 在 good circuit 上模拟所有测试。
2. 对每个 fault $f$，构造 faulty circuit $N_f$。
3. 在 $N_f$ 上再模拟所有测试。
4. 比较输出。
5. 对所有 fault 重复。

如果有：

```text
100000 gates
200000 stuck-at faults
10000 test patterns
```

粗略工作量就是：

```text
200000 * 10000 * 100000
```

所以真正的问题是三个维度相乘：电路规模、故障数量、测试数量。

### 2.4 Event-Driven Simulation

连续测试向量之间通常只有少数输入位改变。event-driven simulation 利用这一点：

```text
只有某条线的值变了，才重新计算它影响到的后继门。
```

基本流程：

1. 比较新旧输入向量。
2. 把变化的输入线加入 event queue。
3. 取出事件，重新计算 fanout gates。
4. 如果门输出也改变，再把输出变化传播下去。
5. 队列为空，当前 pattern 仿真结束。

优点：输入变化少时非常省。  
局限：如果大量节点变化，或者与 word-parallel packed simulation 混用，收益会下降。

### 2.5 Fault Dropping

如果目标只是 fault coverage，一个 fault 一旦被检测到，就没必要继续模拟它。

流程：

```text
simulate all remaining faults under t1
remove faults detected by t1
simulate remaining faults under t2
remove faults detected by t2
...
```

注意：fault diagnosis 通常不能做 fault dropping，因为诊断需要完整 signature：

- 哪些 pattern 检测它？
- 哪些 output 上出错？
- 不同 fault 的 failure signature 是否相同？

过早删除 fault 会丢诊断信息。

### 2.6 Parallel Fault Simulation

机器字有 $W$ 个 bit，比如 64 bit。parallel fault simulation 用一个 word 同时表示：

```text
1 个 good circuit + W-1 个 faulty circuits
```

对某条线 $x$：

```text
word_x = [good, f1, f2, ..., fW-1]
```

一个 2-input AND 门就可以直接用机器字按位 AND：

```text
word_z = word_a & word_b
```

64-bit 机器上一批最多能并行：

```text
1 good circuit + 63 faulty circuits
```

### 2.7 Fault Insertion Mask

如果某个 bit 对应的 fault 是 line $i$ stuck-at $c$，那么计算完 line $i$ 的正常值后，要把那个 bit 强制改成 $c$。

单个 fault 的选择式：

$$
v_{ij}^{new} = v_{ij} \cdot \overline{M_{ij}} + M_{ij} \cdot c
$$

packed word 版本为：

$$
v_i^{new} = (v_i \& \overline{I_i}) \mid (I_i \& S_i)
$$

其中：

- $I_i$：哪些 bit 位置要在 line $i$ 注入故障。
- $S_i$：这些位置各自要被强制成 0 还是 1。

人话：

```text
I_i 负责“选哪些位”
S_i 负责“这些位改成什么值”
```

### 2.8 Parallel Fault Simulation 的优缺点

优点：

- 理想情况下接近加速 $W$ 倍。
- 门运算可以直接用机器字位运算。

缺点：

- 不能充分利用 event-driven simulation。一个 packed circuit 的某个 bit 变化，往往要算整个 word。
- 需要 packing 和 unpacking。
- 一批只能放 $W-1$ 个 fault。
- pattern-parallel 只在有多个 pattern 可同时处理时有用；时序电路中 pattern 顺序依赖会限制它。

### 2.9 Deductive Fault Simulation

演绎仿真一次只处理一个 test pattern，但同时考虑所有 fault。

它为每条线 $i$ 维护一个 fault list：

$$
L_i = \{f \mid \text{line } i \text{ 在 } N \text{ 和 } N_f \text{ 中取值不同}\}
$$

对于 primary input $i$，如果 good value 是 $a$：

$$
L_i = \{i/\overline{a}\}
$$

对于 primary output，$L_i$ 就是当前 pattern 在该输出检测到的 fault 集合。

### 2.10 AND 门的 fault list 传播规则

对 AND 门，输出 $Z$，输入 $A,B,C$。

**情况 1：所有输入都是 1，输出为 1**

任何输入上的差异都会传到输出：

$$
L_Z = L_A \cup L_B \cup \{Z/0\}
$$

多输入时：

$$
L_Z = \bigcup_r L_r \cup \{Z/0\}
$$

**情况 2：一个输入为 0，一个输入为 1，输出为 0**

例如 $A=0, B=1$：

$$
L_Z = (L_A - L_B) \cup \{Z/1\}
$$

为什么要减 $L_B$：同一个 fault 如果同时影响另一条非控制路径，可能抵消或遮蔽输出变化。

**情况 3：多个输入为 0**

例如 $A=0, B=0, C=1$：

$$
L_Z = ((L_A \cap L_B) - L_C) \cup \{Z/1\}
$$

一般规则：

```text
控制值输入的 fault list 取交集
再减去非控制值输入的 fault list
最后加本地输出 opposite stuck-at fault
```

OR 门规则可由 AND 的对偶得到。

### 2.11 Parallel 和 Deductive 的关系

两者表达的是类似信息：

```text
parallel fault simulation:
  每条线存 dense bit vector

deductive fault simulation:
  每条线存 sparse fault set
```

如果当前 pattern 激活的 fault 很少，deductive list 可能更省。  
如果 fault 很多且 word-level 并行高效，parallel simulation 更直接。

### 2.12 Sequential Circuits

对时序电路，测试序列：

$$
T = (t_1, t_2, \ldots, t_n)
$$

后一个 pattern 的初始状态取决于前一个 pattern 的 next state。所以不能完全独立地并行模拟任意 pattern。

但仍可做：

- 同一时刻多个 faulty circuits 的 parallel fault simulation。
- scan 后把 sequential core 转成更接近 combinational core 的测试问题。

---

## CH3. Combinational ATPG 组合电路测试生成

[[#目录|返回目录]]

### 3.1 关键词中英文对照

| English | 中文 | 人话解释 |
|---|---|---|
| ATPG | 自动测试向量生成 | 自动找能检测目标故障的输入 |
| Random Pattern | 随机测试向量 | 不看结构，随机试 |
| Deterministic ATPG | 确定性测试生成 | 根据电路结构有目标地搜索 |
| Simulation-Based Test Generation | 基于仿真的测试生成 | 生成候选向量，靠仿真反馈修改 |
| Sensitive Pattern | 敏感向量 | 输入变化容易影响输出的向量 |
| Three-Valued Logic | 三值逻辑 | 0、1、X |
| Five-Valued Logic | 五值逻辑 | 0、1、D、D'、X |
| D | D 值 | good=1, faulty=0 |
| D' | D 反值 | good=0, faulty=1 |
| Nine-Valued Logic | 九值逻辑 | 区分 good/faulty 一边已知一边未知 |
| D-Algorithm | D 算法 | 经典 fault-oriented ATPG 算法 |
| D-Frontier | D 前沿 | 输入有 D/D'、输出还是 X 的门 |
| J-Frontier | J 前沿 | 输出被要求为某值，但输入尚未完全 justify 的门 |
| Implication | 蕴含 | 一个赋值能强制推出的其他赋值 |
| Backtracking | 回溯 | 决策冲突后撤销，换另一条路 |
| PODEM | 路径导向决策方法 | 只在 primary inputs 上做决策的 ATPG |
| Backtrace | 回溯到输入 | 从内部目标推到一个 PI 赋值 |
| Controllability | 可控性 | 把某条线设成 0/1 的难度 |
| Observability | 可观测性 | 把某条线的差异传到输出的难度 |
| Test Compaction | 测试压缩 | 用更少 pattern 达到同样 coverage |
| Static Compaction | 静态压缩 | 测试生成后再合并/删除 pattern |
| Dynamic Compaction | 动态压缩 | 测试生成过程中就尽量让每个 pattern 多测 fault |
| Test Pattern Relaxation | 测试向量松弛 | 把不必要的指定输入改回 X |
| Power-Aware Refilling | 功耗感知填充 | 给 X 填值时减少切换和功耗 |

### 3.2 Test Generation Problem

给定 single stuck-at fault 集合 $F$，目标是找到测试集 $T$，使得 $F$ 中每个 detectable fault 至少被 $T$ 中某个 test 检测。

还要考虑额外要求：

- 测试集要短，减少测试时间和 tester memory。
- 功耗不能太高，否则测试模式下可能把好芯片测坏或误判。
- 要兼容测试环境，如 scan、BIST、ATE 限制。

### 3.3 Random Patterns 和 Fault Coverage Curve

随机测试生成很简单：

1. 生成随机 pattern $t$。
2. fault simulate $t$。
3. 如果检测到足够多新 fault，就加入测试集并 drop 掉这些 fault。
4. 如果连续很多 pattern 没什么效果，就停止。

人话：

```text
前期随机 pattern 很容易测到很多 fault，
后期剩下的 fault 越来越难测，coverage curve 会变平。
```

### 3.4 Deterministic ATPG 为什么难

确定性 ATPG 要针对一个目标 fault 构造 test。对 stuck-at fault，必须同时解决：

1. activation：把 fault site 设成 stuck-at value 的反值。
2. propagation：让 D/D' 传播到 primary output。
3. justification：让内部需要的值可以由 primary inputs 实现。

单个 stuck-at fault 的 test generation 是 NP-complete。实际工具靠启发式、蕴含、回溯限制、结构度量来让大多数实例能快速解决。

### 3.5 3 值、5 值和 9 值逻辑

三值逻辑：

```text
0, 1, X
```

X 表示 unknown 或 unspecified。

D-Algorithm 使用五值逻辑：

| 值 | 含义 |
|---|---|
| 0 | good=0, faulty=0 |
| 1 | good=1, faulty=1 |
| D | good=1, faulty=0 |
| D' | good=0, faulty=1 |
| X | 未知 |

D/D' 专门用来表示 fault effect。

九值逻辑进一步区分：

```text
0/x, 1/x, x/0, x/1
```

它能表达“good circuit 已知但 faulty circuit 未知”或反过来。这会让 implication 更强，减少不必要决策。

### 3.6 D-Algorithm 的核心思想

对故障 $l$ s.a.$v$：

- 若 $v=0$，要让 good value 为 1，于是 fault site 出现 $D = 1/0$。
- 若 $v=1$，要让 good value 为 0，于是 fault site 出现 $D' = 0/1$。

之后把 D 或 D' 沿某条路径传播到输出。

基本动作：

1. 初始赋值激活 fault。
2. 做 implication，推出所有必然值。
3. 从 D-frontier 选一个门，继续传播 fault effect。
4. 从 J-frontier 选未解决的 justification 问题。
5. 如果冲突，backtrack。
6. 如果 D/D' 到达 primary output 且所有值都能 justify，成功。
7. 如果所有选择都失败，故障不可检测。

### 3.7 D-Frontier 和 J-Frontier

**D-Frontier**

包含所有：

```text
输入上有 D 或 D'
输出还是 X
```

的门。

要继续传播 fault effect，就从 D-frontier 选门，并把未指定 side inputs 设成 non-controlling value。

如果 D-frontier 为空且 fault effect 还没到输出，就需要 backtrack；如果没选择可回，说明 fault undetectable。

**J-Frontier**

包含所有：

```text
输出值已知，但输入还不能证明这个输出值的门
```

比如 AND 门输出需要 0，但多个输入还是 X，必须至少选择一个输入设成 0 来 justify。

### 3.8 Implication

implication 是：

```text
每当赋一个值，就立刻推出所有被强制的值。
```

它可以减少猜测。例如 AND 输出为 1，就能推出所有输入都为 1。又如某输入已经是 controlling value，就能推出输出。

课程里的那句话很好记：

```text
If you can know what to do, don't guess.
```

能靠逻辑推出的，就不要让搜索树来试。

### 3.9 Backtracking

ATPG 中会做很多决策：

- 选哪条路径传播 D/D'。
- 为了 justify 某个门输出，选哪个输入设 controlling value。
- 对某个 X 输入赋 0 还是 1。

如果某个决策导致冲突，就撤销到最近还有其他选择的决策点，再试另一种选择。

最坏情况下 decision tree 指数大，这是 ATPG 难的根源。

### 3.10 D-Algorithm 速记

```text
D-Alg()
  imply()
  if conflict -> FAIL

  if D/D' not at PO:
    if D-frontier empty -> FAIL
    choose untried gate from D-frontier
    assign non-controlling values to propagate D/D'
    recurse

  else:
    if J-frontier empty -> SUCCESS
    choose gate from J-frontier
    try ways to justify its output
    recurse
```

### 3.11 加速技术

**Local implication vs global implication**

- local implication 只看相邻门。
- global implication 看更大电路区域。

Global implication 可以发现局部推不出的关系，例如某输出为 1 可能间接推出某内部线必须为 1。

**X-Path**

X-path 是一条所有线都是 X 的路径。D-frontier 中的 fault effect 只有在门输出到某个 primary output 存在 X-path 时，才有继续传播的可能。

如果没有 X-path，就不用再试，直接 backtrack。

**Backtrack limit**

设置最大回溯次数可以控制运行时间，但会让算法不完整：可能本来有测试，只是没搜到。

### 3.12 PODEM

PODEM 的核心改进：

```text
只在 primary inputs 上做决策，不直接给内部线做决策。
```

为什么有用：

- 内部线很多，搜索空间大。
- PI 数量较少，决策树显著缩小。
- PI 赋值后只做 forward implication，不需要反复做复杂的 backward justification。

PODEM 每轮做：

1. 选 objective。
2. 从 objective backtrace 到某个 PI。
3. 给该 PI 赋值。
4. forward imply。
5. 看 D/D' 是否到达 PO。
6. 若失败，翻转 PI 赋值；再失败就撤销并继续回溯。

### 3.13 Objective 和 Backtrace

Objective 是一个目标对：

```text
(line, value)
```

选择规则：

- 如果 fault site 还没有 D/D'，objective 是激活故障。
- 如果 fault site 已经有 D/D'，objective 是从 D-frontier 选一个门，把某个 X 输入设成 non-controlling value 来传播。

Backtrace 是从内部目标一路推回 primary input。

注意：

```text
backtrace != backtrack
```

- backtrace：从内部线目标找一个 PI 赋值。
- backtrack：搜索失败后撤销决策。

### 3.14 Controllability 和 Observability

ATPG 要做选择时，需要判断“哪个问题更难”“哪个选择更容易成功”。

Controllability：

- $C0(l)$：把 line $l$ 设成 0 的难度。
- $C1(l)$：把 line $l$ 设成 1 的难度。

Primary input：

$$
C0(l) = C1(l) = 1
$$

AND 门：

$$
C0(g) = \min\{C0(A), C0(B), C0(C)\}
$$

$$
C1(g) = C1(A) + C1(B) + C1(C)
$$

人话：

- AND 输出 0，只要一个输入为 0，选最容易的那个。
- AND 输出 1，所有输入都要为 1，所以难度相加。

Observability：

- $O(l)$：把 line $l$ 上的差异传播到 primary output 的难度。

Primary output：

$$
O(l)=0
$$

AND 门中观察输入 $A$ 的差异时，其他输入必须为 1：

$$
O(A) = C1(B) + C1(C) + O(g)
$$

Fanout stem 的 observability 常取各 branch 中最容易的一条：

$$
O(g) = \min\{O(g_1), O(g_2), O(g_3)\}
$$

这些度量不是精确证明，只是启发式，用来让搜索更快。

### 3.15 ATPG 的整体流程

工业工具通常不是只靠一个算法，而是分阶段：

1. 低成本 fault-independent patterns，例如 random patterns。
2. 快速识别一部分 undetectable faults。
3. 中等成本 simulation-based generation。
4. 确定性 fault-oriented ATPG，逐步增加 backtrack limit。
5. 测试集优化和 compaction。

### 3.16 Unspecified Values 和 Test Compaction

ATPG 产生的测试可能不完全指定：

```text
001x0xx
```

X 值很有用，因为它们可以后续被填成：

- 检测更多 fault。
- 和其他 pattern 合并。
- 降低功耗。

**Static compaction**

测试生成完成后再压缩。两条测试 compatible，当且仅当没有任何 PI 被指定成相反值。

例子：

```text
00xx 和 0x1x compatible -> 可合并成 001x
0xxx 和 1xxx incompatible
```

多个 compatible tests 可用 compatibility graph 表示。寻找最少 clique cover 是 NP-complete，所以实际常用 greedy heuristic。

**Reverse order fault simulation**

如果测试按 $t_1, t_2, ..., t_n$ 生成，后面的测试可能已经检测了前面测试负责的 fault。反向仿真：

```text
t_n, t_{n-1}, ..., t_1
```

若某个测试在反向过程中没有检测任何“还没被保留测试覆盖”的 fault，就可以删除。

**Dynamic compaction**

生成一个 primary target fault 的 test 后，利用剩下的 X 值继续尝试检测 secondary target faults。它通常比 static compaction 更有效，因为压缩在生成过程中就发生。

### 3.17 Test Pattern Relaxation

目标：

```text
在保持目标 fault 被检测的前提下，把尽量多的已指定输入改回 X。
```

贪心方法：

1. 逐个尝试把某个指定输入 unset 成 X。
2. fault simulate 检查原 fault 是否仍被检测。
3. 若仍检测，保留 X；否则恢复原值。

Relaxation 后，pattern 更容易与别的 pattern 合并，也更容易做 power-aware filling。

### 3.18 Test Power Consumption

测试模式下功耗常高于功能模式，原因包括：

- scan shifting 产生大量切换。
- compacted tests 可能让电路内部频繁翻转。
- delay fault testing 对时钟和功耗更敏感。

Power-aware test pattern refilling：

```text
给 incompletely specified test 的 X 填值时，尽量减少 switching。
```

本质上也可以建成一个优化问题。

---

## CH4. Boolean Satisfiability 与 SAT-based ATPG

[[#目录|返回目录]]

### 4.1 关键词中英文对照

| English | 中文 | 人话解释 |
|---|---|---|
| SAT Problem | 可满足性问题 | 是否存在变量赋值让公式为真 |
| SAT Solver | SAT 求解器 | 自动搜索满足赋值或证明无解 |
| CNF | 合取范式 | 子句的与，每个子句是文字的或 |
| Literal | 文字 | 变量或变量取反 |
| Clause | 子句 | 若干 literal 的 OR |
| Model | 模型/满足赋值 | 让公式为真的变量赋值 |
| Miter Circuit | Miter 电路 | 比较两个电路输出是否能不同 |
| Tseitin Transformation | Tseitin 转换 | 给每个门加变量，把电路线性编码成 CNF |
| Resolution | 归结 | 从两个子句推出新子句的规则 |
| Unit Propagation | 单子句传播 | 子句只剩一个未定 literal 时强制赋值 |
| Preprocessing | 预处理 | 求解前简化 CNF |
| Decision Stack | 决策栈 | 记录决策和由此推出的赋值 |
| Decision Level | 决策层级 | 每次主动猜值形成的新层 |
| VSIDS | 变量活跃度启发式 | 优先选择最近冲突中常出现的变量 |
| BCP | 布尔约束传播 | 反复做 unit propagation 和冲突检测 |
| Watched Literals | 双文字监视 | 高效实现 BCP 的主流技术 |
| Conflict Analysis | 冲突分析 | 从冲突中学习新子句 |
| Implication Graph | 蕴含图 | 记录哪些赋值导致哪些赋值 |
| 1UIP | 第一唯一蕴含点 | CDCL 中构造冲突子句的标准切点 |
| Learned Clause | 学习子句 | 防止重复犯同类错误的新约束 |
| Non-Chronological Backtracking | 非时间顺序回溯 | 直接跳回真正相关的决策层 |
| Incremental Solving | 增量求解 | 逐步增加约束，复用 solver 状态 |
| Cone-of-Influence | 影响锥 | 与目标故障和输出相关的电路区域 |
| D-Chain | 差异传播链 | 给 SAT solver 加入故障差异如何传播的结构信息 |
| Good-Diff Encoding | Good-Diff 编码 | 用 good value 和 difference 代替 bad value |

### 4.2 SAT 问题

> **一句人话**：SAT 就是在问“有没有一种给所有 0/1 变量赋值的办法，让所有规则同时成立？”有就是 SAT，没有就是 UNSAT。

SAT 问题问：

```text
给定布尔公式 F，是否存在变量赋值 A，使得 A(F)=1？
```

若存在，公式 satisfiable，solver 输出一个 model。  
若不存在，公式 unsatisfiable。

SAT solver 很适合 ATPG，因为“是否存在一个测试向量检测故障”本质上也是存在性问题。

### 4.3 Miter Circuit

> **一句人话**：把“好电路”和“带故障电路”并排跑同一组输入；只要最终输出不同，就说明这组输入能测出故障。

Miter 用来比较两个电路：

```text
同一组输入 -> fault-free circuit
同一组输入 -> faulty circuit
对应输出接 XOR
所有 XOR 输出 OR 起来得到 M
```

如果存在输入使：

$$
M = 1
$$

说明 good circuit 和 faulty circuit 至少一个输出不同。这个输入就是测试向量。

所以 SAT-based ATPG 的核心就是：

```text
把 miter 编码成 CNF，并强制 M=1。
如果 SAT，model 中的 PI 值就是 test。
如果 UNSAT，该 fault 不可检测或在当前约束下不可检测。
```

### 4.4 Tseitin Transformation

> **一句人话**：SAT solver 只爱吃 CNF；Tseitin 就是给每个逻辑门起一个中间变量名，再把门功能翻译成几条 CNF 子句，方便 solver 处理。

直接把大公式转成 CNF 可能指数爆炸。Tseitin transformation 给每个门输出引入一个新变量，并为每个门加局部约束。

只要每个门需要常数个 clauses，整个电路 CNF 大小就和门数线性相关。

常用门编码：

**AND：$x_3 \leftrightarrow x_1 \land x_2$**

$$
(\neg x_3 \lor x_1)
\land
(\neg x_3 \lor x_2)
\land
(x_3 \lor \neg x_1 \lor \neg x_2)
$$

**OR：$x_3 \leftrightarrow x_1 \lor x_2$**

$$
(x_3 \lor \neg x_1)
\land
(x_3 \lor \neg x_2)
\land
(\neg x_3 \lor x_1 \lor x_2)
$$

**XOR：$x_3 \leftrightarrow x_1 \oplus x_2$**

需要 4 个 clauses。

**NOT：$x_2 \leftrightarrow \neg x_1$**

需要 2 个 clauses。

### 4.5 Resolution 归结

> **一句人话**：如果一条规则说“L 或 A”，另一条说“非 L 或 B”，那么不管 L 取什么，至少必须满足“A 或 B”；这就是从已有规则推出新规则。

若两个 clauses 中一个包含 $L$，另一个包含 $\neg L$：

$$
C_1 = (L \lor A), \quad C_2 = (\neg L \lor B)
$$

可以推出 resolvent：

$$
R = A \lor B
$$

Resolution theorem：

```text
CNF F 不可满足，当且仅当反复归结后能推出空子句。
```

现代 SAT solver 不会傻傻枚举所有 resolution，但 conflict analysis 的理论基础和 resolution 密切相关。

### 4.6 现代 SAT Solver 的主循环

> **一句人话**：solver 先聪明地猜一个值，能推的全推；撞墙了就分析为什么撞墙、记住教训，再跳回真正该重试的位置。

现代 SAT solver 基本是 CDCL 风格：

```text
preprocess CNF
while true:
  choose a decision variable and value
  run BCP
  if conflict:
    analyze conflict
    learn clause
    backtrack
  if all variables assigned without conflict:
    SAT
```

关键部件：

- preprocessing：先把公式变小。
- decision heuristic：决定猜哪个变量。
- BCP：快速推出所有强制赋值。
- conflict analysis：从冲突中学习。
- non-chronological backtracking：跳到真正相关的层。
- restarts/unlearning/incremental solving：工程优化。

### 4.7 Preprocessing

> **一句人话**：正式搜索前先做“整理房间”：立刻能确定的值直接定掉，重复或没用的规则删掉，让后续搜索少背包袱。

预处理目标：

```text
在真正搜索前，把公式变小、变容易。
```

常见技术：

- unit propagation
- unit propagation lookahead, UPLA
- self-subsuming resolution
- variable elimination by resolution
- variable elimination by substitution
- forward/backward subsumption
- blocked clause elimination

预处理也要折中：太弱没效果，太强本身花太多时间。

### 4.8 Decision Stack 和 Decision Level

> **一句人话**：decision 是 solver 主动下的一个赌注；由这个赌注连锁推出的结论都记在同一层。冲突时就知道该撤销到哪一层。

SAT solver 的赋值分两类：

1. decision assignment：solver 主动猜的值。
2. implied assignment：BCP 被迫推出的值。

每次主动猜值形成一个新的 decision level。由该决策推出的赋值也属于同一层。

如果在 level 0 就冲突，说明不需要任何猜测公式已经矛盾，结论是 UNSAT。

### 4.9 VSIDS 决策启发式

> **一句人话**：优先处理最近反复引发矛盾的变量，因为它们往往正是把问题卡住的关键。

VSIDS 给 literal 或 variable 维护 activity score：

- 初始可按出现次数设置。
- 每次 learned clause 中出现的 literal activity 增加。
- 周期性衰减旧 activity，让近期冲突更重要。
- 选择未赋值且 activity 高的 literal 作为下一次决策。

人话：

```text
最近总在冲突里出现的变量，很可能是问题核心，优先猜它。
```

### 4.10 BCP 和 Watched Literals

> **一句人话**：BCP 是“规则已经逼得你只能选一个值了，就别猜，直接填上”。Watched literals 用两个哨兵盯住每条规则，避免每次赋值都遍历所有 clause。

BCP 的任务：

- 找出所有由当前赋值强制推出的赋值。
- 发现 conflict。

SAT solver 大约大量时间都花在 BCP 上，所以实现必须快。

Watched literals 的思想：

```text
每个 clause 只盯住两个 literal。
只要这两个 watched literals 中还有一个为真，或两个都不是假，
这个 clause 暂时不可能变成冲突或 unit。
```

当一个 watched literal 被赋成 false 时，才尝试在 clause 中找新的 watched literal。找不到时：

- 如果另一个 watched literal 未赋值，产生 unit implication。
- 如果另一个也为 false，产生 conflict。

### 4.11 Conflict Analysis、1UIP 和 Learned Clause

> **一句人话**：发生冲突不是白失败一次；solver 倒推冲突的根源，写下一条“以后别再同时这样选”的 learned clause，1UIP 是最常用的切分点。

冲突出现时，solver 不只是简单回到上一步，而是分析：

```text
哪些赋值组合导致了这个冲突？
```

implication graph 记录：

- 节点：变量赋值。
- 边：哪些赋值导致某个 implication。

1UIP 是当前 decision level 上离 conflict 最近的 unique implication point。用 1UIP 切分 implication graph，可以得到一个 asserting clause。

Learned clause 的作用：

```text
以后不要再走到同样的冲突组合。
```

Non-chronological backtracking 根据 learned clause 直接跳回相关层，而不是机械地退一层。

### 4.12 SAT for ATPG：怎么编码

> **一句人话**：把“故障要被激活，而且好/坏电路的输出必须不同”翻译成 CNF，交给 SAT solver 找一组输入测试向量。

最直观是编码完整 miter：

```text
good circuit 一份
faulty circuit 一份
输出 XOR/OR，强制 M=1
```

但可以更聪明地只编码相关部分。

Cone-of-influence 分成：

- support cone：影响目标输出和故障传播的输入区域。
- justification cone：为故障点赋值所需的区域。
- propagation cone：故障影响可能从故障点传播到输出的区域。

优化：

1. support cone 外的白色区域无关，不编码。
2. fault-free 和 faulty 在 justification cone 中相同，可合并。
3. propagation cone 中 good 和 bad 可能不同，需要编码两份。

### 4.13 Incremental Solving

> **一句人话**：同一颗电路要测很多 fault，不必每次都从零开始解；保留 solver 已学到的东西，只替换当前故障相关的限制。

ATPG 往往要对很多 fault 逐个求解。增量 SAT 可以复用 solver 的内部状态：

```text
固定一大部分共享电路约束
每次只添加当前 fault 和输出差异约束
求解后再换下一组 assumptions/constraints
```

这样比每个 fault 都从空 solver 开始更高效。

### 4.14 为什么需要 D-Chain

> **一句人话**：普通 SAT 知道好电路和坏电路要不同，但不一定看得出差异怎么走到输出；D-chain 把这条“差异传递路线”明确标出来，帮 solver 少绕路。

普通 CNF 编码里，good circuit 和 faulty circuit 的内部结构关系对 solver 来说不够显式。solver 只看到一堆 clauses，不一定知道：

```text
故障差异应该沿着哪条路径传播到输出。
```

D-chain 是额外加入的冗余 clauses。它不改变问题答案，但给 solver 更多结构信息，让搜索少走弯路。

人话：

```text
D-chain 就是“故障影响能不能真的一路传到输出”的证据链。
```

### 4.15 Forward D-Chain

> **一句人话**：从故障点往后看：既然这里已经不同，后面必须选出一条不被遮住的路，把这个不同送到输出。

Forward D-chain 从 fault site 往输出推：

```text
这里已经有差异 -> 后面必须继续有差异 -> 最后到输出
```

典型约束：

```text
D1 = true
D3 => (G3 xor B3)
D4 => (G4 xor B4)
D1 => (D3 or D4)
D3 => Do1
D4 => (Do1 or Do2)
```

意思：

- fault location 处差异为真。
- 如果某条 D-chain 变量为真，该线 good/bad 必须不同。
- 差异不能断在中间，必须沿某条后继路径传播。

### 4.16 Backward D-Chain

> **一句人话**：从有差异的输出往前追：这个不同不可能凭空产生，必须能一路追溯回故障点。

Backward D-chain 从输出往 fault site 追：

```text
如果输出有差异，这个差异不能凭空出现，
必须来自前面的某个输入差异。
```

典型约束：

```text
D1 = true
D3 <=> (G3 xor B3)
D4 <=> (G4 xor B4)
Do1 => (D3 or D4)
Do2 => D4
D3 => D1
D4 => D1
```

它的作用是加强“差异来源必须合理”的推理。

### 4.17 Combined Backward/Forward D-Chains

> **一句人话**：前推确保差异走得出去，后推确保它来得合理；两边一起夹住后，solver 更容易锁定真正有效的传播路径。

两种 D-chain 可以合起来用，给 solver 最大信息。

每个 gate 引入两个变量：

- $D_f$：forward difference
- $D_b$：backward difference

用更便宜的约束：

$$
D_f \Rightarrow D_b
$$

替代较贵的：

$$
D_f = (G \oplus B)
$$

每个 gate 总共大约 7 个 clauses：

1. 4 个 backward D-chain 的 difference condition clauses。
2. 1 个 $D_f \Rightarrow D_b$。
3. 1 个 forward implication。
4. 1 个 backward implication。

### 4.18 Good-Diff D-Chain

> **一句人话**：不再同时存好值 G、坏值 B 和差异 D 三份信息；利用“两份已知就能推出第三份”，尝试删掉 B 来减少变量和子句。

普通 miter 每个信号有：

```text
G = good value
B = bad value
D = difference
```

且：

$$
D \leftrightarrow (G \oplus B)
$$

也有：

$$
G \leftrightarrow (B \oplus D)
$$

$$
B \leftrightarrow (G \oplus D)
$$

所以知道任意两个就能推出第三个。Good-Diff 的想法：

```text
能不能去掉 B，只保留 G 和 D？
```

例子：

```text
D3 <=> D1 and Ga
D4 <=> D1 and G2
D6 <=> D4 and not G2
```

这些在只有一个输入可能带差异时很便宜。

但如果一个门的多个输入都可能带差异，条件会变复杂。例如 C5 两个输入都可能带差异时：

```text
D5 <=> 
  (D3 and not D4 and G4)
  or (D4 and not D3 and G3)
  or (D3 and D4 and (G3 == G4))
```

因此 Good-Diff 不总是省。

课件给出的代价趋势：

```text
2-input AND, one input with diff: 3 clauses, 7 literals
2-input AND, both inputs with diff: 9 clauses, 35 literals
4-input AND, all inputs with diff: 36 clauses
```

### 4.19 Hybrid D-Chains

> **一句人话**：Good-Diff 在简单门上很省，在复杂门上反而可能更贵；Hybrid 就是哪边便宜用哪边，不死守一种编码。

Hybrid 的思想很务实：

```text
Good-Diff 划算的地方用 Good-Diff；
不划算的地方回到标准 Tseitin encoding。
```

两种策略：

- static：只有一个 diff input 的 gate 用 Good-Diff。
- dynamic/hybrid：更精细地计算每个 gate 哪种编码更便宜。

结果图的总体结论：

- D-chain 会增加 formula size，因为加入了额外 clauses。
- 但通常能减少 solving time，因为 solver 得到更多传播信息。
- Forward-only 不一定总是收益最好。
- Backward、Backward+Forward、Good-Diff、Hybrid 往往能显著降低求解时间。

---

## CH5. Design-for-Testability 可测试性设计

[[#目录|返回目录]]

### 5.1 DFT 为什么存在

测试成本不只是 ATE 跑了多久，还包括：

- 测试开发时间；
- 测试向量占用的 tester memory；
- 每颗芯片的 test application time；
- 覆盖率不够造成的坏芯片流出、退换货和信誉损失。

前四章默认电路已经设计好，然后想办法仿真或生成测试。CH5 换了一个角度：

> 如果原电路实在难测，就修改设计，让内部节点更容易控制、更容易观察。

DFT 的全称是 **Design-for-Testability**。它通常加入额外硬件；正常工作时，这些硬件必须关闭、旁路或保持透明，不能改变芯片原功能。

### 5.2 DFT 与 SFT

| 方法  | 全称                        | 做法                       | 结果             |
| --- | ------------------------- | ------------------------ | -------------- |
| DFT | Design-for-Testability    | 增加 test point、scan 等测试硬件 | 原来的难测故障变得可测    |
| SFT | Synthesis-for-Testability | 重新综合、改变逻辑结构              | 删除或重构造成难测问题的逻辑 |

课件例子中：

$$
f=AB+(A+C)=A+C
$$

所以输出实际与 $B$ 无关，$B$ stuck-at-0 无法检测。

- DFT：加入测试控制输入，在测试模式下让 $B$ 能影响输出；
- SFT：直接把冗余的 $AB$ 支路删除，只留下 $A+C$。

SFT 不一定总能用，因为冗余逻辑可能是为了抗瞬态故障、可靠性、速度或功耗而故意加入的，重新综合可能破坏这些优化。

### 5.3 怎样衡量 Testability

可测试性主要看两个指标：

- **Controllability**：能不能从 primary inputs 容易地把内部节点设成需要的 0 或 1；
- **Observability**：内部节点的故障效应能不能容易地传到 primary outputs。

对应 ATPG 的两个关键动作：

```text
Controllability 不足 → 故障难激活
Observability 不足  → 故障激活了，但差异传不到输出
```

已知难测的结构包括：

- 带反馈的时序电路；
- 输入数量很多的门；
- ATPG 后覆盖率仍低或经常 timeout 的区域；
- 为可靠性故意加入的冗余逻辑。

例如，随机向量让一个 $n$ 输入 AND 门输出 1 的概率是：

$$
P=\left(\frac12\right)^n
$$

输入越多，随机测试越难遇到全 1。

寻找难测结构的信息来源包括：

1. controllability/observability 等结构性指标，但它们只是估算，可能不准确；
2. 随机向量仿真；
3. ATPG 后的 fault coverage 和 timeout 信息。

### 5.4 Control Point 与 Observation Point

测试点有两类：

| 测试点 | 作用 | 解决的问题 |
|---|---|---|
| Control Point, CP | 测试模式下给内部节点指定 0 或 1 | 故障无法激活 |
| Observation Point, OP | 把内部节点接到可观察位置 | 故障效应传不到主输出 |

可以把 CP 理解成内部节点的“遥控器”，把 OP 理解成内部节点的“观察窗口”。

正常模式下，CP 必须透明。例如：

- OR 型控制结构的透明值是 0，因为 $g+0=g$；
- AND 型控制结构的透明值是 1，因为 $g\cdot1=g$。

### 5.5 根据 Fault Simulation 选择测试点

若故障 $f_i$ 已经激活，并能传播到一组内部线路：

$$
G_i=\{g_{i1},g_{i2},\ldots\}
$$

但无法到达主输出，那么在 $G_i$ 中任选一个节点加入 OP，就可以观察该故障。

图中的 `1/0` 表示：

```text
good circuit = 1
faulty circuit = 0
```

它就是 D-Algorithm 中的 $D$。若某内部节点已有 `1/0`，但后面的 OR 门另一个输入是 1，则：

$$
(1/0)+1=1/1
$$

故障效应被控制值遮住。这时可以在被遮住之前的节点加 OP。

如果故障 $f_i=l_i/v_i$ 无法激活，就需要让正常线路满足：

$$
l_i=v_i'=\neg v_i
$$

然后在能帮助实现这个值的线路上加入 CP。

### 5.6 多个故障与 Set Covering

实际中一个观察点可能同时观察多个故障。目标不是每个故障各加一个点，而是找最少的点覆盖所有故障。

假设每个故障 $f_i$ 的可观察节点集合是 $G_i$，要选择集合 $G$，满足：

$$
G\cap G_i\neq\varnothing,\qquad \forall i
$$

并且让 $|G|$ 尽量小。这就是 **Set Covering / Hitting Set** 问题，是 NP-complete。

可用二进制变量表示是否选择节点：

$$
x_j=1 \Longleftrightarrow \text{选择 }g_j
$$

优化目标：

$$
\min\sum_jx_j
$$

对每个故障都要求至少选中一个能观察它的节点。实际工具常用 greedy、ILP、SAT/MaxSAT 或其他启发式方法。

### 5.7 额外测试输入怎么接出去

CP 会产生额外输入，必须让测试机能写入它们。

**方案 1：并行加载触发器**

- 每个测试输入由一个 FF 保存；
- 从多个 primary inputs 同时加载；
- 速度快，几乎不增加测试时间；
- 缺点是需要很多 I/O pins 和布线。

**方案 2：Shift Register / Scan Register**

- 把 FF 串起来；
- 通过一个额外输入逐位 shift in；
- 引脚少；
- 加载 $k$ 位大约需要 $k$ 个 shift clocks。

核心权衡：

| 方法 | 引脚 | 加载时间 |
|---|---:|---:|
| 并行加载 | 多 | 短 |
| 串行移位 | 少 | 长 |

### 5.8 额外测试输出怎么接出去

OP 会产生额外输出，也不能每个点都占一个芯片引脚。课件给出三种方案：

1. **输出扫描寄存器**：先把 observation values 存入 FF，再从一个 scan-out 串行移出；
2. **与 primary outputs 复用**：用 MUX 在正常输出和测试输出之间切换；
3. **XOR tree**：把多个观察点压缩成一个或少量奇偶校验输出。

前两种保留的信息较完整；XOR tree 硬件简单，但可能发生信息抵消。

### 5.9 XOR Tree 与 Aliasing

若多个观察点接到 XOR tree：

$$
O_{extra}=O_1\oplus O_2\oplus\cdots\oplus O_k
$$

故障使奇数个 $O_i$ 翻转时，$O_{extra}$ 一定改变，可以检测；故障使偶数个 $O_i$ 翻转时，变化可能互相抵消。

例如 $O_1$ 和 $O_3$ 同时改变：

$$
1\oplus1=0
$$

压缩输出不变，故障漏检。这种不同内部响应压缩成相同结果的现象叫 **aliasing**。

解决方法是使用多棵 XOR tree，把容易同时翻转的观察点分到不同树上。代价是额外输出和硬件增加。

### 5.10 Test Points 与 BIST

BIST 是 **Built-In Self-Test**，TPG 是 **Test Pattern Generator**。

硬件 TPG 往往生成伪随机向量，结构简单，但可能测不到 random-pattern-resistant faults。可以先仿真 TPG 序列，找出未检测故障，再在这些故障能传播到的内部节点加入 OP。

因此 test point 能让较简单的硬件 TPG 也达到可接受的覆盖率。

### 5.11 时序电路为什么更难测

组合电路的输出只由当前输入决定；时序电路还取决于当前状态：

$$
S(t+1)=F(S(t),X(t)),\qquad Y(t)=G(S(t),X(t))
$$

主要有三类问题：

1. **Initialization**：测试开始时 FF 状态通常未知；
2. **Counters**：某些状态要运行极多周期才能到达；
3. **Sequential ATPG**：要找的不是一个向量，而是多周期序列。

所以时序测试通常需要：

```text
先进入目标状态 → 激活故障 → 再把故障效应传播到输出
```

### 5.12 Circuit Initialization

Initialization 就是把未知状态带到已知状态。

常见方法：

| 方法 | 含义 | 主要问题 |
|---|---|---|
| Synchronizing sequence | 输入一段序列，使所有可能初态汇合到同一状态 | 不一定存在，可能很难找或指数级长 |
| Reset input | 同步或异步清零/置位 FF | reset 线要布到大量 FF |
| Power-up reset | 上电时自动产生 reset | 需要额外检测和复位硬件 |
| Partial reset | 只复位关键 FF | 必须保证剩余未知状态不影响测试 |
| Scan | 直接串行写入目标状态 | 有硬件和移位时间开销 |

初始化很重要，因为测试执行和 debug trace 都需要确定、可重复的起点。

### 5.13 ILA 与同步序列生成

ILA 是 **Iterative Logic Array**。它把时序电路沿时间展开：

```text
S0 → [CL, X0] → S1 → [CL, X1] → S2 → ... → Sk
```

每个时间帧复制一份组合逻辑，前一帧的 next state 接到后一帧的 present state。这样，多周期时序问题就转成一个更大的组合问题。

寻找同步序列可写成 BMC：

- 初始状态：All-X，表示任意状态；
- 转移关系：原电路逻辑；
- 目标：经过限定周期后，状态不含 X，成为确定状态。

从较短长度开始搜索，找不到再增加展开深度。缺点是展开越深，模型越大。

### 5.14 Counter 的测试问题

一个 16-bit counter 从某些初态走到 all-1，可能需要：

$$
2^{16}=65536
$$

个时钟周期。这样的测试序列太长，实际 ATPG 很难处理。

解决办法：

- 把计数器 partition 成较小部分，分别控制；
- 在中间加入测试控制点，打断很长的进位链；
- 使用 scan，直接把目标状态移入 FF。

比如通过 scan 写入 16 位目标状态，只需数量级为 16 的移位周期，而不是数万个正常计数周期。

### 5.15 Sequential ATPG

Sequential ATPG 要寻找一段输入序列，使 fault-free circuit 和 faulty circuit 最终可区分。即使序列存在，也可能需要探索大量状态转换。

一条完整测试通常分成三段：

```text
Initialization Sequence
        ↓
Test Pattern / Fault Activation
        ↓
Fault Propagation Sequence
```

1. 把电路带到需要的初始状态；
2. 让 fault site 的正常值与 stuck-at value 相反；
3. 继续运行若干周期，把故障效应送到可观察输出。

实用方法常借助 ILA，把有限时间范围内的 sequential ATPG 转成 combinational ATPG。Scan 则进一步把内部状态变成可直接写入和读出的量。

### 5.16 Scan 的核心思想

Scan 是时序电路最常用的 DFT 技术。它把功能 FF 串成移位寄存器：

```text
Scan-in → FF1 → FF2 → ... → FFn → Scan-out
```

典型测试分三步：

1. **Shift in**：串行移入目标内部状态；
2. **Capture**：切回功能模式，运行一个或少量时钟捕获响应；
3. **Shift out**：串行移出 FF 中的响应，同时可移入下一组测试状态。

它同时提高：

- controllability：内部状态可以直接写入；
- observability：内部状态可以直接读出。

并行加载也能做到，但需要从大量 PI/PO 到各 FF 的布线，面积开销通常更大。

### 5.17 Scan Cell

Scan cell 本质上是一个普通 D-FF 前面加选择逻辑：

$$
D_{FF}=\begin{cases}
D,&\text{normal mode}\\
S_{in},&\text{test/shift mode}
\end{cases}
$$

课件给出两种实现：

1. **同一时钟**：正常工作和 scan shift 共用 `CK`，用 mode signal 选择数据来源；
2. **两个时钟**：`CK` 负责正常操作，`CKS` 负责扫描移位，控制清楚但多一套时钟布线。

Full Serial Integrated Scan 中，组合逻辑 `CL` 的状态输入和输出接到 scan register `Rs`；测试时通过 $S_{in}$ 写状态，通过 $S_{out}$ 读状态。

### 5.18 Integrated Scan 与 Boundary Scan

**Integrated Scan** 把芯片内部功能 FF 改成 scan cells，主要测试芯片内部组合逻辑和状态。

**Boundary Scan** 在模块或芯片 I/O 边界放扫描单元，主要用于：

- 隔离不同模块；
- 测试模块本身；
- 测试芯片或模块之间的 interconnect，例如 PCB 焊点和连线。

测试 interconnect 的基本过程：

```text
前一模块 R2 发送数据
→ 经过模块间连线
→ 后一模块 R1 捕获
→ scan out 后比较
```

测试一个 module 时，则从前级边界寄存器施加输入，在后级边界寄存器捕获模块输出。

### 5.19 Full Scan 与 Partial Scan

| 方案 | 做法 | ATPG 难度 | 硬件/时序开销 |
|---|---|---:|---:|
| Full Scan | 所有或几乎所有 FF 加入 scan chain | 最低，近似组合 ATPG | 最大 |
| Partial Scan | 只选一部分 FF 加入 scan chain | 较高，仍有部分时序性 | 较小 |

Partial scan 的选择目标是：用尽量少的 scan FF，让测试生成仍可高效完成。选择方法包括：

- Structural：根据反馈环和电路结构选择；
- ATPG-based：根据难测故障、覆盖率或 timeout 结果选择。

实际选择还要考虑 layout、关键路径、功耗和性能，因此加入 scan 的比例常常仍接近 100%。

### 5.20 CH5 考前压缩版

```text
DFT：加测试硬件，让原电路更好测；正常模式必须透明。
SFT：重新综合电路，删除或重构难测逻辑。

难激活 → controllability 差 → 加 control point。
难传播 → observability 差 → 加 observation point。
多个故障共享测试点 → set covering，NP-complete。

额外输入：并行 FF 快但费引脚；scan register 省引脚但费时间。
额外输出：scan-out、MUX 复用、XOR tree。
XOR tree：奇数个变化可见，偶数个变化可能 aliasing。

时序测试 = 初始化 + 故障激活 + 故障传播。
ILA = 按时间展开，把时序问题转成组合问题。
Scan = shift in + capture + shift out。
Integrated scan 测内部；boundary scan 测边界、模块和互连。
Full scan 好测但开销大；partial scan 开销小但 ATPG 更难。
```

---

## 9. CH1-CH5 的核心关系回顾

[[#目录|返回目录]]

### 9.1 从“测得出”到“怎么找”再到“让它好测”

CH1 定义：

$$
Z_f(t) \neq Z(t)
$$

CH2 问：

```text
给定 t，哪些 f 满足这个不等式？
```

CH3 问：

```text
给定 f，怎么搜索一个 t 让这个不等式成立？
```

CH4 问：

```text
能不能把“存在这样的 t”写成 SAT 公式，让 solver 找？
```

CH5 问：

```text
如果 t 很难找到或覆盖率太低，能不能修改电路，让故障更容易激活和观察？
```

### 9.2 三个永远绕不开的动作

不管 D-Algorithm、PODEM 还是 SAT-based ATPG，都在做同一件事：

| 动作  | English     | 说明                                           |
| --- | ----------- | -------------------------------------------- |
| 激活  | Activation  | fault site 的 good value 要和 stuck-at value 相反 |
| 传播  | Propagation | 差异要穿过门，不能被 controlling value 遮住              |
| 观察  | Observation | 差异最终要到 primary output                        |

### 9.3 公式和算法速记

| 内容 | 速记 |
|---|---|
| Fault coverage | $FC = N/M$ |
| Defect level | $DL = 1 - Y^{(1-FC)}$ |
| Single stuck-at 数量 | $2L$ |
| Multiple stuck-at 数量 | $3^L - 1$ |
| Bridging fault 粗略数量 | $L(L-1)$ |
| Test detects fault | $Z_f(t) \neq Z(t)$ |
| AND 控制值 | 0 |
| OR 控制值 | 1 |
| D | good=1, faulty=0 |
| D' | good=0, faulty=1 |
| AND controllability | $C0(g)=\min C0(inputs)$, $C1(g)=\sum C1(inputs)$ |
| AND observability | $O(A)=C1(B)+C1(C)+O(g)$ |
| Tseitin AND | 3 clauses |
| Tseitin XOR | 4 clauses |
| Miter condition | $M=1$ iff good/faulty outputs differ |
| D-chain 目的 | 加强差异传播信息，不改变 SAT 答案 |
| Control point | 改善 controllability，帮助激活故障 |
| Observation point | 改善 observability，帮助观察故障 |
| XOR 压缩检测条件 | 奇数个输入响应发生翻转 |
| Scan 流程 | shift in → capture → shift out |
| ILA | 沿时间展开时序电路 |

### 9.4 高频易错点

1. Defect 和 fault 不是一回事。defect 是物理现实，fault 是抽象模型。
2. Fault coverage 高不等于没有坏芯片，只是坏芯片逃过测试的概率降低。
3. AND 要传播差异，其他输入设 1；OR 要传播差异，其他输入设 0。
4. Fanout stem 和 branch 不能随便等价合并。
5. Dominance 的删除方向容易反：删 detecting set 更大的 dominating fault，保留更难测的 dominated fault。
6. Fault dropping 不适合 diagnosis，因为会丢完整 signature。
7. Parallel fault simulation 和 parallel pattern simulation 不一样：前者 bit 表示 fault，后者 bit 表示 pattern。
8. D-Algorithm 的 backtracking 和 PODEM 的 backtrace 不是一回事。
9. PODEM 只在 PI 上做决策，这是它缩小搜索空间的关键。
10. SAT 的 learned clause 不是随便加的，它由 conflict analysis 和 resolution 保证不会改变 satisfiability。
11. D-chain 是冗余约束，答案不变，但 solver 更容易推理。
12. Good-Diff 去掉 B 变量不一定总省，多输入都可能有差异时编码会变贵。
13. DFT 是增加测试硬件，SFT 是重新综合，两者不要混淆。
14. Control point 帮助激活，observation point 帮助传播后的观察。
15. XOR tree 中偶数个响应同时翻转可能互相抵消，产生 aliasing。
16. Scan 不等于完全没有时序开销；它用移位时间换取少量 I/O 和较简单的 ATPG。
17. Boundary scan 重点是芯片边界、模块和互连；integrated scan 重点是内部逻辑。
18. Partial scan 不是固定比例，而是在测试难度与面积、时序、布线之间折中。

### 9.5 考前压缩版

如果只能记一页：

```text
CH1:
测试 = 找制造电路和设计之间可观察差异。
故障检测 = 激活 + 传播 + 观察。
Fault collapsing 用等价和支配减少 target faults。

CH2:
Fault simulation = 给测试集，算检测了哪些故障。
加速手段 = event-driven, fault dropping, parallel simulation, deductive simulation。

CH3:
ATPG = 给目标 fault，找测试向量。
D-Algorithm 用 D/D'、D-frontier、J-frontier、implication、backtracking。
PODEM 只在 PI 上决策，用 objective + backtrace。
Compaction 利用 X 值减少测试数量。

CH4:
SAT-based ATPG = miter + Tseitin CNF + M=1。
现代 SAT solver = preprocessing + VSIDS + BCP + watched literals + conflict learning + non-chronological backtracking。
D-chain 给 solver 加故障传播结构信息，通常增大公式但减少求解时间。

CH5:
DFT = 修改电路使它更好测，核心是 controllability + observability。
Control point 帮助激活，observation point 帮助观察。
时序测试需要初始化、激活、传播；ILA 做时间展开，scan 直接访问内部状态。
Scan 操作 = shift in + capture + shift out。
```

---

## CH6. BIST and Test Compression 芯片自己测自己

[[#目录|返回目录]]

### 6.1 这一章到底在解决什么

> **一句人话**：以前是外部测试机负责出题和判题，BIST 是让芯片内部自己生成测试、执行测试，最后只把“及格还是不及格”告诉外部。

前面几章默认有一台 ATE（外部测试机）：它把测试向量送进芯片，再把每个输出拿回来比对。CH6 的想法是把这件事的一大部分搬进芯片：

```text
ATE 只负责：开始 / 结束 / 读最终结果
芯片内部负责：出题(TPG) -> 跑被测电路(CUT) -> 判题(ORA)
```

- **TPG, Test Pattern Generator**：产生测试输入；
- **CUT, Circuit Under Test**：被测电路；
- **ORA, Output Response Analyzer**：把输出响应压缩、判断；
- **BIST, Built-In Self-Test**：把 TPG 和 ORA 放在芯片里的自测试结构。

人话：ATE 不必再带着几百万条题目和标准答案来回搬运，芯片自己完成大部分重复工作，只交一份“最终成绩单”。

BIST 特别有价值的原因：

1. 测试机向量存储需求小很多；
2. 测试逻辑靠近嵌入式模块，不必经过很长的 scan chain；
3. 可以 **at-speed** 测试，即用芯片真实工作频率测 delay fault。外部测试机跟不上芯片频率时，这点尤其重要。

### 6.2 On-line 和 Off-line BIST

> **一句人话**：On-line BIST 是芯片使用过程中顺便检查自己，Off-line BIST 是先暂停正常工作，再专门做一次更彻底的体检。

| 类型 | 什么时候测 | 优点 / 代价 |
|---|---|---|
| Concurrent on-line BIST | 正常功能运行时同时测 | 故障刚出现就可能发现，但只能用不影响功能的检查 |
| Non-concurrent on-line BIST | 系统空闲时测 | 不影响忙时功能，但覆盖率受空闲窗口限制 |
| Off-line BIST | 系统暂停正常任务时测 | 可施加更完整的测试序列，典型用于出厂或启动自检 |

并发在线测试常见两条路：**编码检查**（例如 memory word 的 parity）和**复制比较**（两个或三个副本算同一件事，结果不一致就报警）。后者例如 TMR；它更偏可靠性保护，并不等于完整的制造测试。

### 6.3 穷举、伪穷举与 test signal input

> **一句人话**：穷举是把所有输入组合全试一遍；伪穷举利用“每个输出只依赖部分输入”，把能绑在一起变化的输入分组，从而大幅减少测试数量。

对于有 $n$ 个输入的组合电路，穷举测试就是 binary counter 跑完所有输入：

$$
N_{exhaustive}=2^n
$$

它最直接，也最贵。例如 $n=32$ 时，单靠穷举就有约 43 亿组输入，通常不可行。

**Pseudo-exhaustive test（伪穷举）**不是偷工减料地“少测一些随机向量”，而是利用一个事实：一个输出通常只依赖全部输入中的少数几个。把电路按输出依赖关系看成多个小锥体，每个锥体的相关输入组合都穷举到，就叫伪穷举。

- $w$：任意一个输出最多依赖多少个输入；
- $p$：把输入分组后，真正需要独立变化的 **test signal inputs** 数量；
- 测试量在 $2^w$ 和 $2^p$ 之间；若所有输出可以同时完成穷举，则 $p=w$。

分组规则很简单：**如果两个输入从来不会同时影响同一个输出，它们就可以接同一个 counter bit，一起翻转。**

做题步骤：先写 dependency matrix（行是输出函数、列是输入，依赖处填 1）；再把任意同一行不会同时出现 1 的列放进一组。目标是让组数 $p$ 尽量小。这本质上是“哪些输入可以绑在一起”的组合优化问题。

### 6.4 Pseudo-random BIST 与 LFSR

> **一句人话**：LFSR 用很少的触发器和 XOR 门，循环产生一长串看起来随机、实际上可以重复的测试向量，是芯片内部最常见的自动出题器。

伪随机向量看起来像随机：每根输入线上 0 和 1 大致各半；但它实际由确定电路产生，因此可重复，便于 debug。最常用的 TPG 是 **LFSR（线性反馈移位寄存器）**。

```text
DFF 串成移位寄存器 + 若干 tap 做 XOR 反馈
每个 clock：状态移动一次，并生成下一组测试比特
```

LFSR 只有 XOR 和触发器，面积小。一个 $n$-stage LFSR 的最大非零周期是：

$$
2^n-1
$$

达到这个周期时称为 **maximum-length sequence**，其特征多项式是 **primitive polynomial**。不用死背多项式推导，记住：选 primitive polynomial 才不会很早绕回旧状态。

**全 0 是 LFSR 的陷阱**：XOR 反馈下，进入 all-0 后下一拍还是 all-0，所以它不会出现在最大长度序列中。若 CUT 的 `000...0` 真有测试价值，需要额外补一拍、加一位 LFSR，或另用逻辑注入该模式。

LFSR 可以直接驱动 CUT 输入，也常接到 scan chain。后者引脚少，但一条完整 scan pattern 要多次 shift；前者每拍一组向量，但面对很多输入时布线/硬件开销更大。

### 6.5 为什么随机测不全：WRP

> **一句人话**：有些故障只有在输入几乎全是 0 或全是 1 时才会暴露，普通五五开的随机模式很难碰到，所以要故意把 0/1 概率调偏。

有些故障只有极少数输入能测到，或它要求输入大部分为 1（或大部分为 0）。均匀随机输入几乎碰不到它，叫 **random-pattern-resistant fault**。

解决方式是 **Weighted Random Pattern（WRP）**：不再让每个输入 $P(1)=0.5$，而是有偏地生成 0/1，例如把某输入调成 $P(1)=0.75$。

- AND 两个近似独立的 0.5 信号，可得到 $P(1)\approx1/4$；
- OR 两个近似独立的 0.5 信号，可得到 $P(1)\approx3/4$；
- 权重可对每个输入不同，也可分多轮使用不同权重组。

注意：LFSR 各 tap 并非真正独立，所以上面的概率是设计直觉，不是精确统计承诺。实际权重可由结构可检测性分析，或从 deterministic ATPG 给出的 test cube 中统计每个 PI 偏向 0 还是 1 得到。

### 6.6 混合模式 BIST：随机抓大头，确定性补尾巴

> **一句人话**：先用便宜的伪随机模式抓住大多数容易测的故障，再用 reseeding 或 bit flipping 生成少量精准模式，专门收拾剩下的 hard faults。

纯随机通常很快抓住大多数容易测的 faults；剩下少量 hard faults 才需要确定性模式。直接存整条 $n$-bit scan pattern 很浪费，所以有两类经典做法。

**LFSR reseeding（store and generate）**：只存一个较短的 $k$-bit seed。LFSR 从该 seed 出发，shift 后得到目标 test cube 中指定的那些位；`X` 位不管。每个指定 bit 对 seed 是一个 GF(2) 线性方程，解出 seed 即可。于是每个 pattern 从存 $n$ bit 变为大约存 $k$ bit。

若某个 test cube 的约束无法被一个反馈多项式满足，可以准备多个 LFSR polynomial；同一个短 seed 在不同 feedback function 下会产生不同序列，编码成功率更高。

**Bit fixing / bit flipping（predict and correct）**：先用 LFSR 预测一大串伪随机模式，再由小型 control logic 把少数“不对的位”强制改值（fixing）或取反（flipping），把原本没用的随机模式修成能测 hard fault 的确定性模式。优点是存储少；代价是修正逻辑是针对该 CUT 定制的。

### 6.7 Output compaction：为什么只看一个 signature 也能判题

> **一句人话**：测试输出可能有几百万 bit，MISR 等压缩器把它们浓缩成一个短 signature；只要和正确签名不同，就知道测试过程中出现过异常。

若每拍把全部输出送回 ATE，数据仍然很大。**Output compaction** 把长响应压成短 signature：

```text
many output bits over many cycles -> compactor -> final signature
```

- **Space compaction**：同一拍的多个输出合成少数几根线，例如 XOR tree；
- **Time compaction**：多拍响应持续累积到寄存器状态；
- **MISR（Multiple-Input Signature Register）**：多输入 LFSR，是 BIST 中最常用的时空压缩器。

理想无故障电路先离线算好一个 golden signature；测试结束后比较签名，相同则通过。风险叫 **aliasing**：坏响应压缩后恰好得到和好响应一样的 signature，导致漏检。对一个 $m$-bit、设计合理的线性 signature analyzer，随机错误的别名概率常近似为 $2^{-m}$。

这不是“压缩绝对不会丢信息”。它是在硬件、测试时间和极低漏检概率之间做工程取舍。另一个实际问题是 **X 值**：未知值进 XOR/MISR 会污染整个 signature；需要 X-masking、X-tolerant compactor 或控制 X 的来源。

### 6.8 Test compression：压缩的两端都要考虑

> **一句人话**：输入端把少量 ATE 数据解压成很多条 scan 数据，输出端再把大量响应压回少量数据，目的就是少传数据、少占引脚、缩短测试时间。

广义的 test compression 是减少 ATE 和芯片之间传输的数据量/时间：

```text
ATE 少量控制数据 -> on-chip decompressor -> 多条 scan chain
CUT 多条 scan-out -> on-chip compactor -> 少量 ATE 观测数据
```

不要把它和 BIST 混为一谈：

- **BIST**：模式发生器和响应分析器在芯片里，测试可高度自主；
- **test compression**：测试向量通常仍由 ATE 提供，只是在芯片端解压、压缩；
- 两者可以结合，例如 scan-based LBIST 也会使用压缩器。

### 6.9 CH6 考前压缩卡

> **一句人话**：这一节不讲新知识，而是把 CH6 压缩成“LFSR 出题、确定性模式补漏、MISR 压答案、注意 aliasing”这条复习主线。

```text
BIST = TPG 出题 + CUT 执行 + ORA 判题；ATE 只做启动和读取结果。
最大长度 n 级 LFSR 周期 = 2^n - 1；all-0 会锁死，不在该序列中。
穷举 = 2^n；伪穷举利用输出局部依赖，关键是 test signal inputs 的数量 p。
随机测不到的 fault = random-pattern-resistant；用 WRP 改变 0/1 概率。
混合 BIST：随机测大多数，reseeding 用 seed 生成 hard-pattern，bit flipping/fixing 把随机模式修正。
MISR 把多输出、多周期响应压成 signature；aliasing 是压缩后坏响应冒充好响应的低概率风险。
```

---

## CH7. Software-Based Self-Test 用软件测硬件

[[#目录|返回目录]]

### 7.0 按课件页码重新梳理

> 批注 PDF 有少量动画页重复，这里按课件页脚的正式页码 `x/81` 合并。每页先说“它在干什么”，再给最该记的结论。

#### P01/81 标题页

本章主题是 **Software-Based Self-Test**：不主要依赖 scan/ATE，而是让处理器运行软件来测试硬件。

#### P02/81 为什么要做 SBST

DFT、LBIST 会增加面积、布线和时序负担，芯片服役后又会老化；既然 SoC 已经有 CPU，就尽量让 CPU 兼任测试机。

#### P03/81 POST 是最熟悉的 SBST

电脑开机时检查 CPU、cache、DRAM，就是 Power-on Self-Test。人话：正式干活前，系统先给自己做一次体检。

#### P04/81 本章路线图

先讲随机软件测试和 memory pattern，再讲 constrained ATPG、VCM、pattern retargeting，最后落到 startup/online SBST。

#### P05/81 软件版 LBIST

CPU 通过总线写 CUT 输入、读 CUT 输出并判断结果，分别承担 TPG、ORA 和 ATE 的角色；测试走正常功能通路，也能以真实速度运行。

#### P06/81 MAC 例子与 MMIO

MAC 做乘加，`OP1/OP2/SUM` 被映射成地址。CPU 写操作数、读累加结果，就像访问普通内存一样控制硬件。

#### P07/81 MAC 软件测试的三步

RNG 产生操作数并写入 MAC，CPU 读回 `SUMcut`，再用软件计算 `SUMexpected`；两者不同就报错。

#### P08/81 MAC 测试代码

固定 seed 让随机序列可以复现；循环里既喂 MAC，也在软件中累计参考答案，最后只比较一次结果。

#### P09/81 RTL 级测试结果

寄存器层的故障容易被随机输入碰到，3 次 SBST 就达到 100% stuck-at 和 transition-delay coverage。

#### P10/81 Gate 级测试结果

深入到 MUL/ADD 门级后，随机测试要跑 50 次以上，仍有 88 个 fault 没测到。结论：随机测试便宜，但会卡在 random-resistant faults。

#### P11/81 软件版 MBIST

存储器结构规则，适合用 fill、checkerboard、March 等确定性 pattern；这些模式生成便宜，而且知道自己针对哪类故障。

#### P12/81 Register file 测试流程

逐个寄存器执行“保存旧值 → 写 pattern → 读回比较 → 恢复旧值”，避免测试破坏程序现场。

#### P13/81 Register file 汇编例子

给 `x1` 写全 1 来测 stuck-at-0，再用临时寄存器比较并恢复。关键是测试寄存器和保存现场的寄存器不能互相踩数据。

#### P14/81 Scratchpad 基本测试

整块 memory 写同一 pattern，再逐地址读回。因为内容会被覆盖，所以通常在 firmware 启动前的 POST 阶段做。

#### P15/81 Fill pattern

先写 `00` 再写 `FF`，检查每个 bit 能否保持 0 和 1，主要抓 stuck-at-0/1；简单，但对相邻 cell 互相影响不敏感。

#### P16/81 Checkerboard pattern

交替写 `55/AA`，让相邻 bit 取相反值，除了 stuck-at，也更容易暴露相邻线 bridge 或耦合问题。

#### P17/81 March pattern

按地址递增/递减执行规定的 read/write 序列，例如先全写 0，再向上读 0 写 1，再向下读 1 写 0；顺序本身就是测试的一部分。

#### P18/81 三类 pattern 对比

Fill 主要测 stuck-at，checkerboard 增强水平/垂直 bridge 检测，March 还能覆盖对角 bridge 和更复杂的动态/耦合故障。

#### P19/81 March 与基础故障

不同 March element 对应 stuck-at、slow-to-rise/fall、随机状态和地址译码故障。读法：先制造某状态，再执行会让故障暴露的读写动作。

#### P20/81 March 与读写扰动

这里列 incorrect read、read destructive、read disturb、write disturb。重点不是背表，而是懂：一次 read/write 也可能偷偷改变 cell。

#### P21/81 Disturb coupling faults

访问一个 aggressor cell 可能让另一个 victim cell 翻转；所以测试必须安排地址顺序，并在操作后检查邻近 cell。

#### P22/81 Static 与 inversion coupling

一个 cell 的固定状态或翻转可能强迫另一个 cell 保持/反相。单独测每个地址不够，必须测试 cell 之间的相互作用。

#### P23/81 March 算法的成本

MATS+、March C-/C+、March A/B 等覆盖能力不同，复杂度约为 `5N` 到 `22N`。序列越长通常覆盖越广，但测试时间越长。

#### P24/81 参考文献

这一页是 March memory test 的资料来源，没有新概念；复习时知道表格不是要求全部死背即可。

#### P25/81 回顾 SAT-based ATPG

好电路和坏电路共用输入，用 miter 强制至少一个输出不同；SAT 解就是能检测 fault 的测试 pattern。

#### P26/81 回顾 ILA 时间展开

把时序电路按 clock 复制成多个 timeframe，上一帧 next state 接下一帧 state，于是多周期问题变成大组合问题。

#### P27/81 BMC-based ATPG

先试在 `k` 个周期内能否让 miter 输出 1；找不到就增加 `k`。起始状态可以约束为 reset 后全 0，也可以是 All-X。

#### P28/81 为什么一定要加 constraints

CUT 嵌在系统里，CPU 不能随意控制所有输入、观察所有输出，实时系统还不能长时间停机；普通 ATPG 的自由输入假设不成立。

#### P29/81 用约束代替完整系统

不用把整个 SoC 都放进 ATPG，而是用 constraints 描述处理器、环境、总线协议以及 CUT 和其他模块的交互。

#### P30/81 VCM 的工作方式

VCM 观察 CUT 接口并输出“当前行为是否合法”；ATPG 强制 constraint outputs 为 1，于是生成的 pattern 只能落在合法行为里。

#### P31/81 VCM 看哪些信号

VCM 可以检查输入输出、bus protocol、系统交互，必要时也看内部 state。它本质上是 ATPG 前面的“规则裁判”。

#### P32/81 一个最小 VCM

例子规定 `read` 和 `write` 不能同时为 1，并要求至少发生一种 transaction；逻辑约束最终也会被编码进 SAT。

#### P33/81 强制 constraint output

把 VCM 输出固定为 1 后，非法组合会直接被排除。人话：solver 不是先乱找再检查，而是从一开始就不准走非法路线。

#### P34/81 Stateful VCM

有状态的 bus protocol/状态机也要随 CUT 一起展开；每个 timeframe 都检查约束，不能只保证最后一拍合法。

#### P35/81 MAC 的四类约束

Environment：不 reset；System：读写互斥、地址合法；ATPG：good/faulty 外部输入相同；Propagation：差异必须在 read 时从 data 出来。

#### P36/81 Environment/System 代码

Verilog VCM 直接写 `!reset`、读写互斥、地址范围和对齐要求。约束其实就是可综合的布尔规则。

#### P37/81 ATPG constraints 代码

good 和 faulty MAC 必须收到相同 reset/read/write/address/write_data，否则输出差异可能只是因为两边输入不同，不算检测 fault。

#### P38/81 Propagation constraints 代码

要求两边都在 read，并且 `read_data_good XOR read_data_faulty` 非零；这明确规定故障必须被软件真正读到。

#### P39/81 四个 timeframe 的例子

前两拍写 OP1/OP2，最后一拍读 SUM；所有合法性约束一直为 1，最后一拍 good/faulty read data 不同，说明 fault 被检测。

#### P40/81 从事务变成 C 测试

删掉不关心的 `X`，把写 OP1、写 OP2、读 SUM 直接翻译成几行 C。这里展示了 ATPG pattern 最终怎样落到软件。

#### P41/81 Full-scan、Sequential、Functional 对比

Functional ATPG 受约束最多，coverage 略低、生成更慢，但它产生的是软件真实可执行的 bus transactions。

#### P42/81 实时性问题

完整 stuck-at/transition SBST 约需 12.54 ms/18.71 ms，远大于目标 500 us；coverage 好不代表系统允许一次跑完。

#### P43/81 Chunking

把长 SBST 切成小于 100 us 的片段，与 firmware 交替运行。测试总量没少，只是避免一次阻塞系统太久。

#### P44/81 为什么要 retarget

整颗大芯片直接做 functional ATPG 太贵；先给底层唯一单元生成 pattern，再复用到同类实例，并逐层向上转换。

#### P45/81 Retargeting 的任务

既要在顶层找到输入，使子单元看到目标 pattern，又要让子单元的 fault effect 能传到顶层输出；这本身和 ATPG 一样难。

#### P46/81 Strategy 1：人工推理

看外围 MUX/逻辑，手工选择控制值，把目标数据送进子单元并把输出放行；结构简单时最快，但不易自动化。

#### P47/81 Strategy 2：子单元当 black box

BMC 只看外围电路，把子单元输入/输出当约束，自动寻找顶层序列；适合不想展开子单元内部的情况。

#### P48/81 Strategy 3：把子单元也放进 BMC

当外围 DFF 状态依赖子单元时，必须连子单元一起建模并生成 initialization sequence，模型更大但关系更准确。

#### P49/81 Gemmini 例子的层级路线

先测一个 MAC，再依次 retarget 到 PE、Tile、Mesh、Execute Controller，最后把控制器动作翻译成 RISC-V SBST。

#### P50/81 底层 MAC ATPG 结果

一个 MAC 有 2949 个 unique stuck-at faults，177 个 pattern 达到 99.15% coverage，说明底层小模块 ATPG 很快。

#### P51/81 MAC → PE

利用 Gemmini 的 weight-stationary/propagate 和 compute mode，先把 pattern 的 `c` 写进 C1，再施加 `a/b`，让 MAC 真正看到三元输入。

#### P52/81 验证 PE retargeting

高层 testbench 同时检查 PE 外部结果、MAC 实际输入和 MAC signature；第一拍初始化，第二拍才是正式测试。

#### P53/81 PE → Tile 的困难

Tile 中多个 PE 串接，C1 需要逐行 shift；同一入口不一定让所有 PE 同时看到相同 `b`，因此 retarget 并非简单复制。

#### P54/81 改进 PE 流程

明确拆成“初始化 C1 → compute 施加 pattern → propagate 移出结果”，让内部 MAC 的响应可被观察。

#### P55/81 改进 Tile 流程

对每一行完成 initialization、单拍 apply 和多拍 shift-out，再用 testbench 验证每个 PE 实际收到的值。

#### P56/81 Tile → Mesh

Mesh 多了 pipeline register，因此初始化和移出都要增加约 `n-1` 拍；还要处理接口位宽扩展。

#### P57/81 用累加构造 C1 pattern

若 `c` 不能直接写入，就先清零 C1，再用若干乘加把目标值“算出来”；这是功能通路受限时的典型 retarget 技巧。

#### P58/81 MAC 到 Mesh 的完整序列

清零/累加得到 `c`，单拍施加 `a/b`，再把结果 shift 到可见输出；测试 pattern 变成了一段有初始化和排空的时序程序。

#### P59/81 Mesh → Execute Controller

把底层动作包装成 CONFIG、PRELOAD、COMPUTE 等控制器命令，并把 A/B/C 矩阵放进 scratchpad。

#### P60/81 Controller → 软件

每个控制器 command 都有对应的 Gemmini C API，所以高层 pattern 可以机械地翻译成程序和静态矩阵数据。

#### P61/81 Gemmini 代码：配置

程序先分配 A/B/C 矩阵并配置 load/store/execute 模式；这些是让后续测试按预期通过 accelerator 的前提。

#### P62/81 Gemmini 代码：准备数据

把 pattern 展开成矩阵，必要时用多个 convolution，随后把 A/B/C 搬入 scratchpad。

#### P63/81 Gemmini 代码：执行和检查

所有 MAC 并行执行 pattern，结果搬回 CPU 后逐项和 expected 比较；任一不一致就返回 fault。

#### P64/81 Gemmini 结果

256 个 MAC、754944 个 unique stuck-at faults，177 个 pattern 达到 99.15% coverage；代码很小，主要空间花在静态 pattern 数据。

#### P65/81 处理器也能测试自己

指令本身就是 test pattern：取指和译码控制操作/寄存器/ALU，结果再传播到寄存器或总线。CPU 同时是测试者和 CUT。

#### P66/81 一条 ALU SBST 指令序列

给寄存器装载 `AA/BB` 后执行 add，若 ALU 某位 stuck-at-0，实际结果和 expected 不同；这条指令同时经过取指、译码、寄存器和 ALU。

#### P67/81 为什么通用约束难复用

不同 RISC-V core 的 pipeline、ISA、扩展和内部信号名不同，同一套直接绑定 RTL 信号的 VCM 无法搬到所有变体。

#### P68/81 Processor-specific VCM 的问题

VCM 需要观察 good/faulty processor 的 pipeline、register file 和 bus；若直接连内部信号，每换一个 core 就要重写。

#### P69/81 Mapping layer + Generic VCM

先把不同 core 的内部信号映射到统一接口，再复用 behavior/environment/ATPG/propagation constraints；变化留在 mapping 层。

#### P70/81 Signal mapping 代码

左边是统一语义，如 reset、run、PC、x1；右边把某个具体 RTL 的层级信号接进来。人话：先统一插头，再复用充电器。

#### P71/81 Startup SBST

开机时 firmware 尚未占用 data memory，测试可以把 fault effect 写进 memory signature，再由 firmware 初始化过程检查。

#### P72/81 Startup 的传播路径

指令从 IMEM 进入 decoder、register file、ALU，最后写到 DMEM；沿途模块都可能被这段测试覆盖。

#### P73/81 Startup 的约束

只允许合法指令、线性控制流、不碰 CSR；memory 地址不重复，避免已传播的差异被覆盖，最后从 bus transaction 提取线性 RISC-V 程序。

#### P74/81 Startup 实验结果

不同 core 的 coverage 约 79%-90%，程序有数千条指令；带乘法扩展的复杂 core 甚至会耗尽 solver 时间。

#### P75/81 Online SBST

系统空闲时测试，但不能破坏 firmware 状态；fault effect 被累积到指定 checksum register，空闲结束后由 firmware 检查。

#### P76/81 Online 的目标范围

instruction memory 提供 pattern，主要测试 register file 和 ALU，并把差异传到 checksum register，不依赖 data memory。

#### P77/81 Online 的约束和 signature

只允许算术指令、不访问 memory/CSR；用 XOR/XORI 累积差异并 rotate，模仿 CRC/MISR，减少多个错误互相抵消。

#### P78/81 Online coverage 结果

Register file 和 ALU coverage 很高，但 fetch、pipeline、memory 等部分很低，因为“不改系统状态”的限制让很多路径不可达。

#### P79/81 未检测原因拆分

大量 fault 是 `End Not Reached`：solver 在时限内找不到传播路径，不一定真的 untestable。要区分没找到、环境不允许和物理上不可测。

#### P80/81 FPGA 演示

在 FPGA 上让 firmware 周期运行 online SBST，并通过开关注入 stuck-at fault、屏幕/LED 显示结果，证明方法可以真实运行。

#### P81/81 参考文献

本页是 Startup/Online SBST 论文来源。整章最终主线：**CPU 产生合法软件行为，把 fault effect 传到 memory/register signature，再由软件检查。**

### 7.1 核心想法

> **一句人话**：SBST 不额外造一台硬件测试机，而是让 SoC 里现成的 CPU 运行测试程序，通过正常总线去刺激和检查其他硬件模块。

CH5/CH6 的 scan、TPG、ORA 都要加硬件，面积、布线和时序都有代价；而现代 SoC 里常常已经有处理器、总线、寄存器和存储器。**SBST（Software-Based Self-Test）**就把现成处理器当作测试机：软件产生输入、通过正常总线访问被测模块、读回结果并在软件中比较。

```text
Processor / test program = TPG + ATE
MMIO / system bus        = 测试通道
被测 IP                  = CUT
readback / checksum      = ORA
```

因此它能以模块真正的功能模式和工作频率运行，也适合产品服役后的 in-field test；代价是测试受软件可达操作和总线协议限制，不能像 scan 那样任意翻内部寄存器。

### 7.2 Random-based SBIST：软件版 LBIST

> **一句人话**：软件不断生成随机输入喂给硬件，同时自己计算正确答案并比较；实现简单，但对隐藏很深的随机难测故障不一定有效。

以 memory-mapped MAC 为例：CPU 向 `OP1`、`OP2` 寄存器写入伪随机操作数，读取 `SUM`；软件同时用参考运算得到 `expected`，最后比较。

```text
for each random pair (a, b):
    write OP1=a, OP2=b
    expected += a*b
actual = read SUM
assert actual == expected
```

它的优点是非常像真实使用场景，且无需额外 LBIST 硬件。缺点也直观：寄存器级的 stuck-at / transition fault 可能很快满覆盖，但门级深处仍可能剩下随机难测故障；不能因为软件随机跑了很多次就默认 100% 覆盖。

### 7.3 Pattern-based SBIST：软件版 MBIST

> **一句人话**：测试寄存器或存储器时，软件按计划写入特定数据、读回来比较，再根据需要恢复原内容，本质上是在做“写进去什么，就应该读回来什么”。

对 register file 或 SRAM，软件可以逐个地址/寄存器写入固定 pattern，再读回比对。例如测 `x1` 的 stuck-at-0：保存原值，写全 1，读回验证，再恢复原值。

对 scratchpad/DRAM，可跑 March 风格的读写序列来测 stuck-at、transition、地址译码和耦合故障。重点是：若存储器里放着正在运行的 firmware，不能随便全覆盖；所以全内存 MBIST 通常放在 **POST（上电自检）**、firmware 初始化之前执行。

### 7.4 为什么需要 constrained ATPG

> **一句人话**：普通 ATPG 可能给出电路上成立、现实中却无法执行的操作；constraints 就是告诉 solver，测试必须遵守总线协议、地址范围和处理器运行规则。

若用 ATPG 自动生成 SBST，solver 很容易找到“逻辑上能测到、现实中 CPU 根本做不出来”的向量，例如同时 `read=1` 和 `write=1`，或者访问未对齐、越界地址。故要给 ATPG 加 **constraints**。

**VCM（Validity Checker Module）**是一个附加逻辑模块，专门表达“什么样的输入/时序才是合法软件和合法系统会产生的”。它至少包含：

| 约束 | 例子 |
|---|---|
| Environment constraint | 系统在运行，`reset=0` |
| System / protocol constraint | 不能同时读写；地址必须对齐且落在设备地址范围 |
| ATPG constraint | fault-free 与 faulty 电路的外部输入必须相同 |
| Propagation constraint | 故障差异只能沿可被软件读取的 read data、寄存器或 memory 传播 |

对于时序协议，VCM 自己也可以有状态；和 CUT 一样按时间帧展开。这样 solver 找到的不只是“电路输入序列”，而是能翻译成一段真能执行的指令/总线事务。

### 7.5 Test pattern retargeting：从总线事务到指令

> **一句人话**：ATPG 找到的是接口上应该发生哪些读写，retargeting 再把这些抽象动作翻译成处理器真正能执行的汇编指令。

constrained ATPG 先在某个 IP 的接口上得到合法 bus transactions；**retargeting** 再把它们转成特定 CPU 的汇编指令。

难点是转换必须同时满足三层限制：ISA 能表达、处理器微架构会按预期执行、外设协议也合法。把这些限制都丢给 ATPG 会使模型变大、求解慢，但能避免生成“纸面可测、软件不可跑”的模式。

### 7.6 Generic VCM、Startup SBST 与 Online SBST

> **一句人话**：Generic VCM 提供一套可复用的合法行为规则；Startup SBST 可以在开机时大胆使用空闲内存，Online SBST 则必须在系统运行期间小心保护现场。

不同 RISC-V 内核内部信号名不同，因此课件用 mapping layer 把各内核的 PC、寄存器、pipeline 状态、指令/数据总线和 fault-propagation 点映射到统一 VCM 接口。约束本身可以复用，适配新核时主要改 mapping。

**Startup SBST**：开机、firmware 初始化前跑。此时 data memory 还没有重要数据，测试程序可以把故障影响传播到 memory，计算一个 signature，随后由 firmware 检查。它能覆盖 instruction interface、decoder、register file、ALU、data-memory interface 等路径。

**Online SBST**：系统空闲时跑，不能破坏 firmware 状态，因此限制更严：只运行允许的算术指令、不读写 data memory、不改 CSR。故障被累计到一个 checksum register；常用 XOR/XORI 和 rotate，把它做成类似 CRC/MISR 的软件 signature，降低多次错误直接抵消的风险。

```text
Startup：可以借用尚未使用的 memory，当作最终“成绩单”。
Online ：不能碰用户状态，只能把成绩单收在指定寄存器里。
```

### 7.7 CH7 考前压缩卡

> **一句人话**：这一节把 CH7 归结成“CPU 当测试机、VCM 限制合法行为、启动测试可用内存、在线测试要保护系统状态”。

```text
SBST = 用已有 CPU、总线和软件代替部分 DFT/BIST 硬件。
软件 LBIST：随机操作被测 IP，并用软件算 golden result；真实、便宜，但有随机难测 fault。
软件 MBIST：按 pattern 读写寄存器/存储器；全覆盖 memory 通常在 POST 做。
Constrained ATPG 必须服从 reset、bus protocol、地址、ISA 与 fault-propagation 的现实约束。
VCM = 把“合法行为”和“故障要可被软件看到”写给 ATPG 的模块。
Startup SBST 可把差异传到 data memory；online SBST 不改系统状态，传到 checksum register。
```

---

## CH8. Cell-Aware Testing 让 fault model 更接近真实缺陷

> 对应文件 `08-cellaware_annot.pdf`。该课件封面编号为 Chapter 9，主题为 Cell-Aware Testing；这里按文件夹顺序写作 CH8。

[[#目录|返回目录]]

### 8.0 按课件页码重新梳理

> 批注 PDF 为了展示 SPICE 缺陷注入过程，部分页码有多张动画步骤；下面按页脚的正式页码 `x/33` 合并重复动画页。

#### P01/33 标题页

本章主题是 **Cell-Aware Testing**。课件封面标为 Chapter 9，但这里按文件夹中的 08 课件整理。

#### P02/33 为什么需要 Cell-Aware

工艺越小，物理缺陷越容易出现；传统 stuck-at/transition-delay 模型越来越不能代表真实缺陷，坏芯片可能流到现场并产生 silent data corruption。

#### P03/33 动机参考

这一页用 field return 和 SDC 的资料说明后果：芯片不是“测试通过”就等于没有物理问题。

#### P04/33 本章路线图

先讲 Cell-Aware Testing 和 CLIC 的 cell-aware SBST，再讲如何从物理 defect 自动生成 cell-aware fault model。

#### P05/33 CAT 的基本定义

Cell-aware model 可以针对工艺、cell library 和测试目的调整；它只测试真实可能发生、并且值得测试的 physical defects。

#### P06/33 ATPG 如何使用 CAT model

ATPG 把一个坏 cell 当作黑盒：先在 cell 输入上制造缺陷需要的条件，再把 cell 输出的异常传播到芯片输出。

#### P07/33 UDFM 与 CTM

UDFM 直接列出某个 defect 的静态/转换测试条件；CTM 把一个 cell 的多个 defect 统一成可交给 ATPG 的行为表。重点是“故障规则描述 cell 行为”，不是简单固定一根网线。

#### P08/33 CLIC 的 cell-aware SBST

例子是 RISC-V Core Local Interrupt Controller：把 cell-aware fault model、constrained ATPG 和处理器可执行的总线事务结合起来。

#### P09/33 CLIC 测试接口与约束

增加 test mode/CSR 来控制 interrupt line；VCM 同时约束 bus protocol、interrupt acknowledge 延迟和测试接口不能乱用。

#### P10/33 用状态机表示 functional cell-aware test

静态测试表不够表达“先做什么、再等几拍、再做什么”，所以用可重入状态机连接不同 pattern，并允许某些输出为 X。

#### P11/33 CLIC 实验结果

Cell-aware pattern 生成时间明显更长，名义 coverage 可能比 stuck-at 低，但它覆盖的是更真实、数量更多的 fault model；加入 test interface 后 coverage 会提高。

#### P12/33 两种 pattern 交叉比较

cell-aware pattern 通常能抓住大部分 stuck-at；反过来，stuck-at pattern 未必能抓住 cell-aware fault。这正是“传统 coverage 高不等于物理 coverage 高”。

#### P13/33 CAT 参考文献 I

主要是 defect-oriented ATPG、industrial cell library 和 cell-aware test 的来源，没有新的计算内容。

#### P14/33 CAT 参考文献 II

补充 CLIC cell-aware SBST 等工作；复习时记住 CAT 既可以用于生产测试，也可以和 SBST 结合。

#### P15/33 从物理 defect 到高层 model

流程是：物理缺陷 → 电阻等 defect model → SPICE 得到模拟行为 → 转成 cell-aware fault model → 芯片级 ATPG。

#### P16/33 比较 good cell 和 defective cell

对同一组输入分别跑正常/缺陷 cell，只记录输出不同的情况。ATPG 后面只需要处理这些“确实会产生差异”的条件。

#### P17/33 SPICE testbench 结构

testbench 给 cell 输入、电源、负载和输入/输出电阻，观察每个端口的模拟电压；它比普通逻辑仿真多了电气细节。

#### P18/33 从模拟电压映射到 0/1/X

SPICE 输出是连续电压，测试模型要离散化：低于 LOW 算 0，高于 HIGH 算 1，中间不可靠的区域算 X。X 表示“不能放心当作逻辑值”。

#### P19/33 缺陷注入前的 inverter

先建立无缺陷 CMOS inverter 基准：PMOS 拉高、NMOS 拉低，记录正常输入到输出的行为，后面才能和 defect 版本比较。

#### P20/33 Stuck-at 缺陷注入

用很小的电阻把端口和 VDD/VSS 连接，模拟节点被强拉到电源或地；不同输入下如果输出偏离正常 inverter 表，就形成对应 cell-aware test condition。

#### P21/33 Bridge 缺陷注入

用低阻电阻连接两条本不该相连的相邻金属线。理论组合很多，但实际只从 layout 中挑相邻、工艺上真的可能短接的线对。

#### P22/33 Open 缺陷注入

在线路中串入很高的电阻，模拟金属开路或接触不良；信号可能变慢、漂浮或只在转换时出错，所以单纯静态 stuck-at 不一定抓得到。

#### P23/33 Transistor drive 缺陷

给导通晶体管串入中等电阻，表示“管子开了但推不动”；它常表现为电压幅度不足或转换变慢。

#### P24/33 Transistor leak 缺陷

给关断支路加入低阻泄漏，表示“管子关了还漏”；这类缺陷可能只在特定输入组合下扰动输出。

#### P25/33 Cell-aware model 生成案例

用 PySPICE 自动给 cell 注入缺陷并仿真，在 Nangate45 等 library 上并行处理；重点是自动化，而不是手工画一个 defect。

#### P26/33 Generic cell library

教学/benchmark library 只有少量组合和时序 cell，没有真实工艺背景，适合验证算法流程。

#### P27/33 Generic library 仿真量

静态和转换输入共约 396796 次 SPICE simulation，几小时才能完成；即使是小 library，cell-aware 也比 stuck-at 需要更多 pattern。

#### P28/33 Generic library 的行为结果

图示说明不同 defect 会在不同输入序列下暴露；所以 model 不是一个固定错误值，而是多个“输入条件 → 异常输出”的规则。

#### P29/33 Nangate45 library

半真实 45 nm 开源 library 有 105 个组合 cell、21 个时序 cell，规模明显比 generic library 大。

#### P30/33 Nangate45 仿真量

约 4060 万次 SPICE simulation，耗时约 6.49 天；这解释了为什么工业 CAT 需要并行计算、筛选 defect 和高效分析。

#### P31/33 Nangate45 结果图

结果再次强调：cell-aware defects 需要更多、更有针对性的 pattern，stuck-at test 不能直接替代它。

#### P32/33 参考文献 I

列出 defect-oriented test、cell-aware test 和 open-circuit exposure 的论文；没有新的公式。

#### P33/33 参考文献 II

补充 defect acceleration、SRAM periphery 和相关 cell-aware 工作。全章最该记住的是：**先用物理仿真建立模型，再用 ATPG/SBST 生成可执行测试。**

### 8.1 为什么 stuck-at / transition-delay 不够了

工艺缩小后，很多缺陷不再像“某根线永远是 0/1”这样干净。金属桥接、局部开路、晶体管驱动变弱、漏电，都可能只在特定输入转换、特定负载或特定时间点表现出来。

传统 fault model 是高层的、便于 ATPG 的近似；不是物理真相。模型太粗时，ATPG 的 fault coverage 再高，也可能有真实坏芯片漏到客户手里，表现为 field return 或更危险的 **Silent Data Corruption（静默数据错误）**。

### 8.2 Cell-aware 的一句话定义

**Cell-Aware Testing（CAT）**：从 standard-cell 内部可能出现的物理缺陷出发，先用晶体管级仿真得到“这个缺陷会让该 cell 在何种输入序列下输出异常”，再把这个行为交给芯片级 ATPG。

```text
physical defect -> defect model -> SPICE simulation of one cell
                -> cell-aware fault model -> gate-level ATPG -> test pattern
```

所以它不是把整颗芯片都拿去做 SPICE，而是“在 cell 层做物理细节，在 chip 层保留 ATPG 的效率”。

### 8.3 fault model 在这里长什么样

以一个 AND cell 为例，普通功能表只写 `IN1, IN2 -> OUT`。cell-aware model 额外写：某个 bridge/open/drive defect 存在时，哪些**静态输入**或**输入转换**会产生错误输出。

- **Static test**：例如输入为 `11`，无故障输出应为 1，缺陷后却为 0；
- **Transition test**：例如 `01 -> 00` 后，正确输出应及时变为 0，而缺陷让输出保持旧值、变慢或变成不确定；
- 输出可能是 `X`：代表电路模拟表明电压落在不可靠区。`X` 不能被稳定传播，ATPG 需要避开或特殊处理。

UDFM（User-Defined Fault Model）可把每个缺陷的测试条件直接列成表；CTM（Cell-Test Model）更像把多故障及其条件整合进同一个 cell 模型。考试里抓住本质即可：**ATPG 不再只替换一个 stuck-at 网线，而是把出问题的 cell 行为替换为一个更真实的黑盒规则。**

### 8.4 怎么从物理缺陷生成模型

通常假设一次只有一个缺陷，且只影响一个 cell。对 library 中每种 cell：

1. 把可能缺陷注入它的 SPICE netlist；
2. 对无缺陷 cell 和有缺陷 cell 施加静态/转换输入；
3. 比较输出逻辑值和时序；
4. 只记录两者不同的条件，形成 cell-aware fault model；
5. 芯片 ATPG 对每个实例应用该模型，justify cell 输入并把异常输出传播到可观察点。

课件里的典型 defect 注入方式是用电阻近似：

| 物理缺陷 | SPICE 中的简化 | 直觉 |
|---|---|---|
| stuck-at | 端口和 VDD/VSS 之间很低阻桥接 | 节点被强拉到电源或地 |
| bridging | 两根相邻金属线之间低阻 | 两个本不该相连的信号互相影响 |
| open | 金属段串入很高阻 | 信号看似连着，实际充放电很慢或漂浮 |
| transistor drive defect | 导通支路串入中等电阻 | 管子“开了但推不动” |
| transistor leak defect | 关断支路出现低阻泄漏 | 管子“关了还漏电/串扰” |

不是所有几何上可能的 bridge 都要枚举。理论组合会爆炸，实际只保留 layout 上相邻、工艺上有意义的线对。

### 8.5 CAT 的优势与成本

它的模型可以针对具体 **工艺、cell library、测试目的** 调整：production test、binning 或 burn-in 关注的缺陷不必完全一样；后续还可根据 yield 和 field-return 数据补充模型。

代价是模型生成很重。cell 数从教学 generic library 的十几个增至 Nangate45 这类库的一百多个组合 cell、二十多个时序 cell 时，SPICE 仿真量会从几十万级膨胀到数千万级，可能跑数天。芯片级 ATPG 也会有更多 fault、更多时序条件，因此运行更久、名义 fault coverage 反而可能更低。

这不是 CAT 变差了，而是它问的问题更严格：传统 stuck-at pattern 在 cell-aware 模型上的覆盖率并不高；反过来，cell-aware pattern 通常能覆盖大部分 stuck-at fault。前者说明“简单模型高分不代表真实缺陷高覆盖”。

### 8.6 Cell-aware SBST：把真实 cell 缺陷变成可运行软件测试

CAT 也能与 CH7 的 constrained SBST 结合。例如 RISC-V CLIC 的 cell-aware SBST：先给 CLIC 建 cell-aware model，再把 bus protocol、interrupt acknowledge 时间和测试接口控制写进 VCM，ATPG 最终输出可被处理器执行的事务/指令。

需要特别留意：一些 cell-aware pattern 的缺陷输出是 `X`，它们不能可靠地沿系统传播；而一个 cell 测试往往要求特定输入序列。因此课件用可重入状态机来表示模式前缀、不同模式之间的跳转和回到起点的路径，而不只是简单静态真值表。

### 8.7 CH8 考前压缩卡

```text
CAT 的目标：让 ATPG 的 high-level fault model 更贴近 cell 内物理缺陷。
流程：物理 defect -> 电阻式 defect model -> SPICE 比较 good/faulty cell -> cell-aware model -> ATPG。
常见缺陷：stuck-at、bridge、open、drive-weak、leak；尤其要测静态条件和输入转换。
ATPG 做的仍是 activation + propagation + observation，只是故障单元从“网线固定 0/1”升级为“某 cell 在某序列下的异常行为”。
好处：减少传统 fault model 的漏检风险；代价：模型、仿真和 ATPG 都更大、更慢，X 值也更难处理。
结论：stuck-at 高覆盖 != cell-aware 高覆盖；cell-aware pattern 通常也能覆盖大部分 stuck-at。
```
