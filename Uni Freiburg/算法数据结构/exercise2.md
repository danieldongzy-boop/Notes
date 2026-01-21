# Algorithms and Datastructures — Exercise Sheet 2    
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong 6159975
---
## 1.O-notation
- a.true
\(2n^3 + 4n^2 + 7\sqrt{n} \leq 2n^3 + 4n^3 + 7n^3 = 13n^3\)
- b.false
\(\lim_{n \to \infty} \frac{n \log_3 n}{n \log_5 n} = \frac{\ln 5}{\ln 3} < \infty.\)
\(n \log_3 n = \Theta(n \log_5 n)\)
- c.true
\(\lim_{n \to \infty}\frac{2^n}{n!}=0\)  
- d.false
\(2\log_2(n^2) = 4\log_2 n\)
\(4\log_2 n \leq c \cdot (\log_2 n)^2\)。
- e.true
  - \(\max\{f(n), g(n)\} \leq f(n) + g(n)\)
  - \(\max\{a, b\} \geq \frac{a + b}{2}\) , \(\max\{f(n), g(n)\} \geq \frac{1}{2}(f(n) + g(n))\)

## 2.Sorting by asymptotic growth
- \(\sqrt{\log n}\)
- \(\log(\sqrt{n}) =_O (\log n) =_O (\log(n^3))\)
- \((\log n)^2\)
- \(\sqrt{n}\)
- \(10^{100}n\)
- \(n\log n\)
- \((2n)^2\)
- \(n^{100}\)
- \(2^n\)
- \(3^n\)
- \(n!\)
- \((n+1)!\)
- \(n^n\)
- \(2^{n^2}\)
## 3. Event Scheduling
**Greedy algorithm**
- Sort all events in non-decreasing order of their ending time t_i.
- For every next event, if i can attend(Timing doesnt conflict), then take the event.

For Greedy algorithm, the complexity is \(O(n \cdot log(n))\)
- Sorting: 
\(O(n \cdot log(n))\)
- Selection loop: 
\(O(n)\)