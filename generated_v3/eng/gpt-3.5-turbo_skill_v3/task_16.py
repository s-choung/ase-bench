from ase.build import bcc110
from ase.calculators.emt import EMT

surface = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
surface.calc = EMT()

num_atoms = len(surface)
cell_size = surface.get_cell_lengths_and_angles()

print("Number of atoms:", num_atoms)
print("Cell size:", cell_size)
