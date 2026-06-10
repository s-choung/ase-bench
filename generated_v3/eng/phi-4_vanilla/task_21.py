from ase.build import io
from ase.build import make_icosahedron
from ase.visualize import view as ase_view # For visualization, only used for debugging purposes, remove if not required
from ase.data import atomic_numbers

# Create an Au Icosahedron with no shells
au_icosahedron = make_icosahedron('Au', nshells=3, a=2.88)

# Print the number of atoms
num_atoms = len(au_icosahedron)
print(f"Number of atoms: {num_atoms}")

# Calculate and print center of mass
com = au_icosahedron.get_center_of_mass()
print(f"Center of mass: {com}")

# Debugging visualization (optional and can be removed)
# ase_view(au_icosahedron)
