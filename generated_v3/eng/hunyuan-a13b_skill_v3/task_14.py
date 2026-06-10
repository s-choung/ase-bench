from ase.spacegroup import crystal

# Define NaCl structure with lattice constant 5.64 Å and spacegroup 225
atoms = crystal(
    ['Na', 'Cl'],
    [(0, 0, 0), (0.5, 0.5, 0.5)],
    a=5.64,
    spacegroup=225,
    primitive_cell=False
)

# Count atoms and print chemical symbols
num_atoms = len(atoms)
elements = [atom.symbol for atom in atoms]

print(f"Number of atoms: {num_atoms}")
print(f"Chemical symbols: {' '.join(elements)}")
