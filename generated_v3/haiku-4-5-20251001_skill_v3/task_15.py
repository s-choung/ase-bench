from ase.build import fcc100, add_vacuum

atoms = fcc100('Cu', size=(3, 3, 3), a=3.61, vacuum=0)
add_vacuum(atoms, 12)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell parameters:\n{atoms.get_cell()}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")
