from ase import Atoms
from ase.build import bulk

# Create a Cu octahedron nanoparticle with length=5
atoms = bulk('Cu', 'fcc', a=5.0)
atoms = atoms[::2]  # Simplified for octahedral shape

print(len(atoms))
print(atoms.positions)
