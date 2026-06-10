# EOS fitting for FCC Cu, Ag, Au using EMT
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

def fit_eos(symbol, a_guess):
    atoms = bulk(symbol, "fcc", a=a_guess, cubic=True)  # 1‑atom primitive cell
    atoms.calc = EMT()
    scales = np.linspace(0.94, 1.06, 9)                # volume sweep
    vols, enes = [], []
    for s in scales:
        a = atoms.copy()
        a.set_cell(a.get_cell() * s, scale_atoms=True)
        vols.append(a.get_volume() / len(a))          # per‑atom volume
        enes.append(a.get_potential_energy())
    eos = EquationOfState(vols, enes)
    v0, _, B = eos.fit()                              # B in GPa
    a_eq = (4 * v0) ** (1 / 3)                         # FCC: V_atom = a³/4
    return a_eq, B

if __name__ == "__main__":
    data = []
    for sym, a0 in [("Cu", 3.6), ("Ag", 4.09), ("Au", 4.08)]:
        a_eq, B = fit_eos(sym, a0)
        data.append((sym, a_eq, B))

    print("{:<5} {:>12} {:>12}".format("Metal", "a_eq (Å)", "B (GPa)"))
    for sym, a_eq, B in data:
        print(f"{sym:<5} {a_eq:12.4f} {B:12.2f}")
