import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    a_values = np.linspace(3.0, 4.5, 10)
    energies, volumes = [], []
    for a in a_values:
        atoms = bulk(metal, 'fcc', a=a)
        atoms.calc = EMT()
        energies.append(atoms.get_energy())
        volumes.append(atoms.get_volume())
    eos = EquationOfState(volumes, energies)
    v0, B = eos.v0, eos.B
    a0 = v0 ** (1/3)
    results.append((metal, a0, B))

print("Metal | a0 (Å) | B (GPa)")
print("-" * 25)
for metal, a0, B in results:
    print(f"{metal} | {a0:.4f} | {B:.2f}")
