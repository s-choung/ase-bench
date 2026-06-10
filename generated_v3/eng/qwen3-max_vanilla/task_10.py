from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create Cu octahedron nanoparticle with length=5
atoms = Octahedron('Cu', 5)

# Assign EMT calculator (optional but uses only built-in calculators)
atoms.calc = EMT()

# Print number of atoms and positions shape
print(len(atoms))
print(atoms.positions.shape)
