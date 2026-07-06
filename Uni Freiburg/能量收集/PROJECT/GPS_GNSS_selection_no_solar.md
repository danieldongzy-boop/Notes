# GNSS/GPS Positioning Options

## Positioning Requirement

The animal tracker needs at least one position/activity datapoint per minute. Since solar energy is not allowed, the positioning subsystem must minimize both active energy and stored/transmitted data.

The main design question is whether "one datapoint per minute" requires a fresh GNSS fix every minute, or whether a low-energy GNSS snapshot can be post-processed by the base station.

## Candidate Components

| Option | Component / method | Type | Size and mass | Power / energy | Stored data per point | Main advantage | Main risk |
|---|---|---|---|---|---|---|---|
| A | Quectel LC76G(PA) | Conventional GNSS module, external antenna | 10.1 x 9.7 x 2.4 mm, 0.3 g; antenna not included | About 33 mW during acquisition/tracking; backup about 13 uA | 20-40 B after the module computes latitude/longitude | Best conventional low-power choice; small and light | Still too power-hungry for fresh 1 min fixes without solar |
| B | Quectel LC86G series, especially PA/LA variants | Conventional GNSS module with integrated patch antenna | Integrated antenna family, about 16-18.4 mm square; LA approx. 8 g | PA tracking current about 11 mA at 3.3 V; other variants about 30-34 mA | 20-40 B after the module computes latitude/longitude | Easier RF design because patch antenna is included | Larger/heavier than LC76G; current depends on variant |
| C | SnapperGPS / Snapshot GNSS | Records raw GNSS signal snapshot, position solved later by base station/cloud | SnapperGPS PCB v2: 36.4 x 31.2 mm; battery-dependent mass | Less than 0.3 uAh per snapshot, about 0.004 J at 3.7 V | About 6 kB raw data per snapshot | Enables minute-scale positioning energy | Raw data is too large for LoRa bulk upload |

## Energy Comparison for 1 Position per Minute

Assume 1440 position samples per day.

| Method | Energy per sample | Daily positioning energy | Comment |
|---|---:|---:|---|
| Conventional GNSS, optimistic 7 s active time at 33 mW | 0.23 J | 331 J/day | Requires excellent antenna and assisted/warm starts |
| Conventional GNSS, literature value from thermal tracker | 0.621 J | 894 J/day | Freiburg tracker achieved one fix every 1.1-1.5 h, not every minute |
| Snapshot GNSS | about 0.004 J | about 5.8 J/day | Much better for no-solar operation |

Conclusion: conventional GNSS is suitable for low-frequency fixes, but not for a fresh fix every minute in a no-solar energy-harvesting design. Snapshot GNSS is the only positioning option in this list that makes minute-scale sampling energetically realistic.

## Data Storage and Transmission

### Conventional GNSS

The GNSS module outputs computed position data. A compact record can contain timestamp, latitude, longitude, fix quality, activity state, and battery voltage.

```text
Record size:        about 20-40 B
1 day at 1/min:     28.8-57.6 kB
3 days at 1/min:    86.4-172.8 kB
```

This is compatible with local flash and later LoRa batch upload.

### Snapshot GNSS

Snapshot GNSS stores raw signal data instead of latitude/longitude.

```text
Snapshot size:      about 6 kB
1 day at 1/min:     8.64 MB
3 days at 1/min:    25.9 MB
7 days at 1/min:    60.5 MB
```

A SnapperGPS-style board with 22,000 snapshot capacity stores about 15 days at one snapshot per minute.

This data volume is not suitable for LoRa. LoRa should only transmit status packets, alarms, or a small number of selected records. Snapshot GNSS would require a higher-data-rate local upload method, for example Wi-Fi, Wi-Fi HaLow, BLE at short range, or physical retrieval.



## Sources

- Quectel LC76G series: https://www.quectel.com/product/gnss-lc76g-series/
- Quectel LC86G series: https://www.quectel.com/product/gnss-lc86g/
- Quectel GNSS product overview: https://www.avnet.com/wcm/connect/9d7ace1a-3bff-4742-84c1-248fd9271190/quectel-gnss-module-product-overview.pdf
- SnapperGPS PCB v2: https://github.com/SnapperGPS/snappergps-pcb-2
- SnapperGPS paper: https://ojs.lib.uwo.ca/index.php/openhardware/article/view/17860/13495
- Baeumker et al., thermal wildlife tracker: https://doi.org/10.3390/en14196363
