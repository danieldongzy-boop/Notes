# CPS I — Exercise Sheet 11
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong, Xin Pu

---
## Exercise 1: Safety-Liveness Decomposition
1. \(P_{1safe}=P_1\)    
   \(P_{1live}=\Sigma ^\omega\)
   \(P_{1safe} ∩P_{1live}=P_1\)
2. \(P_{2safe}=\Sigma ^\omega\)
   \(P_{2live}=P_2\) 
   \(P_{2safe} ∩P_{2live}=P_2\)
3. \(P_{3safe}
​
 =\{σ\in \Sigma ^\omega∣∣{i∣a∈A 
i
​
 }∣≤3\}\) 
 \(P_{3live}=P_3\)
 \(P_{3safe} ∩P_{3live}=P_3\)
4. \(P_{4safe}=\{\sigma \in \Sigma ^\omega \mid a \in A_0\}\)
   \(P_{4live}
 =\{σ\in \Sigma ^\omega∣∀i\in N \  ∃j>i\ a∈A_j
 \}\)
   \(P_{4safe} ∩P_{4live}=P_4\)
5. \(P_{5safe}=\Sigma ^\omega\)
   \(P_{5live}=\Sigma ^\omega\)
   \(P_{5safe} ∩P_{5live}=P_5\)

## Exercise 2: Satisfaction under Fairness Assumptions
1. - fair execution：$ s_0 \xrightarrow{\alpha} s_4 \xrightarrow{\beta} (s_5 \xrightarrow{\gamma} s_5)^\omega $
   - unfair execution:$(s_0 \xrightarrow{\eta} s_1\xrightarrow{\eta} s_3\xrightarrow{\eta} s_0)^\omega$
2. - fair execution：Not exist
   - unfair execution:$ s_0 \xrightarrow{\alpha} s_4 \xrightarrow{\beta} (s_5 \xrightarrow{\gamma} s_5)^\omega $
3. - fair execution:$ (s_0 \xrightarrow{\alpha} s_4  \xrightarrow{\delta} s_0 )^\omega$
   - unfair execution:$(s_0 \xrightarrow{\eta} s_1\xrightarrow{\eta} s_3\xrightarrow{\eta} s_0)^\omega$
4. - fair execution: $(s_0 \xrightarrow{\eta} s_1\xrightarrow{\eta} s_3\xrightarrow{\eta} s_0)^\omega$(not enabled)
   - unfair execution:$ (s_0 \xrightarrow{\alpha} s_4  \xrightarrow{\delta} s_0 )^\omega$
5. - fair execution: $s_0 \xrightarrow{\eta} (s_1\xrightarrow{\delta} s_2\xrightarrow{\delta} s_1)^\omega$(not enabled)
   - unfair execution:$ (s_0 \xrightarrow{\alpha} s_4  \xrightarrow{\delta} s_0 )^\omega$
6. - fair execution: $ s_0 \xrightarrow{\alpha} s_4 \xrightarrow{\beta} (s_5 \xrightarrow{\gamma} s_5)^\omega $(not enabled)
   - unfair execution:$ (s_0 \xrightarrow{\alpha} s_4  \xrightarrow{\delta} s_0 )^\omega$
7. - fair execution:$(s_0 \xrightarrow{\eta} s_1\xrightarrow{\eta} s_3\xrightarrow{\eta} s_0)^\omega$
   - unfair execution: $s_0 \xrightarrow{\eta} (s_1\xrightarrow{\delta} s_2\xrightarrow{\delta} s_1)^\omega$
8. - fair execution: $ s_0 \xrightarrow{\alpha} s_4 \xrightarrow{\beta} (s_5 \xrightarrow{\gamma} s_5)^\omega $(not enabled)
   - unfair execution: $s_0 \xrightarrow{\eta} (s_1\xrightarrow{\delta} s_2\xrightarrow{\delta} s_1)^\omega$

(1)and (2)satisfy property "eventually a"