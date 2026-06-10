from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ["Cu", "Ag", "Au"]
results = []

for m in metals:
    atoms0 = bulk(m, "fcc")
    vols = []
    energies = []
    a0 = atoms0.cell.lengths()[0]
    scales = np.linspace(0.94, 1.06, 9)

    for s in scales:
        atoms = bulk(m, "fcc", a=a0 * s)
        atoms.calc = EMT()
        vols.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(vols, energies)
    v0, e0, B = eos.fit()
    a_eq = (4.0 * v0) ** (1.0 / 3.0)
    results.append((m, a_eq, B))

print(f"{'Metal':<6} {'a_eq (Å)':>12} {'Bulk modulus (eV/Å^3)':>24} {'Bulk modulus (GPa)':>22}")
for m, a_eq, B in results:
    print(f"{m:<6} {a_eq:12.6f} {B:24.6f} {B * 160.21766208:22.3f}")
