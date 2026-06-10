from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    a0 = 3.6 if metal == 'Cu' else 4.1 if metal == 'Ag' else 4.1
    atoms = bulk(metal, 'fcc', a=a0, cubic=True)
    atoms.calc = EMT()
    cell0 = atoms.get_cell()
    volumes = []
    energies = []
    for x in np.linspace(0.92, 1.08, 9):
        atoms.set_cell(cell0 * x, scale_atoms=True)
        e = atoms.get_potential_energy()
        volumes.append(atoms.get_volume())
        energies.append(e)
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = (v0 * 4)** (1.0/3.0)
    B_gpa = B * 1e4 / 160.217662
    results.append((metal, a_eq, B_gpa))

print('Metal | a_eq (Å) | B (GPa)')
print('------|----------|---------')
for m, a, b in results:
    print(f'{m:4}  | {a:8.3f}  | {b:7.1f}')
