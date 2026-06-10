import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

a_guess = {"Cu": 3.61, "Ag": 4.09, "Au": 4.08}

print(f"{'Metal':<6} {'a0 (Å)':>12} {'B (GPa)':>12}")
print("-" * 32)

for metal, a0 in a_guess.items():
    volumes, energies = [], []

    for a in a0 * np.linspace(0.94, 1.06, 13):
        atoms = bulk(metal, "fcc", a=a, cubic=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
    v0, e0, B = eos.fit()

    a_eq = v0 ** (1.0 / 3.0)
    B_gpa = B / kJ * 1.0e24

    print(f"{metal:<6} {a_eq:12.4f} {B_gpa:12.2f}")
