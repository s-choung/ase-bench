from ase.spacegroup import crystal

# Define lattice constant and spacegroup
a = 5.64  # Angstrom
spacegroup = 225  # Fm-3m

# Define atomic positions and symbols
symbols = ['Na', 'Cl']
positions = [(0, 0, 0), (0.5, 0.5, 0.5)]

# Create the crystal structure
atoms = crystal(symbols=symbols, positions=positions, spacegroup=spacegroup,
              cell=[a, a, a], scale_atoms=True)

# Print the number of atoms and chemical symbols
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
