# CPS I — Exercise Sheet 6 
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong, Xin Pu

---
## Exercise 1: Executions, Paths and Traces
- (a)
  - \(s_1 \xrightarrow{\alpha} s_1\) 
  - \(s_0 \xrightarrow{\alpha} s_1\)
  - \(s_1 \xrightarrow{\alpha} s_1 \xrightarrow{\alpha} s_1 \dots\) (infinite)
  - \(s_0 \xrightarrow{\alpha} s_1 \xrightarrow{\alpha} s_1 \dots\) (infinite)
- (b) 
  - \( s_0 \xrightarrow{\alpha} s_1 \): Only 1 execution.
  - \( s_0 \xrightarrow{\beta} s_2 \): At each \( s_2 \), choose \( \beta \) (stay) or \( \gamma \) (go to \( s_3 \)).
**Infinitely many executions**.
- (c) 
**Infinitely many** 
- (d) 
  - Trace 1: \( \emptyset, \{a\}, \{a\}, \{a\}, \dots \) 
  - Trace 2 : \( \emptyset, \{b\}, \{b\}, \{b\}, \dots \) 
**2 traces** .
-  (e) Bonus
Yes, it is possible. 
Consider a single state \( s \) with two distinct self-loops on \( s \): \( s \xrightarrow{a} s \) and \( s \xrightarrow{b} s \) (where \( a \neq b \)).
   - **Only 1 path**: A path is an infinite sequence of states. Since there’s only one state \( s \), the only possible state sequence is \( s \to s \to s \to \dots \).
   - **Infinitely many executions**: At each step, we can choose either transition \( a \) or \( b \), leading to infinitely many distinct sequences 

## Exercise 2: Linear-Time Properties
- (a)
  - \( T_1 \) \( \{ A_0A_1A_2\ldots \mid A_0 = \{a\} \land A_1 = \{b\} \} \)
  - \( T_2 \) \( \{ A_0A_1A_2\ldots \mid \forall i \in \mathbb{N}.\ (i\text{ odd} \implies a \in A_i) \land (i\text{ even} \implies b \in A_i) \} \)
  - \( T_3 \) \( \{ A_0 A_1 A_2 \dots \mid \forall i\in \mathbb{N}.  (A_i = \emptyset \implies (a \in A_{i+1} \lor b \in A_{i+1})) \} \)
  - \( T_4 \) \( \{ A_0A_1A_2\ldots \mid A_0 = \{b\}  \}\)
  - \( T_5 \) \( \{ A_0A_1A_2\ldots \mid A_0 = \{a\} \land A_1 = \{a\} \} \land \{\exist k. \forall i > k. a \notin A_i\}\)
- (b)
  - \( T_1 \) \( \{ A_0A_1A_2\ldots \mid \forall i \in \mathbb{N}.\ a \in A_i \} \)
  - \( T_2 \) \( \{ A_0A_1A_2\ldots \mid \forall i \in \mathbb{N}.\ a \in A_i \} \)
  - \( T_3 \) \( \{ A_0A_1A_2\ldots \mid \forall i \in \mathbb{N}.\ a \in A_i \} \)
  - \( T_4 \) \( \{ A_0A_1A_2\ldots \mid \forall i \in \mathbb{N}.\ a \in A_i \} \)
  - \( T_5 \) \( \{ A_0A_1A_2\ldots \mid \exists i \in \mathbb{N}.\ a \in A_i \land b \in A_i \} \)

## Exercise 3: Starvation Freedom
* (a) \( \mathrm{LIVE'} \subseteq \mathrm{LIVE} \)

  If a trace \( \pi \in \mathrm{LIVE'} \), then for every \( i \in \mathbb{N} \):
  $$
  \text{if } \text{wait1} \in A_i \text{ then } \exists j \ge i\land \text{crit1} \in A_j
  $$
  and similarly for process 2.

  If \( \text{wait1} \) occurs infinitely often (\( \exists^\infty i. \text{wait1} \in A_i \)), then infinitely many corresponding \( j \) exist such that \( \text{crit1} \in A_j \).
  Hence:
  $$
  \pi \in \mathrm{LIVE}
  $$

* (b)
  Consider the trace:
  $$
  \pi = \{ \text{wait1} \}, \varnothing, \varnothing, \dots
  $$

  * **LIVE:**
    \( \text{wait1} \) occurs only once, so the antecedent of LIVE is false → implication holds →
    $$
    \pi \in \mathrm{LIVE}
    $$

  * **LIVE':**
    At \( i=0 \), \( \text{wait1} \in A_0 \) but there is no \( j \ge 0 \) with \( \text{crit1} \in A_j \) →
    $$
    \pi \notin \mathrm{LIVE'}
    $$

* (c) False
  In mutual exclusion algorithms with starvation freedom (semaphore or Peterson), every wait is eventually followed by crit.
  This means LIVE′ automatically holds

  
* (d) False
  The same reason in (a)
