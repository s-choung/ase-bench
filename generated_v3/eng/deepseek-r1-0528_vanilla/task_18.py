from ase.collections import g2
from ase import Atoms

atoms = g2['CH4']
print("Atomic coordinates:")
for atom in atoms:
    print(f"{atom.symbol} {atom.position[0]:.6f} {atom.position[1]:.6f} {atom.position[2]:.6f}")

c_index = [i for i, atom in enumerate(atoms) if atom.symbol == 'C'][0]
h_indices = [i for i, atom in enumerate(atoms) if atom.symbol == 'H']
bond_lengths = [atoms.get_distance(c_index, h, mic=False) for h in h_indices]

print("\nC-H bond lengths:")
for i, length in enumerate(bond_lengths):
    print(f"Bond {i+1}: {length:.6f} Å")

print(f"\nChemical formula: {atoms.get_chemical_formula()}")
