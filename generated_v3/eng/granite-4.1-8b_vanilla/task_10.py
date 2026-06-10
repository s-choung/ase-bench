from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create a Cu octahedron nanoparticle with a specified length
length = 5  # Length in angstroms
atoms = Octahedron('Cu', length)

# Assign a calculator (EMT) for potential energy calculations, though not used here
atoms.set_calculator(EMT())

# Print the number of atoms and the shape of the positions array
print("Number of atoms:", len(atoms))
print("Positions shape:", atoms.positions.shape)
