from ase import Atoms, Surface
from ase.calculators import EMT

# Define Cu bulk structure
Cu = Atoms('Cu', pos=[(0,0,0)], cell=[[3.61,0,0],[0,3.61,0],[0,0,3.61]], pbc=True)

# Cut (2,1,1) surface with 3 layers
surface = Surface(Cu, (2, 1, 1), 3, vacuum=10.0)

# Calculate using EMT
calc = EMT()
surface.set_calculator(calc)

# Print number of atoms and cell
print("Number of atoms:", surface.natoms)
print("Unit cell:", surface.cell)
