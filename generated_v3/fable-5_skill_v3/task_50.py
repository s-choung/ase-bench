import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

guess_a = {'Cu': 3.6, 'Ag': 4.1, 'Au': 4.1}
results = []

for metal, a0 in guess_a.items():
    atoms = bulk(metal, 'fcc', a=a0, cubic=True)
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
    a_eq = v0 ** (1.0 / 3.0)  # cubic cell, 4 atoms
    B_GPa = B / units.kJ * 1.0e24
    results.append((metal, a_eq, B_GPa))

print(f"{'Metal':<8}{'a_eq (Ang)':<14}{'B (GPa)':<10}")
print("-" * 32)
for metal, a_eq, B_GPa in results:
    print(f"{metal:<8}{a_eq:<14.4f}{B_GPa:<10.2f}")
