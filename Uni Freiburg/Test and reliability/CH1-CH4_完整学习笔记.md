# Test and Reliability CH1-CH4 完整学习笔记

> 范围：只整理文件夹中的 CH1、CH2、CH3、CH4 课件内容。  
> 不包含：`ex*.pdf`、作业解析、exercise 解答。  
> 目标：用比较人话的方式，把概念、公式、算法和容易混淆的点串起来。

## 0. 四章在讲什么

这门课前四章其实是一条线：

| Chapter | 英文主题 | 中文主题 | 一句话 |
|---|---|---|---|
| CH1 | Introduction to Circuit Testing, Fault Collapsing | 电路测试基础与故障压缩 | 为什么要测、测什么、怎么定义故障和覆盖率 |
| CH2 | Fault Simulation | 故障仿真 | 给一组测试向量，算它们能测出哪些故障 |
| CH3 | Test Generation for Single Stuck-At Faults | 单固定故障的测试生成 | 自动找测试向量，让故障被激活、传播、观察 |
| CH4 | Boolean Satisfiability | 布尔可满足性与 SAT-based ATPG | 把测试生成翻译成 SAT，让 SAT solver 搜索测试 |

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
```

---

## CH1. Circuit Testing 基础与 Fault Collapsing

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

### 2.1 关键词中英文对照

| English | 中文 | 人话解释 |
|---|---|---|
| Fault Simulation | 故障仿真 | 算测试集能检测哪些故障 |
| Serial Fault Simulation | 串行故障仿真 | 一个故障一个故障地模拟，最直观也最慢 |
| Event-Driven Simulation | 事件驱动仿真 | 只重新计算值发生变化影响到的门 |
| Fault Dropping | 故障丢弃 | 故障一旦被测到，就从后续仿真中删掉 |
| Parallel Fault Simulation | 并行故障仿真 | 一个机器字里同时装 good circuit 和多个 faulty circuits |
| Parallel Pattern Simulation | 并行向量仿真 | 一个机器字里同时装多个测试向量 |
| Fault Insertion Mask | 故障注入掩码 | 指定哪些 bit 位置要被强制成 stuck-at 值 |
| Deductive Fault Simulation | 演绎故障仿真 | 每条线维护一个“哪些故障会让它不同”的集合 |
| Fault List | 故障列表 | 某条线或某个测试下相关的 fault 集合 |
| Active Faults | 活跃故障 | 当前测试下已经造成内部差异的故障 |

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

SAT 问题问：

```text
给定布尔公式 F，是否存在变量赋值 A，使得 A(F)=1？
```

若存在，公式 satisfiable，solver 输出一个 model。  
若不存在，公式 unsatisfiable。

SAT solver 很适合 ATPG，因为“是否存在一个测试向量检测故障”本质上也是存在性问题。

### 4.3 Miter Circuit

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

SAT solver 的赋值分两类：

1. decision assignment：solver 主动猜的值。
2. implied assignment：BCP 被迫推出的值。

每次主动猜值形成一个新的 decision level。由该决策推出的赋值也属于同一层。

如果在 level 0 就冲突，说明不需要任何猜测公式已经矛盾，结论是 UNSAT。

### 4.9 VSIDS 决策启发式

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

ATPG 往往要对很多 fault 逐个求解。增量 SAT 可以复用 solver 的内部状态：

```text
固定一大部分共享电路约束
每次只添加当前 fault 和输出差异约束
求解后再换下一组 assumptions/constraints
```

这样比每个 fault 都从空 solver 开始更高效。

### 4.14 为什么需要 D-Chain

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

## 5. 四章之间的核心关系

### 5.1 从“测得出”到“怎么找”

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

### 5.2 三个永远绕不开的动作

不管 D-Algorithm、PODEM 还是 SAT-based ATPG，都在做同一件事：

| 动作 | English | 说明 |
|---|---|---|
| 激活 | Activation | fault site 的 good value 要和 stuck-at value 相反 |
| 传播 | Propagation | 差异要穿过门，不能被 controlling value 遮住 |
| 观察 | Observation | 差异最终要到 primary output |

### 5.3 公式和算法速记

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

### 5.4 高频易错点

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

### 5.5 考前压缩版

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
```

