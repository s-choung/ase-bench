from ase.build import nanotube

# Create a (6,6) armchair carbon nanotube with 4 unit cells
atoms = nanotube(6, 6, length=4)

print("Number of atoms:", len(atoms))
print("Cell:")
print(atoms.get_cell())
