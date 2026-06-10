import numpy as np
from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create Cu Octahedron nanoparticle
# length is specified by the number of shells/layers
atoms = Octahedron('Cu', shells=5)
atoms.set_calculator(EMT())

print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.get_positions().shape}")
