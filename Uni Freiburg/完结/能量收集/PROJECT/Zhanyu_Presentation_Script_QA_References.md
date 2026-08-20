# Zhanyu - Presentation Script, Q&A, and References

Presentation date: 24 July 2026  
Target speaking time: about 5 minutes, including slide changes and pauses
Slides: PDF pages 13, 14, 16, 19, 21, and 22
Speaking note: present the English text only. The Chinese text is for understanding and rehearsal.

## Important PPT checks before the presentation

1. The system flowchart says that data is sent through the integrated LoRa radio, but the BOM also lists a separate SX1261. Confirm whether both devices are really required. The script below follows the current slides without claiming that either item can be removed.
2. The BOM reports a total weight of `370.9 mg`, but several row values appear to mix milligrams and grams. In particular, `0.3 mg` for the LC76G and `2.6 mg` for the LIR2032 are not plausible. Confirm the unit before presenting the total as a verified mass.
3. The BOM currently has no quantity, unit price, subtotal, unit mass, or total mass columns. This makes it unclear whether the `€65` TEG cost represents one module or the five-module array.
4. On the system flowchart, the single `1.8 V` label should ideally become `regulated 1.8 V and 3.0/3.3 V rails`, because the GNSS uses 1.8 V while the MCU figures use 3.0 or 3.3 V.
5. On the worst-case energy slide, the radio sleep energy should be about `0.017 mJ`, not `2.682 mJ`. The total radio energy, active plus sleep, is about `2.682 mJ`.

## Concise bilingual presentation script

### PDF page 16 - Power Management ICs (about 50 seconds)

**English**

Here we compare three power-management ICs. We selected the AEM30940 because it can cold-start from 380 millivolts at 3 microwatts, reaches about 80 to 90 percent efficiency, and provides two regulated outputs. This is suitable for our sensors and controller. With five TEGs and a temperature difference of five kelvin, the array produces about 14.66 milliwatts. After an assumed 90 percent conversion efficiency, about 13.19 milliwatts is available to the system.

**中文**

这里我们比较了三款电源管理芯片。我们选择 AEM30940，因为它可以在 3 微瓦输入功率、380 毫伏电压下冷启动，效率约为 80% 到 90%，并且能够提供两路稳压输出，适合我们的传感器和控制器。五片 TEG 在 5 开尔文温差下可以产生约 14.66 毫瓦功率。假设转换效率为 90%，系统最终可以获得约 13.19 毫瓦。

**Transition:** Next, I will compare the storage options and explain our selection.
**过渡：** 接下来我会比较储能方案，并说明我们的选择。

### PDF page 13 - Storage (about 45 seconds)

**English**

This slide compares two supercapacitors with the rechargeable LIR2032 button cell. The supercapacitors have the advantage of fast charging and a high cycle life, but their stored energy is very limited. Between 2 and 4.5 volts, the 0.1-farad device stores only about 0.81 joules, and the 0.06-farad device stores about 0.49 joules. In contrast, the 45-milliampere-hour LIR2032 at 3.6 volts stores about 583 joules. This much higher energy density allows it to buffer a GNSS acquisition and temporary periods of low harvested power. Therefore, we selected the LIR2032. Its cycle-life rating is below 400 cycles, so the final design should avoid deep discharge cycles and must use correct charge protection.

**中文**

这一页比较了两个超级电容和可充电的 LIR2032 纽扣电池。超级电容的优点是充电很快、循环寿命高，但储能非常有限。在 2 V 到 4.5 V 的工作范围内，0.1 F 电容只能储存约 0.81 J，0.06 F 电容只能储存约 0.49 J。相比之下，45 mAh、3.6 V 的 LIR2032 可以储存约 583 J。因此它能够缓冲一次 GNSS 定位和短时间的低采能阶段，所以我们选择 LIR2032。它的循环寿命低于 400 次，因此最终设计需要避免深度充放电，并正确设置充电保护。

**Transition:** The next slide quantifies how quickly each storage option can be charged.
**过渡：** 下一页量化比较这些储能器件的充电时间。

### PDF page 14 - Time to Charge (about 50 seconds)

**English**

Using the estimated PMIC output of 13.19 milliwatts, the two supercapacitors can be charged quickly from 2 to 4.5 volts: about 61.6 seconds for the 0.1-farad device and about 37 seconds for the 0.06-farad device. The LIR2032 stores much more energy, so charging it from empty takes about 12.28 hours in this ideal calculation. This calculation assumes that the full harvested power is available for charging and therefore represents the best case. After one GNSS burst, the cell has used approximately 0.139 coulombs. With an ideal charging current of about 3.66 milliamperes, the energy can be recovered in about 38 seconds. In practice, system consumption, battery losses, and changing temperature differences will make recovery slower.

**中文**

按照 PMIC 输出约 13.19 mW 计算，两个超级电容从 2 V 充到 4.5 V 很快：0.1 F 电容约需要 61.6 秒，0.06 F 电容约需要 37 秒。LIR2032 储能更多，因此从完全放电充满，在理想计算下约需要 12.28 小时。这里假设全部采集功率都用于充电，所以这是最佳情况。一次 GNSS burst 大约消耗 0.139 C 电量；在理想充电电流约 3.66 mA 下，理论上约 38 秒可以补回。实际恢复会更慢，因为系统本身也在耗电，电池和转换器存在损耗，而且温差会变化。

**Transition:** With the storage choice and charging behavior defined, the next slide shows how the complete system operates.
**过渡：** 明确了储能选择和充电行为后，下一页展示完整系统如何运行。

### PDF page 19 - System Operation Flowchart (about 55 seconds)

**English**

This flowchart has two parts. In the continuous energy path, five TEGs supply the AEM30940, which manages the rechargeable LIR2032 cell. In the data path, the real-time clock wakes the controller every minute. The controller reads the ADXL362, obtains a position from the LC76G, and stores both results. Normally, it then returns to Stop 2 mode. Every few days, the buffered data is transmitted to the base station. In this way, energy is harvested continuously, sensing happens every minute, and communication happens much less often.

**中文**

这个流程图分为两部分。在持续供能路径中，五片 TEG 为 AEM30940 供电，由它管理可充电的 LIR2032 电池。在数据路径中，实时时钟每分钟唤醒一次控制器。控制器读取 ADXL362 的活动数据，通过 LC76G 获取位置，并保存这两类信息。通常系统随后返回 Stop 2 模式。每隔几天，缓存的数据会发送到基站。因此，系统可以持续采集能量、每分钟进行一次测量，同时大幅降低通信频率。

**Transition:** Based on this design, the updated BOM is shown on the next slide.
**过渡：** 根据这一设计，下一页给出了更新后的物料清单。

### PDF page 21 - Bill of Materials (about 40 seconds)

**English**

The updated BOM lists seven commercial components: the activity sensor, GNSS module, LoRa transceiver, TEG harvester, power-management IC, rechargeable cell, and microcontroller. The total listed cost is 161 euros and 2 cents. The two largest cost items are the AEM30940 at 70 euros and the TEG harvester at 65 euros. Together, they account for most of the total cost. The table currently reports a total component weight of 370.9 milligrams, which is below the one-kilogram limit.

**中文**

更新后的 BOM 列出了七个商用部件：活动传感器、GNSS 模块、LoRa 收发器、TEG 能量采集器、电源管理芯片、可充电电池和微控制器。清单中的总成本为 161.02 欧元。其中成本最高的是 70 欧元的 AEM30940 和 65 欧元的 TEG 能量采集器，两者占总成本的大部分。表格目前给出的部件总重量为 370.9 毫克，低于 1 千克的限制。

**Transition:** Finally, these are the main sources used for our component data.
**过渡：** 最后，这些是我们获取部件数据时使用的主要资料来源。

### PDF page 22 - References and conclusion (about 35 seconds)

**English**

Our component values mainly come from manufacturer datasheets and official product pages. They provide the electrical limits, power consumption, start-up conditions, and package information used in our calculations. The main conclusion is that, at the assumed five-kelvin temperature difference, about 13.19 milliwatts is available after conversion, compared with an estimated average demand of about 8.3 milliwatts. The key remaining risk is whether this temperature difference can be maintained across the TEG in real outdoor conditions.

**中文**

我们的部件参数主要来自制造商数据手册和官方网站。这些资料提供了计算中使用的电气限制、功耗、启动条件和封装信息。主要结论是：在假设温差为 5 开尔文时，转换后可获得约 13.19 毫瓦，而系统的估算平均需求约为 8.3 毫瓦。剩余的主要风险是，在真实户外环境中能否在 TEG 两端维持这一温差。

**Closing:** Thank you. We are happy to answer your questions.
**结束语：** 谢谢。我们很乐意回答大家的问题。

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

The current slides are inconsistent: the flowchart uses the STM32WLE5 integrated radio, while the BOM also lists an SX1261. If the integrated radio is used, the separate SX1261 is normally unnecessary. The team should confirm the final radio architecture before the presentation and then use the same choice in the flowchart, energy calculation, and BOM.

### 10. Why do the slides show different LoRa transmit powers?

They refer to different transmit-power operating points. The STM32WLE5 value of 85.8 milliwatts is calculated for plus 14 dBm output, while a value above 200 milliwatts corresponds to a higher-power transmit mode. The link budget should determine which mode is required, and the final energy calculation must use that same mode consistently.

### 11. Why is the GNSS energy much larger than the other loads?

The LC76G is assumed to consume 33 milliwatts for 15 seconds, which is 495 millijoules per fix. This dominates the one-minute energy budget. The controller, accelerometer, and scheduled LoRa transmission are much smaller. Assisted GNSS, warm starts, adaptive fix intervals, or motion-triggered fixes could reduce this load substantially.

### 12. Can the PMIC directly supply the GNSS and radio current peaks?

The storage cell supplies short high-power peaks, while the harvester replenishes the stored energy over time. The AEM30940 high-voltage output is rated up to 80 milliamps, but the peak-current path, output capacitors, battery internal resistance, and voltage droop must still be verified on the prototype.

### 13. Why upload only every few days?

Buffering data reduces the number of radio start-ups and transmissions. A one-minute record is small, so several days of data fit easily in local non-volatile memory and in a LoRa packet sequence. The exact upload interval is a trade-off between energy, memory, and acceptable data-delivery latency.

### 14. Is the system really below 1000 g?

The current BOM reports 370.9 milligrams, but its row values appear to mix milligrams and grams, so this total is not yet reliable. The final proof must use consistent units and include quantities, the enclosure, antennas, wiring, thermal spreader or heat sink, collar, and attachment hardware.

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
