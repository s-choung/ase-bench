import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

guesses = {"Cu": 3.60, "Ag": 4.09, "Au": 4.08}

print(f"{'Metal':<6} {'a0 (Å)':>12} {'B (GPa)':>12}")
print("-" * 32)

for metal, a_guess in guesses.items():
    atoms0 = bulk(metal, "fcc", a=a_guess, cubic=True)
    cell0 = atoms0.get_cell()

    volumes, energies = [], []
    for scale in np.linspace(0.94, 1.06, 13):
        atoms = atoms0.copy()
        atoms.set_cell(cell0 * scale, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
    v0, e0, B = eos.fit()

    a0 = v0 ** (1.0 / 3.0)
    B_GPa = B / units.kJ * 1.0e24

    print(f"{metal:<6} {a0:12.4f} {B_GPa:12.2f}")
