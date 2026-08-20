# Chapter 1 - Introduction: 能量收集先算清楚账

来源：

- Lecture: `MicroEnergyHarvesting_Lecture_1_Introduction_SS_2026.pdf`
- Exercise: `Exercise 1_Energy, power, energy forms and conversion_SOLVED_SS_2026.pdf`

## 这一章在讲什么

微能量收集不是“把大规模可再生能源缩小一下”这么简单。它面对的是很小、很不稳定的环境能量，比如光、温差、振动，同时负载却常常有突发高功耗，比如无线发送。

所以第一章的核心不是某一种发电器，而是一个系统问题：

- 负载到底要多少能量？
- 环境能量平均能给多少？
- 没能量的时候靠什么撑过去？
- 用电池、布线、能量收集，哪个更划算？

## 作业重点公式

### 能量和功率

$$
E = P \cdot t
$$

$$
P = \frac{E}{t}
$$

说人话：能量是“总共用了多少”，功率是“用得有多快”。一个设备功率很小，但时间很长，总能量也可能很大。

常用换算：

$$
1 \ \mathrm{Wh} = 3600 \ \mathrm{J}
$$

$$
1 \ \mathrm{kWh} = 3.6 \ \mathrm{MJ}
$$

### 重力势能

$$
E_\mathrm{pot} = mgh
$$

作业里把 $g$ 近似成 $10 \ \mathrm{m/s^2}$。例如把 $1 \ \mathrm{kg}$ 抬高 $1 \ \mathrm{m}$：

$$
E = 1 \cdot 10 \cdot 1 = 10 \ \mathrm{J}
$$

如果每 10 秒做一次，那么平均功率：

$$
P = \frac{10 \ \mathrm{J}}{10 \ \mathrm{s}} = 1 \ \mathrm{W}
$$

### 动能

$$
E_\mathrm{kin} = \frac{1}{2}mv^2
$$

速度是平方项，所以速度翻倍，动能变四倍。估算车辆、运动物体能量时很重要。

### 热能

$$
E_\mathrm{therm} = c m \Delta T
$$

$c$ 是比热容。水的比热容很大，所以“加热一点水”其实要不少能量。

### 电能

$$
E_\mathrm{el} = U I t
$$

也可以写成：

$$
E_\mathrm{el} = UQ
$$

因为 $Q = It$。看到电池容量 `mAh` 时，经常要乘电压才能得到能量。

### 光子能量

$$
E_\mathrm{photon} = hf = \frac{hc}{\lambda}
$$

波长越短，单个光子的能量越高。这个公式后面太阳能电池会用到。

## 作业怎么解

### 跳绳/拳击训练功率

题目：体重 $75 \ \mathrm{kg}$，每次跳高 $0.1 \ \mathrm{m}$，每秒 2 次。

每次跳跃的能量：

$$
E = mgh = 75 \cdot 10 \cdot 0.1 = 75 \ \mathrm{J}
$$

每秒 2 次：

$$
P = 75 \cdot 2 = 150 \ \mathrm{W}
$$

坚持 30 分钟：

$$
E = 150 \ \mathrm{W} \cdot 1800 \ \mathrm{s} = 270000 \ \mathrm{J} = 75 \ \mathrm{Wh}
$$

直观理解：人运动时的机械功率可以到百瓦量级，而很多传感器是微瓦到毫瓦量级，两者差了很多数量级。

### 灰能量

灰能量就是制造某个东西本身花掉的能量。课件里用电缆举例：为了给一个低功耗温度传感器接线，制造铜线和 PVC 绝缘层本身已经消耗了很多能量。

基本算法：

$$
E_\mathrm{grey} = e_\mathrm{specific} \cdot m
$$

然后看这些制造能量如果拿来直接供电，可以供多久：

$$
t = \frac{E_\mathrm{grey}}{P_\mathrm{load}}
$$

课件例子里，1 m 细电缆的灰能量约为 $300000 \ \mathrm{Ws}$，温度传感器功耗 $300 \ \mathrm{\mu W}$：

$$
t = \frac{300000}{300 \cdot 10^{-6}} \approx 10^9 \ \mathrm{s} \approx 31.7 \ \mathrm{years}
$$

这不是说“线一定不好”，而是提醒你：低功耗系统里，安装、维护、布线的代价可能比运行能量更重要。

## 系统设计的关键词

### EPC 和 EIP

课件里把系统看成两个账本：

- EPC: effective power consumption，系统实际需要的有效功耗。
- EIP: effective input power，环境和发电器能稳定提供的有效输入功率。

设计时要留安全系数：

$$
EIP = S \cdot EPC
$$

$S>1$。说人话：环境能量不稳定，计算时不能刚好够用，必须留余量。

### 能量收集系统的典型模块

- generator：把光、热、振动等环境能变成电。
- energy storage：电容、电池、超级电容等，用来熬过没能量的时间。
- power management：升压、降压、整流、充电保护、启动关断。
- load：传感器、微控制器、无线通信。

## 易错点

- 不要把功率和能量混在一起。`W` 是功率，`J` 或 `Wh` 是能量。
- `mAh` 不是能量单位，要乘电压才接近能量。
- 微能量收集最怕“平均功率看起来够，但瞬时功率不够”。无线发送就是典型突发负载。
- 估算时先看数量级，不要一上来追求很多位小数。

