Arijeet Dutta
Partha Sarthi Bhattacharya
Zhanyu Dong 
## Task2

1. Number 2.) In theory: Independent of its length. It is only determined by the geometry(a, b) and material parameters (L, C)
$$Z0=\sqrt{\frac{L}{C}}$$​​
In practice the Z0 is still independent of the length however it is depended on the frequency of the signal (omega)

$$Z0 = \sqrt{{(R+jwL)/(G+jwC)}}$$
2. Number 3.)Yes.  Electrical length is frequency dependent.
3. Number 5:)
$$Z_0 = \frac{60}{\sqrt{\varepsilon_r}} \ln\left(\frac{b}{a}\right)$$
- $D_o = 6.66 \,\text{mm}$
4. Number 6 :)Ground to Ground Spacing is $2W+G=16.08\mu m$
5. Number 8:)$70Ω：W=30\mu m$
$30Ω：W=178\mu m$
---
## Task3
1. Number2:) ![[Pasted image 20260428163545.png]]![[Pasted image 20260428163822.png]]
2. Number3:)
- Linecalc only calculates transmission line parameters
- Momentum performs full EM field simulation
- Structures: bends, junctions or coupled lines
3. Number4:)
 A transmission line transforms the load impedance depending on its characteristic impedance and electrical length.
 A transmission line introduces a phase shift to the traveling wave proportional to the line length and wavelength.
 A transmission line can cause reflections if the load impedance does not match the characteristic impedance of the line.
4. Number5:)![[Pasted image 20260505171056.png]]
- The resonating behavior is caused by standing waves due to reflections along the transmission lines
- Line length is a multiple of λ/2(maxima)
- λ/4(minima)
5. Number7:)![[Pasted image 20260505173251.png]]
![[Pasted image 20260505173336.png]]
- S(1,3) shows stronger crosstalk because the lines are physically closer and have stronger electromagnetic coupling
- S(1,10) is weaker due to larger distance
6. Number8:)
$$P_{out} = P_{in} \cdot |S(10,1)|^2$$
$$S(10,1)_{max}=-32.15db$$
$$P_{out} = 6.1mW$$
7. Number9:)
- directional coupler
- high-speed circuit
---
## Task4
1. Number 3:)
![[Pasted image 20260511073628.png]]
- A pure inductor shows an impedance increasing with frequency.
- Ideally, the inductor has no resistive loss or parasitic capacitance.
- The phase response should remain close to +90 degrees.
2. Number 4:)
![[Pasted image 20260511073536.png]]
- The Momentum simulation deviates from the compact model at higher frequencies.  
- The EM simulation shows additional loss and parasitic effects.  
- The compact model behaves more ideally than the full electromagnetic simulation.
3. Number5:)
- The layout introduces parasitic capacitances and coupling effects.
- Metal losses and substrate losses are included in the Momentum simulation.
- The compact model is simplified and cannot fully represent distributed electromagnetic behavior.
4. Number6:)
![[Pasted image 20260511073414.png]]
![[Pasted image 20260511073421.png]]
- The Momentum simulation shows higher losses than the schematic simulation.  
- The bends and discontinuities introduce additional parasitic effects.  
- Electromagnetic coupling and radiation are only captured in the EM simulation.
---
## Task5
1. Number 2:)
    4 ports
	- Port1: Input 
	- Port2: Through
	- Port3: Coupled
	- Port4: Isolated
    Quantities
     - Coupling
     - Insertion loss
     - Directivity
2. Number3:)
    ![[Pasted image 20260511142606.png]]
    Maximal we can get -8db
    ![[Pasted image 20260509223554.png]]
3. Number4:)
![[Pasted image 20260509224351.png]]
4. Number5:)
![[Pasted image 20260511073745.png]]