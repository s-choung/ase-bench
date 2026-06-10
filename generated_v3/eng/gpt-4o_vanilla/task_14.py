from ase.spacegroup import crystal

# Define the lattice parameters
a = 5.64

# Create NaCl crystal structure
nacl = crystal(['Na', 'Cl'], 
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)], 
               spacegroup=225, 
               cellpar=[a, a, a, 90, 90, 90])

# Output the number of atoms and chemical symbols
print(f'Number of atoms: {len(nacl)}')
print(f'Chemical symbols: {nacl.get_chemical_symbols()}')
