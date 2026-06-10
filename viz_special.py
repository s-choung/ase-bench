"""Type-aware visualizations for tasks whose ESSENCE is not a static structure:
  - EOS tasks (T05, T36, T50): energy-vs-volume curve + Birch-Murnaghan fit
  - vibration tasks (T08, T32, T33): vibrational frequency spectrum
These re-run the (cheap, EMT) computation and write a matplotlib figure to
renders/<tid>.png, OVERWRITING the misleading static-bulk render. Run AFTER
render_gallery.py. MD trajectory overlays are handled separately (viz_md.py).
"""
import os
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ase.build import bulk, molecule
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.vibrations import Vibrations
import tempfile

BASE = os.path.dirname(os.path.abspath(__file__))
RENDERS = os.path.join(BASE, "renders_plot")
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
ACCENT = "#4f46e5"


def eos_curve(metal, a0, frac=0.06, npts=9, eos_type="sj"):
    at = bulk(metal, "fcc", a=a0)
    cell0 = at.get_cell()
    vols, engs = [], []
    for s in np.linspace(1 - frac, 1 + frac, npts):
        a = at.copy()
        a.set_cell(cell0 * s, scale_atoms=True)
        a.calc = EMT()
        vols.append(a.get_volume())
        engs.append(a.get_potential_energy())
    eos = EquationOfState(vols, engs, eos=eos_type)
    v0, e0, B = eos.fit()
    from ase.units import kJ
    B_GPa = B / kJ * 1.0e24
    return np.array(vols), np.array(engs), v0, e0, B_GPa


def plot_eos_single(tid, metal, a0, title):
    vols, engs, v0, e0, B = eos_curve(metal, a0)
    vv = np.linspace(vols.min(), vols.max(), 200)
    # smooth fit via parabola-ish using EOS object refit
    eos = EquationOfState(vols, engs)
    eos.fit()
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    ax.plot(vols, engs, "o", color=ACCENT, ms=7, label="EMT points")
    try:
        # ASE EOS can give a fit function
        from ase.eos import EquationOfState as E2
        ax.plot(vv, np.poly1d(np.polyfit(vols, engs, 3))(vv), "-", color="#111", lw=1.6, label="fit")
    except Exception:
        pass
    ax.axvline(v0, ls="--", color="#dc2626", lw=1.2)
    ax.set_xlabel("Volume (Å³)")
    ax.set_ylabel("Energy (eV)")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.text(0.04, 0.04, f"$V_0$={v0:.2f} Å³\n$B$={B:.0f} GPa",
            transform=ax.transAxes, fontsize=10.5, va="bottom",
            bbox=dict(boxstyle="round,pad=0.3", fc="#eef2ff", ec="#c7d2fe"))
    ax.legend(fontsize=9, frameon=False, loc="upper center")
    fig.tight_layout()
    fig.savefig(os.path.join(RENDERS, f"{tid}.png"), dpi=150, facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"{tid}: EOS {metal}  V0={v0:.2f} B={B:.0f}GPa")


def plot_eos_multi(tid, metals_a0, title):
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    cols = {"Cu": "#c05a3c", "Ag": "#6b7280", "Au": "#d4a017"}
    for metal, a0 in metals_a0.items():
        vols, engs, v0, e0, B = eos_curve(metal, a0)
        ax.plot(vols, engs - e0, "o-", ms=5, lw=1.3, color=cols.get(metal, ACCENT),
                label=f"{metal}: B={B:.0f} GPa")
    ax.set_xlabel("Volume (Å³)")
    ax.set_ylabel("E − E₀ (eV)")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.legend(fontsize=9.5, frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(RENDERS, f"{tid}.png"), dpi=150, facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"{tid}: EOS multi {list(metals_a0)}")


def vib_freqs(atoms):
    atoms = atoms.copy()
    atoms.calc = EMT()
    with tempfile.TemporaryDirectory() as d:
        vib = Vibrations(atoms, name=os.path.join(d, "vib"))
        vib.run()
        fr = vib.get_frequencies()  # cm^-1, complex for imaginary modes
    return fr


def plot_vib(tid, atoms, label, title):
    fr = vib_freqs(atoms)
    real = np.array([f.real if abs(f.imag) < 1e-6 else 0.0 for f in fr])
    imag = np.array([f.imag for f in fr])
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    idx = np.arange(len(fr))
    realmask = np.abs(imag) < 1e-6
    ax.bar(idx[realmask], real[realmask], color=ACCENT, width=0.6, label="real modes")
    if (~realmask).any():
        ax.bar(idx[~realmask], imag[~realmask], color="#dc2626", width=0.6, label="imaginary (trans/rot)")
    ax.set_xlabel("mode index")
    ax.set_ylabel("frequency (cm⁻¹)")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.axhline(0, color="#999", lw=0.8)
    top = np.max(real) if real.size else 1
    ax.text(0.04, 0.95, f"{label}\nmax {top:.0f} cm⁻¹", transform=ax.transAxes,
            fontsize=10.5, va="top",
            bbox=dict(boxstyle="round,pad=0.3", fc="#eef2ff", ec="#c7d2fe"))
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(os.path.join(RENDERS, f"{tid}.png"), dpi=150, facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"{tid}: vib {label}  {len(fr)} modes")


def main():
    os.makedirs(RENDERS, exist_ok=True)
    # EOS
    plot_eos_single("T05", "Cu", 3.6, "T05 · Cu FCC EOS")
    plot_eos_single("T36", "Ag", 4.09, "T36 · Ag FCC EOS")
    plot_eos_multi("T50", {"Cu": 3.6, "Ag": 4.09, "Au": 4.08}, "T50 · Cu/Ag/Au EOS")
    # vibration
    plot_vib("T08", molecule("N2"), "N₂", "T08 · N₂ vibrations")
    plot_vib("T32", molecule("H2O"), "H₂O", "T32 · H₂O vib modes")
    plot_vib("T33", molecule("CH4"), "CH₄", "T33 · CH₄ vibrations")


if __name__ == "__main__":
    main()
