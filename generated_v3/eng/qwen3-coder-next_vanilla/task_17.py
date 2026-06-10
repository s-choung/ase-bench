from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.build import surface

# Create bulk Cu (FCC)
bulk = FaceCenteredCubic('Cu', latticeconstant=3.61)

# Cut (2,1,1) surface with 3 layers and 10 Å vacuum
slab = surface(bulk, (2,1,1), layers=3, vacuum=10.0)

# Set calculator (not used for anything here, but required per instructions)
slab.calc = EMT()

# Print number of atoms and cell
print(f"Number of atoms: {len(slab)}")
print(f"Cell: {slab.cell}")
