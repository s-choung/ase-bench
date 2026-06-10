from ase.spacegroup import crystal

atoms = crystal('NaCl', spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
