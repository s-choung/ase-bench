from ase.spacegroup import crystal

a = 5.64  # lattice constant in Å

# NaCl in space group 225 (Fm-3m) with Na at (0,0,0) and Cl at (0.5,0.5,0.5)
structure = crystal(
    [('Na', [(0, 0, 0)]), ('Cl', [(0.5, 0.5, 0.5)])],
    spacegroup=225,
    cellpar=[a, a, a, 90, 90, 90]
)

print('Number of atoms:', len(structure))
print('Chemical symbols:', structure.get_chemical_symbols())
