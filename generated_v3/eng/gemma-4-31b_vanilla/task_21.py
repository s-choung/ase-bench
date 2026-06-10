from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

# Create Au Icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Attach a built-in calculator
atoms.calc = EMT()

# Print requested properties
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
