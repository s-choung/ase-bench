from ase.db import connect
from ase.geometry import get_distances
from ase.build import molecule

# Connect to the G2 database
db = connect('g2.db')

# Retrieve the methane molecule
mol = db.get_atoms('fchem molecule CH4')

# Print the atomic coordinates
for atom in mol:
    print(f'{atom.symbol} at {atom.position}')

# Calculate and print bond lengths
positions = mol.get_positions()
distances = get_distances(mol.cell, mol.positions, mol.get_scaled_positions())
print('Bond lengths (in Angstroms):')
for i, (dist, idx) in enumerate(distances):
    for d, j in zip(dist, idx):
        if j < i and d < 1.5:  # Assuming a bond length threshold
            print(f'Bond length between atom {mol.get_atomic_numbers()[i]} and {mol.get_atomic_numbers()[j]}: {d:.2f}')

# Print chemical formula
print(f'Chemical formula: {mol.formula}')
