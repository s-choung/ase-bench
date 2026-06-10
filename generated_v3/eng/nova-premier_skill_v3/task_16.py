from ase.build import bcc110
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Create Fe BCC(110) surface
surf = bcc110('Fe', size=(2,2,4), vacuum=10.0, a=2.86)

# Fix bottom layers
mask = [atom.tag > 2 for atom in surf]
surf.set_constraint(FixAtoms(mask=mask))

# Assign calculator
surf.calc = EMT()

# Output results
print(f"Atoms: {len(surf)}")
print("Cell:", surf.cell.lengths())
