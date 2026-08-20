# Long Term Animal Tracking System - Hybrid Harvesting Concept

## Goal

Design an energy-autonomous tracking device for a sheep-size animal.

Main requirements:

- Position + activity datapoint at least every 1 min
- Local data logging, upload to base station every few days
- Maximum free-field transmission range: 100 m
- Lifetime: at least 2 years
- Total weight: below 1000 g
- Only commercially available components

## Recommended Concept

Use a hybrid energy harvesting collar:

```text
Solar     = main energy source
Kinetic   = motion-dependent supplement
Thermal   = continuous trickle source
Battery   = long-term buffer
LIC/supercap = pulse buffer for GNSS and LoRa
```

This is more robust than pure thermal or pure kinetic harvesting. It is also more distinctive than a simple solar-only tracker because it uses animal-specific energy sources.

## System Architecture

```text
Solar panel
-> solar PMIC / MPPT
-> storage

Kinetic generator
-> rectifier / harvester interface
-> storage

TEG thermal module
-> low-voltage boost converter
-> storage

Storage
-> regulators + load switches
-> MCU + GNSS + accelerometer + flash + LoRa
```

## Operating Assumptions

- Datapoint interval: 1 min
- Each datapoint: timestamp, GNSS position, sleeping/awake state, storage voltage
- Upload interval: every 3 days
- Wireless link: LoRa to local base station
- GNSS and LoRa are power-gated when not used

## Daily Energy Consumption

| Module | Assumption | Energy |
|---|---:|---:|
| GNSS | 621 mJ/fix, 1440 fixes/day | 0.248 Wh/day |
| MCU | periodic low-power wake-up | 0.005 Wh/day |
| Accelerometer | ADXL362, <2 uA | 0.0002 Wh/day |
| Flash logging | one write/min | 0.001 Wh/day |
| LoRa upload | batch upload every 3 days | 0.006 Wh/day |
| PMIC/regulator losses | approx. 10-15% margin | 0.030 Wh/day |

Total:

```text
0.291 Wh/day
= 1046 J/day
```

## Daily Harvested Energy

| Source | Assumption | Energy |
|---|---:|---:|
| Solar | 2 W panel, 0.5 peak sun h/day, 70% efficiency | 0.70 Wh/day |
| Thermal | 100 uW average | 0.0024 Wh/day |
| Kinetic | conservative animal motion estimate | 0.00056 Wh/day |

Total input:

```text
0.703 Wh/day
```

Energy margin:

```text
0.703 / 0.291 = 2.4
```

So the design can close the energy budget even under conservative winter solar assumptions.

## Storage

Main storage:

```text
1x 18650 Li-ion cell
3.6 V * 3500 mAh = 12.6 Wh
```

Autonomy without harvesting:

```text
12.6 Wh / 0.291 Wh/day = approx. 43 days
```

Add a 30 F LIC or supercapacitor to handle GNSS and LoRa current peaks.

## Component Candidates

| Function          | Candidate                                                  |
| ----------------- | ---------------------------------------------------------- |
| Solar harvester   | Voltaic Systems 2 W / 6 V flexible panel                   |
| Kinetic harvester | Kinetron MSG32 / mechanical generator system               |
| Thermal harvester | TEC Microsystems 1MC06-048-15_TEG or Matrix thermal module |
| Solar PMIC        | e-peas AEM10941                                            |
| Thermal PMIC      | Matrix MCRY12, LTC3108, or AEM20940                        |
| GNSS              | u-blox MAX-M10S                                            |
| Activity sensor   | Analog Devices ADXL362                                     |
| MCU               | TI MSP430FR5969 or STM32L4                                 |
| Wireless          | Semtech SX1262 LoRa                                        |
| Memory            | SPI NOR flash, e.g. Winbond W25Q                           |
| Load switch       | Vishay SIP32431                                            |

## Weight Estimate

| Part | Weight |
|---|---:|
| 2 W solar panel | 60-100 g |
| Kinetic generator | 18-30 g |
| Thermal modules + heat spreader | 60-100 g |
| 18650 battery | 45-50 g |
| LIC/supercap | 20-40 g |
| PCB + electronics + antenna | 30-60 g |
| Enclosure | 100-200 g |
| Collar/mounting | 150-250 g |

Total estimate:

```text
500-830 g
```

Below the 1000 g limit.

## Possible Improvements

### 1. Kinetic Harvester as Activity Indicator

The kinetic generator output can also be used to estimate activity.

Possible features:

- pulse count per minute
- peak voltage
- harvested energy per minute
- time above voltage threshold

Example interpretation:

| Kinetic signal | Activity |
|---|---|
| almost no pulses | sleeping/resting |
| low intermittent pulses | awake/grazing |
| frequent high pulses | walking/running |

Still keep the accelerometer as the primary activity sensor. The kinetic signal is useful as a secondary passive indicator.

### 2. Adaptive GNSS Interval

Reduce GNSS energy by changing the fix interval:

| State | GNSS strategy |
|---|---|
| sleeping/resting | reuse last position or fix every 10-30 min |
| grazing/slow movement | fix every 5 min |
| active/walking | fix every 1 min |
| low storage voltage | reduce GNSS frequency |

### 3. Energy-Aware Scheduler

Use storage voltage to decide system behavior:

| Storage level | Behavior |
|---|---|
| high | full GNSS + normal upload |
| medium | reduced GNSS interval |
| low | activity logging only, rare GNSS |
| critical | safe mode: RTC + wake-up only |

## Key Conclusion

Pure thermal + kinetic harvesting is not enough for one GNSS fix per minute. The hybrid solution is:

```text
small solar panel + kinetic generator + thermal harvester + rechargeable storage
```

Estimated daily consumption:

```text
0.291 Wh/day
```

Estimated daily harvested energy:

```text
0.703 Wh/day
```

This gives an energy margin of about 2.4 while keeping the total weight below 1000 g.
