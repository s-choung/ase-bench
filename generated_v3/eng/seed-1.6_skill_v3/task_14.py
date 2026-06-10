from ase.spacegroup import crystal

# Create NaCl (Fm-3m, spacegroup 225)
nacl = crystal(
    symbols=['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    a=5.64
)

# Print required properties
print(f"Number of atoms: {nacl.get_number_of_atoms()}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
