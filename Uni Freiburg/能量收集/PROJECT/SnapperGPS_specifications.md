# SnapperGPS / Snapshot GNSS (PCB v2.0.0)

## Overview

SnapperGPS is an open-source snapshot GNSS receiver developed for low-power, non-real-time wildlife tracking. Instead of calculating latitude and longitude on the device, it records a short raw GNSS signal snapshot. The recorded data is later uploaded to the SnapperGPS cloud platform, where the position is calculated. This greatly reduces the energy required for each position sample, but produces much more data than a conventional GNSS receiver.

## Key Specifications

| Parameter                         | SnapperGPS PCB v2.0.0                                                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| GNSS method                       | Snapshot GNSS with cloud post-processing                                                                                |
| Supported constellations          | GPS, Galileo, and BeiDou                                                                                                |
| Supply voltage for testing        | 2.7-3.3 V external DC; approximately 3 V with two button cells                                                          |
| Sleep current                     | Approximately 1 uA at 3 V                                                                                               |
| Peak current during snapshot      | Approximately 25 mA                                                                                                     |
| Charge per snapshot               | Less than 0.3 uAh                                                                                                       |
| Signal reception time             | 12 ms per snapshot                                                                                                      |
| Estimated energy per snapshot     | Less than approximately 2.9-3.6 mJ over 2.7-3.3 V; approximately 3.24 mJ at 3.0 V                                       |
| Board dimensions                  | 36.4 mm x 31.2 mm                                                                                                       |
| Mass                              | 12.7 g or 17.7 g with LR44/SR44 batteries and antenna; approximately 3-3.5 g less with LR41/SR41 batteries              |
| Flash memory options              | 512 Mbit or 1 Gbit NAND flash                                                                                           |
| Snapshot capacity                 | 10,901 or 21,824 snapshots, depending on flash option                                                                   |
| Approximate raw data per snapshot | Approximately 6 kB, inferred from flash capacity and snapshot count                                                     |
| Antenna                           | Integrated passive GPS/Galileo patch antenna; optional external active antenna through U.FL                             |
| Reported positioning accuracy     | Approximately 12 m median error before smoothing in real-world tests                                                    |
| Battery lifetime                  | More than one year using two LR44 or SR44 cells                                                                         |
| Additional functions              | RTC timestamping, temperature measurement, user-defined or externally triggered sampling, and USB browser configuration |

The snapshot energy is calculated from the official charge limit:

```text
E = V x Q
Q < 0.3 uAh = 0.00108 C

At 3.0 V:
E < 3.0 V x 0.00108 C = 0.00324 J = 3.24 mJ
```

The earlier value of approximately 4 mJ per snapshot assumes a 3.7 V supply and is more representative of the original LiPo-powered SnapperGPS version. For PCB v2.0.0, the official 2.7-3.3 V test range gives an upper bound of approximately 2.9-3.6 mJ per snapshot.

## Relevance to the Animal Tracker

At one snapshot per minute, SnapperGPS would generate approximately:

```text
6 kB x 1,440 snapshots/day = 8.64 MB/day
```

The 21,824-snapshot version therefore stores about 15 days of data at one snapshot per minute. The energy consumption is much lower than that of a conventional GNSS fix, but the raw snapshots are not suitable for bulk transmission through LoRa. SnapperGPS is designed mainly for later USB recovery and cloud upload; a remotely connected system would require a higher-data-rate link or local physical retrieval.

SnapperGPS also does not have a conventional TTFF specification. The receiver captures 12 ms of satellite signal, but the final position becomes available only after the raw snapshot has been transferred and processed externally.

## Sources

1. SnapperGPS PCB v2.0.0 official hardware repository, including measured current, voltage range, dimensions, memory options, BOM, schematic, antenna and battery configurations:  
   https://github.com/SnapperGPS/snappergps-pcb-2

2. Beuchert, J., Matthes, A., and Rogers, A., "SnapperGPS: Open Hardware for Energy-Efficient, Low-Cost Wildlife Location Tracking with Snapshot GNSS," *Journal of Open Hardware*, 7(1), 2023. DOI: 10.5334/joh.48:  
   https://ojs.lib.uwo.ca/index.php/openhardware/article/view/17860  
   PDF: https://ojs.lib.uwo.ca/index.php/openhardware/article/view/17860/13494

3. SnapperGPS algorithms paper describing cloud-based position estimation from GNSS snapshots:  
   https://doi.org/10.1145/3485730.3485931

4. Silicon Labs EFM32HG MCU datasheet, used by the SnapperGPS PCB:  
   https://www.silabs.com/documents/public/data-sheets/efm32hg-datasheet.pdf

5. Texas Instruments TPS61291 boost converter datasheet, used in the SnapperGPS PCB v2.0.0 power path:  
   https://www.ti.com/lit/ds/symlink/tps61291.pdf

## Source Note

SnapperGPS PCB v2.0.0 is an open-source assembled design rather than a commercial GNSS module, so the project does not publish one manufacturer-style board datasheet. The official repository README, schematic, BOM, peer-reviewed hardware paper, and individual component datasheets are the primary specification sources.
