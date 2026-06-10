from ase.collections import g2
atoms = g2['CH4']
print(atoms.get_chemical_formula())
print(atoms.get_positions())
print(atoms.get_all_distances())
