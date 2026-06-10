from ase.build import bulk
from ase.visualize import view

# Create Si bulk with diamond structure
si = bulk('Si', 'diamond', a=5.43, cubic=True)

# Create 3x3x3 supercell
supercell = si.repeat((3, 3, 3))

# Print results
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} Å³")
