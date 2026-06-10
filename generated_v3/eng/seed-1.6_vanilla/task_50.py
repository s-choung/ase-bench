import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}
conv = 160.21766208  # eV/Å³ to GPa

for metal in metals:
    atoms = bulk(metal, 'fcc')
    a_init = atoms.cell[0, 0]
    a_vals = a_init * np.linspace(0.95, 1.05, 7)
    vols, eners = [], []
    for a in a_vals:
        atoms.set_cell([a, a, a], scale_atoms=True)
        atoms.calc = EMT()
        eners.append(atoms.get_potential_energy())
        vols.append(atoms.get_volume())
    eos = EquationOfState(vols, eners, 'birchmurnaghan')
    v0, _, B0 = eos.fit()
    a0 = v0 ** (1/3)
    results[metal] = (a0.round(3), B0 * conv.round(2))

# Print comparison table
print(f"{'Metal':<4} | {'a0 (Å)':<7} | {'B0 (GPa)':<9}")
print('-'*30)
for m, (a, b) in results.items():
    print(f"{m:<4} | {a:<7} | {b:<9.1f}")
