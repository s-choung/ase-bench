from ase.spacegroup import crystal

# Lattice constant (Å)
a = 5.64

# NaCl rock‑salt structure, space group 225 (Fm-3m)
atoms = crystal(
    symbols=['Na', 'Cl'],
    basis=[[0, 0, 0], [0.5, 0.5, 0.5]],
    spacegroup=225,
    cellpar=[a, a, a, 90, 90, 90],
)

print("Number of atoms :", len(atoms))
print("Symbols          :", atoms.get_chemical_symbols())
