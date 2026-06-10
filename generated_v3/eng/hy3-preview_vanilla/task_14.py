from ase.spacegroup import crystal

# Create NaCl crystal (spacegroup 225 - Fm-3m)
a = 5.64  # lattice constant in angstroms
atoms = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cell=(a, a, a))

# Print results
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
