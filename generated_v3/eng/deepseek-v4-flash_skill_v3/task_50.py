import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)
    cell = atoms.get_cell()
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 9):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 * 4) ** (1/3)
    results[metal] = (a0, B)

print(f"{'Metal':<6} {'a0 (Å)':<10} {'B (GPa)':<10}")
print("-" * 26)
for metal, (a0, B) in results.items():
    print(f"{metal:<6} {a0:<10.4f} {B:<10.2f}")
