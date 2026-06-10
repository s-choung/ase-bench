from ase.build import surface
from ase import Atoms, units

# Create a (2,1,1) surface of Cu with 3 layers and add 10 angstroms of vacuum
slab = surface('Cu', (2,1,1), 3, vacuum=10.0)

# Print the number of atoms and cell
num_atoms = len(slab)
cell_lengths, cell_angles = slab.get_cell_lengths_and_angles()

print(f'Number of atoms: {num_atoms}')
print(f'Cell lengths and angles: {cell_lengths} Å, {cell_angles} degrees')
