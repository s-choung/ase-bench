from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)  # initial guess
    atoms.calc = EMT()
    a0 = atoms.cell.lengths()[0]

    cell = atoms.get_cell()
    volumes, energies = [], []
    for scale in np.linspace(0.90, 1.10, 11):
        atoms.set_cell(cell * scale, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = (4 * v0 / len(atoms)) ** (1/3)
    B_GPa = B / units.GPa
    results.append((metal, a_eq, B_GPa))

print(f"{'Metal':<6} {'a_eq (Å)':<12} {'Bulk Modulus (GPa)':<20}")
print('-' * 40)
for metal, a_eq, B in results:
    print(f"{metal:<6} {a_eq:<12.4f} {B:<20.2f}")
