from ase import Atoms
from ase.build import (crystal, get_surface_area, get_cell_lengths_and_angles)

# HCP lattice parameters
a = 2.95  # unit cell length
c = a * 1.59  # c/a ratio

# Build HCP bulk for Ti (atomic number 22) on the a‑b plane
atoms = crystal('Ti',
                [(0, 0, 0), (2/3, 1/3, 1/2)],  # basis (two atoms per cell)
                spacegroup=194,
                cellpar=(a, a, c, 90, 90, 120))

# Print cell vectors
print("Cell vectors:")
for i, vec in enumerate(atoms.get_cell(), start=1):
    print(f"  vec{i}: {vec}")

# Print atomic positions (Å)
print("\nAtomic positions (Å):")
for i, atom in enumerate(atoms, start=1):
    print(f"  atom{i}: {atom.position}")

# Print cell geometry
lengths = get_cell_lengths_and_angles(atoms, 1e-6)
print("\nCell lengths and angles (Å, deg):")
print(f"a={lengths[0]:.6f}, b={lengths[1]:.6f}, c={lengths[2]:.6f}")
print(f"alpha={lengths[3]:.6f}, beta={lengths[4]:.6f}, gamma={lengths[5]:.6f}")
