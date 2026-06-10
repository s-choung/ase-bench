from ase.build import molecule

# Retrieve CH4 molecule
ch4 = molecule('CH4')

# Print atomic coordinates
positions = ch4.get_positions()
print("Atomic coordinates:")
for i, position in enumerate(positions):
    print(f"Atom {ch4[i].symbol}: {position}")

# Print bond lengths
print("\nBond lengths:")
for bond in ch4.get_bonds():
    bonded_atoms = bond.connected_atoms
    distance = bond.distance
    print(f"Between {bonded_atoms[0].symbol} and {bonded_atoms[1].symbol}: {distance} Å")

# Print chemical formula
print("\nChemical formula: CH4")
