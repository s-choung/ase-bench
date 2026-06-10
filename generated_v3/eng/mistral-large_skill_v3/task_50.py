from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()
    cell = atoms.get_cell()
    volumes, energies = [], []

    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4 * v0)**(1/3)
    B_GPa = B / units.GPa
    results.append((metal, a0, B_GPa))

print(f"{'Metal':<6} {'a0 (Å)':<8} {'B (GPa)':<8}")
print("-" * 24)
for metal, a0, B in results:
    print(f"{metal:<6} {a0:<8.4f} {B:<8.2f}")
