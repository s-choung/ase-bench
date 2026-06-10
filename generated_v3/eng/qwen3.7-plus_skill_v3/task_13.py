from ase.build import bulk

atoms = bulk('Si', 'diamond', a=5.43).repeat((3, 3, 3))

print(f"Number of atoms: {len(atoms)}")
print(f"Cell volume: {atoms.get_volume():.3f} Å³")
