# Fault Collapsing 课件详细解读 / Detailed Lecture Guide

> 来源 / Source: `01c-fault_collapse_annot.pdf`, Test and Reliability, Chapter 1c, Summer Term 2026  
> 目标 / Goal: 理解为什么要做故障折叠、EFC 与 DFC 的区别、扇出带来的问题、简单算法以及 Checkpoint Theorem。

## 1. 本章在解决什么问题？ / What problem does this chapter solve?

**中文**

数字电路采用 single stuck-at fault model（单固定故障模型）时，每一条可观察的信号线通常有两种故障：

- `x/0`：信号 `x` 永久固定为 0，即 stuck-at-0。
- `x/1`：信号 `x` 永久固定为 1，即 stuck-at-1。

若电路有很多信号线，原始故障表会非常大。故障模拟需要把测试向量施加到许多故障电路上，ATPG（Automatic Test Pattern Generation，自动测试向量生成）也需要逐一处理目标故障。因此，故障数量直接影响计算时间和测试集大小。

Fault collapsing 的思想是：不要机械地保留所有故障，而是利用故障之间的关系，仅保留有代表性的故障。只要折叠过程不漏掉必须测试的行为，就可以减少仿真和 ATPG 的工作量。

**English**

Under the single stuck-at fault model, every relevant signal location normally has two faults:

- `x/0`: signal `x` is permanently stuck at logic 0.
- `x/1`: signal `x` is permanently stuck at logic 1.

For a large circuit, the raw fault list becomes very large. Fault simulation must evaluate many faulty circuits, and ATPG must generate patterns for many target faults. Fault collapsing exploits relationships among faults and keeps only representative faults, reducing simulation time, ATPG effort, and often the number of generated patterns.

## 2. 基础术语 / Basic terminology

### 2.1 控制值与非控制值 / Controlling and non-controlling values

| Gate / 门 | Controlling value / 控制值 | Non-controlling value / 非控制值 | 原因 / Reason |
|---|---:|---:|---|
| AND / NAND | 0 | 1 | 任一输入为 0 就控制 AND 核心输出为 0。/ Any 0 forces the AND core to 0. |
| OR / NOR | 1 | 0 | 任一输入为 1 就控制 OR 核心输出为 1。/ Any 1 forces the OR core to 1. |

**中文**

传播某条输入上的故障效应时，其他输入一般要设置为非控制值。例如，要让 AND 门输入 `a` 的差异到达输出，其余输入必须为 1；否则另一个 0 会遮蔽 `a` 的影响。

**English**

To propagate a fault effect from one gate input to the output, the other inputs are normally assigned the non-controlling value. For an AND gate, the side inputs must be 1; otherwise a side-input 0 masks the effect.

### 2.2 检测集合 / Detecting set

令 $$T_f$$ 表示能够检测故障 $$f$$ 的所有输入向量组成的集合。

Let $$T_f$$ be the set of all input patterns that detect fault $$f$$.

一个向量检测故障需要同时满足：

1. **激活 / Sensitization**：无故障值必须与 stuck-at 值相反。
2. **传播 / Propagation**：故障效应必须沿至少一条未被控制值遮蔽的路径到达主输出。
3. **观察 / Observation**：无故障输出与故障输出不同。

A test detects a fault only if it activates the fault, propagates the resulting discrepancy, and makes the good and faulty primary-output values different.

## 3. 等价故障 / Equivalent faults

### 3.1 定义 / Definition

**中文**

若任意测试向量都无法区分故障 $$f$$ 与 $$g$$，则二者功能等价：

$$
f \equiv g \iff \forall t,\ C_f(t)=C_g(t)
$$

等价故障具有完全相同的检测集合：$$T_f=T_g$$。因此，一个等价类只需保留一个代表故障。

**English**

Faults $$f$$ and $$g$$ are functionally equivalent if no input pattern can distinguish their faulty circuits:

$$
f \equiv g \iff \forall t,\ C_f(t)=C_g(t)
$$

They have identical detecting sets, $$T_f=T_g$$, so only one representative from each equivalence class is required.

### 3.2 为什么它是等价关系？ / Why is it an equivalence relation?

- Reflexive / 自反：$$f\equiv f$$。
- Symmetric / 对称：若 $$f\equiv g$$，则 $$g\equiv f$$。
- Transitive / 传递：若 $$f\equiv g$$ 且 $$g\equiv h$$，则 $$f\equiv h$$。

这些性质允许把故障划分成互不重叠的 equivalence classes（等价类）。

These properties partition the original fault list into disjoint equivalence classes.

## 4. EFC：等价故障折叠 / Equivalent Fault Collapsing

### 4.1 基本门的等价关系 / Equivalence relations for elementary gates

设两输入 AND 门输出为 $$z=xy$$：

$$
x/0 \equiv y/0 \equiv z/0
$$

因为这三个故障都会使输出在相关情况下表现为 0。`x/1`、`y/1` 和 `z/1` 通常不彼此等价。

For a two-input AND gate $$z=xy$$, the two input stuck-at-0 faults and the output stuck-at-0 fault are equivalent.

设两输入 OR 门输出为 $$z=x+y$$：

$$
x/1 \equiv y/1 \equiv z/1
$$

For a two-input OR gate, the two input stuck-at-1 faults and the output stuck-at-1 fault are equivalent.

反相门满足：

$$
x/0 \equiv z/1,\qquad x/1 \equiv z/0
$$

For an inverter, an input stuck-at-0 is equivalent to an output stuck-at-1, and vice versa.

NAND 与 NOR 可以看成 AND/OR 后接反相，因此对应的输出 stuck-at 极性会翻转。

NAND and NOR follow the same core-gate logic, with the output stuck-at polarity inverted.

### 4.2 两输入门为什么从 6 个故障降到 4 个？ / Why does EFC reduce six faults to four?

一个两输入门有两个输入和一个输出，因此原始共有 $$3\times2=6$$ 个 stuck-at faults。对 AND/OR 族基本门，三个控制值相关故障可合并成一个等价类，另外三个故障各自保留，所以剩 4 个代表。

A two-input gate has six raw stuck-at faults. The three equivalent controlling-value-related faults collapse into one class; the other three remain separate, leaving four representatives.

EFC 代表的选择不唯一。选择哪个成员作为代表不重要，重要的是保存“该代表对应哪些原始故障”。

The representative is not unique. What matters is retaining the mapping from each representative to all original faults in its class.

## 5. 功能分析与结构分析 / Functional versus structural analysis

### 5.1 Functional analysis / 功能分析

**中文**

构造两个故障电路，证明它们对所有输入都有相同输出。最直接的方法是穷举输入并比较输出，但复杂度通常过高。

**English**

Construct the two faulty circuits and prove that their outputs agree for every input. Exhaustive enumeration is exact but generally too expensive.

### 5.2 Structural analysis / 结构分析

**中文**

依据门类型、连接方式和局部规则识别等价关系，不需要施加测试向量。它速度快，但可能找不到所有功能等价关系，因此通常是不完全但实用的方法。

**English**

Structural analysis derives equivalences from gate types and connectivity without applying patterns. It is fast, although incomplete: some functional equivalences may remain undiscovered.

本课件选择线性时间的结构算法，因为 fault collapsing 本身若太慢，就失去了预处理的意义。

The lecture favors a linear-time structural method because collapsing is useful only when its own cost remains low.

## 6. 无扇出电路中的 EFC / EFC in fanout-free circuits

Fanout-free circuit 指每条信号只驱动一个后继门，整体呈树状。

A fanout-free circuit is tree-shaped: each signal drives only one successor gate.

课件给出的保留规则可以理解为：

1. 每个主输出保留 `s-a-0` 和 `s-a-1`。
2. AND/NAND 的每个门输入保留非控制值故障 `s-a-1`。
3. OR/NOR 的每个门输入保留非控制值故障 `s-a-0`。

The retained list contains both faults at every primary output and one non-controlling-value fault at each gate input.

### 为什么规则有效？ / Why does the rule work?

从电路叶端向输出走：

- AND 输入 `s-a-0` 可以与该门相应的输出故障合并。
- OR 输入 `s-a-1` 可以与该门相应的输出故障合并。
- 这种等价关系可沿无扇出路径传递，直到某个保留位置。

Working from the leaves toward the output, controlling-value input faults collapse with the corresponding gate-output fault. In a fanout-free path, these equivalences can be carried forward until a retained location is reached.

## 7. 扇出为什么困难？ / Why do fanouts make collapsing harder?

### 7.1 Stem 与 branches / 扇出干与分支

一条信号分叉前的位置叫 fanout stem，分叉后的每条路径叫 fanout branch。

The common signal before a split is the fanout stem; each path after the split is a fanout branch.

**关键区别 / Key distinction**

- Stem 故障会同时影响所有分支。
- Branch 故障只影响一个分支。

A stem fault affects every branch simultaneously, whereas a branch fault affects only one branch. Therefore, stem and branch faults are not automatically equivalent.

在重汇合扇出中，不同分支上的故障效应可能互相遮蔽、强化或在不同输出上出现。仅靠单门局部规则无法保证找到正确的全部等价关系。

In reconvergent fanout, branch effects may be masked or may interact after reconvergence, so local gate rules alone are insufficient for exact collapsing.

### 7.2 实用近似 / Practical approximation

课件采用如下方法：

1. 在每个 fanout stem 处切分电路。
2. 把各部分看成独立的 fanout-free subcircuits。
3. 把 stem 当作前一子电路的主输出，因此保留 stem 的两种故障。
4. 各 branch 作为下一子电路的输入，分支故障不跨分支随意折叠。

The circuit is partitioned into fanout-free regions. Each stem is treated as a pseudo-primary output and each branch as an independent input to the next region.

结果通常不是最小故障集，但算法为线性时间，而且不会因为激进折叠而漏掉故障。

The result may be non-minimal, but it is linear-time and conservative.

## 8. SIMPLE_EFC 算法解读 / Understanding SIMPLE_EFC

课件伪代码可整理为以下思路：

```text
fault_list = empty
for each PI, PO, and gate:
    keep both faults at every PO
    keep both faults at every fanout stem
    for AND/NAND:
        keep s-a-1 on each input
    for OR/NOR:
        keep s-a-0 on each input
return fault_list
```

**中文解读**

- PO 的两种故障必须能被覆盖，因为没有后级位置可用来代表它们。
- Fanout stem 的两种故障都保留，因为 stem 与 branch 的行为可能不同。
- 门输入仅保留非控制值故障；控制值故障由结构上的等价代表覆盖。
- 反相器可以通过输入/输出极性映射直接消去，不必额外增加代表。

**English interpretation**

- Both faults at a primary output must remain because no downstream site can represent them.
- Both faults at a fanout stem remain because a stem fault may differ from every individual branch fault.
- Only the non-controlling stuck-at value is retained at elementary-gate inputs.
- Inverter faults can be mapped across the inverter with reversed polarity.

### 算法代价 / Complexity

每个门、PI 和 PO 只访问常数次，因此时间复杂度为：

$$
O(|V|+|E|)
$$

Each gate and connection is processed a constant number of times, so the algorithm is linear in netlist size.

## 9. SIMPLE_EFC 的两个问题 / Two limitations of SIMPLE_EFC

### 9.1 结果不保证最优 / The result is not guaranteed to be minimal

由于不进行昂贵的 stem analysis，算法可能同时保留实际上等价的两个故障。这不会造成覆盖漏洞，但会少获得一些压缩收益。

Because stem analysis is omitted, two faults that are actually equivalent may both remain. This reduces compression efficiency but does not create a coverage hole.

### 9.2 丢失原始故障映射 / Loss of the original-fault mapping

若只输出代表故障列表，却不记录每个代表的 equivalence class，便无法准确从 collapsed coverage 换算 uncollapsed coverage。

If the algorithm outputs only representatives and discards class membership, collapsed fault coverage cannot be converted accurately into uncollapsed fault coverage.

例如检测到 3 个代表，不一定只代表 3 个原始故障；其中一个代表可能对应 4 个原始故障。

Detecting three representatives may correspond to more than three raw faults because one representative can stand for an entire class.

**实现建议 / Implementation note**

实际工具应保存：

```text
representative -> {all equivalent original faults}
```

并记录等价类大小，用于报告原始故障覆盖率。

## 10. XOR 门为什么特殊？ / Why are XOR gates special?

XOR 没有像 AND/OR 那样的单一控制值：

$$
x\oplus 0=x,\qquad x\oplus1=\overline{x}
$$

任一输入的 0 或 1 都不会恒定地控制输出。因此，AND/OR 的“控制值输入故障与输出故障等价”规则不能直接套用。

XOR has no controlling input value. Neither 0 nor 1 independently forces a constant output, so the elementary AND/OR collapsing rule cannot be applied directly.

XOR 的等价关系需要按具体结构或通过更强的功能分析确定。

XOR equivalences require structure-specific reasoning or stronger functional analysis.

## 11. 故障支配 / Fault dominance

### 11.1 定义 / Definition

课件定义：若

$$
T_f \supseteq T_g
$$

则故障 $$f$$ dominates（支配）故障 $$g$$。

Fault $$f$$ dominates $$g$$ when every test that detects $$g$$ also detects $$f$$.

注意方向：

- $$f$$ 的检测集合更大，$$f$$ 是 dominating fault。
- $$g$$ 更难检测，$$g$$ 是 dominated fault。
- 为了 ATPG，只需针对更难检测的 $$g$$ 生成测试；检测 $$g$$ 时自然也检测 $$f$$。

The dominated fault has the smaller detecting set and is harder to detect. Generating a test for it automatically covers the dominating fault, so the dominating fault may be removed from the ATPG target list.

### 11.2 支配关系是不是等价关系？ / Is dominance an equivalence relation?

- Reflexive / 自反：是，$$T_f\supseteq T_f$$。
- Transitive / 传递：是，集合包含具有传递性。
- Symmetric / 对称：一般不是。$$T_f\supseteq T_g$$ 不代表 $$T_g\supseteq T_f$$。

因此 dominance 不是 equivalence relation，而是偏序式关系。只有当两个方向都成立时，才有 $$T_f=T_g$$，即故障等价。

Dominance is not an equivalence relation because it is generally not symmetric. Mutual dominance implies equivalence.

## 12. DFC：支配故障折叠 / Dominance Fault Collapsing

DFC 同时利用等价和支配关系，比 EFC 更激进。

DFC uses dominance in addition to equivalence and is therefore more aggressive than EFC.

对于一个 $$n$$ 输入 AND/OR 族基本门：

- 原始故障：$$2(n+1)$$。
- EFC 后：$$n+2$$。
- EFC + DFC 后：$$n+1$$。

For an $$n$$-input elementary AND/OR-family gate, EFC and DFC together leave $$n+1$$ target faults.

### Fanout-free DFC rules / 无扇出 DFC 规则

1. 每个主输入保留一个 `s-a-non-controlling-value` 故障。
2. 每个“所有输入均直接来自 PI”的门，在输出保留一个 `s-a-controlling-value` 故障。

1. Keep one non-controlling-value fault at every primary input.
2. Keep one controlling-value output fault for every gate whose inputs are all primary inputs.

直观上，内部输入/输出故障可由更难检测的上游或下游目标覆盖，因此可进一步删除。

Intuitively, many internal faults are dominated by harder-to-detect boundary faults and can be removed from the ATPG target list.

## 13. 有扇出电路中的 DFC / DFC in circuits with fanout

与 EFC 一样，扇出破坏简单的局部推理。Branch fault 不一定支配 stem fault，反之也不一定成立。

As with EFC, fanout invalidates simple local reasoning. A branch fault does not necessarily dominate the stem fault, nor vice versa.

实用方法仍是：

- 分割成 fanout-free regions。
- 每个区域独立执行 DFC。
- 获得线性时间但不保证最优的结果。

The practical method independently collapses fanout-free regions, producing a linear-time but potentially non-minimal result.

课件示例从 18 个原始故障，经 EFC 降为 10 个，再经 DFC 降为 7 个；但更深入的跨区域分析仍可继续减少，所以 7 不是全局最优。

In the lecture example, 18 raw faults become 10 after EFC and 7 after DFC, but the result is still not globally minimal.

## 14. Checkpoint Theorem / 检查点定理

### 14.1 定理 / Theorem

Checkpoints 定义为：

1. Primary inputs / 主输入。
2. Fanout branches / 扇出分支。

若测试集检测了所有 checkpoints 上的 stuck-at faults，则它也检测电路中的所有 single stuck-at faults。

If a test set detects every stuck-at fault on all checkpoints, it detects every single stuck-at fault in the circuit.

### 14.2 为什么有用？ / Why is it useful?

Checkpoint theorem 不需要显式计算所有等价类或支配关系，就给出一个保证完备的目标故障集合。

The theorem gives a complete target set without explicitly deriving all equivalence and dominance relations.

课件给出的数量关系为：

$$
|CHKPT| \ge |EFC| \ge |DFC|
$$

这里数量按保留的 fault targets 计算。Checkpoint 集通常比折叠后的 EFC/DFC 集大，但仍明显小于原始故障表。

The checkpoint set is usually larger than the EFC or DFC target set, but still much smaller than the raw fault list.

## 15. 为什么工业实践更常用 EFC 而不是 DFC？ / Why is EFC more common than DFC?

**中文**

DFC 删除 dominating faults，是因为“检测 dominated fault 一定检测 dominating fault”。但反方向不成立：一个测试可能检测被删除的 dominating fault，却没有检测保留下来的 dominated fault。

如果覆盖率只根据 DFC 保留列表计算，这个额外检测不会被计入，报告会显得 pessimistic（偏悲观）。换言之，真实检测到的原始故障可能多于 DFC 覆盖率所显示的数量。

**English**

DFC removes a dominating fault because every test for the dominated fault also detects it. The converse is false: a pattern may detect the removed dominating fault without detecting the retained dominated fault.

Consequently, coverage computed only on the DFC target list can be pessimistic. Real raw-fault coverage may be higher than the reported DFC coverage.

EFC 没有这个方向性问题：等价类内的故障检测集合完全相同，所以代表故障的检测状态可以可靠地映射回所有类成员。

EFC does not have this ambiguity because all members of an equivalence class have identical detecting sets.

## 16. 三种方法对比 / Comparison

| Method / 方法 | 保留对象 / Retained targets | 优点 / Advantage | 局限 / Limitation |
|---|---|---|---|
| EFC | 每个等价类一个代表 / One per equivalence class | 覆盖映射准确，实践常用 / Accurate coverage mapping | 压缩程度低于 DFC / Less aggressive |
| DFC | 删除 dominating faults / Remove dominating faults | 目标数更少 / Fewer ATPG targets | 覆盖率可能偏悲观 / Coverage may be pessimistic |
| Checkpoints | PI 与 fanout branches 上全部故障 / All faults at PIs and fanout branches | 简单且有完备性保证 / Simple and complete | 通常比 EFC/DFC 列表大 / Usually larger |

## 17. 解题工作流 / Problem-solving workflow

### EFC 题 / For an EFC problem

1. 标出所有 PI、PO、gate outputs、fanout stems 和 branches。
2. 每个位置先列 `s-a-0` 与 `s-a-1`。
3. 对 AND/OR/NAND/NOR/NOT 应用局部等价规则。
4. 遇到 fanout 时停止跨分支的武断合并。
5. 为每个 equivalence class 选择代表。
6. 保存 `representative -> original faults` 映射。

1. Mark PIs, POs, gate outputs, fanout stems, and branches.
2. List both stuck-at values at every location.
3. Apply elementary-gate equivalence rules.
4. Do not merge across fanout without justification.
5. Select one representative per class.
6. Preserve class membership.

### DFC 题 / For a DFC problem

1. 先做 EFC，避免把等价与支配混为一谈。
2. 写出或推理各故障检测集合的包含关系。
3. 删除 detecting set 更大的 dominating fault。
4. 检查方向：ATPG 应保留更难检测、检测集合更小的 fault。

First perform EFC, then use detecting-set containment. Remove the dominating fault with the larger detecting set and retain the harder-to-detect dominated fault.

## 18. 高频易错点 / Common mistakes

1. **把 dominance 方向写反。**  
   If $$T_f\supseteq T_g$$, remove $$f$$, not $$g$$, from the ATPG target list.

2. **认为 stem fault 与每个 branch fault 自动等价。**  
   A stem affects all branches; a branch affects only one.

3. **忘记非控制值。**  
   AND/NAND 的 side inputs 设 1；OR/NOR 的 side inputs 设 0，才能传播目标输入的故障效应。

4. **只记录 collapsed list，不记录类成员。**  
   This makes uncollapsed fault coverage impossible to reconstruct accurately.

5. **把 DFC coverage 当成真实 raw coverage。**  
   DFC coverage can be pessimistic because removed dominating faults may still be detected independently.

6. **对 XOR 直接套 AND/OR 规则。**  
   XOR has no controlling value, so separate analysis is required.

## 19. 一页复习 / One-page recap

**中文速记**

- EFC：检测集合相同，留一个代表。
- DFC：若 $$T_f\supseteq T_g$$，测试 $$g$$ 一定顺带检测 $$f$$，所以 ATPG 可删 $$f$$。
- AND 控制值 0、非控制值 1；OR 控制值 1、非控制值 0。
- 扇出 stem 与 branch 不能随意合并。
- SIMPLE_EFC 快、线性、保守，但不保证最小。
- Checkpoints = PI + fanout branches。
- EFC 常用于实践；DFC 更小但覆盖率报告偏悲观。

**English recap**

- EFC keeps one representative for faults with identical detecting sets.
- If $$T_f\supseteq T_g$$, $$f$$ dominates $$g$$; ATPG may remove $$f$$.
- AND controlling/non-controlling values are 0/1; OR values are 1/0.
- Never collapse a fanout stem with branches without proof.
- SIMPLE_EFC is fast and conservative, but not optimal.
- Checkpoints are primary inputs and fanout branches.
- EFC is common in practice; DFC is more aggressive but gives pessimistic coverage.

