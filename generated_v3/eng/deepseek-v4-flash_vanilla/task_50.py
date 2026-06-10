from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    volumes = []
    energies = []
    for a in np.linspace(0.95, 1.05, 11) * atoms.cell[0, 0]:
        atoms.set_cell([a, a, a], scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = (4 * v0) ** (1/3)
    results.append((metal, a0, B))

print(f"{'Metal':<8} {'a0 (Å)':<12} {'B (GPa)':<12}")
print("-" * 32)
for metal, a0, B in results:
    print(f"{metal:<8} {a0:<12.4f} {B:<12.1f}")
