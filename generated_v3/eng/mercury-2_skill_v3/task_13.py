from ase.build import bulk

# bulk Si, diamond structure, a = 5.43 Å
atoms = bulk('Si', 'diamond', a=5.43)

# 3×3×3 supercell
atoms = atoms * (3, 3, 3)

# output
print(atoms.get_number_of_atoms(), atoms.get_volume())
