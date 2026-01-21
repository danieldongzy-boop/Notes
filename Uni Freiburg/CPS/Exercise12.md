# CPS I — Exercise Sheet 12
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong, Xin Pu

---
## Exercise 1 :Done
## Exercise 2: Fairness
F1 : For (a) to (f) all false.
F2
a:Yes, it is not enabled.
b:Yes, $\delta$ is enabled and executed  
c.Yes, we have execution.$s_0 \xrightarrow{\beta} s_2 \xrightarrow{\delta} \left( s_1 \xrightarrow{\delta} s_2 \xrightarrow{\delta} \right)^\omega$ It satisfies weak fairness for $\delta$
d.No, $\delta$ is infinite enabled since $s_1$, but only execute only once.
e.Yes, the same in (c). We have execution.$s_0 \xrightarrow{\beta} s_2 \xrightarrow{\delta} \left( s_1 \xrightarrow{\delta} s_2 \xrightarrow{\delta} \right)^\omega$ It satisfies weak fairness for $\delta$
f.Yes, the same in (c). We have execution.$s_0 \xrightarrow{\beta} s_2 \xrightarrow{\delta} \left( s_1 \xrightarrow{\delta} s_2 \xrightarrow{\delta} \right)^\omega$ It satisfies weak fairness for $\delta$
F3:
a:Yes, not enabled.
b:No, infinite enabled but not executed.
c:Yes, we have execution$s_0\xrightarrow{\alpha}(s_1\xrightarrow{\gamma})^\omega$
d:Yes, infinite enabled and executed.
e:Yes, same in (d)
f:Yes, same in (d)
F4:
a:Yes
b:No,$\eta$ is infinite enabled but not executed.
c:No,$F4 = F2 \cap F3$ Even though F2 and F3 both satisfy (c), but in different executions.
d:No,$\delta$ infinite enabled but not execute.
e:Yes, execution$s_0\xrightarrow{\beta}s_2\xrightarrow{\eta}(s_3\xrightarrow{\eta})^\omega$
f: Yes, same in (e)

## Exercise 3: Fairness 
1. weak fairness for "enter"
- Sufficiency. "Enter" is always enabled in "w", we dont want it to do self loop on "w", so "Enter" must infinite execute.
- Weakest. Weak Fairness is the weakest. Without weak fairness for "enter", it will do self loop on "w".
2. Strong fairness for "enter"
-  Sufficiency. We dont want the case $(w_1\xrightarrow \  w_2\xrightarrow\ )^\omega$ If "Enter" is infinite enabled, it must infinite executed.
- Weakest. Weak fairness for "enter" is not possible. Because in the case $(w_1\xrightarrow \  w_2\xrightarrow\ )^\omega$ "Enter" is infinite enabled, but not always enabled.
3.  Not possible to give fairness assumption on action enter to ensure non-starvation？