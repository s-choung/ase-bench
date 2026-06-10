import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.io import write

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()

    cell = atoms.get_cell()
    volumes, energies = [], []
    scale_factors = np.linspace(0.94, 1.06, 9)

    for s in scale_factors:
        test_atoms = atoms.copy()
        test_atoms.set_cell(cell * s, scale_atoms=True)
        test_atoms.calc = EMT()
        volumes.append(test_atoms.get_volume())
        energies.append(test_atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4 * v0) ** (1/3)
    results[metal] = {'a0': a0, 'B': B / units.kJ * 1e24}

print("-" * 45)
print(f"{'Metal':<8} {'a0 (Å)':<12} {'B (GPa)':<12}")
print("-" * 45)
for metal in ['Cu', 'Ag', 'Au']:
    print(f"{metal:<8} {results[metal]['a0']:<12.4f} {results[metal]['B']:<12.2f}")
print("-" * 45)
