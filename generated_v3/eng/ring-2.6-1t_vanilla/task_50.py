from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import fit_eos
import numpy as np

metals = ['Cu', 'Ag', 'Au']
a_guess = {'Cu': 3.60, 'Ag': 4.09, 'Au': 4.08}

table = []

for sym in metals:
    a0_init = a_guess[sym]
    atoms = bulk(sym, 'fcc', a=a0_init)
    a_vals = a0_init * np.linspace(0.9, 1.1, 15)

    volumes, energies = [], []
    for a in a_vals:
        atoms.set_cell([a, a, a], scale_atoms=True)
        atoms.calc = EMT()
        e = atoms.get_potential_energy()
        volumes.append(atoms.get_volume())
        energies.append(e)

    e0, B0_ev, B1, V0 = fit_eos(volumes, energies)
    a_eq = V0 ** (1.0 / 3.0)                # conventional cubic cell
    B0_GPa = B0_ev * 160.217662              # 1 eV/Å³ → 160.218 GPa
    table.append((sym, a_eq, B0_GPa))

print(f"{'Metal':<6} {'a₀ (Å)':>9} {'B₀ (GPa)':>10}")
print("-" * 28)
for sym, a, B in table:
    print(f"{sym:<6} {a:9.4f} {B:10.2f}")
