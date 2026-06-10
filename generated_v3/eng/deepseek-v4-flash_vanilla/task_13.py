import ase

# Create bulk Si with diamond structure
atoms = ase.build.bulk('Si', 'diamond', a=5.43)

# Make 3x3x3 supercell
atoms = atoms.repeat((3, 3, 3))

# Print number of atoms and cell volume
print(len(atoms))
print(atoms.get_volume())
