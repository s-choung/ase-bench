from ase.spacegroup import crystal
atoms = crystal(['Na', 'Cl'], 
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)], 
                spacegroup=225, 
                cellpar=5.64)
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
