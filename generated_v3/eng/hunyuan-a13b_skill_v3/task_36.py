from ase import Atoms
from ase.eos import EquationOfState
import numpy as np

# Initial lattice constant for Ag FCC
a_initial = 4.08  # Angstrom
percent_range = 0.05  # +/-5% range
num_points = 7

# Create initial atoms object
atoms = Atoms('Ag', cell=[a_initial] * 3, pbc=True)
atoms.calc = EMT()

# Prepare data for EOS fitting
volumes, energies = [], []
for i in range(num_points):
    a = a_initial * (1 + (i - (num_points - 1) / 2) * 2 * percent_range / num_points)
    atoms.set_cell([a] * 3, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Perform EOS fitting
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium lattice constant: {v0:.4f} Å")
print(f"Bulk modulus: {B / 1e5:.2f} GPa")  # Convert界面到GPa
