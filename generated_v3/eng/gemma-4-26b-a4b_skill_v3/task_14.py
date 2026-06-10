from ase.spacegroup import crystal

# Create NaCl structure using spacegroup 225 (Fm-3m)
# Na at (0,0,0), Cl at (0.5, 0.5, 0.5), lattice constant 5.64 A
atoms = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)], 
                spacegroup=225, a=5.64)

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
