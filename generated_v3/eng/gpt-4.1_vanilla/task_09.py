from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import write, read

# Create FCC Cu bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Set EMT calculator
atoms.calc = EMT()

# Save to POSCAR
write('POSCAR', atoms, format='vasp')

# Read back the POSCAR
atoms2 = read('POSCAR')

# Print number of atoms and cell parameters
print('Number of atoms:', len(atoms2))
print('Cell parameters (rows):')
for vec in atoms2.cell:
    print(vec)
