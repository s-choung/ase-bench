from ase.db import connect

# Connect to the G2 database
db = connect('g2.db')

# Retrieve CH4 molecule from the database
ch4 = db.get(molecule='CH4')

# Print the atomic coordinates
print('Atomic coordinates:')
for i, atom in enumerate(ch4.positions):
    print(f'Atom {i+1}: {atom}')

# Print the bond lengths
bond_lengths = ch4.get_all_distances()
print('Bond lengths:')
for i in range(1, len(ch4)):
    for j in range(i):
        print(f'{ch4.get_chemical_symbols()[i]}-{ch4.get_chemical_symbols()[j]} bond length: {bond_lengths[i][j]} Å')

# Print the chemical formula
print('Chemical formula:', ch4.get_chemical_formula())
