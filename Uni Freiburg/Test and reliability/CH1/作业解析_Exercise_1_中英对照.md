# Exercise Sheet 1 作业逐步解析 / Step-by-step Solutions

> 来源 / Sources: `ex01.pdf`（题目）与 `ex01_slides_annot.pdf`（课堂批注解答）  
> 课程 / Course: Test and Reliability, Exercise Sheet 1  
> 说明 / Note: 以下不仅给出结果，还给出每一步为何这样做。图中手写内容较简略的地方，本文用电路逻辑重新推导并明确假设。

## Exercise 1：Scan chain / 扫描链

### 1.1 先理解电路模型 / Understand the circuit model

**中文**

时序电路被拆成：

- combinational core（组合逻辑核心）；
- primary inputs：`pi1`, `pi2`；
- primary output：`po1`；
- four flip-flops：`FF1...FF4`；
- secondary inputs：`si1...si4`，即当前触发器状态送入组合逻辑；
- secondary outputs：`so1...so4`，即组合逻辑产生的下一状态。

因此一个测试向量写成：

\[
pi_1pi_2\mid si_1si_2si_3si_4
\rightarrow
po_1\mid so_1so_2so_3so_4
\]

**English**

The sequential circuit is viewed as a combinational core surrounded by four flip-flops. The current flip-flop contents are the secondary inputs, and the next-state values produced by the core are the secondary outputs.

The two supplied combinational tests are:
$$
\[
11\mid0011\rightarrow0\mid0111
\]

$$$$\[
01\mid0101\rightarrow1\mid1100
\]$$

### 1.2 Scan mode 与 capture mode / Scan and capture modes

| `scan_enable` | Mode / 模式 | Flip-flop behavior / 触发器行为 |
|---:|---|---|
| 1 | Scan shift / 扫描移位 | `FF1 <- scan_in`, `FF2 <- FF1`, `FF3 <- FF2`, `FF4 <- FF3` |
| 0 | Functional capture / 功能捕获 | `FFi <- soi`; 组合逻辑响应被装入触发器 |

`scan_out` 观察扫描链末端，即移位前 `FF4` 的内容。

`scan_out` observes the last flip-flop, i.e. the value shifted out of `FF4`.

### 1.3 为什么装入位序要反着看？ / Why must the scan-in order be read carefully?

扫描链顺序是：

\[
scan\_in\rightarrow FF1\rightarrow FF2\rightarrow FF3\rightarrow FF4\rightarrow scan\_out
\]

连续移入 4 位 \(u_1,u_2,u_3,u_4\) 后，状态为：

\[
FF1FF2FF3FF4=u_4u_3u_2u_1
\]

所以要得到 `0011`，输入顺序应为 `1,1,0,0`。

After four shifts, the first bit has moved to `FF4`, so the desired state `0011` must be shifted in as `1,1,0,0`.

### 1.4 逐时钟填写 / Fill the table cycle by cycle

初始状态为 `0000`。

The initial state is `0000`.

| Cycle | `pi1` | `pi2` | `scan_enable` | `scan_in` | `po1` | `scan_out` | Explanation / 解释 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | X | X | 1 | 1 | X | 0 | 移出原 `FF4=0`，状态变 `1000`。/ Shift out 0; state becomes `1000`. |
| 2 | X | X | 1 | 1 | X | 0 | 状态 `1100`。/ State becomes `1100`. |
| 3 | X | X | 1 | 0 | X | 0 | 状态 `0110`。/ State becomes `0110`. |
| 4 | X | X | 1 | 0 | X | 1 | 移出原 `FF4=1`，状态 `0011`。/ Shift out 1; state becomes `0011`. |
| 5 | 1 | 1 | 0 | X | 0 | 1 | 施加第一向量；响应为 `0|0111`，捕获后状态 `0111`。/ Apply test 1 and capture `0111`. |
| 6 | X | X | 1 | 1 | X | 1 | 开始一边移出 `0111`，一边装入下一状态；状态 `1011`。 |
| 7 | X | X | 1 | 0 | X | 1 | 状态 `0101`。 |
| 8 | X | X | 1 | 1 | X | 1 | 状态 `1010`。 |
| 9 | X | X | 1 | 0 | X | 0 | 状态 `0101`，第二测试状态装入完成。 |
| 10 | 0 | 1 | 0 | X | 1 | 0 | 施加第二向量；响应为 `1|1100`，捕获后状态 `1100`。 |
| 11 | X | X | 1 | X | X | 0 | 移出 `FF4=0`。 |
| 12 | X | X | 1 | X | X | 0 | 移出下一位 0。 |
| 13 | X | X | 1 | X | X | 1 | 移出下一位 1。 |
| 14 | X | X | 1 | X | X | 1 | 移出最后一位 1。 |

因此完整 `scan_out` 列为：

\[
0,0,0,1,\ 1,\ 1,1,1,0,\ 0,\ 0,0,1,1
\]

The final four scan-out bits after the second capture are `0011` in temporal order, corresponding to the stored state `1100` because `FF4` exits first.

### 1.5 这一题真正考什么？ / What is this exercise testing?

1. 区分当前状态 `si` 与下一状态 `so`。
2. 理解 scan shift 与 functional capture 不能同时发生。
3. 掌握 shift-in 位序与寄存器排列相反。
4. 理解可以同时 shift out 旧响应并 shift in 新测试状态，从而减少测试时间。

The key idea is that scan shifting provides controllability and observability for internal states. Old responses can be shifted out while the next state is shifted in.

---

## Exercise 2：Stuck-at collapse 与 bridging faults

电路为：

\[
e=ab,\qquad f=cd,\qquad g=e+f=ab+cd
\]

The circuit implements \(g=ab+cd\) using two AND gates followed by an OR gate.

给定测试向量 / Given patterns:

\[
0101,\quad0111,\quad1010,\quad1110
\]

位序均为 `abcd`。

### 2(a) 列出全部 stuck-at faults / List all stuck-at faults

信号线为 `a,b,c,d,e,f,g`。每条线有 s-a-0 和 s-a-1：

\[
\begin{aligned}
&a/0,a/1,b/0,b/1,c/0,c/1,d/0,d/1,\\
&e/0,e/1,f/0,f/1,g/0,g/1
\end{aligned}
\]

总计：

\[
7\times2=14\text{ faults}
\]

There are seven signal lines and therefore fourteen raw single stuck-at faults.

### 2(a)-1 做 EFC / Perform equivalent fault collapsing

对上方 AND 门：

\[
a/0\equiv b/0\equiv e/0
\]

For the upper AND gate, either input stuck at 0 has the same output behavior as `e/0`.

对下方 AND 门：

\[
c/0\equiv d/0\equiv f/0
\]

For the lower AND gate:

\[
c/0\equiv d/0\equiv f/0
\]

对 OR 门：

\[
e/1\equiv f/1\equiv g/1
\]

For the OR gate, either input stuck at 1 is equivalent to the output stuck at 1.

其余故障没有被这些局部等价关系合并：

\[
a/1,b/1,c/1,d/1,g/0
\]

可选择以下 8 个代表：

\[
\boxed{\{e/0,\ f/0,\ g/1,\ a/1,\ b/1,\ c/1,\ d/1,\ g/0\}}
\]

Any member of each class may be chosen, so the EFC representative list is not unique.

### 2(a)-2 用给定向量检查故障覆盖 / Check detection by the supplied patterns

先算无故障输出：

| `abcd` | `e=ab` | `f=cd` | `g=e+f` |
|---|---:|---:|---:|
| 0101 | 0 | 0 | 0 |
| 0111 | 0 | 1 | 1 |
| 1010 | 0 | 0 | 0 |
| 1110 | 1 | 0 | 1 |

然后对每个代表故障寻找至少一个检测向量：

| Representative / 代表故障 | Activation and propagation / 激活与传播 | Detecting pattern / 检测向量 |
|---|---|---|
| `e/0` | 需 good `e=1` 且 `f=0` | `1110` |
| `f/0` | 需 good `f=1` 且 `e=0` | `0111` |
| `g/1` | 需 good `g=0` | `0101` 或 `1010` |
| `a/1` | 需 `a=0,b=1`，并令 `f=0` | `0101` |
| `b/1` | 需 `b=0,a=1`，并令 `f=0` | `1010` |
| `c/1` | 需 `c=0,d=1`，并令 `e=0` | `0101` |
| `d/1` | 需 `d=0,c=1`，并令 `e=0` | `1010` |
| `g/0` | 需 good `g=1` | `0111` 或 `1110` |

因此给定 4 个向量检测全部 8 个代表故障，也就检测全部 14 个原始故障。

Therefore, the four supplied patterns cover every collapsed representative and consequently all fourteen original stuck-at faults.

### 2(b) 找可能的 shorts / Identify possible bridging shorts

题目给出：

- 导电铝颗粒最大尺寸为 12 nm；
- 一块芯片上最多一个颗粒；
- 只有金属间最短距离不超过 12 nm 时，单颗粒才可能同时接触两条线。

The maximum particle size is 12 nm, and only one particle can occur. A possible bridge therefore requires two polygons whose minimum separation is at most 12 nm.

借助图中的 20 nm 标尺比较间距，可识别出：

\[
\boxed{b\leftrightarrow c}
\]

\[
\boxed{e\leftrightarrow g}
\]

其他线对的最近距离大于 12 nm，单颗粒无法形成短路。

The only geometrically possible bridges are `b-c` and `e-g`.

### 2(c) 判断 bridge 的电气行为 / Determine the electrical behavior

规则：

1. 若一个 polygon 面积超过另一个的两倍，大 polygon 对应线为 aggressor，小 polygon 对应线为 victim；victim 被强制为 aggressor 的逻辑值。
2. 若面积大致相近，则按 wired-AND：

\[
x'=y'=x\land y
\]

According to the statement, a much larger polygon dominates the smaller one; otherwise the short behaves as a wired AND.

从版图面积可见：

- `b` 明显大于 `c`，所以 `b` 是 aggressor，`c` 是 victim：\(\boxed{c\leftarrow b}\)。
- `e` 明显大于 `g`，所以 `e` 是 aggressor，`g` 是 victim：\(\boxed{g\leftarrow e}\)。

From the relative polygon areas, the intended lecture solution treats `b` as the aggressor over `c`, and `e` as the aggressor over `g`.

### 2(c)-1 模拟 `b -> c` / Simulate the `b`-to-`c` bridge

故障电路中：

\[
c_f=b
\]

所以：

\[
g_f=ab+(b)d
\]

| Pattern | Good `g` | Faulty `c_f` | Faulty `g_f` | Detected? |
|---|---:|---:|---:|---|
| 0101 | 0 | 1 | 1 | Yes |
| 0111 | 1 | 1 | 1 | No |
| 1010 | 0 | 0 | 0 | No |
| 1110 | 1 | 1 | 1 | No |

检测向量为：

\[
\boxed{0101}
\]

The pattern `0101` makes good `c=0` but forces faulty `c_f=b=1`; since `d=1` and the upper product is 0, the output changes from 0 to 1.

### 2(c)-2 模拟 `e -> g` / Simulate the `e`-to-`g` bridge

正常情况下：

\[
g=e+f
\]

短路后 victim `g` 跟随 aggressor `e`：

\[
g_f=e
\]

| Pattern | `e` | `f` | Good `g` | Faulty `g_f=e` | Detected? |
|---|---:|---:|---:|---:|---|
| 0101 | 0 | 0 | 0 | 0 | No |
| 0111 | 0 | 1 | 1 | 0 | Yes |
| 1010 | 0 | 0 | 0 | 0 | No |
| 1110 | 1 | 0 | 1 | 1 | No |

检测向量为：

\[
\boxed{0111}
\]

`0111` is ideal because the correct output is produced only by the lower product `f=1`, while the aggressor `e=0` incorrectly forces `g` to 0.

### 2(c)-3 是否需要补充测试？ / Are additional patterns needed?

不需要。`0101` 检测 `b-c` bridge，`0111` 检测 `e-g` bridge。两种可能的 bridging faults 都已被给定测试集检测。

No additional pattern is required because both possible bridges are already covered.

---

## Exercise 3：故障位置、ATPG 与 transition delay fault

### 3.1 先写出门级逻辑 / Reconstruct the gate equations

根据图 5，可写成：

\[
\begin{aligned}
n_7&=\overline a\\
n_8&=\overline d\\
l&=n_1=\overline{bc} &&\text{(G1)}\\
n_2&=\overline{b\,n_7} &&\text{(G2)}\\
n_3&=\overline{c\,n_8} &&\text{(G3)}\\
n_4&=\overline{a\,l} &&\text{(G4)}\\
n_5&=\overline{l\,d} &&\text{(G5)}\\
y&=\overline{n_2n_4n_5n_3} &&\text{(G6)}
\end{aligned}
\]

`l` 是 G1 输出，也是题图中标注 `sa1` 的位置。

The marked fault site `l` is the output of NAND gate G1 and fans out to G4 and G5.

## 3(a) 一共有多少 stuck-at faults？ / How many stuck-at faults are there?

### 标准 fanout-branch 计数 / Standard fanout-branch counting

在 stuck-at 模型中，fanout stem 与每个 branch 可作为独立故障位置：

- `a,b,c,d` 各有一个 stem 和两个 branches：\(4\times3=12\) 个位置。
- `l`（G1 输出）有一个 stem 和两个 branches：3 个位置。
- G2、G3、G4、G5、G6、G7、G8 的非扇出输出：7 个位置。

总位置数：

\[
12+3+7=22
\]

每个位置有两种 stuck-at 值，因此：

\[
\boxed{22\times2=44\text{ single stuck-at faults}}
\]

Under the standard convention that distinguishes fanout stems and branches, the circuit has 22 fault sites and 44 single stuck-at faults.

> 注 / Note: 若某门课程采用“每个逻辑 net 只计一次、不把 branch 单列”的简化口径，则有 4 个 PI nets 加 8 个 gate-output nets，共 12 个 nets、24 个 faults。但本章专门强调 stem/branch 差异，故标准答案应采用 44。

## 3(b) 为 `l/1` 生成测试 / Generate a test for `l` stuck at 1

ATPG 分三步：激活、传播、观察。

ATPG proceeds through sensitization, propagation, and observation.

### Step 1：激活故障 / Sensitize the fault

目标故障为 `l/1`。要激活它，无故障电路中必须有：

\[
l=0
\]

而：

\[
l=\overline{bc}
\]

NAND 输出为 0 仅当两个输入均为 1：

\[
\boxed{b=1,\ c=1}
\]

To activate a stuck-at-1 fault, the good value must be 0, so both inputs of G1 must be 1.

### Step 2：通过 G4 和 G5 传播 / Propagate through G4 and G5

`l` 分别进入 NAND 门 G4 和 G5。

要通过 G4 传播，另一个输入必须是 NAND 的非控制值 1：

\[
\boxed{a=1}
\]

要通过 G5 传播，另一个输入也必须为 1：

\[
\boxed{d=1}
\]

To propagate through each NAND, its side input must be 1. Therefore set `a=d=1`.

### Step 3：检查旁路输入 / Check the side paths

当 `a=b=c=d=1` 时：

\[
n_7=\overline a=0,\qquad n_8=\overline d=0
\]

\[
n_2=\overline{b n_7}=\overline{1\cdot0}=1
\]

\[
n_3=\overline{c n_8}=\overline{1\cdot0}=1
\]

所以 G6 的旁路输入 `n2`、`n3` 都是非控制值 1，不会遮蔽来自 G4/G5 的故障效应。

The outer paths automatically produce 1 at G2 and G3, allowing G6 to observe the effects from G4 and G5.

### Step 4：比较 good 与 faulty / Compare good and faulty circuits

测试向量：

\[
\boxed{abcd=1111}
\]

无故障：

\[
l=0,\quad n_4=n_5=1,\quad n_2=n_3=1
\]

\[
y_{good}=\overline{1\cdot1\cdot1\cdot1}=0
\]

故障 `l/1`：

\[
l_f=1,\quad n_{4f}=n_{5f}=0
\]

\[
y_{faulty}=\overline{1\cdot0\cdot0\cdot1}=1
\]

因此：

\[
\boxed{1111:\ y_{good}=0,\ y_{faulty}=1}
\]

The stuck-at-1 fault is detected by `1111`.

### 为什么要同时传播两条路径？ / Why must both reconvergent paths be considered?

`l` 扇出到 G4 与 G5，随后在 G6 重汇合。如果只让一条路径传播而另一条给 G6 一个控制值 0，G6 的 NAND 输出会被固定为 1，目标路径上的差异可能被遮蔽。

Because the fault fans out and reconverges at G6, all relevant side inputs must be controlled. A controlling 0 on any unaffected G6 input would mask the discrepancy.

## 3(c)-1 Stuck-at fault 与 transition fault 的关系

**中文**

Stuck-at fault 是静态模型：故障节点永久为 0 或 1。

Transition delay fault 是动态时序模型：

- slow-to-rise（STR）：节点应从 0 变 1，但在捕获时刻仍保持 0，短时间内表现得像 `s-a-0`。
- slow-to-fall（STF）：节点应从 1 变 0，但在捕获时刻仍保持 1，短时间内表现得像 `s-a-1`。

所以 transition fault 的第二个捕获向量可借用对应 stuck-at fault 的传播条件，但还必须增加第一个 launch vector 来制造所需跳变。

**English**

A stuck-at fault is static. A transition fault is timing-dependent:

- A slow-to-rise fault temporarily resembles stuck-at-0 at capture.
- A slow-to-fall fault temporarily resembles stuck-at-1 at capture.

The capture vector can reuse the propagation conditions of the corresponding stuck-at test, but a preceding launch vector is required to create the transition.

## 3(c)-2 为 G1 输出的 slow-to-fall 生成两向量测试

需要在 `l` 上制造：

\[
1\rightarrow0
\]

并在第二拍传播这个迟到的 1。

We need a launch-capture pair that creates a `1 -> 0` transition at `l`.

### Capture vector / 捕获向量

由 3(b)，传播 `l` 在捕获时刻表现出的 `s-a-1` 效应需要：

\[
V_2=1111
\]

此时 good `l` 应为 0；若 slow-to-fall，则捕获瞬间 faulty `l` 仍为 1。

The second vector is the stuck-at-1 test `1111`.

### Launch vector / 启动向量

第一拍要令：

\[
l=1=\overline{bc}
\]

因此 `b,c` 至少一个为 0。为减少不必要输入变化，可保持 `a=c=d=1`，仅把 `b` 从 0 切到 1：

\[
V_1=1011
\]

检查：

\[
V_1=1011:\quad l=\overline{0\cdot1}=1
\]

\[
V_2=1111:\quad l=\overline{1\cdot1}=0
\]

所以有效测试对为：

\[
\boxed{1011\rightarrow1111}
\]

An equally valid alternative is:

\[
\boxed{1101\rightarrow1111}
\]

because changing `c:0->1` also causes `l:1->0`.

### 捕获时的输出 / Output at capture

- 无故障电路：`l` 已及时降到 0，输出 \(y=0\)。
- STF 故障电路：`l` 在捕获边沿仍为 1，效果等同瞬时 `l/1`，输出 \(y=1\)。

In the fault-free circuit the output is 0. With the slow-to-fall defect, `l` remains 1 long enough to produce faulty output 1.

## 最终答案汇总 / Final answer summary

| Item | Answer / 答案 |
|---|---|
| Ex.1 first scan-in | `1,1,0,0` loads `0011` |
| Ex.1 second scan-in | `1,0,1,0` loads `0101` |
| Ex.1 captured responses | `0111`, then `1100` |
| Ex.2 raw stuck-at count | 14 |
| Ex.2 EFC representatives | 8 representatives |
| Ex.2 possible bridges | `b-c`, `e-g` |
| Ex.2 bridge tests | `0101` detects `b->c`; `0111` detects `e->g` |
| Ex.3 standard stuck-at count | 44 |
| Ex.3 `l/1` test | `1111` |
| Ex.3 slow-to-fall test | `1011 -> 1111` or `1101 -> 1111` |

## 自检清单 / Self-check checklist

- Scan shift 时是否记住 `FF4` 先从 `scan_out` 出来？
- EFC 是否把 AND 输入 s-a-0 与输出 s-a-0 合并？
- OR 是否把输入 s-a-1 与输出 s-a-1 合并？
- Bridge 测试是否同时比较 good output 与 faulty output？
- Stuck-at ATPG 是否完成 activation、propagation、observation？
- Transition test 是否包含 launch 和 capture 两个向量？
- Fanout 计数时是否明确采用 stem/branch 口径？

