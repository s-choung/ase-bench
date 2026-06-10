from ase import Atoms
from ase.build import octahedron

# Create a Cu octahedron nanoparticle with edge length 5 Å
np_size = 5
cu_atom = Atoms('Cu', [(0, 0, 0)], pbc=False)
nanoparticle = octahedron('Cu', np_size, pbc=False)

# Significant basis for NP indicates ionic radii
nanoparticle.extend(cu_atom)
nanoparticle.build()

# Print number of atoms and positions shape
print(f"Number of atoms: {len(nanoparticle)}")
print(f"Positions shape: {nanoparticle.positions.shape}")
