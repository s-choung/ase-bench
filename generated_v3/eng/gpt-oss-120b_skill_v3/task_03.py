from ase.build import mx2, add_vacuum
from ase import units

# Build a 2H MoS2 monolayer (default a≈3.18 Å, one layer)
atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=0.0)

# Add 10 Å of vacuum in the z‑direction
add_vacuum(atoms, 10.0)

# Show cell vectors and lengths/angles
cell = atoms.get_cell()
lengths_angles = atoms.get_cell_lengths_and_angles()
print("Cell vectors (Å):")
print(cell)
print("\nLengths (a,b,c) and angles (α,β,γ) in Å/deg:")
print(lengths_angles)
