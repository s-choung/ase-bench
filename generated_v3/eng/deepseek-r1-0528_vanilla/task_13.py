from ase.build import bulk

atoms = bulk('Si', 'diamond', a=5.43, cubic=True)
supercell = atoms.repeat((3, 3, 3))
num_atoms = len(supercell)
volume = supercell.get_volume()
print(f"Number of atoms: {num_atoms}")
print(f"Volume: {volume:.3f} Å³")
