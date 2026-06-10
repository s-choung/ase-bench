import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

results = {}
for metal in ["Cu", "Ag", "Au"]:
    atoms = bulk(metal, "fcc", cubic=True)
    cell0 = atoms.get_cell()
    volumes, energies = [], []
    for s in np.linspace(0.95, 1.05, 11):
        atoms.set_cell(cell0 * s, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
    v0, e0, B = eos.fit()
    a0 = v0 ** (1 / 3)  # cubic cell, 4 atoms
    B_GPa = B / units.kJ * 1.0e24
    results[metal] = (a0, B_GPa)

print(f"{'Metal':<8}{'a0 (Ang)':<12}{'B (GPa)':<10}")
print("-" * 30)
for metal, (a0, B) in results.items():
    print(f"{metal:<8}{a0:<12.4f}{B:<10.2f}")
