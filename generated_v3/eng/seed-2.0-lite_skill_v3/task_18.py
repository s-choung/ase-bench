from ase.build import molecule

# Retrieve CH4 molecule from ASE's G2 database
ch4 = molecule('CH4')

# Print chemical formula
print(f"Chemical Formula: {ch4.get_chemical_formula()}\n")

# Print atomic coordinates
print("Atomic Coordinates (Å):")
for symbol, pos in zip(ch4.get_chemical_symbols(), ch4.get_positions()):
    print(f"{symbol}: {pos.round(4)}")
print("\n")

# Calculate and print C-H bond lengths
c_index = ch4.get_chemical_symbols().index('C')
print("C-H Bond Lengths (Å):")
for atom_idx, symbol in enumerate(ch4.get_chemical_symbols()):
    if symbol == 'H':
        bond_length = ch4.get_distance(c_index, atom_idx)
        print(f"C-H{atom_idx}: {bond_length.round(4)}")
