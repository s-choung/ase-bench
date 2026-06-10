import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ["Cu", "Ag", "Au"]
results = []

for m in metals:
    atoms0 = bulk(m, "fcc", cubic=True)
    a0 = atoms0.cell.lengths()[0]
    scales = np.linspace(0.94, 1.06, 9)
    volumes, energies = [], []

    for s in scales:
        atoms = atoms0.copy()
        atoms.set_cell(atoms0.cell * s, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
    v0, e0, B = eos.fit()
    a_eq = (4.0 * v0) ** (1.0 / 3.0)
    B_GPa = B * 160.21766208

    results.append((m, a_eq, B_GPa))

print(f"{'Metal':<6} {'a_eq (Å)':>12} {'B (GPa)':>12}")
print("-" * 32)
for m, a_eq, B_GPa in results:
    print(f"{m:<6} {a_eq:12.4f} {B_GPa:12.2f}")
