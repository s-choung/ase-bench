from ase.build import bulk
from ase.build import make_supercell  # Alternatively, you can use multiplication as shown below

# Create Si diamond bulk with lattice constant 5.43 Å
si_bulk = bulk('Si', 'diamond', a=5.43)

# Create 3x3x3 supercell (two equivalent ways shown - choose one)
si_supercell = si_bulk * (3, 3, 3)  # Method 1: Using multiplication
# Or equivalently: si_supercell = make_supercell(si_bulk, [[3,0,0], [0,3,0], [0,0,3]])  # Method 2

# Print number of atoms and cell volume
print(f"Number of atoms: {len(si_supercell)}")
print(f"Cell volume (Å³): {si_supercell.get_volume():.2f}")
