from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create FCC Ag unit cell with initial lattice constant
a0 = 4.08  # approximate lattice constant for Ag in Angstrom
atoms = Atoms('Ag', positions=[[0, 0, 0]], cell=[a0, a0, a0], pbc=True)
atoms.set_calculator(EMT())

# Generate 7 lattice constants within ±5% range
a_range = np.linspace(a0 * 0.95, a0 * 1.05, 7)

# Calculate energies for each lattice constant
volumes = []
energies = []

for a in a_range:
    # Scale the cell
    cell = [[a, 0, 0], [0, a, 0], [0, 0, a]]
    atoms.set_cell(cell, scale_atoms=True)
    
    # Calculate energy
    energy = atoms.get_potential_energy()
    
    # Calculate volume (FCC unit cell has 1 atom, volume = a^3)
    volume = a**3
    volumes.append(volume)
    energies.append(energy)

# Fit with Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, equation='birch-murnaghan')
eos.fit()

# Get equilibrium parameters
aeq, Beq = eos.eos_parameters
B_GPa = Beq / 160.21766208  # Convert from eV/Å^3 to GPa

print(f"Equilibrium lattice constant (a0): {aeq**(1/3):.4f} Å")
print(f"Bulk modulus (B0): {B_GPa:.2f} GPa")
