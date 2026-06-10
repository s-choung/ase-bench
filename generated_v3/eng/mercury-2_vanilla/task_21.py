from ase.build import icosahedron
from ase.calculators.emt import EMT

# Create Au icosahedron with 3 shells
atoms = icosahedron('Au', shells=3)

# Assign a built‑in calculator
atoms.set_calculator(EMT())

# Output requested information
print("Number of atoms:", len(atoms))
print("Center of mass:", atoms.get_center_of_mass())
