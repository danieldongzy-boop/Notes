---
marp: true
theme: harvest
size: 16:9
paginate: true
footer: "Hybrid Harvesting Animal Tracker · University of Freiburg"
style: |
  @import 'default';
  @font-face { font-family: AptosLocal; src: local("Aptos"); }
  :root {
    --blue: #123b5d;
    --green: #2d7a53;
    --orange: #e59a22;
    --ink: #17212b;
    --muted: #5c6975;
    --line: #d7dee5;
    --paper: #f7f9fb;
  }
  section {
    font-family: AptosLocal, "Segoe UI", Arial, sans-serif;
    color: var(--ink);
    background: #ffffff;
    padding: 54px 66px 48px;
    font-size: 27px;
    letter-spacing: 0;
  }
  section:not(.title) {
    padding-top: 126px;
  }
  section::after {
    color: var(--blue);
    font-size: 15px;
  }
  header, footer { color: var(--muted); font-size: 14px; }
  h1, h2 { color: var(--blue); letter-spacing: 0; }
  h1 { font-size: 52px; line-height: 1.05; }
  h2 {
    position: absolute;
    top: 48px;
    left: 66px;
    right: 66px;
    height: 48px;
    font-size: 36px;
    border-bottom: 3px solid var(--green);
    padding-bottom: 8px;
    margin: 0;
  }
  h3 { color: var(--green); font-size: 25px; margin: 4px 0 12px; }
  strong { color: var(--blue); }
  ul, ol { margin-top: 8px; }
  li { margin: 8px 0; }
  table { width: 100%; font-size: 20px; border-collapse: collapse; }
  th { background: var(--blue); color: white; }
  th, td { padding: 7px 10px; border: 1px solid var(--line); }
  tr:nth-child(even) td { background: var(--paper); }
  blockquote {
    border-left: 7px solid var(--orange);
    background: #fff7e8;
    margin: 18px 0;
    padding: 12px 20px;
    color: var(--ink);
  }
  section.title {
    background: linear-gradient(110deg, #123b5d 0 66%, #2d7a53 66% 100%);
    color: white;
  }
  section.title h1, section.title h3, section.title strong { color: white; }
  section.title footer, section.title::after { color: rgba(255,255,255,.8); }
  .metric {
    display: inline-block;
    color: white;
    background: var(--blue);
    padding: 12px 20px;
    margin: 8px 12px 8px 0;
    font-size: 30px;
    font-weight: 700;
  }
  .accent { color: var(--orange); }
  .columns { display: flex; gap: 42px; }
  .columns > div { flex: 1; }
  .flow {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr;
    align-items: center;
    gap: 14px;
    text-align: center;
    margin-top: 40px;
  }
  .flow .box { border-top: 6px solid var(--green); background: var(--paper); padding: 20px 12px; }
  .flow .arrow { color: var(--orange); font-size: 38px; font-weight: 700; }
  .small { font-size: 19px; }
  .center { text-align: center; }
  .muted { color: var(--muted); }
---

<!-- _class: title -->

# Long-Term Animal Tracking System

### An animal-specific hybrid energy harvesting collar

**Solar + kinetic + thermal · 2-year target · <1000 g**

Micro Energy Harvesting · University of Freiburg · June 2026

---

## Design Target

**Energy-autonomous tracking for a sheep-sized animal**

| Requirement | Target |
|---|---|
| Position and activity | At least one datapoint every minute |
| Data transfer | Batch upload every 3 days |
| Radio range | Up to 100 m free field |
| Operating life | At least 2 years |
| Total mass | Below 1000 g |
| Components | Commercially available |

> The challenge is closing the energy budget under outdoor uncertainty.

---

## Why Hybrid Harvesting?

<div class="columns">
<div>

### The bottleneck

- 1440 GNSS fixes per day
- GNSS and LoRa create current peaks
- Battery-only operation is difficult for 2 years
- Thermal and kinetic harvesting are too small alone

</div>
<div>

### Design decision

<span class="metric">Solar</span> closes the average budget

<span class="metric">Kinetic</span> adds motion-linked energy

<span class="metric">Thermal</span> provides continuous trickle

</div>
</div>

---

## System Architecture

<div class="flow">
  <div class="box"><strong>Ambient energy</strong><br>Solar<br>Kinetic<br>Body heat</div>
  <div class="arrow">→</div>
  <div class="box"><strong>Power conversion</strong><br>MPPT<br>Rectifier<br>Boost</div>
  <div class="arrow">→</div>
  <div class="box"><strong>Storage + loads</strong><br>Li-ion + LIC<br>MCU · GNSS · IMU<br>Flash · LoRa</div>
</div>

<br>

> Solar is the main source. The LIC handles GNSS and LoRa pulse power.

---

## Operating Scenario

<div class="columns">
<div>

### Every minute

1. Wake MCU
2. Read accelerometer
3. Acquire GNSS position
4. Record timestamp and voltage
5. Write one local datapoint

</div>
<div>

### Every 3 days

1. Wake LoRa
2. Transfer buffered records
3. Confirm reception
4. Return radio to hard-off state

</div>
</div>

> Load switches disconnect GNSS and LoRa between events.

---

## Daily Load Budget

| Module | Assumption | Energy |
|---|---|---:|
| GNSS | 621 mJ/fix × 1440 | 0.248 Wh/day |
| MCU | Periodic low-power wake-up | 0.005 Wh/day |
| Accelerometer | ADXL362, <2 µA | 0.0002 Wh/day |
| Flash logging | One write per minute | 0.001 Wh/day |
| LoRa upload | Batch every 3 days | 0.006 Wh/day |
| PMIC / regulator losses | 10–15% allowance | 0.030 Wh/day |
| **Total** |  | **0.291 Wh/day** |

<div class="center"><span class="metric">1046 J/day</span></div>

---

## Daily Harvest Estimate

| Source | Conservative assumption | Energy |
|---|---|---:|
| Solar | 2 W × 0.5 sun-hours × 70% | 0.700 Wh/day |
| Thermal | 100 µW average | 0.0024 Wh/day |
| Kinetic | Conservative animal-motion estimate | 0.00056 Wh/day |
| **Total input** |  | **0.703 Wh/day** |

<div class="center">
<span class="metric">Solar >99%</span>
<span class="metric">Auxiliary ≈0.4%</span>
</div>

Kinetic and thermal harvesters are auxiliary, not primary sources.

---

## Energy Closure

<div class="columns center">
<div>

### Harvested

<span class="metric">0.703 Wh/day</span>

Solar + kinetic + thermal

</div>
<div>

### Consumed

<span class="metric">0.291 Wh/day</span>

Sensing + storage + transfer

</div>
</div>

<div class="center">

# <span class="accent">2.4× design margin</span>

</div>

<p class="small muted center">Field tests must validate shading, orientation, temperature gradient, and motion.</p>

---

## Storage and Peak Power

<div class="columns">
<div>

### Long-term buffer

**1 × 18650 Li-ion**

<span class="metric">12.6 Wh</span>

3.6 V × 3.5 Ah

No-harvest autonomy:

**12.6 / 0.291 ≈ 43 days**

</div>
<div>

### Pulse buffer

**30 F LIC or supercapacitor**

- Supplies GNSS and LoRa peaks
- Reduces battery stress
- Improves cold-weather stability
- Supports controlled shutdown

</div>
</div>

---

## Commercial Components

| Function | Candidate |
|---|---|
| Solar / kinetic / thermal | Voltaic 2 W panel · Kinetron MSG32 · TEC 1MC06-048-15 |
| Harvester PMICs | e-peas AEM10941 · LTC3108 / AEM20940 |
| GNSS | u-blox MAX-M10S |
| Activity sensor | Analog Devices ADXL362 |
| MCU | TI MSP430FR5969 or STM32L4 |
| Wireless | Semtech SX1262 LoRa |
| Memory / switch | SPI NOR flash · Vishay SIP32431 |

> All core functions can be implemented with commercially available parts.

---

## Weight Estimate

| Part | Estimated mass |
|---|---:|
| Solar + kinetic + thermal harvesters | 138–230 g |
| Battery + pulse buffer | 65–90 g |
| PCB, electronics, antennas | 30–60 g |
| Enclosure | 100–200 g |
| Collar and mounting | 150–250 g |
| **Total estimate** | **500–830 g** |

<div class="center">
<span class="metric">Requirement: &lt;1000 g</span>
<span class="metric">Margin: 170–500 g</span>
</div>

---

## Kinetic Signal = Activity Feature

| Kinetic signature | Likely behavior |
|---|---|
| Almost no pulses | Sleeping / resting |
| Low intermittent pulses | Awake / grazing |
| Frequent high pulses | Walking / running |

**Features per minute:** pulse count · peak voltage · harvested energy · time above threshold

> The accelerometer remains the primary classifier. The kinetic generator adds a passive auxiliary signal.

---

## Adaptive GNSS Strategy

| Detected state | GNSS policy |
|---|---|
| Sleeping / resting | Fix every 10–30 min; keep one-minute activity data |
| Grazing / slow movement | Fix every 5 min |
| Walking / running | Fix every 1 min |
| Low storage voltage | Reduce GNSS rate; preserve activity logging |

### Energy-aware fallback

**High:** full service → **Medium:** reduced GNSS → **Low:** activity only → **Critical:** RTC only

<p class="small muted">The task asks for a datapoint every minute; repeated positions must be clearly flagged if a fresh GNSS fix is skipped.</p>

---

## Risks and Validation

<div class="columns">
<div>

### Main risks

- Solar shading by wool, mud, or posture
- Weak body-to-air temperature gradient
- Kinetic device affecting comfort
- Terrain-dependent LoRa link
- Winter battery performance

</div>
<div>

### Validation plan

- Measure every operating state
- Test solar yield versus orientation
- Test kinetic output on rig and animal
- Verify TEG contact and heat rejection
- Perform a 100 m radio test

</div>
</div>

---

## Key Takeaways

1. **Kinetic and thermal harvesting alone cannot support minute-scale GNSS.**
2. **Small solar closes the baseline budget; kinetic and thermal add resilience and research value.**
3. **Estimated input: 0.703 Wh/day. Estimated demand: 0.291 Wh/day.**
4. **The 2.4× design margin and 500–830 g mass meet the initial targets.**
5. **Adaptive GNSS and energy-aware scheduling are the strongest improvements.**

---

<!-- _class: title -->

# Questions?

### Long-Term Animal Tracking System

**Hybrid solar + kinetic + thermal energy harvesting**
