from ase.cluster import Octahedron

# Build Cu octahedral nanoparticle (edge length = 5 atoms)
np_atom = Octahedron('Cu', length=5)

# Output atom count and shape of the position array
print(np_atom.get_number_of_atoms())   # number of atoms
print(np_atom.positions.shape)        # (N, 3) where N = number of atoms
