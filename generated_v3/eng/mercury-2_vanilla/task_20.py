from ase.build import nanotube
from ase.calculators.emt import EMT

tube = nanotube(6, 6, length=4, vacuum=10.0)
tube.set_calculator(EMT())

print("Number of atoms:", len(tube))
print("Cell vectors (Å):")
print(tube.get_cell())
print("Cell lengths & angles (Å, deg):")
print(tube.get_cell_lengths_and_angles())
