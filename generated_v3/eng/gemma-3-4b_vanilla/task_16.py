from ase import Atoms
from ase.build import fcc110_surface
from ase.calculators import EMT
from ase.io import write

calc = EMT()
atoms = fcc110_surface(size=(2, 2, 4), vacuum=10.0, a=3.615)
atoms.set_calculator(calc)

print("Number of atoms:", len(atoms))
print("Cell size:", atoms.cell)
write("fe_bcc110_surface.xyz", atoms)
