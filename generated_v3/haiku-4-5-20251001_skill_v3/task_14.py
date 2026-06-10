from ase.spacegroup import crystal

atoms = crystal(['Na', 'Cl'], 
                [(0, 0, 0), (0.5, 0.5, 0.5)], 
                spacegroup=225, 
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

print(f"Total atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
print(f"Atomic numbers: {atoms.get_atomic_numbers()}")
