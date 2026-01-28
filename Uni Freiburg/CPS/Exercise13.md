# CPS I — Exercise Sheet 13
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong, Xin Pu

---
## Exercise 1：LTL Properties 
(a)satisfies
- $\{a\}\{b\}^\omega$
- $\{a\}\{a\}\{b\}^\omega$
-  $\{c\}\{b\}^\omega$
- $\{c\}\{a\}^\omega$
- $\{a\}^\omega$
- $\{c\}^\omega$

(b)violates
- $\{a\}^\omega$
- $\{a\}\{c\}^\omega$
- $\{a\}\{b\}^\omega$
- $\{a\}^\omega$
- $\{b\}^\omega$
- $\{c\}\{a\}^\omega$

(c)TS
- No, because $A_0 = \{b\}$ or $A_0 = \{a,c\}A_1 = \{a\}$ dont satisfy a and next b
- Yes, $s_1\xrightarrow{} s_2\xrightarrow{}(s_3\xrightarrow{})^\omega$
- No, because $s_1\xrightarrow{} s_2\xrightarrow{}(s_3\xrightarrow{})^\omega$ satisfies $aU□b$
- Yes, $s_1\xrightarrow{} s_2\xrightarrow{}(s_3\xrightarrow{})^\omega$ 
- Yes, $s_1\xrightarrow{} s_2\xrightarrow{}(s_3\xrightarrow{})^\omega$ 
- Yes, infinite c. $(s_1\xrightarrow{} s_2\xrightarrow{}s_3\xrightarrow{})^\omega$ 

(d)set comprehension
- $Words(\phi_1​)=\{A_0A_1...\in(2^{AP})^ω|a \in A_0​\land b \in A_1​\}$}
- $Words(\phi_2)=\{A_0A_1...\in(2^{AP})^ω|\exists k \in N.(b \in A_k \land \forall i<k.a\in A_i)\}\}$}
- $Words(\phi_3)=\{A_0A_1...\in(2^{AP})^ω|¬(\exists k \in N.(\forall j \ge k. b \in A_j) \land ( \forall i<k.a\in A_i))\}$}
- $Words(\phi_4)=\{A_0A_1...\in(2^{AP})^ω|\exists k \in N.(c \in A_k \land \forall i > k.a\in A_i)\}\}$}
- $Words(\phi_5)=\{A_0A_1...\in(2^{AP})^ω|\exists k \in N. \forall i \ge k.a\in A_i\}\}$}
- $Words(\phi_6)=\{A_0A_1...\in(2^{AP})^ω|\forall k \in N. \exists i \ge k.a\in A_i\}\}$}

## Exercise 2: Stating properties in LTL
(a)□¬(Peter.use∧Betsy.use)
(b)□(Peter.use→◊Peter.release)∧□(Betsy.use→◊Betsy.release)
(c)□(Peter.request→◊Peter.use)∧□(Betsy.request→◊Betsy.use)
(d)□(Peter.request→◊¬Peter.request)∧□(Betsy.request→◊¬Betsy.request)
(e)□((Peter.use→(¬Peter.useUBetsy.use))∧(Betsy.use→(¬Betsy.useUPeter.use))​)

## Exercise 3: From Set Notation to LTL
(a)φ1=◊(a∧◯b)
(b)No
(c)φ3​=□((a↔◯◯a)∧(b↔◯◯b))
(d)φ4​=□(a→◊b)