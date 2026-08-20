# Exercise Sheet 2 作业逐步解析 / Step-by-step Solutions

> 来源 / Sources: `ex02.pdf` 与 `ex02_slides_annot.pdf`  
> 主题 / Topics: Parallel fault simulation, EFC/DFC, deductive fault simulation, AIG bit-parallel C code

## Exercise 1(a)：Fault-parallel simulation

### 1. 电路结构 / Circuit structure

图 1 中的 branch lines 可写成：

$$
e=b,\qquad f=b,\qquad g=c,\qquad h=c
$$

各门输出为：

$$
i=a\land e
$$

$$
j=f\land h
$$

$$
k=g\lor d
$$

$$
l=\overline{j\land i}
$$

$$
m=k\land l
$$

The labels $e,f$ are branches of input $b$, and $g,h$ are branches of input $c$.

### 2. Packed columns / 并行列定义

题目要求同时模拟四个 circuit instances：

| Column | Meaning |
|---:|---|
| 0 | fault-free / 无故障 |
| 1 | $j$ s-a-1 |
| 2 | $l$ s-a-0 |
| 3 | $k$ s-a-1 |

每条线可看成一个 4-bit word：

```text
[good, j/1, l/0, k/1]
```

The four bits are evaluated simultaneously by bitwise gate operations.

### 3. 初始化主输入 / Initialize primary inputs

测试向量为：

$$
(a,b,c,d)=(0,1,0,1)
$$

在故障注入前，所有 circuit instances 使用相同输入：

```text
a = 0000
b = 1111
c = 0000
d = 1111
```

### 4. 计算 fanout branches / Evaluate branches

$$
e=f=b=1
$$

$$
g=h=c=0
$$

因此 packed values 为：

```text
e = 1111
f = 1111
g = 0000
h = 0000
```

### 5. 计算 $i$ / Compute line i

$$
i=a\land e=0\land1=0
$$

这里没有 $i$ 上的目标故障，所以：

```text
i = 0000
```

### 6. 计算并注入 $j$ s-a-1

正常逻辑：

$$
j=f\land h=1\land0=0
$$

未注入时四列均为 0。第 1 个 faulty column 对应 $j/1$，所以强制该 bit 为 1：

```text
j = 0100
```

按表格逐列写为：

```text
good=0, j/1=1, l/0=0, k/1=0
```

### 7. 计算并注入 $k$ s-a-1

正常逻辑：

$$
k=g\lor d=0\lor1=1
$$

目标故障也是 $k/1$。由于 good value 本来已经是 1，故障没有被激活：

```text
k = 1111
```

The $k$ stuck-at-1 column is indistinguishable from the good circuit at this line.

### 8. 计算并注入 $l$ s-a-0

$$
l=\overline{j\land i}
$$

逐列分析：

- good：$\overline{0\land0}=1$；
- $j/1$：$\overline{1\land0}=1$，故障被 $i=0$ 遮蔽；
- $l/0$：正常先算 1，然后在 line $l$ 强制成 0；
- $k/1$：$\overline{0\land0}=1$。

所以：

```text
l = 1101
```

### 9. 计算输出 $m$ / Compute output m

$$
m=k\land l
$$

由于 $k=1111$：

```text
m = 1111 & 1101 = 1101
```

### 10. 完整赋值表 / Complete assignment table

| Line | Fault-free | $j$ s-a-1 | $l$ s-a-0 | $k$ s-a-1 |
|---|---:|---:|---:|---:|
| $a$ | 0 | 0 | 0 | 0 |
| $b$ | 1 | 1 | 1 | 1 |
| $c$ | 0 | 0 | 0 | 0 |
| $d$ | 1 | 1 | 1 | 1 |
| $e$ | 1 | 1 | 1 | 1 |
| $f$ | 1 | 1 | 1 | 1 |
| $g$ | 0 | 0 | 0 | 0 |
| $h$ | 0 | 0 | 0 | 0 |
| $i$ | 0 | 0 | 0 | 0 |
| $j$ | 0 | 1 | 0 | 0 |
| $k$ | 1 | 1 | 1 | 1 |
| $l$ | 1 | 1 | 0 | 1 |
| $m$ | 1 | 1 | 0 | 1 |

### 11. 哪些故障被检测？ / Which faults are detected?

比较输出 $m$：

```text
good output = 1
j/1 output  = 1
l/0 output  = 0
k/1 output  = 1
```

因此只有：

$$
\boxed{l\text{ s-a-0}}
$$

被测试向量 `0101` 检测。

Only $l$ stuck-at-0 changes the primary output.

### 12. 另外两个为什么没检测？ / Why are the other two faults missed?

- $j/1$ 已被激活，但 $i=0$ 控制 NAND 输出 $l=1$，故障效应被遮蔽。
- $k/1$ 没有激活，因为 good $k$ 已经是 1。

This illustrates the difference between activation and propagation.

---

## Exercise 1(b)：EFC 与 DFC

### 1. 给每条 fault site 命名 / Name the fault sites

图 2 的逻辑为：

$$
D=a\oplus b_1
$$

$$
F=\overline D
$$

$$
E=b_2\land c
$$

$$
G=\overline{F\lor E}
$$

$b$ 是 fanout stem，$b_1$ 与 $b_2$ 是两个独立 branches。

故障位置为：

```text
a, b(stem), b1, b2, c, D, F, E, G
```

共有 9 个 fault sites，每个有两种 stuck-at faults：

$$
9\times2=\boxed{18}
$$

### 2. EFC 等价类 / EFC equivalence classes

XOR 门没有简单 controlling-value 等价规则，因此其输入与输出故障通常分别保留。

The inverter gives:

$$
D/0\equiv F/1
$$

$$
D/1\equiv F/0
$$

AND gate gives:

$$
b_2/0\equiv c/0\equiv E/0
$$

NOR gate gives:

$$
F/1\equiv E/1\equiv G/0
$$

结合传递性：

$$
D/0\equiv F/1\equiv E/1\equiv G/0
$$

各 equivalence classes 可整理为：

| Class | Members |
|---:|---|
| 1 | $a/0$ |
| 2 | $a/1$ |
| 3 | $b/0$ |
| 4 | $b/1$ |
| 5 | $b_1/0$ |
| 6 | $b_1/1$ |
| 7 | $b_2/0,c/0,E/0$ |
| 8 | $b_2/1$ |
| 9 | $c/1$ |
| 10 | $D/0,F/1,E/1,G/0$ |
| 11 | $D/1,F/0$ |
| 12 | $G/1$ |

因此 EFC 后：

$$
\boxed{12\text{ representative faults}}
$$

The representative chosen from each class is arbitrary.

### 3. DFC 结果 / DFC result

按本课程课件采用的 structural DFC procedure，在 fanout boundaries 与 XOR 附近保守地保留故障，并利用可证明的 dominance relation 再删除 dominating targets。

课上批注结果保留 11 个 target faults：

$$
\boxed{11\text{ faults after DFC}}
$$

The structural result is conservative and is not guaranteed to be globally minimal.

### 4. 数量汇总 / Count summary

| Method | Number of faults |
|---|---:|
| Without collapsing / 不折叠 | $\boxed{18}$ |
| EFC | $\boxed{12}$ |
| DFC used in the exercise | $\boxed{11}$ |

> 注意 / Note: 若对完整真值表做更昂贵的 global functional dominance analysis，还可能发现更多支配关系。这里应报告课程幻灯片所采用的结构折叠结果，而不是另行求全局最小集。

---

## Exercise 2：Deductive fault simulation

### 1. 电路与 22 条 fault lines / Circuit and its 22 lines

门级逻辑为：

$$
k=\overline a
$$

$$
l=\overline d
$$

$$
e=\overline{bc}
$$

$$
f=\overline{bk}
$$

$$
g=\overline{ae}
$$

$$
h=\overline{ed}
$$

$$
i=\overline{cl}
$$

$$
j=\overline{fghi}
$$

为明确区分 fanout branches，本文使用：

```text
a→k, a→g
b→e, b→f
c→e, c→i
d→l, d→h
e→g, e→h
```

22 条线为：

- 4 个 PI stems：$a,b,c,d$；
- 8 个 PI branches；
- $e$ stem 与 2 个 branches；
- 7 个非扇出 gate outputs：$k,l,f,g,h,i,j$。

总计：

$$
4+8+3+7=22
$$

所以原始 stuck-at faults 数为：

$$
22\times2=44
$$

### 2. 演绎规则回顾 / Deductive rules

若 line $x$ 的 good value 为 $v$，本地故障为：

$$
\{x/\overline v\}
$$

Fanout branch list：

$$
L_{branch}=L_{stem}\cup\{branch/\overline v\}
$$

Inverter：

$$
L_z=L_x\cup\{z/\overline{v_z}\}
$$

NAND 的 fault-list propagation 与其 AND core 相同，但加入的本地 fault 由实际 NAND output 决定。

## Pattern 1001

### 3. Good values / 无故障值

$$
(a,b,c,d)=(1,0,0,1)
$$

依次得到：

| Line | Value |
|---|---:|
| $a,b,c,d$ | $1,0,0,1$ |
| $k,l$ | $0,0$ |
| $e$ | 1 |
| $f,g,h,i$ | $1,0,0,1$ |
| $j$ | 1 |

### 4. PI stems 与 branches 的列表

| Line | Value | Fault list |
|---|---:|---|
| $a$ | 1 | $\{a/0\}$ |
| $a\to k$ | 1 | $\{a/0,(a\to k)/0\}$ |
| $a\to g$ | 1 | $\{a/0,(a\to g)/0\}$ |
| $b$ | 0 | $\{b/1\}$ |
| $b\to e$ | 0 | $\{b/1,(b\to e)/1\}$ |
| $b\to f$ | 0 | $\{b/1,(b\to f)/1\}$ |
| $c$ | 0 | $\{c/1\}$ |
| $c\to e$ | 0 | $\{c/1,(c\to e)/1\}$ |
| $c\to i$ | 0 | $\{c/1,(c\to i)/1\}$ |
| $d$ | 1 | $\{d/0\}$ |
| $d\to l$ | 1 | $\{d/0,(d\to l)/0\}$ |
| $d\to h$ | 1 | $\{d/0,(d\to h)/0\}$ |

### 5. 第一层 gates / First gate level

#### Inverter $k$

$$
L_k=L_{a\to k}\cup\{k/1\}
$$

$$
L_k=\{a/0,(a\to k)/0,k/1\}
$$

#### Inverter $l$

$$
L_l=\{d/0,(d\to l)/0,l/1\}
$$

#### NAND $e=\overline{bc}$

两个 AND-core 输入都是 0。要使 AND core 从 0 变 1，同一个 fault 必须同时出现在两个输入列表中：

$$
L_e=L_{b\to e}\cap L_{c\to e}\cup\{e/0\}
$$

两列表无公共 fault，所以：

$$
L_e=\{e/0\}
$$

### 6. $e$ 的两个 branches

$$
L_{e\to g}=\{e/0,(e\to g)/0\}
$$

$$
L_{e\to h}=\{e/0,(e\to h)/0\}
$$

### 7. 中间 NAND gates

#### $f=\overline{bk}$

AND core inputs 为 $0,0$。两个列表没有共同 fault，因此：

$$
L_f=\{f/0\}
$$

#### $g=\overline{ae}$

AND core inputs 为 $1,1$，所以使用 union：

$$
L_g=L_{a\to g}\cup L_{e\to g}\cup\{g/1\}
$$

$$
L_g=
\{a/0,(a\to g)/0,e/0,(e\to g)/0,g/1\}
$$

#### $h=\overline{ed}$

同样两个输入都是 1：

$$
L_h=
\{e/0,(e\to h)/0,d/0,(d\to h)/0,h/1\}
$$

#### $i=\overline{cl}$

AND core inputs 为 $0,0$，没有共同 active fault：

$$
L_i=\{i/0\}
$$

### 8. 输出 $j$ 的重汇合处理

$j$ 的 NAND core inputs 为：

$$
(f,g,h,i)=(1,0,0,1)
$$

要使 AND core 从 0 变 1，同一个 fault 必须同时改变两个 controlling-zero inputs $g,h$，并且不能改变 $f,i$：

$$
L_j=
\left[
(L_g\cap L_h)-(L_f\cup L_i)
\right]
\cup\{j/0\}
$$

$L_g$ 与 $L_h$ 的公共 fault 是 $e/0$：

$$
L_g\cap L_h=\{e/0\}
$$

它不在 $L_f$ 或 $L_i$ 中，因此：

$$
\boxed{L_j=\{e/0,j/0\}}
$$

### 9. Pattern 1001 的质量 / Quality

检测数：

$$
2
$$

覆盖率：

$$
\frac{2}{44}\times100\%\approx4.55\%
$$

This pattern is weak for the given fault list.

## Pattern 1111

### 10. Good values

$$
(a,b,c,d)=(1,1,1,1)
$$

得到：

| Line | Value |
|---|---:|
| $k,l$ | $0,0$ |
| $e$ | 0 |
| $f,g,h,i$ | $1,1,1,1$ |
| $j$ | 0 |

### 11. 关键 line lists / Important line lists

PI 与 branch lists：

$$
L_a=\{a/0\},\quad
L_b=\{b/0\},\quad
L_c=\{c/0\},\quad
L_d=\{d/0\}
$$

Inverters：

$$
L_k=\{a/0,(a\to k)/0,k/1\}
$$

$$
L_l=\{d/0,(d\to l)/0,l/1\}
$$

NAND $e$ 的两个输入均为 1：

$$
L_e=
\{b/0,(b\to e)/0,c/0,(c\to e)/0,e/1\}
$$

Branches:

$$
L_{e\to g}=L_e\cup\{(e\to g)/1\}
$$

$$
L_{e\to h}=L_e\cup\{(e\to h)/1\}
$$

中间 gates：

$$
L_f=\{a/0,(a\to k)/0,k/1,f/0\}
$$

$$
L_g=
\{b/0,(b\to e)/0,c/0,(c\to e)/0,e/1,(e\to g)/1,g/0\}
$$

$$
L_h=
\{b/0,(b\to e)/0,c/0,(c\to e)/0,e/1,(e\to h)/1,h/0\}
$$

$$
L_i=\{d/0,(d\to l)/0,l/1,i/0\}
$$

### 12. 输出 list / Output fault list

此时 $f=g=h=i=1$。NAND core 的所有输入均为 1，所以全部输入列表取 union，并加入 $j/1$：

$$
L_j=L_f\cup L_g\cup L_h\cup L_i\cup\{j/1\}
$$

展开后：

$$
\boxed{
\begin{aligned}
L_j=\{&
a/0,(a\to k)/0,k/1,f/0,\\
&b/0,(b\to e)/0,c/0,(c\to e)/0,e/1,\\
&(e\to g)/1,g/0,(e\to h)/1,h/0,\\
&d/0,(d\to l)/0,l/1,i/0,j/1
\}
\end{aligned}
}
$$

共有：

$$
\boxed{18\text{ detected faults}}
$$

### 13. Pattern 1111 的质量 / Quality

$$
\frac{18}{44}\times100\%\approx40.91\%
$$

`1111` 明显优于 `1001`，因为它让最终 NAND 的四个输入全部为非控制值 1，许多不同路径上的故障效应都能到达输出。

Pattern `1111` is substantially better because the final NAND receives all ones, so discrepancies from every input path can propagate.

### 14. 两个向量合起来 / Combined coverage

`1001` 检测 $\{e/0,j/0\}$，这两个故障不在 `1111` 的 18 个检测故障中。因此并集为：

$$
2+18=20
$$

$$
FC_{combined}=\frac{20}{44}\times100\%\approx45.45\%
$$

The patterns complement each other, but the combined coverage is still below 50%.

---

## Exercise 3：AIG bit-parallel simulation code

### 1. AIG 是什么？ / What is an AIG?

AIG（And-Inverter Graph）只包含：

- two-input AND nodes；
- complemented edges，即输入可按需取反。

根据 De Morgan's law，任意组合逻辑都可转换为 AND 与 inversion 的组合。

An AIG stores inversion on edges rather than requiring a separate inverter node for every negation.

### 2. Odd-even literal encoding / 奇偶 literal 编码

变量编号为 $v$：

$$
\text{positive literal}=2v
$$

$$
\text{negated literal}=2v+1
$$

因此：

- `literal / 2` 得到 variable index；
- `literal & 1` 读取最低位，判断是否取反。

Examples:

| Literal | Variable | Negated? |
|---:|---:|---|
| 12 | 6 | No |
| 3 | 1 | Yes |
| 8 | 4 | No |

所以：

```text
12 3 8
```

表示：

$$
v_6=\overline{v_1}\land v_4
$$

### 3. `current_valuation` 中存的不是单 bit

数组的每个元素是 `unsigned int` word：

```c
current_valuation[v]
```

word 中每个 bit 表示一个并行 pattern 或 circuit instance 的 line value。

Thus a single CPU bitwise operation computes many Boolean simulations at once.

### 4. 解释 `deref` / Explain `deref`

```c
unsigned int variable_of_literal = literal / 2;
```

删除最低的 negation bit，得到变量编号。

```c
unsigned int result = current_valuation[variable_of_literal];
```

读取该变量的 packed word。

```c
unsigned int negated_literal = literal & 1;
```

检查 literal 是否为奇数。

若为 negated literal，需要逐 bit 取反整个 word。

### 5. 第一处缺失代码 / First missing part

`UINT_MAX` 的每个 bit 都是 1：

```text
111...111
```

与它 XOR 等价于逐 bit NOT：

$$
x\oplus1=\overline x
$$

所以：

```c
result = result ^ UINT_MAX;
```

也可以更直接写：

```c
result = ~result;
```

The exercise solution uses XOR with `UINT_MAX`.

### 6. Gate loop / 门循环

```c
l = deref(and->rhs0);
r = deref(and->rhs1);
```

这两句读取两个输入 literal，并自动处理 complemented edge。

AND node 必须使用逐位 AND：

```c
tmp = l & r;
```

不能使用：

```c
l && r
```

因为 `&&` 只返回单个布尔结果 0 或 1，会破坏 packed parallel data。

### 7. 存储输出 / Store the output

AIG AND specification 的左侧 literal 是非取反的偶数 literal，因此：

```c
current_valuation[and->lhs / 2] = tmp;
```

### 8. 完整代码 / Completed code

```c
unsigned int deref(unsigned int literal)
{
    unsigned int variable_of_literal = literal / 2;
    unsigned int result = current_valuation[variable_of_literal];
    unsigned int negated_literal = literal & 1;

    if (negated_literal)
    {
        result = result ^ UINT_MAX;
    }

    return result;
}

unsigned int l, r, tmp, j;

for (j = 0; j < model->num_ands; j++)
{
    and_gate *and = model->ands + j;

    l = deref(and->rhs0);
    r = deref(and->rhs1);
    tmp = l & r;

    current_valuation[and->lhs / 2] = tmp;
}
```

### 9. 为什么这是“真正的并行”？ / Why is this real parallelism?

假设 `unsigned int` 是 32 bit：

$$
l=l_{31}l_{30}\ldots l_0
$$

$$
r=r_{31}r_{30}\ldots r_0
$$

执行一次：

```c
tmp = l & r;
```

硬件同时产生：

$$
tmp_i=l_i\land r_i,\qquad i=0,\ldots,31
$$

因此一次 CPU 指令完成 32 个独立 AND simulations。若使用 64-bit `uint64_t`，则一次处理 64 个 bit positions。

### 10. XOR 的 AIG 示例 / XOR as an AIG

题目中的结构实现：

$$
x\oplus y=(x\land\overline y)\lor(\overline x\land y)
$$

而 OR 通过 De Morgan 转换：

$$
p\lor q=\overline{\overline p\land\overline q}
$$

所以最终输出 literal 为奇数，表示对最后一个 AND node 的结果取反。

## 最终答案汇总 / Final answer summary

| Exercise | Result |
|---|---|
| 1(a) detected fault | Only $l$ s-a-0 |
| 1(b) raw faults | 18 |
| 1(b) after EFC | 12 |
| 1(b) after course DFC | 11 |
| 2, pattern `1001` | $\{e/0,j/0\}$, 2 faults |
| 2, pattern `1111` | 18 faults |
| 2, combined | 20 of 44 faults |
| 3 negation | `result = result ^ UINT_MAX;` |
| 3 AND simulation | `tmp = l & r;` |
| 3 output storage | `current_valuation[and->lhs / 2] = tmp;` |

## 自检清单 / Self-check checklist

- 是否固定并标明 packed bit-column 顺序？
- 是否在 gate 正常计算后再注入 line fault？
- 是否用主输出与 good column 比较检测结果？
- 是否把 fanout stem 和 branches 分开计数？
- 演绎模拟中，多个 controlling inputs 是否取 intersection？
- 是否减去了 non-controlling input lists？
- 是否为每条 line 加入与 good value 相反的本地 stuck-at fault？
- C 代码中是否使用 bitwise `~`, `^`, `&`，而不是 logical `!`, `&&`？

