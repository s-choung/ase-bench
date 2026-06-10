from ase.build import bulk
from ase.calculators.emt import EMT

# Cu FCC bulk with lattice constant a = 3.6 Å
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()                     # attach calculator

# 2×2×2 supercell
sc = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)

# Print requested information
print('Supercell cell (Å):', sc.get_cell().T)
print('Cell lengths:', sc.get_cell_lengths_and_angles()[0:3])
print('Cell angles (degree):', sc.get_cell_lengths_and_angles()[3:])
print('Number of atoms:', len(sc))
