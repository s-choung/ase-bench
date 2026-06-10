import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

a0 = 4.09
volumes, energies = [], []

for a in np.linspace(a0 * 0.95, a0 * 1.05, 7):
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (4 * v0) ** (1 / 3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Ang")
print(f"Bulk modulus: {B / GPa:.2f} GPa")
