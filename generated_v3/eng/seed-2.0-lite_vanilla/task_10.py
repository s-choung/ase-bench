from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create Cu octahedron nanoparticle with edge length (number of atoms per edge) = 5
cu_octahedron = Octahedron(symbol='Cu', length=5, latticeconstant=3.61)
# Attach built-in EMT calculator
cu_octahedron.calc = EMT()

# Output required metrics
print(f"Number of atoms: {len(cu_octahedron)}")
print(f"Positions array shape: {cu_octahedron.positions.shape}")
