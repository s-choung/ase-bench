from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT

atoms = FaceCenteredCubic('Cu', size=(1, 1, 1), pbc=True)
atoms *= (2, 2, 2)
atoms.set_calculator(EMT())

print("Cell info:", atoms.cell)
print("Number of atoms:", len(atoms))
