from ase import Atoms
from ase.build import bulk
from ase.spacegroup import crystal

# Create a Ti HCP bulk structure
atoms = bulk('Ti', 'hcp', a=2.95, c=2.95*1.59, cubic=False, orthorhombic=False)

# Get the cell vectors
cell_vectors = atoms.get_cell_lengths_and_angles()
print("Cell Vectors:")
print("a =", cell_vectors[0])
print("b =", cell_vectors[1])
print("c =", cell_vectors[2])
print("alpha =", cell_vectors[3])
print("beta =", cell_vectors[4])
print("gamma =", cell_vectors[5])

# Get the atomic positions
print("\nAtomic Positions:")
print(atoms.positions)
