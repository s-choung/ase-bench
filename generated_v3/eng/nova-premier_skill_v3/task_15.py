from ase.build import fcc100
from ase.calculators.emt import EMT
cu = fcc100('Cu', size=(3,3,3), vacuum=12)
cu.calc = EMT()
print("Atoms:", len(cu))
print("Cell:", cu.cell)
print("Lengths+angles:", cu.get_cell_lengths_and_angles())
