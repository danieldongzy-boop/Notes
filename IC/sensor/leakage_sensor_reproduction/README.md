# LDRO temperature-sensor behavioral reproduction

This folder reproduces the mathematical model in Tang et al., JSSC 2020:

- Fig. 5 trend from equation (11)
- Fig. 6 supply-sensitivity surface and contour map
- the `a1=0.5`, `a2=0.28`, independent `+/-10%` robustness example
- ideal equation (7) temperature-frequency curves fitted to the measured endpoint ranges
- FDC range, conversion time, energy, and resolution-FoM arithmetic

## Run

Python 3 with `numpy` and `matplotlib` is required.

```powershell
python .\reproduce_ldro.py
```

Generated plots and CSV checks are written to `results/`.

## Scope boundary

This is a behavior-level reproduction. A transistor-level or post-layout reproduction requires the original 55-nm RVT model cards, process corners, mismatch models, extracted parasitics, and the authors' raw data. Those inputs are not included in the paper.
