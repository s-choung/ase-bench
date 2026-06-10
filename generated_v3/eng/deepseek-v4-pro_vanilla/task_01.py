from ase.build import bulk

# Create Cu FCC bulk with lattice constant 3.6 Å
atoms = bulk('Cu', 'fcc', a=3.6)

# Generate a 2x2x2 supercell
supercell = atoms * (2, 2, 2)

# Print original cell, number of atoms, then supercell info
print("Original cell:")
print(atoms.cell)
print(f"Number of original atoms: {len(atoms)}")
print("\nSupercell (2x2x2):")
print(supercell.cell)
print(f"Number of supercell atoms: {len(supercell)}")
