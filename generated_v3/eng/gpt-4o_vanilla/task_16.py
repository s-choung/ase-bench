from ase.build import fcc111
from ase.build import bcc110
from ase.constraints import FixAtoms
from ase import Atoms
cell = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print("Number of atoms:", len(cell))
print("Cell size:", cell.get_cell().lengths())
