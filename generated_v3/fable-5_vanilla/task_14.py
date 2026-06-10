from ase.spacegroup import crystal

a = 5.64
nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=[a, a, a, 90, 90, 90])

print("Number of atoms:", len(nacl))
print("Chemical symbols:", nacl.get_chemical_symbols())
