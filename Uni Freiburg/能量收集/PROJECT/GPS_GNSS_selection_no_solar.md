# GPS/GNSS Selection for the Long-Term Animal Tracker

Status: draft for group discussion  
Scope: positioning subsystem only, after removing solar energy from the concept

## 1. Task Boundary

The system must log position and activity for a sheep-size animal, with at least one datapoint per minute, a lifetime target of 2 years or more, mass below 1000 g, and only commercially available components.

Because the teacher now excludes solar energy, the GPS/GNSS choice must be judged mainly by energy per valid fix, not only by datasheet tracking current.

Important interpretation to clarify with the teacher:

- Strict interpretation: one fresh GPS/GNSS position fix every minute.
- More energy-realistic interpretation: one logged datapoint every minute, but the position can be updated less often and repeated/interpolated between fresh fixes.

For now, the numbers below assume the strict case first, because that is the hardest case.

## 2. What the Existing Literature Says

### Thermal tracker paper

The Freiburg/IMTEK thermal tracker paper is directly relevant because it is a no-solar wildlife tracker. It reports:

- Energy source: animal body heat via TEGs.
- Harvested electrical power: about 100 uW over 2 x 20.5 cm2 TEG area.
- Total tracker mass: 286 g.
- GPS interval in field test: one fix every 1.1 h to 1.5 h.
- GPS energy: about 620-621 mJ per fix.
- LoRaWAN transmission interval: 14 min.
- Overall deep sleep power: about 8 uW.

This is the strongest warning for our design: thermal harvesting can support occasional GPS, but not minute-scale fresh GPS fixes.

Source: Baeumker et al., "A Fully Featured Thermal Energy Harvesting Tracker for Wildlife", Energies 2021. [DOI / MDPI](https://doi.org/10.3390/en14196363). Local file: `energies-14-06363-v2.pdf`.

### Kinetic tracker paper

The Kinefox paper is relevant because it tests animal-mounted kinetic harvesting with a real GPS-enabled device. It reports:

- Harvester: Kinetron MSG32 micro-generator, 18 g, 32 mm diameter.
- Storage: lithium-ion capacitor.
- GPS module used in prototype: Quectel L70B-M39.
- GPS was power-gated with a load switch.
- Energy generated in experiments:
  - Exmoor pony: about 0.69 J/day.
  - Wisent: about 2.38 J/day.
  - Domestic dog cases: about 2.26-10.04 J/day, depending strongly on mounting.
- In the Exmoor pony GPS experiment, one GPS plus acceleration transmission cycle consumed about 4.6 J, with the GPS part around 3.26 J because time-to-fix was long.

This shows that kinetic harvesting is useful, but real mounted GPS can become much more expensive than the datasheet estimate if antenna placement or sky view is poor.

Source: Gregersen et al., "A novel kinetic energy harvesting system for lifetime deployments of wildlife trackers", PLOS ONE 2023. [DOI / PLOS](https://doi.org/10.1371/journal.pone.0285930). Local file: `journal.pone.0285930.pdf`.

## 3. GPS/GNSS Selection Criteria

The positioning module should satisfy:

- Commercial availability through normal distributors.
- Low acquisition and tracking current.
- Fast time-to-first-fix with assisted data or warm/hot start.
- External antenna or good integrated patch antenna.
- UART/I2C/SPI interface that a low-power MCU can handle.
- Separate backup or power-gating strategy.
- Operation around 1.8-3.3 V.
- Documented current values and lifecycle status.

The key metric for the energy budget is:

```text
Energy per fix = supply voltage x active current x time-to-fix
```

For the system budget, the daily GPS energy is:

```text
Daily GPS energy = energy per fix x 1440 fixes/day
```

## 4. Candidate GPS/GNSS Modules

| Option | Module | Why consider it | Power data to use initially | Pros | Risks |
|---|---|---|---:|---|---|
| A | Quectel LC76G(PA) | Best final candidate after the no-solar change | About 10 mA acquisition/tracking, about 33 mW; backup around 13 uA; EASY/EPO support for faster fixes | Very attractive current, small 10.1 x 9.7 mm module, official page lists low-power tracking features and 0.3 g mass | Less continuity with current draft; must validate toolchain and real time-to-fix |
| B | u-blox MAX-M10S | Best continuity/prototype candidate because it matches the previous draft and has strong documentation/ecosystem | Approx. 9.5 mA tracking + 2.3 mA I/O, 11.5 mA acquisition + 2.3 mA I/O at 3 V in common multi-GNSS mode | Good documentation, small 10.1 x 9.7 mm module, mature u-blox tooling, external antenna choice | u-blox product page currently lists MAX-M10 variants as no longer available, although distributor stock still exists; backup current can matter |
| C | u-blox SAM-M10Q | Easiest RF/prototype option because it includes a patch antenna | About 10 mA tracking, 13 mA acquisition at 3 V; around 37 mW tracking | Integrated antenna reduces RF design risk; useful for a quick measurement prototype | Larger and heavier, less flexible placement, energy not better than A/B |

Sources checked:

- u-blox MAX-M10S datasheet: [MAX-M10S DataSheet UBX-20035208](https://content.u-blox.com/sites/default/files/MAX-M10S_DataSheet_UBX-20035208.pdf)
- u-blox MAX-M10 product page and lifecycle note: [MAX-M10 series](https://www.u-blox.com/en/product/max-m10-series)
- u-blox SAM-M10Q datasheet: [SAM-M10Q DataSheet UBX-20012619](https://content.u-blox.com/sites/default/files/documents/SAM-M10Q_DataSheet_UBX-20012619.pdf)
- Quectel LC76G product page: [LC76G Series](https://www.quectel.com/product/gnss-lc76g-series/)
- Quectel LC76G hardware design: [LC76G Series Hardware Design](https://forums.quectel.com/uploads/short-url/2v9ImaRc5iQji91xIiJJBXWK04s.pdf)
- u-blox F11/M11 2026 announcement: [F11 GNSS products](https://www.u-blox.com/en/f11-ultra-low-power-gnss-products)

## 5. Recommended GPS Choice

Recommended final candidate: Quectel LC76G(PA).

Reason:

- It has the lowest normal-operation power among the checked stable module options.
- It is small and light enough for a collar PCB.
- The official product page explicitly targets low-power portable/tracking use cases.
- Quectel lists EASY/low-power support, which is important for reducing time-to-fix.

Recommended continuity/prototype option: u-blox MAX-M10S.

Reason:

- It fits the existing draft and is easy to justify technically.
- It has complete official documentation and mature u-blox tooling.
- Distributor stock still exists, but the official product page status means it should not be the safest long-term final choice unless sourcing is confirmed.

New 2026 option to watch: u-blox MAX-M11N / F11-M11 family.

Reason:

- u-blox announced F11/M11 products on 02 July 2026 with LEAP mode and very low typical power.
- As of this check, the parts are available for engineering sample requests, so they are promising but too new to be the main course-design baseline.

Not recommended as final baseline: Quectel L70B-M39.

Reason:

- It is useful because the Kinefox paper used it, but it is older.
- We should not base the final 2026 design on it unless current sourcing is confirmed.

## 6. GPS Block Architecture

Recommended architecture for the positioning block:

```text
Main storage / LIC
  -> load switch
  -> GNSS module at 3.0-3.3 V
  -> UART to MCU
  -> position record in FRAM/flash

MCU
  -> controls GNSS enable
  -> stores aiding data if supported
  -> logs time-to-fix and fix quality

GNSS module
  -> external ceramic patch antenna on top of collar
  -> antenna placed away from LoRa antenna and metal parts
```

Electrical design notes:

- Use a load switch for the GNSS main supply.
- Keep the RF path short and place the antenna on the highest part of the collar.
- A 15 x 15 mm or larger ceramic patch antenna is preferable for first tests.
- Measure the real time-to-first-fix in collar orientation, not only on a desk.
- Decide later whether to keep the backup domain powered. Backup power improves warm starts, but in a no-solar system even 10-30 uA can be a large fraction of harvested power.

## 7. First Energy Estimate for GPS

### Conservative literature number

Using the Freiburg thermal tracker value:

```text
GPS energy per fix = 621 mJ
Fixes per day      = 1440
Daily GPS energy   = 0.621 J x 1440 = 894 J/day
                   = 0.248 Wh/day
```

This is the same value used in the earlier draft.

### Optimistic module-level estimates

These values assume good antenna placement and assisted or warm starts:

| Scenario | Approx. active power | Active time per fix | Energy per fix | Energy per day at 1 fix/min |
|---|---:|---:|---:|---:|
| Very good hot start | 33-40 mW | 1-2 s | 0.03-0.08 J | 43-115 J/day |
| Good assisted start | 33-45 mW | 7 s | 0.23-0.32 J | 331-461 J/day |
| Conservative design value | 40-45 mW | 15 s | 0.60-0.68 J | 864-979 J/day |
| Bad mounted antenna / poor sky view | about 50 mW | 60 s or more | 3 J or more | 4320 J/day or more |

For presentations and first system sizing, use:

```text
GPS block baseline = 0.62 J/fix
GPS daily energy   = 0.248 Wh/day for one fresh fix every minute
```

For a stretch/optimized case, show:

```text
GPS optimized case = 0.10 Wh/day or lower
only if warm-start behavior is reliable in field tests
```

## 8. Immediate No-Solar Feasibility Warning

No-solar harvesting numbers from the two papers:

```text
Thermal: about 100 uW = 8.64 J/day = 0.0024 Wh/day
Kinetic: about 0.69-10.04 J/day in reported animal tests
```

Even if we combine an optimistic thermal source with a good kinetic case:

```text
Thermal + kinetic ~= 9-19 J/day
```

This is much smaller than one fresh GPS fix every minute:

```text
Conservative GPS-only demand ~= 894 J/day
Optimistic GPS-only demand   ~= 100-400 J/day
```

Preliminary conclusion:

```text
Without solar, strict 1 fresh GPS fix per minute is not feasible with thermal + kinetic harvesting alone.
```

This does not mean the project is impossible. It means the system concept probably needs one of these changes:

- Fresh GPS less often, for example every 5-30 min, while logging accelerometer/activity every minute.
- Use repeated last-known position for sleeping/resting minutes and clearly mark it as repeated.
- Use activity-triggered GPS: frequent fixes only when the animal is moving.
- Use a larger rechargeable battery as a 2-year energy reservoir, while harvesting only extends lifetime.
- Use another non-solar harvester with much higher average power, if a realistic commercial option exists.

## 9. Data Interface for Other Group Members

For the LoRa teammate:

- GPS record size can be small: timestamp, latitude, longitude, fix quality, activity state, battery voltage.
- One record can fit in roughly 20-40 bytes before compression.
- If data is transmitted every few days, local flash/FRAM buffering is required.

For the activity-sensor teammate:

- Activity state should control GPS frequency.
- Sleeping/resting: skip or reduce GPS fixes.
- Awake/grazing: medium interval.
- Walking/running: shortest interval.

For the power-budget teammate:

Use two GPS rows in the system power table:

| GPS case | Value |
|---|---:|
| Baseline/conservative | 0.621 J/fix |
| Optimistic measured target | 0.1-0.3 J/fix |

Then compute daily energy with:

```text
E_GPS_day = E_fix x number_of_fresh_fixes_per_day
```

Example intervals:

| Fresh GPS interval | Fixes/day | GPS energy at 0.621 J/fix |
|---:|---:|---:|
| 1 min | 1440 | 894 J/day = 0.248 Wh/day |
| 5 min | 288 | 179 J/day = 0.050 Wh/day |
| 15 min | 96 | 59.6 J/day = 0.0166 Wh/day |
| 30 min | 48 | 29.8 J/day = 0.0083 Wh/day |
| 60 min | 24 | 14.9 J/day = 0.0041 Wh/day |

The literature thermal tracker reaches about one GPS fix every 1.1-1.5 h, which matches this table: no-solar systems become plausible only when the GPS interval is tens of minutes to hours, not one minute.

## 10. Next Step

Before finalizing the full system, the group should agree on one wording:

```text
"Datapoint every minute" means:
1. fresh GPS every minute, or
2. one logged record every minute, with adaptive GPS updates.
```

If option 1 is mandatory, no-solar energy autonomy is very unlikely.  
If option 2 is accepted, the no-solar design can still be developed around thermal + kinetic harvesting, adaptive GPS, and a carefully sized storage element.
