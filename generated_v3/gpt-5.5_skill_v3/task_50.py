import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

EV_A3_TO_GPA = 160.21766208

metals = {"Cu": 3.60, "Ag": 4.09, "Au": 4.08}
results = []

for sym, a_guess in metals.items():
    atoms0 = bulk(sym, "fcc", a=a_guess, cubic=True)
    cell0 = atoms0.get_cell()
    volumes, energies = [], []

    for s in np.linspace(0.94, 1.06, 13):
        atoms = atoms0.copy()
        atoms.set_cell(cell0 * s, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
    v0, e0, B = eos.fit()
    a0 = v0 ** (1.0 / 3.0)
    results.append((sym, a0, B * EV_A3_TO_GPA, e0))

print(f"{'Metal':<6} {'a0 (Å)':>12} {'Bulk modulus (GPa)':>20} {'E0 (eV/cell)':>16}")
print("-" * 58)
for sym, a0, B_gpa, e0 in results:
    print(f"{sym:<6} {a0:12.4f} {B_gpa:20.2f} {e0:16.6f}")
