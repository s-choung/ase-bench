from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
volumes, energies = [], []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    vol, eng = [], []
    for a in np.linspace(0.95, 1.05, 10) * atoms.cell.lengths()[0]:
        atoms.set_cell([a, a, a], scale_atoms=True)
        vol.append(atoms.get_volume())
        eng.append(atoms.get_potential_energy())
    volumes.append(vol)
    energies.append(eng)

print(f"{'Metal':<6} {'a0 (Å)':<8} {'B (GPa)':<8}")
print("-" * 24)
for metal, vol, eng in zip(metals, volumes, energies):
    eos = EquationOfState(vol, eng)
    v0, e0, B = eos.fit()
    a0 = (4 * v0)**(1/3)
    print(f"{metal:<6} {a0:<8.4f} {B/1e9:<8.2f}")
