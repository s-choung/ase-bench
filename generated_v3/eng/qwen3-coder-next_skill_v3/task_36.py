import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Create bulk Ag FCC
atoms = bulk('Ag', 'fcc')
a0 = atoms.get_cell_lengths_and_angles()[0]  # Initial lattice constant

# Generate 7 lattice constants within ±5% range
a_vals = np.linspace(0.95 * a0, 1.05 * a0, 7)
volumes, energies = [], []

for a in a_vals:
    # Create new cell with scaled lattice constant
    cell = atoms.get_cell()
    new_cell = cell.copy()
    new_cell[0] *= a / a0  # Scale x-direction (cell is cubic, so all same)
    new_cell[1] *= a / a0
    new_cell[2] *= a / a0
    
    # Create new Atoms object with scaled positions
    scaled_atoms = atoms.copy()
    scaled_atoms.set_cell(new_cell, scale_atoms=True)
    scaled_atoms.calc = EMT()
    
    volumes.append(scaled_atoms.get_volume())
    energies.append(scaled_atoms.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus to GPa
B_GPa = B / 1e9  # EMT energies in eV, volumes in Å³, so B in eV/Å³ -> GPa

print(f"Equilibrium lattice constant: {((v0 * 4 / np.pi) ** (1/3)):.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
