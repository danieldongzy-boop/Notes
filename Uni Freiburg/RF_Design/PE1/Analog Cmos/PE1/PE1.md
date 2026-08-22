### T1: DC Analysis, DC Sweep, Parameter Sweep
#### Hand Calculation
1. Calculate the signal transfer function
$${\frac{V_{\text{out}}}{V_{\text{in}}} = \frac{R_2}{R_1 + R_2}}$$
2. $$V_{out}=0.5V_{in}$$

| Vin (V)  | 0.1  | 0.2  | 0.3  | 0.4  | 0.5  | 0.6  | 0.7  | 0.8  | 0.9  | 1.0  |
| -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Vout (V) | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | 0.35 | 0.40 | 0.45 | 0.50 |

|Vin​(V)|1.1|1.2|1.3|1.4|1.5|1.6|1.7|1.8|1.9|2.0|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Vout​(V)|0.55|0.60|0.65|0.70|0.75|0.80|0.85|0.90|0.95|1.00|

|Vin​(V)|2.1|2.2|2.3|2.4|2.5|2.6|2.7|2.8|2.9|3.0|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Vout​(V)|1.05|1.10|1.15|1.20|1.25|1.30|1.35|1.40|1.45|1.50|

|Vin​(V)|3.1|3.2|3.3|
|:--|:-:|:-:|:-:|
|Vout​(V)|1.55|1.60|1.65|
3. $$V_{out}=3.3V\frac{R_2}{1k \Omega +R_2}$$

| R2       |  1   |  2   |   3   |  4   |  5   |   6    |   7    |   8    |  9   | 10  |
| :------- | :--: | :--: | :---: | :--: | :--: | :----: | :----: | :----: | :--: | :-: |
| Vout​(V) | 1.65 | 2.20 | 2.475 | 2.64 | 2.75 | 2.8286 | 2.8875 | 2.9333 | 2.97 | 3.0 |

#### Cadence Verify
b
![[Pasted image 20260507102359.png]]
c
![[Pasted image 20260507103509.png]]

### T2: Transient Analysis, AC-Analysis
1. Transfer function $$H(s)=\frac{\frac{1}{sC}}{R+\frac{1}{sC}}=\frac{1}{1+sRC}=\frac{1}{1+j\omega RC}$$
Magnitude$$|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega RC)^2}} = \frac{1}{\sqrt{1 + (2\pi f RC)^2}}$$
Phase
$$\angle H(j\omega) = 0 - \arctan\left(\frac{\omega RC}{1}\right) = -\arctan(\omega RC)$$
2. -3db cut-off frequency
Cut-off frequency is defined as the frequency at which the magnitude of the circuit's frequency response drops to $1/\sqrt{2} \approx 0.707$ times its DC gain
$$|H(j\omega_c)| = \frac{1}{\sqrt{2}}$$
$$\omega_c RC = 1 \implies \omega_c = \frac{1}{RC}$$
$$f_c = \frac{1}{2\pi RC}$$

$$RC = 12.5 \times 10^3 \times 8 \times 10^{-12} = 10^{-7}\,\text{s}$$

$$f_c = \frac{1}{2\pi \times 10^{-7}} \approx 1.59\,\text{MHz}$$
3. Sketch 
ac
$$f_c = 1.588\,\text{MHz}$$
$$Phase shift \approx -45deg$$
![[Pasted image 20260508110405.png]]tran
![[Pasted image 20260508102442.png]]
### T3: Transistor Transfer Characteristic Curve
1. Simulate the ID versus UDS characteristic
![[Pasted image 20260508114025.png]]
2. $${\lambda = \frac{I_{D2}-I_{D1}}{I_{D1}V_{DS2} - I_{D2}V_{DS1}}}$$
3. 
- For short channel L=0.35um,$\lambda$ is higher because of stronger channel length modulation.
- The higher the Vgs, the bigger the $\lambda$.
    

