from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create Cu octahedron nanoparticle
nano = Octahedron('Cu', length=5)
nano.calc = EMT()

# Cell not needed: use EMT potential
print("Atoms count:", len(nano))
print("Positions shape:", nano.positions.shape)
