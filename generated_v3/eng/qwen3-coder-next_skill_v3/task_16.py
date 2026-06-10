from ase.build import bcc110
from ase import Atoms

# Create Fe BCC(110) surface with 4 layers
atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print number of atoms and cell size
print(f"Number of atoms: {len(atoms)}")
cell_params = atoms.get_cell_lengths_and_angles()
print(f"Cell size: a={cell_params[0]:.2f} Å, b={cell_params[1]:.2f} Å, c={cell_params[2]:.2f} Å")
