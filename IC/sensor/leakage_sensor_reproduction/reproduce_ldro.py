"""Behavioral reproduction of Tang et al., JSSC 2020.

The script reproduces the mathematical-model trends in Fig. 5 and Fig. 6,
checks the FDC and FoM arithmetic, and reconstructs ideal temperature-frequency
curves from the measured endpoint ranges reported in the paper.

This is not a transistor-level reproduction. The foundry models, extracted
parasitics, and raw measurement data are not provided by the paper.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


@dataclass(frozen=True)
class PaperModel:
    dibl_lambda: float = 0.1
    subthreshold_n: float = 1.5
    thermal_voltage_v: float = 0.026
    temp_sensitivity_per_c: float = 0.046
    vdd_min_v: float = 0.8
    vdd_max_v: float = 1.3


MODEL = PaperModel()


def delay_factor(vdd_v: np.ndarray, a1: float, a2: float) -> np.ndarray:
    """Equation (11), omitting the VDD-independent scale factor K1."""
    if a2 >= a1:
        raise ValueError("Equation (11) requires a2 < a1 so that VTL < VX.")
    scale = MODEL.dibl_lambda / (MODEL.subthreshold_n * MODEL.thermal_voltage_v)
    return np.exp(-scale * a2 * vdd_v) - np.exp(-scale * a1 * vdd_v)


def range_supply_sensitivity_c_per_v(a1: float, a2: float, points: int = 1001) -> float:
    """Paper-style full-range supply sensitivity converted to degC/V.

    Fig. 5's stated 7.5%/V is recovered by taking the peak-to-peak relative
    delay excursion, dividing by the 0.5-V sweep, then dividing by the
    normalized temperature sensitivity of 4.6%/degC.
    """
    vdd = np.linspace(MODEL.vdd_min_v, MODEL.vdd_max_v, points)
    delay = delay_factor(vdd, a1, a2)
    relative_per_v = (delay.max() - delay.min()) / delay.mean() / (
        MODEL.vdd_max_v - MODEL.vdd_min_v
    )
    return float(relative_per_v / MODEL.temp_sensitivity_per_c)


def plot_fig5(output_dir: Path) -> dict[str, float]:
    vdd = np.arange(0.8, 1.3001, 0.05)
    a1 = 0.5
    a2_values = [0.2, 0.25, 0.3, 0.35, 0.4, 0.45]

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for a2 in a2_values:
        delay = delay_factor(vdd, a1, a2)
        normalized = delay / delay[np.argmin(np.abs(vdd - 1.0))]
        ax.plot(vdd, normalized, marker="o", linewidth=1.8, label=fr"$a_2={a2:g}$")

    ax.set(
        xlabel="Supply voltage (V)",
        ylabel="Normalized delay",
        title="Equation (11): reproduction of the Fig. 5 trend",
        xlim=(0.78, 1.32),
    )
    ax.grid(True, alpha=0.3)
    ax.legend(ncol=2, frameon=False)
    fig.tight_layout()
    fig.savefig(output_dir / "fig5_model.png", dpi=220)
    plt.close(fig)

    return {
        f"a2_{a2:g}_delay_sensitivity_percent_per_v":
        range_supply_sensitivity_c_per_v(a1, a2)
        * MODEL.temp_sensitivity_per_c
        * 100
        for a2 in a2_values
    }


def plot_fig6(output_dir: Path) -> tuple[float, float, float, float]:
    a1_values = np.linspace(0.3, 0.8, 151)
    a2_values = np.linspace(0.1, 0.7, 181)
    sensitivity = np.full((len(a2_values), len(a1_values)), np.nan)

    for row, a2 in enumerate(a2_values):
        for col, a1 in enumerate(a1_values):
            if a2 < a1 - 1e-12:
                sensitivity[row, col] = range_supply_sensitivity_c_per_v(a1, a2, points=501)

    a1_grid, a2_grid = np.meshgrid(a1_values, a2_values)
    fig, ax = plt.subplots(figsize=(7.4, 5.6))
    mesh = ax.pcolormesh(a1_grid, a2_grid, sensitivity, shading="auto", cmap="turbo", vmin=0, vmax=21)
    contours = ax.contour(
        a1_grid,
        a2_grid,
        sensitivity,
        levels=np.arange(2, 22, 2),
        colors="white",
        linewidths=0.8,
    )
    ax.clabel(contours, inline=True, fontsize=8, fmt="%g")
    ax.plot(0.5, 0.28, marker="*", color="red", markersize=12, label="Nominal (0.50, 0.28)")
    ax.add_patch(plt.Rectangle((0.45, 0.252), 0.10, 0.056, fill=False, color="black", linewidth=1.5))
    ax.set(
        xlabel=r"$a_1$ in $V_X=a_1V_{DD}$",
        ylabel=r"$a_2$ in $V_{TL}=a_2V_{DD}$",
        title="Equation (11): range-based supply sensitivity",
        xlim=(0.3, 0.8),
        ylim=(0.1, 0.7),
    )
    ax.legend(loc="upper left", frameon=True)
    colorbar = fig.colorbar(mesh, ax=ax)
    colorbar.set_label("Supply sensitivity (degC/V)")
    fig.tight_layout()
    fig.savefig(output_dir / "fig6_model.png", dpi=220)
    plt.close(fig)

    nominal = range_supply_sensitivity_c_per_v(0.5, 0.28)
    max_perturbed = -np.inf
    worst_a1 = np.nan
    worst_a2 = np.nan
    for a1 in np.linspace(0.45, 0.55, 101):
        for a2 in np.linspace(0.252, 0.308, 101):
            value = range_supply_sensitivity_c_per_v(a1, a2, points=501)
            if value > max_perturbed:
                max_perturbed = value
                worst_a1 = a1
                worst_a2 = a2
    return nominal, max_perturbed, worst_a1, worst_a2


def reconstruct_temperature_law(output_dir: Path) -> list[dict[str, float | str]]:
    """Reconstruct ideal Eq. (7) curves from the reported frequency endpoints."""
    temp_c = np.linspace(-40.0, 125.0, 400)
    temp_k = temp_c + 273.15
    endpoints = {
        "N-mode": (4.0e3, 15.0e6),
        "P-mode": (3.5e3, 23.0e6),
    }

    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    rows: list[dict[str, float | str]] = []
    x_end = np.array([1.0 / (273.15 - 40.0), 1.0 / (273.15 + 125.0)])
    for mode, (f_low, f_high) in endpoints.items():
        a, b = np.polyfit(x_end, np.log([f_low, f_high]), 1)
        frequency = np.exp(a / temp_k + b)
        sensitivity_20 = -a / (293.15**2)
        ax.semilogy(temp_c, frequency, linewidth=2.0, label=mode)
        rows.append(
            {
                "mode": mode,
                "eq7_a_kelvin": a,
                "eq7_b": b,
                "reconstructed_sensitivity_at_20c_percent_per_c": 100 * sensitivity_20,
                "reported_sensitivity_at_20c_percent_per_c": 5.6 if mode == "N-mode" else 6.1,
            }
        )

    ax.set(
        xlabel="Temperature (degC)",
        ylabel="Frequency (Hz)",
        title="Ideal Eq. (7) curves fitted to the reported endpoint ranges",
        xlim=(-40, 125),
    )
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output_dir / "temperature_frequency_reconstruction.png", dpi=220)
    plt.close(fig)
    return rows


def write_checks(output_dir: Path, fig5_checks: dict[str, float], fig6_checks: tuple[float, ...], temp_rows: list[dict[str, float | str]]) -> None:
    nominal, perturbed, worst_a1, worst_a2 = fig6_checks
    f_ref_hz = 50e6
    n_max = 2**16
    fdc_min_hz = f_ref_hz / n_max
    conversion_time_s = n_max / f_ref_hz

    n_power_w = 9.3e-6
    p_power_w = 9.8e-6
    n_resolution_k = 0.016
    p_resolution_k = 0.013
    n_energy_j = n_power_w * conversion_time_s
    p_energy_j = p_power_w * conversion_time_s
    n_fom_j_k2 = n_energy_j * n_resolution_k**2
    p_fom_j_k2 = p_energy_j * p_resolution_k**2

    summary_rows = [
        ("Fig5 a1=0.5, a2=0.3 delay sensitivity", fig5_checks["a2_0.3_delay_sensitivity_percent_per_v"], "%/V", "7.5"),
        ("Fig6 nominal a1=0.5, a2=0.28", nominal, "degC/V", "<2 contour"),
        ("Fig6 worst within independent +/-10% box", perturbed, "degC/V", "about 2.6"),
        ("Worst-box a1", worst_a1, "", "not reported"),
        ("Worst-box a2", worst_a2, "", "not reported"),
        ("16-bit FDC minimum at 50 MHz", fdc_min_hz / 1e3, "kHz", "0.763"),
        ("16-bit FDC conversion time at 50 MHz", conversion_time_s * 1e3, "ms", "1.31"),
        ("N-mode energy", n_energy_j * 1e9, "nJ", "12.2"),
        ("P-mode energy", p_energy_j * 1e9, "nJ", "12.8"),
        ("N-mode resolution FoM", n_fom_j_k2 * 1e12, "pJ*K^2", "3.1"),
        ("P-mode resolution FoM", p_fom_j_k2 * 1e12, "pJ*K^2", "2.2"),
    ]

    with (output_dir / "model_checks.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["check", "reproduced_value", "unit", "paper_value"])
        writer.writerows(summary_rows)

    with (output_dir / "temperature_fit.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(temp_rows[0].keys()))
        writer.writeheader()
        writer.writerows(temp_rows)

    print("Reproduction checks")
    for name, value, unit, paper_value in summary_rows:
        print(f"- {name}: {value:.6g} {unit} (paper: {paper_value})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "results",
        help="Directory for plots and CSV checks.",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    fig5_checks = plot_fig5(args.output_dir)
    fig6_checks = plot_fig6(args.output_dir)
    temp_rows = reconstruct_temperature_law(args.output_dir)
    write_checks(args.output_dir, fig5_checks, fig6_checks, temp_rows)


if __name__ == "__main__":
    main()
