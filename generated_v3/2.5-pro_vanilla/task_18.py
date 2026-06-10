from ase.db import connect

db = connect('g2.db')
row = next(db.select(formula='CH4'))
ch4 = row.toatoms()

print("Atomic Coordinates (Å):")
print(ch4.positions)
print("-" * 25)

print("Bond Lengths (Å):")
c_index = [atom.index for atom in ch4 if atom.symbol == 'C'][0]
for atom in ch4:
    if atom.symbol == 'H':
        dist = ch4.get_distance(c_index, atom.index)
        print(f"C-H: {dist:.4f}")
print("-" * 25)

print("Chemical Formula:")
print(ch4.get_chemical_formula())
