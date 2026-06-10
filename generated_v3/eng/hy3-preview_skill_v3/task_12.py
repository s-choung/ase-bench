from ase import Atoms
from ase.io import write

# Create Ti HCP bulk structure
a = 2.95
c = a * 1.59

# HCP unit cell vectors
cell = [[a, 0, 0],
        [-a/2, a*3**0.5/2, 0],
        [0, 0, c]]

# HCP atomic positions (basis atoms)
positions = [[0, 0, 0],
             [a/2, a*3**0.5/6, c/2]]

# Create atoms object
atoms = Atoms('Ti2', positions=positions, cell=cell, pbc=True)

# Print cell vectors
print("Cell vectors (Å):")
for i, vec in enumerate(atoms.cell):
    print(f"  a{i+1}: {vec}")

# Print atomic positions
print("\nAtomic positions (Å):")
for i, pos in enumerate(atoms.positions):
    print(f"  Ti{i+1}: {pos}")

# Optional: write to file for verification
write('ti_hcp.xyz', atoms)
