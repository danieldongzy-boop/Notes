# CPS I — Exercise Sheet 8
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong, Xin Pu

---
## Exercise 1: Invariant checking I
\(U=\emptyset,\pi=\emptyset\)
- DFS(S0,a) \(U=\{S_0\},\pi=\{S_0\}\)
  - DFS(S3,a)\(U=\{S_0,S_3\},\pi=\{S_0,S_3\}\)
    - DFS(S3,a)\(U=\{S_0,S_3\},\pi=\{S_0,S_3,S_3\}\)
    - DFS(S2,a)\(U=\{S_0,S_3,S_2\},\pi=\{S_0,S_3,S_2\}\)
      - DFS(S0,a)\(U=\{S_0,S_3,S_2\},\pi=\{S_0,S_3,S_2,S_0\}\)
- DFS(S1,a)\(U=\{S_1\},\pi=\{S_1\}\)
  - DFS(S3,a)\(U=\{S_1,S_3\},\pi=\{S_1,S_3\}\)
    - DFS(S3,a)\(U=\{S_1,S_3\},\pi=\{S_1,S_3,S_3\}\)
  - DFS(S4,a)\(U=\{S_1,S_4\},\pi=\{S_1,S_4\}\)
    - DFS(S3,a)\(U=\{S_1,S_4,S_3\},\pi=\{S_1,S_4,S_3\}\)
      - DFS(S3,a)\(U=\{S_1,S_4,S_3\},\pi=\{S_1,S_4,S_3,S_3\}\)

\(S_0,S_1,S_2,S_3 ⊨a\)
\(S_4 ⊭a\)
**\(S_0 ⊭ always \ a\)** counter example:S1,S4

## Exercise 2: Invariant checking II
![
](image-31.png)
\(\Phi={a} \)
The counterexample with non-minimal length S0,S1,S2
A counterexample of minimal length S0,S2

# Exercise 3: Invariants 
(a) No Idea
(b)
- \(\sigma=(\{a\}\emptyset)^\omega\)
  - For \(A_i=\{a\}\)  ,  \(\sigma=(\{a\}\{b\})^\omega\) , \(\sigma\in E\)
  -  For \(A_i=\emptyset\) , \(\sigma=(\emptyset)^\omega\) , \(\sigma\in E\)
-  \(\sigma=(\{a\}\{b\})^\omega\)
   -   For \(A_i=\{a\}\) , \(\sigma=\{a\}^\omega\) , \(\sigma\in E\)
   -   For \(A_i=\{b\}\) , \(\sigma=\{b\}^\omega\) , \(\sigma\in E\)
-  \(\sigma=(\{a\}\emptyset)^\omega\)
   -  For \(A_i=\{a\}\) , \(\sigma=\{a\},\{a\},\emptyset^\omega\) , \(\sigma\in E\)
   -  For \(A_i=\emptyset\) , \(\sigma=\{a\},\{a\},\emptyset^\omega\) , \(\sigma\in E\)