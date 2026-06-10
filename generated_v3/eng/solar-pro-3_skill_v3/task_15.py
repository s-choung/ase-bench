from ase.build import fcc100
from ase import atoms_from_file

# Build bulk Cu
bulk = bulk('Cu','fcc', a=3.6)

# Generate (100) surface with 3 layers, supercell 3×3×3, vacuum 12 Å
slab = fcc100(bulk, layers=3, size=(3,3,3), vacuum=12.0)

print(f'Number of atoms: {len(slab)}')
print(slab.get_cell())
print(slab.get_cell_lengths_and_angles())
