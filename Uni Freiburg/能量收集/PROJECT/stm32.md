\subsection{Microcontroller and LoRa SoC}

The \textbf{STM32WLE5CCU6} is selected as the system controller. It integrates a 48 MHz Arm Cortex-M4 microcontroller and a sub-GHz LoRa transceiver in a single device, replacing the separate MCU and SX1262 while reducing component count, PCB area, and weight.

\begin{table}[H]
\centering
\caption{STM32WLE5 Typical Power Consumption}
\label{tab:stm32wle5_power}
\small
\begin{tabular}{l c c}
\toprule
\textbf{Operating Mode} & \textbf{Typical Current} & \textbf{Approximate Power} \\
\midrule
Shutdown & $31\text{ nA}$ at $3\text{ V}$ & $0.093\text{ }\mu\text{W}$ \\
Standby with 32 kB RAM & $360\text{ nA}$ at $3\text{ V}$ & $1.08\text{ }\mu\text{W}$ \\
Stop 2 with RTC & $1.07\text{ }\mu\text{A}$ at $3\text{ V}$ & $3.21\text{ }\mu\text{W}$ \\
Low-Power Run at 2 MHz & $220\text{ }\mu\text{A}$ at $3\text{ V}$ & $0.66\text{ mW}$ \\
Run at 48 MHz, SMPS enabled & $3.45\text{ mA}$ at $3\text{ V}$ & $10.35\text{ mW}$ \\
LoRa Receive & $4.82\text{ mA}$ at $3\text{ V}$ & $14.46\text{ mW}$ \\
LoRa Transmit at $+14\text{ dBm}$ & $26\text{ mA}$ at $3.3\text{ V}$ & $85.8\text{ mW}$ \\
\bottomrule
\end{tabular}
\end{table}

During normal operation, the device remains in Stop 2 mode with the RTC enabled and wakes briefly for sensing and data handling. Assuming a \SI{50}{\milli\second} active interval in each one-minute cycle, the MCU energy consumption is

\begin{align*}
E_{\text{MCU}} &= (3.45\text{ mA})(3\text{ V})(0.05\text{ s}) \\
&\quad + (1.07\text{ }\mu\text{A})(3\text{ V})(59.95\text{ s}) \\
&\approx \SI{0.71}{\milli\joule\per\minute}.
\end{align*}

The selected UFQFPN48 package measures $7\text{ mm}\times7\text{ mm}\times0.6\text{ mm}$. Its mass is not specified by the manufacturer; a conservative engineering estimate of less than $0.2\text{ g}$ is used. The MCU contribution is therefore small compared with the GNSS energy consumption and the total collar mass.
