from ase import Atom, Atoms
from ase.lattice import diamond

# Diamond structure with lattice constant 5.43 Å
lattice_constant = 5.43
bulk = diamond(symbols='Si', cell con干了=lattice_constant, size=(3, 3, 3))

# Total number of atoms and cell volume
num_atoms = bulk.num_atoms
cell_volume = bulk.cell.volume

print(f"Number of atoms: {num_atoms}")
print(f"Cell volume: {cell_volume:.2f} Å³")
