"""MD visualization = Temperature & Energy vs time trace. A single MD frame is
indistinguishable from a static bulk, and thermal vibration at the task
temperature is too small to read as a structure overlay. A T(t)/E(t) trace is
the standard, unambiguous 'this is molecular dynamics' signal. Re-runs a short
EMT MD from each task's system and plots. Writes renders/<tid>.png (overwriting
the static render). Run after structure_extract."""
import os
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ase.io import read
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase import units

BASE = os.path.dirname(os.path.abspath(__file__))
STRUCT = os.path.join(BASE, "structures")
RENDERS = os.path.join(BASE, "renders_plot")
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})

# tid -> (temperature K, ensemble label, nve?)
MD_TASKS = {
    "T06": (300, "Langevin NVT", False), "T07": (300, "NVE", True),
    "T27": (500, "NVT", False), "T28": (450, "NVT ramp", False),
    "T29": (500, "NVE", True), "T30": (300, "NPT", False),
    "T31": (500, "NPT", False),
}


def run_trace(tid, temp, nve, nsteps=120, dt=5.0):
    atoms = read(os.path.join(STRUCT, f"{tid}.xyz"))
    atoms.calc = EMT()
    MaxwellBoltzmannDistribution(atoms, temperature_K=temp)
    if nve:
        dyn = VelocityVerlet(atoms, timestep=dt * units.fs)
    else:
        dyn = Langevin(atoms, timestep=dt * units.fs, temperature_K=temp, friction=0.01)
    T, E, t = [], [], []
    for i in range(nsteps):
        dyn.run(1)
        T.append(atoms.get_temperature())
        E.append(atoms.get_potential_energy() + atoms.get_kinetic_energy())
        t.append(i * dt)
    return np.array(t), np.array(T), np.array(E)


def plot_md(tid, temp, label, nve):
    t, T, E = run_trace(tid, temp, nve)
    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    ax.plot(t, T, color="#dc2626", lw=1.6, label="Temperature")
    ax.set_xlabel("time (fs)")
    ax.set_ylabel("Temperature (K)", color="#dc2626")
    ax.tick_params(axis="y", labelcolor="#dc2626")
    ax.axhline(temp, ls="--", color="#dc2626", lw=0.8, alpha=0.5)
    ax2 = ax.twinx()
    ax2.plot(t, E - E[0], color="#4f46e5", lw=1.6, label="Total E")
    ax2.set_ylabel("E − E₀ (eV)", color="#4f46e5")
    ax2.tick_params(axis="y", labelcolor="#4f46e5")
    ax.set_title(f"{tid} · {label}  ({temp} K)", fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(os.path.join(RENDERS, f"{tid}.png"), dpi=150, facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"{tid}: MD trace  Tmean={T.mean():.0f}K  dE={E.max()-E.min():.3f}eV")


def main():
    os.makedirs(RENDERS, exist_ok=True)
    for tid, (temp, label, nve) in MD_TASKS.items():
        try:
            plot_md(tid, temp, label, nve)
        except Exception as e:
            print(f"{tid}: fail {e}")


if __name__ == "__main__":
    main()
