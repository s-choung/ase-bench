from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ["Cu", "Ag", "Au"]

print(f"{'Metal':<6} {'a0 (Å)':>12} {'B0 (GPa)':>12}")
print("-" * 32)

for m in metals:
    atoms0 = bulk(m, "fcc", a=1.0)
    atoms0.calc = EMT()
    e0 = atoms0.get_potential_energy()

    a_vals = np.linspace(0.94, 1.06, 9) * atoms0.cell.lengths()[0]
    volumes, energies = [], []

    for a in a_vals:
        atoms = bulk(m, "fcc", a=a)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    v0, e0_fit, B = eos.fit()
    a0 = (4.0 * v0) ** (1.0 / 3.0)
    B_GPa = B / 1.0e9

    print(f"{m:<6} {a0:12.4f} {B_GPa:12.2f}")
