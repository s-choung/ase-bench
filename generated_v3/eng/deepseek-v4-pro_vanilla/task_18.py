from ase.build import molecule

# Retrieve CH4 from the ASE G2 database
atoms = molecule('CH4')

# Chemical formula
print("Chemical formula:", atoms.get_chemical_formula())

# Atomic coordinates (symbol and position)
print("\nAtomic coordinates:")
for atom in atoms:
    print(f"  {atom.symbol}   {atom.position[0]:.6f}  {atom.position[1]:.6f}  {atom.position[2]:.6f} Å")

# Bond lengths (C-H bonds; C is the first atom)
print("\nBond lengths (C-H):")
c_index = 0
for i in range(1, len(atoms)):
    d = atoms.get_distance(c_index, i)
    print(f"  C–H{i}: {d:.4f} Å")
