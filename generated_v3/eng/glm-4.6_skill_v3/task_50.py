import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
scales = np.linspace(0.96, 1.04, 7)
results = []

for metal in metals:
    volumes, energies = [], []
    for s in scales:
        atoms = bulk(metal, 'fcc', a=4.0, cubic=True)
        atoms.set_cell(atoms.get_cell() * s, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    results.append((metal, a0, B))

print(f"{'Metal':<5} {'a0 (Å)':<10} {'B (GPa)':<10}")
for m, a, b in results:
    print(f"{m:<5} {a:<10.3f} {b:<10.3f}")
