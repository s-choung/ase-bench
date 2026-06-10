from ase import Atoms
from a valence_electrons, EMT
from ase.build import fcc100
from ase.units import Bohr

# Create Cu(100) surface
surface = fcc100('Cu', a=3.61, size=(3, 3, 3), vacuum=12)

# Print number of atoms and cell
print("Number of atoms:", len(surface))
print("Cell:\n", surface.get_cell())
