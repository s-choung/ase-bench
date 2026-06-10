from ase.spacegroup import crystal

nacl = crystal(
    symbols=["Na", "Cl"],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90],
)

print("Number of atoms:", len(nacl))
print("Chemical symbols:", nacl.get_chemical_symbols())
