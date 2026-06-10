from ase.db import g2

ch4 = g2.get_atoms('CH4')

# Atomic coordinates
print("Atomic coordinates (Å):")
print(ch4.get_positions())

# C-H bond lengths (C:0, H:1-4)
print("\nC-H bond lengths (Å):")
for i in range(1, 5):
    print(ch4.get_distance(0, i))

# Chemical formula (Hill system)
print("\nChemical formula:", ch4.get_chemical_formula(mode='hill'))
