from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.09  # Ag FCC initial lattice constant (Å)
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    a = a0 * x
    atoms = Atoms('Ag', cell=np.eye(3) * a, pbc=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
