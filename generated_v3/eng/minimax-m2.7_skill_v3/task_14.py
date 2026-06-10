from ase.spacegroup import crystal

atoms = crystal(
    ['Na', 'Cl'],
    [[0, 0, 0], [0.5, 0.5, 0.5]],
    spacegroup=225,
    cell=[5.64, 5.64, 5.64]
)

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {''.join(atoms.get_chemical_symbols())}")
