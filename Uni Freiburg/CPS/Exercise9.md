# CPS I — Exercise Sheet 9
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong, Xin Pu

---
## Exercise 1: Prefixes and Closure I
(a)
- Take arbitrary \(\pi \in P\)
- Take any finite prefix \(\sigma\) of \(\pi\), \(\sigma \in pref(\pi)\)
- \(pref(P)=⋃ _{τ∈P}
 pref(τ)\)
- \(pref(\pi)⊆pref(P)\)
- \(\pi \in cl(P)\)
- \(P \subseteq cl(P)\)

(b)
(1) From (a) we know\(P \subseteq cl(P)\), so \(pref(P) \subseteq pref(cl(P))\)
(2)
- Let \(\sigma \in pref(cl(P))\), there exists \(\pi \in cl(P)\)
- \(pref(\pi)\in pref(P)\)
- \(\sigma\in pref(P)\)
- \(pref(cl(P)) \subseteq pref(P)\)

So from (1) and (2)  \(pref(cl(P)) = pref(P)\)

(c)
(1)From (a) we know that \(P \subseteq cl(P)\). Let P be \(cl(P)\), so \(cl(P) \subseteq cl(cl(P))\)
(2)
- Take arbitrary \(\pi \in cl(cl(P))\)
- \(\sigma \in \pi\)
- \(\sigma \in pref(cl(P))\)
- According to (b) \(pref(cl(P)) = pref(P)\)
- \(\sigma \in pref(P)\)
- \(\pi \in cl(P)\)
- so \(cl(cl(P) \subseteq cl(P)  )\)

So from (1) and (2) \(cl(cl(P) = cl(P)  )\)

## Exercise 2: Prefixes and Closure II 
1. (a)
$$
P_1 = \left\{ A_0 A_1 A_2 \cdots \in (2^{AP})^\omega \ \middle| \ \exists k \in \mathbb{N},\ a \in A_k \ \land (\ \forall j \in \mathbb{N},\ j \neq k \implies a \notin A_j )\right\}
$$

(b)