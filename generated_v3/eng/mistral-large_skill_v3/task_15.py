from ase.build import fcc100
from ase.calculators.emt import EMT

atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
print(f"Number of atoms: {len(atoms)}")
print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
print("Cell vectors:\n", atoms.cell)
