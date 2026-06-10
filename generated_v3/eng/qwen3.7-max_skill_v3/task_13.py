from ase.build import bulk

atoms = bulk('Si', 'diamond', a=5.43, cubic=True).repeat((3, 3, 3))

print(f"Number of atoms: {len(atoms)}")
print(f"Cell volume: {atoms.get_volume():.2f} Å^3")
