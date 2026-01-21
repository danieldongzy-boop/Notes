# Algorithms and Datastructures — Exercise Sheet 5
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong 6159975
---
## Exercise 1: Bad Hash Functions
1. Keys 0-9 have 0；Keys 10-19 have 1... Which is **not uniform**
2. All the even Buckets are **wasted**
3. Out of the hash values: When m=10,x=0 or 9. \(x \  mod \ m + \frac{m}{x+1}=10\) **Out of Range**
4. This hash function is **not deterministic**.
5. x can not be 0
6. Single hash function is already good. It wastes Resources.
   
## Exercise 2: (No) Families of Universal Hash Functions
1. \(h(0)=h(m)=0\) Hence the hash function is not c-universal.
2. Assume \(\Sigma_0^k a_i x_i=\Sigma_0^k a_iy_i \ mod \ m\)
   means \(a_j x_j-a_j y_j=Constant \  mod \ m\)
   \(a_j (x_j-y_j)=Constant \ mod \ m \)
   \(x_j-y_j=\frac{Constant}{a_j} \ mod \ m \)
   \(\frac{Constant}{a_j} =1\)
   So only one \(a_j\) and a ∈ {1, ..., m − 1},so 1-universal