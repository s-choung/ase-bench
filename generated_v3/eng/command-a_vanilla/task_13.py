from ase import Atoms
from ase.build import bulk

# Create Si bulk with diamond structure and lattice constant 5.43 Angstroms
si_bulk = bulk('Si', 'diamond', a=5.43)

# Make a 3x3x3 supercell
supercell = si_bulk.repeat((3, 3, 3))

# Print number of atoms and cell volume
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume()} Angstrom^3")
