# Data converter

## Chapter 1 Background Elements

**1.Problem 4  Page 24**
**I am confused about the function, to remove  the quantization noise, why it is division instead of subtraction.**
 $$V^2_{n,budget}=\frac{V^2_{FS}}{24\cdot2^{24}}   (1)$$

 $$SNR=10lg\frac{Signal}{Quantum+Jitter+Thermal}(2)$$
 **Because you can not split the +/- in logarithmic（这里不知道用英语怎么表述，就是2式这里分母的加号不能写成lg相乘的形式）**

 ---
**2.Page 28**
**According to the book:One of the disadvantages of windowing is that it gives rise to spectral leakage.**
But without windowing there wil be more "spectral leakage", if the Nyquist and Sampling Periods are not propotional.

---
**Page 26**
**According to the book:The FFT algorithm reduces the number of computations from $N^2$ down to $N · log2(N)$. Therefore, for instance, with a series of 1024 points the computation time diminishes by a factor 10.
<font color="#dd0000">the factor is actually 100</font>**
$$ \frac{1024^2}{1024\cdot log2(1024)}=100$$






