from ase import Atoms
from ase.spacegroup import crystal

# Create HCP Ti structure with given a and c/a ratio
a = 2.95
c = a * 1.59
symbols = ['Ti'] * 2  # HCP has 2 atoms per conventional unit cell
basis = [(0, 0, 0), (2/3, 1/3, 1/2)]  # HCP atomic positions in fractional coordinates

# Alternatively using crystal() function (more general approach)
atoms = crystal('Ti', [(0, 0, 0), (2/3, 1/3, 1/2)], 
                spacegroup=194,  # P63/mmc space group for HCP
                cellparam=[a, a, c, 90, 90, 120])  # [a, b, c, alpha, beta, gamma]

# Print cell vectors (in Å)
print("Cell vectors (Å):")
for i, vec in enumerate(atoms.cell):
    print(f"a{i+1}: {vec[0]:.4f} {vec[1]:.4f} {vec[2]:.4f}")

# Print atomic positions (in Å)
print("\nAtomic positions (Å):")
for atom in atoms:
    pos = atom.position
    print(f"{atom.symbol} {pos[0]:.4f} {pos[1]:.4f} {pos[2]:.4f}")
