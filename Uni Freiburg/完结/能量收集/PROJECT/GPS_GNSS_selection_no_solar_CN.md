# GNSS/GPS 定位方案选择

## 定位需求

动物追踪器需要至少每分钟记录一次位置/活动 datapoint。由于不能使用太阳能，定位模块必须重点优化两个指标：

- 每次定位的能量消耗
- 每个 datapoint 需要存储和传输的数据量

这里需要先区分两种理解：

```text
方案 1: 每分钟都获得一次新的 GNSS/GPS fix
方案 2: 每分钟记录一次定位相关数据，但位置可以由 Snapshot GNSS 后处理得到
```

如果必须使用传统 GNSS 模块每分钟 fresh fix，一般能耗会太高。Snapshot GNSS 是目前更有希望满足每分钟定位能耗的方向。

## 候选组件

| 选项 | 组件/方法 | 类型 | 尺寸和重量 | 供电/功耗 | 每个 datapoint 数据量 | 优点 | 风险 |
|---|---|---|---|---|---|---|---|
| A | Quectel LC76G(PA) | 常规 GNSS 模块，外接天线 | 10.1 x 9.7 x 2.4 mm，0.3 g；不含天线 | 工作功耗约 33 mW，等效约 10 mA at 3.3 V；backup 约 13 uA | 模块输出经纬度后约 20-40 B | 常规 GNSS 中功耗较低，体积小，重量低 | 如果每分钟 fresh fix，在无太阳能系统中仍然太耗能 |
| B | Quectel LC86G 系列，优先 PA/LA 低功耗版本 | 常规 GNSS 模块，集成 patch antenna | 集成天线系列，约 16-18.4 mm 方形；LA 约 8 g | PA 版本 tracking current 约 11 mA at 3.3 V，约 36 mW；其它版本约 30-34 mA | 模块输出经纬度后约 20-40 B | 天线已经集成，RF 设计风险更低，适合原型 | 比 LC76G 更大更重；不同版本功耗差异大 |
| C | SnapperGPS / Snapshot GNSS | 记录原始 GNSS snapshot，位置由基站/云端后处理 | SnapperGPS PCB v2: 36.4 x 31.2 mm；重量取决于电池和外壳 | 每次 snapshot 小于 0.3 uAh；按 3.7 V 计算约 0.004 J | 每次 snapshot 约 6 kB raw data | 每分钟定位在能耗上变得可行 | raw data 太大，不能用 LoRa 批量上传 |

## 功耗计算方法

常规 GNSS 的能量按开机定位时间计算：

```text
E_fix = P_active x t_fix
```

例如 LC76G(PA)：

```text
P_active = 33 mW
t_fix = 7 s
E_fix = 0.033 W x 7 s = 0.231 J
```

Snapshot GNSS 的能量按单次 snapshot 电荷计算：

```text
E_snapshot = V x Q
Q = 0.3 uAh = 0.3 x 10^-6 Ah x 3600 = 0.00108 C
E = 3.7 V x 0.00108 C = 0.0040 J
```

如果按 3.3 V 计算：

```text
E = 3.3 V x 0.00108 C = 0.0036 J
```

所以文档中取约 0.004 J/snapshot。

## 每分钟一次定位的能耗对比

假设每天 1440 个 position samples。

| 方法 | 单次能量 | 每日定位能量 | 说明 |
|---|---:|---:|---|
| 常规 GNSS，乐观情况：33 mW 工作 7 s | 0.23 J | 331 J/day | 需要良好天线、辅助定位或 warm start |
| 常规 GNSS，Freiburg thermal tracker 文献值 | 0.621 J | 894 J/day | 论文中实际只能做到约 1.1-1.5 h 一次 GPS fix |
| Snapshot GNSS | 约 0.004 J | 约 5.8 J/day | 能耗比传统 GNSS 低很多，适合无太阳能方案讨论 |

结论：

```text
传统 GNSS: 适合低频 fresh GPS fix，不适合无太阳能条件下每分钟 fresh fix
Snapshot GNSS: 更适合每分钟定位采样，但数据传输方式必须改变
```

## 数据存储和传输

### 常规 GNSS

常规 GNSS 模块直接输出经纬度。一个紧凑 record 可以包括：

```text
timestamp
latitude
longitude
fix quality
activity state
battery voltage
```

估算数据量：

```text
Record size:        about 20-40 B
1 day at 1/min:     28.8-57.6 kB
3 days at 1/min:    86.4-172.8 kB
```

这个数据量可以本地 flash 存储，并且适合几天后通过 LoRa 批量上传。

### Snapshot GNSS

Snapshot GNSS 存储的是原始 GNSS 信号片段，不是经纬度。

估算数据量：

```text
Snapshot size:      about 6 kB
1 day at 1/min:     8.64 MB
3 days at 1/min:    25.9 MB
7 days at 1/min:    60.5 MB
```

SnapperGPS v2 约可存储 22,000 个 snapshots。如果每分钟一次：

```text
22000 / 1440 = 15.3 days
```

所以存储容量是可行的，但传输是问题。

Snapshot GNSS 的 raw data 不适合用 LoRa 批量上传。LoRa 更适合传：

- 状态包
- 报警
- 电池电压
- 少量 summary data

如果使用 Snapshot GNSS，需要增加高速本地上传方式，例如：

- Wi-Fi
- Wi-Fi HaLow
- 短距离 BLE
- 靠近基站后批量上传
- 物理回收设备后导出数据

## 推荐选择

无太阳能方案下，推荐优先级如下：

```text
首选: Snapshot GNSS
条件: 允许基站/云端后处理位置，并接受不能用 LoRa 上传全部 raw data

备选: Quectel LC76G(PA)
条件: 老师要求常规 GNSS/GPS 模块，且 GPS interval 可以自适应降低

原型/RF 安全选项: Quectel LC86G PA/LA
条件: 希望集成 patch antenna，降低天线设计风险
```

如果最终选择常规 GNSS：

```text
GPS interval should be adaptive, not one fresh fix per minute.
```

如果最终选择 Snapshot GNSS：

```text
LoRa can only be used for status.
Bulk raw snapshot upload needs Wi-Fi / Wi-Fi HaLow / BLE / physical retrieval.
```

## Sources

- Quectel LC76G series: https://www.quectel.com/product/gnss-lc76g-series/
- Quectel LC86G series: https://www.quectel.com/product/gnss-lc86g/
- Quectel GNSS product overview: https://www.avnet.com/wcm/connect/9d7ace1a-3bff-4742-84c1-248fd9271190/quectel-gnss-module-product-overview.pdf
- SnapperGPS PCB v2: https://github.com/SnapperGPS/snappergps-pcb-2
- SnapperGPS paper: https://ojs.lib.uwo.ca/index.php/openhardware/article/view/17860/13495
- Baeumker et al., thermal wildlife tracker: https://doi.org/10.3390/en14196363
