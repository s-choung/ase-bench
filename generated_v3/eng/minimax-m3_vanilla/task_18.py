from ase.db import connect

# Connect to ASE G2 database
db = connect('g2.db')

# Retrieve CH4 molecule
atoms = db.get(name='CH4').toatoms()

# Chemical formula
print(f"Chemical formula: {atoms.get_chemical_formula()}")

# Atomic coordinates
print("Atomic coordinates (Å):")
for i, (sym, pos) in enumerate(zip(atoms.symbols, atoms.positions)):
    print(f"  {i}: {sym}  {pos[0]:10.5f} {pos[1]:10.5f} {pos[2]:10.5f}")

# Bond lengths
print("Bond lengths (Å):")
c_idx = [i for i, s in enumerate(atoms.symbols) if s == 'C']
h_idx = [i for i, s in enumerate(atoms.symbols) if s == 'H']
for c in c_idx:
    for h in h_idx:
        d = atoms.get_distance(c, h)
        print(f"  C{c}-H{h}: {d:.5f}")
