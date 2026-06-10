from ase import Atoms
from ase.cell import Cell

# HCP structure parameters
a = 2.95
c = a * 1.59

# Create HCP unit cell vectors
cell = Cell(
    basis=[[0, 0, 0], [2/3, 1/3, 1/2]],
    a=a,
    c=c,
    pbc=True,
)

# Create Ti atoms at HCP positions
positions = [
    [0, 0, 0],
    [2/3, 1/3, 1/2],
]
atoms = Atoms(symbols='Ti', positions=positions, cell=cell, pbc=True)

# Print cell vectors
print("Cell vectors (Å):")
print(cell.cell_vectors(unit='Å'))

# Print atomic positions
print("
Atomic positions (Å):")
print(atoms.get_positions(unit='Å'))
