from ase.build import surface, add_vacuum

atoms = surface('fcc', (2, 1, 1), layers=3)
add_vacuum(atoms, 10)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell:\n{atoms.cell}")
