# Algorithms and Datastructures — Exercise Sheet 4
**University of Freiburg · Winter Term 2025/26**

**Author:** Zhanyu Dong 6159975
---
## Exercise 1: Hashing with Open Addressing
(a)
- \( h_1(23) = 5 \mod 13 = 5 \)
- \( h_1(12) = 3 \mod 13 = 3 \)
- \( h_1(75) = 12 \mod 13 = 12 \)
- \( h_1(945) = 18 \mod 13 = 5 \)
\( i=1 \)：\( (5+1) \mod 13 = 6 \)
- \( h_1(30) = 3 \mod 13 = 3 \)
\( i=1 \)：\( (3+1) \mod 13 = 4 \)
- \( h_1(99) = 18 \mod 13 = 5 \)
\( i=2 \)：\( (5+2) \mod 13 = 7 \)
- \( h_1(345) = 12 \mod 13 = 12 \)
\( i=1 \)：\( (12+1) \mod 13 = 0 \)

| Index | 0    | 1 | 2 | 3  | 4  | 5  | 6    | 7  | 8 | 9 | 10 | 11 | 12  |
|------|------|---|---|----|----|----|------|----|---|---|----|----|-----|
| Key   | 345  | - | - | 12 | 30 | 23 | 945  | 99 | - | - | -  | -  | 75  |


(b)
- \( h_2 (23)=\)\( 69 \mod 13 = 4 \)
- \( h_2(12) \)\(= 36 \mod13 = 10 \)
- \( h_2(75) = 225 \mod13 = 4 \)
\( (4 +  75+1) \mod13 = 2 \)
- \( h_2(945) =2835 mod 13= 1 \)
- \( (h_2(30)) =90 mod 13= 12 \)
- \( (h_2(99)) =297 mod 13= 11 \)
- \( (h_2(345)) =1035 mod 13= 8 \)

| Index | 0 | 1    | 2  | 3 | 4  | 5 | 6 | 7 | 8    | 9 | 10  | 11  | 12  |
|------|---|------|----|---|----|---|---|---|------|---|-----|-----|-----|
| Key   | - | 945  | 75 | - | 23 | - | - | - | 345  | - | 12  | 99  | 30  |

## Exercise 2: Hashing with Chaining
 (a)
Assume for contradiction that every bucket has fewer than (y) elements
Then
\[\sum_{j=0}^{m-1} n_j \le m\cdot (y-1) = my - m < my\]
which contradicts \(|S|\ge my\).
Therefore the assumption is false
Take \(Y = B_j\). Then \(|Y| \ge y\) and every element of \(Y\) has the same hash value \(j\).


(b) 
So the worst-case time for find is proportional to the bucket size, i.e. at least \(\Omega(y)\).
In the extreme (all elements in one bucket), find can be \(\Theta(n)\) (linear time).
## Exercise 3: Application of Hashtables
(a) If the absolute difference between A(i) and A(j)=A(k) exist.

Total operations: \( O(n^3)\)

(b)
prestore all elements of \(A\) in a hash table first,for O(1) lookups.
Check pairwise differences:  
   - Loop \(i\) from 1 to n-1 (O(n) times).  
   - Loop \(j\) from 0 to i-1 (O(n) times per \(i\)).  
   - Compute \(diff = |A[i] - A[j]|\).  
   - Check if \(diff\) is in \(H\) (O(1) time per check). If yes, return true.   

(c)
Instead of a hash table, sort \(A\) first (O(n log n) time). Then for each \((i,j)\), compute \(diff = |A[i]-A[j]|\) and use binary search (O(log n) time) to check if \(diff\) exists in the sorted \(A\) 

