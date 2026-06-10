from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
print("Number of atoms:", len(atoms))
