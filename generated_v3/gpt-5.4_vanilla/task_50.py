from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ["Cu", "Ag", "Au"]
results = []

for metal in metals:
    atoms0 = bulk(metal, "fcc")
    a0 = atoms0.cell.lengths()[0]
    scales = np.linspace(0.96, 1.04, 9)
    volumes = []
    energies = []

    for s in scales:
        atoms = bulk(metal, "fcc", a=a0 * s)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a_eq = (4.0 * v0) ** (1.0 / 3.0)
    B_GPa = B / 1.0e9 / 1.602176634e-19 * 1.0e30

    results.append((metal, a_eq, B_GPa))

print(f"{'Metal':<6} {'a_eq (Å)':>12} {'Bulk Modulus (GPa)':>22}")
print("-" * 42)
for metal, a_eq, B_GPa in results:
    print(f"{metal:<6} {a_eq:12.4f} {B_GPa:22.2f}")
