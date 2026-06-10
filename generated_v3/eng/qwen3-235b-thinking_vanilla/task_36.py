from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.09  # Initial guess for Ag FCC lattice constant (Å)
factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for f in factors:
    atoms = bulk('Ag', a=a0*f, cubic=True)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (4 * v0)**(1/3)  # FCC: 4 atoms per conventional cell
B_GPa = B / units.GPa  # Convert eV/Å³ to GPa

print(f"Equilibrium lattice constant: {a_eq:.5f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
