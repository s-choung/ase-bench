from ase.db import connect
from ase.calculators.emt import EMT

# Connect to the G2 database
db = connect('g2.db')

# Get the CH4 molecule
ch4 = db.get_atoms(molecule='CH4')

# Print atomic positions
print("Atomic positions:\n", ch4.get_positions())

# Print bond lengths
# For CH4, we expect C-H bonds. We can iterate through pairs of atoms.
# A more robust way would be to use neighbor lists, but for simplicity:
print("\nBond lengths:")
for i in range(len(ch4)):
    for j in range(i + 1, len(ch4)):
        # Assuming C is atom 0 and H are atoms 1, 2, 3, 4
        # This is a simplification and might not work for all molecules
        if ch4.symbols[i] == 'C' and ch4.symbols[j] == 'H':
            print(f"C-H bond length: {ch4.get_distance(i, j):.3f} Å")
        elif ch4.symbols[i] == 'H' and ch4.symbols[j] == 'C':
            print(f"H-C bond length: {ch4.get_distance(i, j):.3f} Å")

# Print chemical formula
print("\nChemical formula:", ch4.get_chemical_formula())
