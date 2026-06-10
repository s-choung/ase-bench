from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa
import numpy as np

a0 = 4.09
factors = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []

for f in factors:
    atoms = bulk('Ag', 'fcc', a=a0*f)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium lattice constant: {v0**(1/3):.4f} Angstrom")
print(f"Bulk modulus: {B/GPa:.2f} GPa")
