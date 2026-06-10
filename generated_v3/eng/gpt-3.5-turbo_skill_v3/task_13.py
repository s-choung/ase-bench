from ase.build import bulk

# Create a Si bulk with diamond structure
atoms = bulk('Si', crystalstructure='diamond', a=5.43)

# Make a 3x3x3 supercell
supercell = atoms * (3, 3, 3)

# Print the number of atoms and cell volume
num_atoms = len(supercell)
cell_volume = supercell.get_volume()

print(f"Number of atoms: {num_atoms}")
print(f"Cell volume: {cell_volume:.2f} Å^3")
