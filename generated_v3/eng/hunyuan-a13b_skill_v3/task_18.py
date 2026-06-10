from ase.build import molecule

CH4 = molecule('CH4')
print("Atomic coordinates:")
print(CH4.get_positions())
print("
Bond lengths (Å):")
print(CH4.get_distances(unit=ase.units.Å))
print("
Chemical formula:", CH4.get_chemical_formula())
