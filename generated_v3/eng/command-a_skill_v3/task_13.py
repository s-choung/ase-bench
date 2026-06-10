from ase.build import bulk
from ase.build import make_supercell

# Create Si bulk with diamond structure
atoms = bulk('Si', 'diamond', a=5.43)

# Make a 3x3x3 supercell
supercell = make_supercell(atoms, (3, 3, 3))

# Print number of atoms and cell volume
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} angstrom^3")
