from ase import Atoms
from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

# Create Au icosahedron with 3 shells
noshells = 3
gold_icosahedron = Icosahedron('Au', noshells=noshells)

# Print number of atoms
print(f"Number of atoms: {len(gold_icosahedron)}")

# Calculate and print center of mass
com = gold_icosahedron.get_center_of_mass()
print(f"Center of mass: [{com[0]:.4f}, {com[1]:.4f}, {com[2]:.4f}]")
