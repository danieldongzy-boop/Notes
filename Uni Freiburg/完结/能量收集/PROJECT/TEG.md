# Thermoelectric Generator Selection and Energy Budget

## 1. Fixed Electrical Load

The selected system components and operating cycle are fixed:

- Activity sensor: Analog Devices ADXL362
- GNSS: Quectel LC76G, active for 15 s every minute
- Radio: Semtech SX1262

| Load | Energy per day |
|---|---:|
| LC76G active and power-saving modes | 715.5864 J/day |
| ADXL362 active and standby modes | 0.0019 J/day |
| SX1262 transmit and sleep modes | 0.2412 J/day |
| **Total lower-bound load** | **715.8295 J/day** |

The corresponding average power is

```text
Pload = 715.8295 J / 86400 s = 8.285 mW.
```

This value does not yet include the MCU, memory, power-management quiescent current, or storage losses. The 500 mJ buffer only supports one 495 mJ GNSS event; it does not prove daily energy neutrality.

## 2. Selected Commercial TEG

The proposed module is the **TECTEG TEG2-126LDT**, which is designed for low-temperature-difference body and sensor harvesting.

| Parameter | Value |
|---|---:|
| Module size | 40 x 40 x 5.45 mm |
| Test temperatures | Th = 40 degC, Tc = 30 degC |
| Module temperature difference | 10 K |
| Matched-load voltage | 0.2 V |
| Matched-load current | 45 mA |
| Matched-load power | 9 mW |

For the theoretical low-temperature range, power is approximated by

```text
PTEG(DeltaT) = 9 mW x (DeltaT / 10 K)^2.
```

## 3. Proposed TEG Array

The proposed array uses **four TEG2-126LDT modules** in a 2-series, 2-parallel configuration. A 70% average power-conversion efficiency is assumed.

At the selected theoretical design point of `DeltaTTEG,rms = 7 K`:

```text
Power per module = 9 x (7/10)^2 = 4.41 mW
Array raw power  = 4 x 4.41     = 17.64 mW
Usable power     = 17.64 x 0.70 = 12.348 mW
```

| Quantity | Result |
|---|---:|
| Usable harvested power | 12.348 mW |
| Fixed load | 8.285 mW |
| Power margin | 4.063 mW |
| Relative margin | 49.0% |
| Usable harvested energy | 1066.87 J/day |
| Fixed load energy | 715.83 J/day |
| Daily energy margin | 351.04 J/day |

Therefore, the theoretical energy budget closes at a 7 K RMS temperature difference.

## 4. Minimum Required Temperature Difference

For four modules and 70% conversion efficiency:

```text
8.285 mW = 4 x 9 mW x (DeltaTreq / 10 K)^2 x 0.70

DeltaTreq = 5.74 K RMS.
```

For a 30% power margin, the required value increases to approximately

```text
DeltaTtarget = 6.54 K RMS.
```

The 7 K design point therefore provides slightly more than the desired 30% margin.

## 5. Temperature-Difference Risk

The Freiburg goat-collar experiment measured only

```text
mean DeltaTTEG = 2.5 +/- 1.0 K
observed range = approximately -0.5 K to 6 K.
```

At a constant 2.5 K, the proposed four-module array would provide only

```text
4 x 9 x (2.5/10)^2 x 0.70 = 1.575 mW,
```

which is insufficient. Consequently, feasibility depends on an improved fur-side thermal connector and external heat sink maintaining at least 5.74 K RMS directly across the TEG ceramic surfaces. Body-to-ambient temperature difference must not be substituted for actual TEG temperature difference.

At zero temperature difference, TEG output is zero. Energy storage must bridge these periods:

| Zero-output duration | Required stored load energy |
|---|---:|
| 12 h | 357.9 J = 0.099 Wh |
| 24 h | 715.8 J = 0.199 Wh |
| 7 days | 1.39 Wh |

## 6. Conclusion

The selected theoretical solution is **4 x TECTEG TEG2-126LDT**. It supplies approximately 12.35 mW usable power at a 7 K RMS module temperature difference, compared with the 8.285 mW fixed lower-bound load, giving a 49% power margin.

The electrical energy budget is therefore conditionally feasible. The decisive design condition is maintaining at least 5.74 K RMS across the TEGs; this thermal condition, rather than the catalog power rating, is the main project risk.

## Sources

- TECTEG, TEG2-126LDT low-temperature-difference module: https://tecteg.com/low-dt-thermoelectric-harvesting-teg-power-module/
- Baeumker et al., "A Fully Featured Thermal Energy Harvesting Tracker for Wildlife," Energies 2021: https://doi.org/10.3390/en14196363
