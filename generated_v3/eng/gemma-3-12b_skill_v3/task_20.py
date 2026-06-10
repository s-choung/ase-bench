from ase.build import nanotube
from ase.calculators.emt import EMT
import ase

tube = nanotube(n=6, m=6, length=4)
tube.calc = EMT()

print(f"Number of atoms: {len(tube)}")
print(f"Cell lengths: {tube.get_cell_lengths()}")
print(f"Cell angles: {tube.get_cell_angles()}")
