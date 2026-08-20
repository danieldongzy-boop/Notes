# Chapter 2 Fault Simulation 课件详细解读 / Detailed Lecture Guide

> 来源 / Source: `02-fsim_annot.pdf`  
> 课程 / Course: Test and Reliability, Summer Term 2026  
> 主题 / Topic: Fault Simulation（故障模拟）

## 1. 什么是故障模拟？ / What is fault simulation?

**中文**

故障模拟的输入是：

- 一个测试集 $T=\{t_1,t_2,\ldots,t_n\}$；
- 一个故障列表 $F=\{f_1,f_2,\ldots,f_m\}$；
- 一个无故障电路 $N$。

目标是找出测试集 $T$ 能检测到故障列表 $F$ 中的哪些故障。

若对某个测试向量 $t$，无故障电路与故障电路 $N_f$ 的至少一个主输出不同，则 $t$ 检测故障 $f$：

$$
N(t)\neq N_f(t)
$$

**English**

Fault simulation takes a test set, a fault list, and a circuit. Its purpose is to determine which faults are distinguished by the test set. A fault is detected if the good circuit and the corresponding faulty circuit produce different primary-output responses.

### 两种主要用途 / Two main uses

1. **测试生成之后 / After test generation**  
   计算测试集检测了多少故障，从而得到 fault coverage（故障覆盖率）。

2. **测试生成过程中 / During test generation**  
   每生成一个新向量，就判断它又检测了哪些尚未覆盖的故障。

Fault coverage 通常写成：

$$
FC=\frac{\text{number of detected faults}}{\text{number of target faults}}\times100\%
$$

The denominator must be stated clearly: it may refer to the original, EFC-collapsed, or another target fault list.

## 2. 最直接的方法为什么不可行？ / Why is the naive method impractical?

最直接的 serial fault simulation（串行故障模拟）步骤如下：

1. 在无故障电路 $N$ 上模拟测试集。
2. 对每个故障 $f$ 构造故障电路 $N_f$。
3. 在 $N_f$ 上再次模拟测试集。
4. 比较无故障与故障输出。
5. 对故障表中的每个故障重复。

The straightforward method simulates one good circuit and then repeats the entire simulation for every faulty circuit.

若：

- 电路有 $100\,000$ 个门；
- 至少有 $200\,000$ 个 stuck-at faults；
- 测试集有 $10\,000$ 个向量；

则粗略工作量为：

$$
200\,000\times10\,000\times100\,000
$$

这说明问题不在于一次逻辑仿真，而在于“故障数 × 测试数 × 电路规模”的乘积。

The challenge is the multiplicative combination of circuit size, number of faults, and number of patterns.

## 3. 故障检测的本质 / The essence of fault detection

一个 stuck-at fault 被检测通常需要三个条件：

1. **Fault activation / 故障激活**  
   无故障线值必须与 stuck-at 值相反。

2. **Fault propagation / 故障传播**  
   故障效应必须通过后续逻辑门传播。

3. **Fault observation / 故障观察**  
   差异必须到达主输出。

For example, a line stuck at 0 is activated only when its good value is 1. At an AND gate, the other inputs must normally be 1 to propagate the discrepancy.

## 4. Event-driven simulation / 事件驱动模拟

### 4.1 核心思想 / Core idea

连续测试向量通常只有少数输入位变化。若某条门输入没有变化，门输出往往无需重新计算。

Event-driven simulation therefore recomputes a line only when one of its driving lines has changed.

维护一个 event queue（事件队列）：

1. 比较新旧输入向量。
2. 把值发生变化的输入线加入队列。
3. 取出事件，重新计算其 fanout gates。
4. 只有当门输出真的改变时，才为后继门产生新事件。
5. 队列为空时，本次仿真稳定。

### 4.2 课件示例 / Lecture example

从 `1011` 切换到 `1010` 时，只有第 4 条输入线变化：

$$
1\rightarrow0
$$

因此先产生事件 `<4>`。该变化导致内部线 6 改变，再导致输出线 7 改变：

$$
\langle4\rangle\rightarrow\langle6\rangle\rightarrow\langle7\rangle
$$

The simulator evaluates only the affected cone instead of recomputing the entire circuit.

### 4.3 优点与限制 / Advantages and limitations

**优点 / Advantages**

- 输入变化少时非常有效。
- 大量未受影响的门被跳过。
- 适合门级仿真和连续向量序列。

**限制 / Limitations**

- 需要事件队列和电路拓扑管理。
- 若很多节点同时变化，收益下降。
- 与 word-parallel fault simulation 组合时，一个 bit 的变化可能迫使整个 word 对应的门重新计算。

## 5. Fault dropping / 故障丢弃

### 5.1 方法 / Method

对测试序列 $T=(t_1,t_2,\ldots,t_n)$：

1. 用 $t_1$ 模拟当前故障表。
2. 删除被 $t_1$ 检测的故障。
3. 仅对剩余故障模拟 $t_2$。
4. 重复直到测试结束或故障表为空。

Once a fault has been detected, it does not need to be simulated again when the goal is only fault coverage.

### 5.2 为什么有效？ / Why does it help?

设初始有 $m$ 个故障。如果早期向量检测了大量故障，后续向量只需处理较小的剩余集合。

The ordering of patterns can therefore affect simulation time even though it does not change final set coverage.

### 5.3 为什么故障诊断通常不使用 dropping？ / Why is dropping avoided in diagnosis?

Fault diagnosis 不只关心“是否检测”，还关心：

- 哪些向量检测某故障；
- 哪些输出发生差异；
- 不同故障的 failure signature 是否相同。

若第一次检测后立刻删除故障，就会丢失后续诊断信息。

Diagnosis needs the complete response signature of each fault, so early fault dropping is usually inappropriate.

## 6. 两种 word-level 并行方向 / Two forms of word-level parallelism

现代 CPU 的一个机器字有 $W$ 个 bit，例如 $W=64$。一次位运算能同时处理 $W$ 个相互独立的布尔位置。

A machine-word operation is genuine SIMD-like parallel work at the bit level.

### 6.1 Parallel fault simulation / 并行故障模拟

- 一次处理一个测试向量。
- 一个 bit 保存无故障电路。
- 其余 $W-1$ 个 bit 保存不同故障电路。

因此一个 64-bit word 可同时模拟：

$$
1\text{ good circuit}+63\text{ faulty circuits}
$$

### 6.2 Parallel pattern simulation / 并行向量模拟

- 一次处理一个电路。
- word 中不同 bit 保存不同测试向量的值。
- 同一门的 word-level operation 同时计算多个 pattern。

Parallel pattern simulation is useful only when several patterns are available at the same time.

### 6.3 两者不要混淆 / Do not confuse them

| Method | Each bit represents / 每个 bit 表示 | Fixed item / 固定对象 |
|---|---|---|
| Parallel fault simulation | 一个故障电路 / One faulty circuit | 一个测试向量 / One pattern |
| Parallel pattern simulation | 一个测试向量 / One pattern | 一个电路模型 / One circuit |

## 7. Parallel fault simulation 的数据编码

设 word 的 bit 排列为：

```text
[fault-free, f1, f2, ..., fW-1]
```

对于某一条线 $x$，word $v_x$ 的每个 bit 是该线在相应电路实例中的逻辑值。

For a two-input AND gate:

$$
v_z=v_x\mathbin{\&}v_y
$$

这里 `&` 是机器字逐位 AND。一次 CPU 指令同时计算所有 packed circuits。

例如：

```text
v_x = 0011...
v_y = 0101...
v_z = 0001...
```

每一列彼此独立，相当于同时执行许多个单 bit AND。

## 8. 输入 word 如何初始化？ / How are input words initialized?

对当前测试向量 $t=a_1a_2\ldots a_n$，在尚未注入输入故障前，第 $j$ 个主输入的所有 bit 都复制 $a_j$：

$$
v_{PI_j}=a_ja_j\ldots a_j
$$

例如测试值为 0，则初始 word 是全 0；测试值为 1，则初始 word 是全 1。

Fault-specific bit positions are then overwritten by fault insertion masks.

## 9. Fault insertion mask / 故障注入掩码

### 9.1 单个故障的选择公式 / Single-fault selection formula

令 $v_{ij}$ 表示 line $i$ 在故障电路 $N_{f_j}$ 中的正常计算值。若故障 $j$ 位于 line $i$ 且 stuck-at 值为 $c$，必须把该 bit 强制为 $c$。

定义：

$$
M_{ij}=
\begin{cases}
1,&i=j\\
0,&i\neq j
\end{cases}
$$

故障注入后：

$$
v_{ij}^{new}=v_{ij}\cdot\overline{M_{ij}}+M_{ij}\cdot c
$$

This is a Boolean multiplexer: keep the computed value when the mask is 0 and select the stuck-at value when the mask is 1.

### 9.2 同时注入 $W$ 个 bit / Word-level insertion

对每条 line $i$ 预先建立两个 word：

- $I_i$：哪些 bit 位置需要在线 $i$ 注入故障；
- $S_i$：这些位置对应的 stuck-at 值。

注入公式：

$$
v_i^{new}=(v_i\mathbin{\&}\overline{I_i})\mathbin{|}(I_i\mathbin{\&}S_i)
$$

等价写法：

```c
v_i = (v_i & ~I_i) | (I_i & S_i);
```

### 9.3 为什么需要两个 mask？ / Why are two masks needed?

$I_i$ 只说明“在哪里覆盖”，不说明覆盖成 0 还是 1。$S_i$ 提供被选中位置的目标 stuck-at 值。

$I_i$ is the selection mask; $S_i$ is the data word selected at the faulty positions.

### 9.4 例子 / Example

若 packed faults 包含 `X/1`, `Y/1`, `Z/0`, `Z/1`，则在计算 line $Z$ 后：

- $I_Z$ 在 `Z/0` 与 `Z/1` 两列为 1；
- $S_Z$ 在 `Z/0` 列为 0，在 `Z/1` 列为 1；
- 其他列保留正常计算值。

The two Z-fault columns are overwritten while all unrelated columns pass through unchanged.

## 10. Parallel fault simulation 完整流程 / Complete procedure

1. 选择最多 $W-1$ 个故障，与无故障电路打包。
2. 把测试向量的每个 PI 值复制到对应 input word。
3. 若 PI 本身有 packed fault，应用其注入 mask。
4. 按拓扑顺序计算每个门的 output word。
5. 在相应 line 上应用 $I_i$ 与 $S_i$。
6. 把 fanout stem word 复制到 branches，并在 branch 上注入 branch fault。
7. 比较每个主输出 word 与 fault-free bit。
8. 任一输出 bit 与 good bit 不同，则相应故障被检测。
9. 可对已检测故障执行 fault dropping。
10. 装入下一批故障，直到故障表完成。

## 11. 并行模拟的优点与限制 / Advantages and limitations

### 优点 / Advantage

理想情况下，故障模拟时间约缩短 $W$ 倍：

$$
T_{parallel}\approx\frac{T_{serial}}{W}
$$

实际速度提升通常小于 $W$，因为还存在 packing、mask、输出检查和批次切换开销。

### 限制 / Limitations

1. **Event-driven 能力受限**  
   word 中任一故障电路的节点改变，就要对整个 word 执行门运算。

2. **Packing/unpacking overhead**  
   构造 word、提取单个 fault bit 都需要额外操作。

3. **Word capacity**  
   一批只能容纳 $W-1$ 个故障。

4. **不同故障活动区域不同**  
   某些故障只影响很小逻辑锥，但 packed simulation 仍按统一门顺序处理。

## 12. Deductive fault simulation / 演绎故障模拟

### 12.1 核心思想 / Core idea

演绎故障模拟一次处理一个测试向量，但不显式模拟每个故障电路。它：

1. 先做一次无故障逻辑仿真；
2. 为每条 line $i$ 维护一个 fault list $L_i$；
3. 用集合运算沿门传播故障列表。

$L_i$ 的含义是：

$$
L_i=\{f\mid \text{line }i\text{ 在 }N\text{ 与 }N_f\text{ 中取值不同}\}
$$

For a primary output, $L_i$ is exactly the set of faults detected at that output for the current binary test pattern.

### 12.2 Primary input list / 主输入故障表

若主输入 line $i$ 的正确值为 $a$，只有相反的 stuck-at fault 会在该线上产生差异：

$$
L_i=\{i/\overline a\}
$$

Examples:

$$
i=0\Rightarrow L_i=\{i/1\}
$$

$$
i=1\Rightarrow L_i=\{i/0\}
$$

### 12.3 每条门输出还要加入本地故障 / Add the local output fault

若门输出 $z$ 的 good value 为 $v_z$，本地可激活故障是：

$$
z/\overline{v_z}
$$

它必须加入 $L_z$。

## 13. AND 门的演绎传播规则 / Deductive rules for an AND gate

### 13.1 输出为 1 / Output is 1

若 AND 的全部输入为 1，任一输入差异都可能把输出变成 0，因此：

$$
L_Z=L_A\cup L_B\cup\{Z/0\}
$$

For an $n$-input AND with all inputs equal to 1:

$$
L_Z=\bigcup_r L_r\cup\{Z/0\}
$$

### 13.2 一个输入为 0，另一个为 1 / One controlling input

若 $A=0,B=1,Z=0$，要改变输出：

- 故障必须改变控制输入 $A$；
- 同一故障不能同时改变 $B$，否则结果可能仍被遮蔽或恢复。

因此：

$$
L_Z=(L_A-L_B)\cup\{Z/1\}
$$

The set difference removes faults whose effects also occur on the non-controlling path and cancel or mask the intended propagation.

### 13.3 多个输入为 0 / Multiple controlling inputs

若三输入 AND 中 $A=0,B=0,C=1$，输出要从 0 变 1，同一个故障必须同时改变两个控制输入，并且不能破坏 $C=1$：

$$
L_Z=((L_A\cap L_B)-L_C)\cup\{Z/1\}
$$

一般规则：

1. 对所有 controlling-value inputs 的列表取交集；
2. 减去所有 non-controlling inputs 的列表并集；
3. 加入本地输出故障。

For an AND gate with zero-input set $C_0$ and one-input set $C_1$:

$$
L_Z=
\left(
\bigcap_{r\in C_0}L_r
-
\bigcup_{s\in C_1}L_s
\right)
\cup\{Z/1\}
$$

### 13.4 NAND 门 / NAND gate

反相不会改变“哪些故障导致差异”，所以输入列表组合规则与 AND core 相同；但本地输出 stuck-at 极性由实际 NAND 输出决定。

Inversion preserves discrepancy membership, while the local output fault is always the complement of the good NAND output.

## 14. OR、NOR 与 NOT 的规则 / Rules for OR, NOR, and NOT

OR 可通过 duality 从 AND 得到：

- OR 输出为 0，即所有输入为 0：取输入 fault lists 的并集。
- OR 输出为 1：对值为 1 的 controlling inputs 取交集，再减去值为 0 的输入列表。

For an inverter:

$$
L_Z=L_A\cup\{Z/\overline{v_Z}\}
$$

The input discrepancy always propagates through a NOT gate.

## 15. Reconvergent fanout / 重汇合扇出

重汇合是演绎故障模拟最容易出错的地方。

A fault may travel along multiple branches and reconverge at a downstream gate.

不能简单认为：

$$
L_Z=L_A\cup L_B
$$

因为同一个故障可能：

- 同时出现在多个 controlling inputs 上，因此必须通过交集才能改变输出；
- 同时出现在控制与非控制路径上，因此需要集合差消除；
- 在不同路径产生相互抵消的逻辑效果。

The set operations encode whether one physical fault can produce the simultaneous input changes required at the reconvergent gate.

## 16. Parallel 与 deductive 的关系 / Relationship between parallel and deductive simulation

Parallel fault simulation 为每条 line 存储一个 dense bit vector：

```text
fault-free | f1 | f2 | f3 | ...
```

Deductive simulation 存储 sparse active-fault set：

```text
LZ = {faults that currently invert Z}
```

两者表达的是相同信息：

- bit vector 适合故障很多且机器字并行有效的情况；
- fault list 适合当前向量只激活少量故障的情况。

Deductive simulation can reduce storage and work by retaining only active faults, but set operations may become expensive when lists grow large.

## 17. 时序电路中的故障模拟 / Fault simulation of sequential circuits

对测试序列：

$$
T=(t_1,t_2,\ldots,t_n)
$$

下一向量的仿真依赖当前向量产生的 next state：

$$
s_{i+1}=\delta(s_i,t_i)
$$

因此不能在不知道 $t_i$ 结果时完整模拟 $t_{i+1}$。

Patterns are temporally dependent through the state elements, so arbitrary pattern-parallel simulation is restricted.

但仍可：

- 对同一时刻的多个故障电路做 parallel fault simulation；
- 对某些 single-fault propagation 组织并行计算；
- 使用 scan 把时序问题转化成组合 core 的测试问题。

## 18. 工具与现代实现 / Tools and modern implementations

课件列出的历史或商业工具包括：

- Differential fault simulator；
- PARIS；
- Fastscan；
- Tetramax；
- Verifault。

现代实现还会利用：

- 64/128/256-bit vector instructions；
- multicore parallelism；
- GPGPU；
- 更紧凑的 AIG/netlist representation；
- cache-friendly fault batching。

The underlying ideas remain the same: avoid redundant gate evaluation, drop completed work, and exploit data-level parallelism.

## 19. 方法对比 / Comparison of methods

| Method | Main idea | Strength | Weakness |
|---|---|---|---|
| Serial | 每故障单独模拟 / Simulate each fault separately | 简单、准确 / Simple | 极慢 / Very slow |
| Event-driven | 只计算变化锥 / Evaluate changed cone | 输入变化少时快 | 事件管理开销 |
| Fault dropping | 检出后删除 / Remove detected faults | 后期故障表小 | 不适合诊断 |
| Parallel fault | word 的 bit 表示故障电路 | 机器字级并行 | packing 与 event-driven 冲突 |
| Parallel pattern | bit 表示测试向量 | 同时算多个 pattern | 时序依赖时受限 |
| Deductive | 每条线传播 fault set | 一次处理全部故障 | 集合可能膨胀 |

## 20. 解题模板 / Problem-solving templates

### Parallel fault simulation

1. 固定 bit-column 顺序。
2. 给 PI 创建重复值 word。
3. 按拓扑顺序计算门输出。
4. 到故障位置时覆盖对应 bit。
5. 比较 PO word 与 good column。

### Deductive fault simulation

1. 先计算所有 good values。
2. PI：加入相反 stuck-at fault。
3. Fanout branch：复制 stem list，再加入 branch 本地故障。
4. 根据门输入值选择 union、intersection、difference。
5. 加入 output local fault。
6. 在 PO 读取 detected fault list。

## 21. 高频易错点 / Common mistakes

1. **把 parallel fault 与 parallel pattern 混淆。**
2. **忘记 good circuit 也占一个 bit。**
3. **故障注入后又被正常门值覆盖。**  
   Injection must occur at the faulty line after its normal value is computed.
4. **使用逻辑 `&&` 代替逐位 `&`。**
5. **演绎模拟中只做 union。**  
   Reconvergence often requires intersection and set difference.
6. **忘记每条线的本地 opposite stuck-at fault。**
7. **把 stem 与 branch 当作同一 fault site。**
8. **诊断任务仍然 fault dropping，导致 signature 丢失。**

## 22. 一页复习 / One-page recap

**中文**

- Fault simulation：找出测试集检测的故障。
- Event-driven：只重新计算受输入变化影响的逻辑锥。
- Fault dropping：故障一旦检出便从覆盖仿真中删除。
- Parallel fault simulation：一个 word 同时表示 good circuit 与多个 faulty circuits。
- Fault mask 公式：

$$
v_i^{new}=(v_i\mathbin{\&}\overline{I_i})\mathbin{|}(I_i\mathbin{\&}S_i)
$$

- Deductive simulation：每条线维护导致该线与 good circuit 不同的 fault set。
- AND 全 1 用 union；多个控制 0 用 intersection；非控制路径通过 set difference 排除。
- PO 的 fault list 就是该向量检测的故障集合。

**English**

- Event-driven simulation skips unaffected gates.
- Fault dropping removes already detected faults.
- Parallel simulation packs circuits or patterns into machine words.
- Deductive simulation propagates active-fault sets.
- Reconvergent fanout requires careful intersection and difference operations.

