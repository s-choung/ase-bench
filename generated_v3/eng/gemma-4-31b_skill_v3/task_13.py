from ase.build import bulk

atoms = bulk('Si', 'diamond', a=5.43)
atoms = atoms * (3, 3, 3)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell volume: {atoms.get_volume():.2f}")
