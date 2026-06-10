from ase import Atoms
from ase.build import diamond
from ase.build import make_supercell

# Create Si bulk with diamond structure
si_bulk = diamond('Si', cubic=True, a=5.43)

# Create 3x3x3 supercell
supercell = make_supercell(si_bulk, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])

# Print number of atoms and cell volume
print("Number of atoms:", len(supercell))
print("Cell volume (A^3):", supercell.get_volume())
