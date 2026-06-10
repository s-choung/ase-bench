from ase.spacegroup import crystal

# NaCl in spacegroup Fm-3m (225)
atoms = crystal(
    symbols=['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90]  # a, b, c, alpha, beta, gamma
)

print(len(atoms))
print(atoms.get_chemical_symbols())
