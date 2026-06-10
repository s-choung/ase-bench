from ase import Atoms
from ase.build import nanotube

# Create a (6,6) carbon nanotube with length=4 Å
atoms = nanotube((6, 6), 4)

# Print the number of atoms
print("Number of atoms:", len(atoms))

# Print cell information (dimensions and lattice vectors)
print("Cell length (a):", atoms.cell[0, 0])
print("Cell length (b):", atoms.cell[1, 1])
print("Cell angle (γ):", atoms.cell.angles[-1])
