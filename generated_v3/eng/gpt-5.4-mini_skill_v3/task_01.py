from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms.repeat((2, 2, 2))
supercell.calc = EMT()

print("Cell:")
print(supercell.cell)
print("Cell lengths and angles [a, b, c, alpha, beta, gamma]:")
print(supercell.get_cell_lengths_and_angles())
print("Number of atoms:", len(supercell))
