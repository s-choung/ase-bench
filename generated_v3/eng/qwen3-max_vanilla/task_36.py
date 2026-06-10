from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Set up FCC Ag unit cell
a0_guess = 4.0  # Initial guess in Angstrom
cell = 0.5 * a0_guess * np.array([[1,1,0], [1,0,1], [0,1,1]])
atoms = Atoms('Ag', positions=[[0,0,0]], cell=cell, pbc=True)
atoms.calc = EMT()

# Generate lattice constants in ±5% range
a_vals = np.linspace(0.95 * a0_guess, 1.05 * a0_guess, 7)
energies = []

# Compute energies for each lattice constant
for a in a_vals:
    atoms.set_cell(0.5 * a * np.array([[1,1,0], [1,0,1], [0,1,1]]), scale_atoms=True)
    energies.append(atoms.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(a_vals**3, energies, eos='birch_murnaghan')
v0, e0, B0 = eos.fit()

# Calculate equilibrium lattice constant and bulk modulus in GPa
a0 = (4 * v0)**(1/3)
B0_GPa = B0 * 160.21766208  # Convert eV/Å^3 to GPa

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B0_GPa:.2f} GPa")
