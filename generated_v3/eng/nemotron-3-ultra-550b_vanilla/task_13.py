from ase.build import bulk
from ase import Atoms

# Create Si diamond structure
si = bulk('Si', 'diamond', a=5.43)

# Make 3x3x3 supercell
supercell = si * (3, 3, 3)

# Print results
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} Å³")
