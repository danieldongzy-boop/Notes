# Zhanyu - Presentation Script, Q&A, and References

Presentation date: 24 July 2026  
Target speaking time: about 5 minutes  
Slides: PDF pages 16, 18, 19, 21, and 22

## Final checks before export

1. On the Power Management slide, change `38 mV @ 3 uW` to `380 mV @ 3 uW`. The e-peas specification states a 380 mV cold start and harvesting from 50 mV only after startup.
2. Use one radio architecture consistently. The current deck selects the discrete SX1261 on slide 6, but the final system uses the STM32WLE5 with an integrated LoRa radio. The recommended final architecture is STM32WLE5 without a separate SX1261 in the BOM. The SX1261 can remain on the comparison slide, but should not be labelled as the selected module.
3. On the system flowchart, replace the single `1.8 V` label with `regulated 1.8 V and 3.0/3.3 V rails`. The GNSS uses 1.8 V, while the MCU power figures shown on slide 16 were calculated at 3.0 or 3.3 V.
4. In the worst-case energy calculation, the radio sleep energy is about `0.017 mJ`, not `2.682 mJ`. The complete radio energy, active plus sleep, is about `2.682 mJ`.
5. The complete one-minute system energy is about `500 mJ/min`, not only 495 mJ. This includes GNSS active and standby energy, the radio, the accelerometer, and the MCU, but still excludes some board-level losses and PMIC quiescent current.
6. The BOM should contain quantity, unit price, subtotal, unit mass, and total mass. Do not include both STM32WLE5 and SX1261 as required parts if the integrated-radio architecture is used.

## Five-minute presentation script

### Slide 12 - Power Management ICs (about 65 seconds)

The power-management IC is the interface between the thermoelectric generator, the rechargeable storage element, and the electronic load. We compared three commercial devices. The LTC3108-1 has the lowest start-up voltage, but it needs an external transformer and its reported efficiency is much lower. The BQ25505 is efficient, but its cold-start voltage is at least 600 millivolts. We therefore selected the e-peas AEM30940. It can cold-start from 380 millivolts at 3 microwatts, supports maximum-power-point tracking, and provides two regulated output rails. This is useful because the GNSS operates at 1.8 volts, while the controller and radio can use a higher rail. At a five-kelvin temperature difference, our five-TEG array produces about 14.66 milliwatts at its maximum-power point. Assuming 90 percent conversion efficiency, approximately 13.2 milliwatts is available to the system.

Transition: With the power path defined, the next step is to minimize the number of active electronic components.

### Slide 16 - Microcontroller (about 55 seconds)

For the controller, we selected the STM32WLE5CCU6. It combines a 48-megahertz Arm Cortex-M4 processor and a sub-gigahertz LoRa radio in one package. This removes the need for a separate microcontroller and SX1261 transceiver, reducing PCB area, mass, cost, and standby losses. Most of the time, the controller remains in Stop 2 mode with the real-time clock active, where it consumes about 3.21 microwatts at 3 volts. We assume only 50 milliseconds of processor activity in each one-minute cycle. Under this assumption, the controller consumes approximately 0.71 millijoules per minute, which is very small compared with the roughly 495-millijoule GNSS acquisition. The integrated radio is activated only during the scheduled upload every few days.

Transition: These low-power states are coordinated by the operating sequence shown on the next slide.

### Slide 17 - System Operation Flowchart (about 70 seconds)

This flowchart combines the continuous energy path with the duty-cycled data path. Five TEG modules are connected in series to raise the voltage, and the AEM30940 extracts energy and manages the rechargeable LIR2032 storage cell. The PMIC then provides regulated rails for the electronics. Every minute, the real-time clock wakes the STM32WLE5. The controller reads the ADXL362, requests a position fix from the LC76G, and stores the activity and position record locally. It then checks whether the upload interval has been reached. Normally, it immediately returns to Stop 2 mode. Every few days, it sends the buffered data through the integrated LoRa radio before returning to sleep. This architecture separates a relatively expensive GNSS event from infrequent communication, while energy is harvested continuously and the battery supplies short power peaks.

Transition: The same architecture determines which components and quantities appear in the final BOM.

### Slide 19 - Bill of Materials (about 55 seconds)

The bill of materials contains only commercially available components, as required. The main functional parts are five thermoelectric generators, one AEM30940 power-management IC, one LIR2032 rechargeable cell, one ADXL362 accelerometer, one LC76G GNSS module, and one STM32WLE5 controller with integrated LoRa. The final table also includes the antenna, passives, PCB, thermal interface, heat spreader, enclosure, and collar attachment, because these items affect both cost and mass. The main cost drivers are the TEG array and the GNSS and radio hardware, while the integrated controller reduces component count. Based on the completed BOM, the component total is [TOTAL COST] and the estimated complete mass is [TOTAL MASS], leaving a margin below the one-kilogram requirement.

Fallback if the final total is not ready: replace the last sentence with: `The final supplier prices are still being consolidated, but the architecture already minimizes component count and remains comfortably below the one-kilogram mass limit.`

Transition: Finally, all component values and design assumptions are traceable to the following sources.

### Slide 20 - References and conclusion (about 45 seconds)

These references are primarily manufacturer datasheets and official product pages. They provide the electrical limits, operating currents, start-up conditions, package sizes, and storage specifications used in our comparisons and energy calculations. We use distributor pages only where a manufacturer page is not readily available for the exact commercial storage component. The key result is that the proposed system is electrically energy-positive at the assumed five-kelvin temperature difference: about 13.2 milliwatts is available after conversion, compared with an estimated average system demand of about 8.3 milliwatts. However, the temperature difference must exist across the TEG itself. Therefore, the thermal interface and outdoor validation remain the most important practical risks.

Closing sentence: Thank you. We are happy to answer your questions.

## Likely questions and concise answers

### 1. Why did you select the AEM30940 instead of the LTC3108-1?

The LTC3108-1 starts from a lower voltage, but it requires an external transformer and has lower conversion efficiency in our comparison. With five TEGs in series at a five-kelvin temperature difference, the matched-load voltage is about 485 millivolts, which is above the AEM30940 cold-start requirement of 380 millivolts. The AEM30940 also provides MPPT, storage protection, and two regulated output rails.

### 2. What happens if the temperature difference is below 5 K?

TEG power approximately scales with the square of the temperature difference. At 2.5 K, the raw power would be about one quarter of the 5 K value, so the energy budget would no longer close. The battery can bridge short low-gradient periods, but it cannot compensate indefinitely. This is why the thermal contact and field-measured temperature difference are the main feasibility risks.

### 3. Is 5 K the difference between the animal body and the ambient air?

No. It must be the temperature difference directly across the two ceramic faces of the TEG. Fur, skin contact, the thermal interface, and the heat sink all reduce the actual gradient. A prototype must measure both TEG surface temperatures under realistic outdoor conditions.

### 4. How do you demonstrate operation for two years?

The two-year lifetime is based on energy autonomy rather than the battery capacity alone. At the 5 K design point, harvested power is approximately 13.2 milliwatts after conversion, while the calculated average load is about 8.3 milliwatts. The battery only buffers power peaks and temporary energy deficits. A final two-year claim would still require seasonal thermal data, leakage and aging models, and long-duration field testing.

### 5. How long can the LIR2032 operate without harvesting?

Its nominal energy is about 583 joules. At an average load of roughly 8.3 milliwatts, the ideal autonomy is approximately 19 hours. The practical value is lower because of converter losses, voltage limits, temperature, and battery aging. It is a short-term buffer, not a multi-day backup source.

### 6. Why use a battery instead of the supercapacitors?

The LIR2032 stores about 583 joules, compared with roughly 1.51 joules for the 0.1-farad capacitor and 0.91 joules for the 0.06-farad capacitor at their rated voltage. The battery therefore provides much better energy density and can support the GNSS bursts and periods of weak harvesting. The trade-off is finite cycle life and the need for correct charge protection.

### 7. Does a rating below 400 cycles mean the battery fails before two years?

Not necessarily, because the system should perform shallow charge-discharge cycles rather than one full cycle every minute. However, the exact two-year life cannot be guaranteed from the nominal cycle rating alone. Depth of discharge, temperature, charge voltage, and calendar aging must be validated.

### 8. Why are five TEGs connected in series?

The series connection raises the voltage. At 5 K, one module produces about 194 millivolts open circuit, while five produce about 970 millivolts open circuit and about 485 millivolts at the maximum-power point. This enables the AEM30940 to cold-start while keeping the array compact.

### 9. Why use STM32WLE5 if an SX1261 was already selected?

The final architecture should use only the STM32WLE5 integrated radio. The SX1261 slide is useful as a radio comparison, but a separate SX1261 should not be included in the final BOM. Integrating the radio reduces component count, mass, PCB area, and interface overhead.

### 10. Why do the slides show different LoRa transmit powers?

They refer to different transmit-power operating points. The STM32WLE5 value of 85.8 milliwatts is calculated for plus 14 dBm output, while a value above 200 milliwatts corresponds to a higher-power transmit mode. The link budget should determine which mode is required, and the final energy calculation must use that same mode consistently.

### 11. Why is the GNSS energy much larger than the other loads?

The LC76G is assumed to consume 33 milliwatts for 15 seconds, which is 495 millijoules per fix. This dominates the one-minute energy budget. The controller, accelerometer, and scheduled LoRa transmission are much smaller. Assisted GNSS, warm starts, adaptive fix intervals, or motion-triggered fixes could reduce this load substantially.

### 12. Can the PMIC directly supply the GNSS and radio current peaks?

The storage cell supplies short high-power peaks, while the harvester replenishes the stored energy over time. The AEM30940 high-voltage output is rated up to 80 milliamps, but the peak-current path, output capacitors, battery internal resistance, and voltage droop must still be verified on the prototype.

### 13. Why upload only every few days?

Buffering data reduces the number of radio start-ups and transmissions. A one-minute record is small, so several days of data fit easily in local non-volatile memory and in a LoRa packet sequence. The exact upload interval is a trade-off between energy, memory, and acceptable data-delivery latency.

### 14. Is the system really below 1000 g?

The electronic components are far below the limit, but the final proof must include the enclosure, antennas, wiring, thermal spreader or heat sink, collar, and attachment hardware. The BOM should therefore include both unit mass and extended mass, followed by a mechanical contingency margin.

### 15. What is the biggest unresolved risk?

The biggest risk is not the electrical conversion circuit; it is maintaining a sufficient temperature difference directly across the small TEG array on a moving animal in changing weather. The next engineering step is a thermal prototype with logged hot-side and cold-side temperatures, followed by a measured daily energy balance.

## Reference slide - ready-to-paste content

Do not display raw tracking URLs. Use the short titles below as hyperlink text. A two-column layout with references 1-7 on the left and 8-14 on the right will fit on one slide more clearly than the current long URLs.

### Left column

1. Bosch Sensortec, *BMA280 Data Sheet*  
   https://www.edn.com/wp-content/uploads/bst-bma280-ds000.pdf
2. STMicroelectronics, *LIS2DH12 Data Sheet*  
   https://www.st.com/resource/en/datasheet/lis2dh12.pdf
3. Analog Devices, *ADXL362 Data Sheet*  
   https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL362.pdf
4. Quectel, *LC76G Series GNSS Module*  
   https://www.quectel.com/product/gnss-lc76g-series/
5. u-blox, *MAX-M10 Series GNSS Module*  
   https://www.u-blox.com/en/product/max-m10-series
6. Semtech, *SX1261 Low-Power LoRa Transceiver*  
   https://www.semtech.com/products/wireless-rf/lora-connect/sx1261
7. STMicroelectronics, *STM32WLE5CC Data Sheet*  
   https://www.st.com/resource/en/datasheet/stm32wle5cc.pdf

### Right column

8. TEC Microsystems, *1MD06-097-05 TEG*  
   https://www.tec-microsystems.com/product/1md06-097-05/
9. e-peas, *AEM30940 Energy-Harvesting PMIC*  
   https://e-peas.com/product/aem30940/
10. Texas Instruments, *BQ25505 Energy-Harvesting Battery Manager*  
    https://www.ti.com/product/BQ25505
11. Analog Devices, *LTC3108-1 Ultralow-Voltage Converter*  
    https://www.analog.com/en/products/ltc3108-1.html
12. RS, *NEXT104Z5.5V11.5X8.5F Supercapacitor*  
    https://de.rs-online.com/web/p/superkondensatoren/7374430
13. KYOCERA AVX, *BZ015B603ZSB Supercapacitor*  
    https://www.digikey.com/en/products/detail/kyocera-avx/BZ015B603ZSB/2506228
14. VOLTCRAFT, *LIR2032 Rechargeable Cell, 45 mAh*  
    https://www.conrad.com/en/p/voltcraft-lir2032-button-cell-rechargeable-lir2032-lithium-45-mah-3-6-v-1-pc-s-2542816.html

Accessed: 22 July 2026.

Optional background source for the feasibility discussion:

15. Baeumker et al., *A Fully Featured Thermal Energy Harvesting Tracker for Wildlife*, Energies 2021.  
    https://doi.org/10.3390/en14196363

## Numbers to remember

- Five TEGs at 5 K: `Voc = 0.970 V`, matched-load voltage `about 0.485 V`, raw `Pmax = 14.66 mW`.
- AEM30940 output at 90% assumed efficiency: `about 13.19 mW`.
- Estimated complete load: `about 500 mJ/min`, or `about 8.3 mW average`.
- Estimated power margin at 5 K: `about 4.9 mW`, before unmodelled board-level losses.
- LIR2032 nominal energy: `45 mAh x 3.6 V = 162 mWh = 583 J`.
- Ideal no-harvest autonomy: `about 19 h`; practical autonomy is lower.
- STM32WLE5 MCU energy: `about 0.71 mJ/min` under the stated 50 ms active-time assumption.
- GNSS acquisition: `495 mJ` per assumed 15-second fix; it dominates the energy budget.
