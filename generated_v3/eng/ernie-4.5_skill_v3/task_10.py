from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create Cu octahedron nanoparticle with length=5
atoms = Octahedron('Cu', length=5)

# Set EMT calculator (optional for this task, but shown for completeness)
atoms.calc = EMT()

# Print number of atoms and positions shape
print(f"Number of atoms: {len(atoms)}")
print(f"Positions array shape: {atoms.positions.shape}")
