from ase.cluster.octahedron import Octahedron

# Create Cu octahedron nanoparticle with length=5
atoms = Octahedron('Cu', length=5)

print(len(atoms))
print(atoms.positions.shape)
