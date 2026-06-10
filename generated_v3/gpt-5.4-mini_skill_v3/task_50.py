import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for sym in metals:
    atoms0 = bulk(sym, 'fcc', a=4.0, cubic=True)
    cell0 = atoms0.get_cell().copy()
    vols, ens = [], []

    for s in np.linspace(0.94, 1.06, 9):
        atoms = atoms0.copy()
        atoms.set_cell(cell0 * s, scale_atoms=True)
        atoms.calc = EMT()
        vols.append(atoms.get_volume())
        ens.append(atoms.get_potential_energy())

    eos = EquationOfState(vols, ens, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4.0 * v0 / len(atoms0)) ** (1.0 / 3.0)

    results.append((sym, a0, B))

print(f"{'Metal':<6} {'a0 (Å)':>12} {'B (eV/Å^3)':>14} {'B (GPa)':>12}")
for sym, a0, B in results:
    print(f"{sym:<6} {a0:12.4f} {B:14.6f} {B * 160.21766208:12.2f}")
