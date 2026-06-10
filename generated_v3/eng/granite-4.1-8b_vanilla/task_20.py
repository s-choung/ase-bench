from ase import Atoms
from ase.build import nanotube

# Create a (6,6) carbon nanotube with length = 4 Å
cntr = (6, 6)
length = 4  # in Ångström
tube = nanotube((cntr, length), graphene_layer=1)

# Print the number of atoms
print(f"Number of atoms: {len(tube)}")

# Print cell information
print("Cell info:")
print(tube.cell)

# Optional: print the lattice parameter of the nanotube
print(f"Lattice constant (diameter): {tube.get_circumference() / (cntr[0] + cntr[1]) * 2:.3f} Å")
