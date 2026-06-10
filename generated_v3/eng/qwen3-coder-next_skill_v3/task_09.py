from ase import Atoms
from ase.build import bulk
from ase.io import write, read
from ase.cell import Cell
import numpy as np

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Save to POSCAR
write('POSCAR', atoms, format='vasp')

# Read back
atoms_read = read('POSCAR', format='vasp')

# Print results
print(f"Number of atoms: {len(atoms_read)}")
a, b, c, alpha, beta, gamma = atoms_read.get_cell_lengths_and_angles()
print(f"Cell parameters: a={a:.4f} Å, b={b:.4f} Å, c={c:.4f} Å, α={alpha:.2f}°, β={beta:.2f}°, γ={gamma:.2f}°")
