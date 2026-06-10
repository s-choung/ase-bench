from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

# Create Au icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Assign EMT calculator (required for some ASE operations, though not used here)
atoms.calc = EMT()

# Print number of atoms and center of mass
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
