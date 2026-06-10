from ase.build import molecule

# Retrieve CH4 molecule from ASE G2 database
ch4 = molecule('CH4')

# Print atomic coordinates
print('Atomic Coordinates:')
for i, atom in enumerate(ch4):
    print(f'{atom.symbol}: {ch4.positions[i]}')

# Calculate bond lengths
C_H_bond_length = ch4.get_distance(0, 1)
print(f'C-H bond length: {C_H_bond_length:.2f} Å')

# Print chemical formula
chemical_formula = ch4.get_chemical_formula()
print('Chemical Formula:', chemical_formula)
