from ase.spacegroup import crystal

nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

print("원자 수:", len(nacl))
print("Chemical symbols:", nacl.get_chemical_symbols())
print("Chemical formula:", nacl.get_chemical_formula())
