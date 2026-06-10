from ase.build import bulk

# 1. Create a primitive diamond Si cell
si_primitive = bulk('Si', 'diamond', a=5.43)

# 2. Create a 3x3x3 supercell
si_supercell = si_primitive * (3, 3, 3)

# 3. Get and print the number of atoms and volume
num_atoms = len(si_supercell)
volume = si_supercell.get_volume()

print(f"Number of atoms: {num_atoms}")
print(f"Cell volume (Å^3): {volume:.2f}")
