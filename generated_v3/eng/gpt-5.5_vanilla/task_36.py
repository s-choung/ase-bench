import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

a_ref = 4.09
a_values = np.linspace(0.95 * a_ref, 1.05 * a_ref, 7)

volumes, energies = [], []

for a in a_values:
    atoms = bulk("Ag", "fcc", a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()

a0 = v0 ** (1 / 3)

print(f"Equilibrium lattice constant: {a0:.6f} Angstrom")
print(f"Bulk modulus: {B / GPa:.3f} GPa")
