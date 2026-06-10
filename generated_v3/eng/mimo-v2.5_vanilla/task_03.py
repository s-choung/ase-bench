from ase import Atoms
import numpy as np

# MoS2 monolayer parameters
a = 3.16  # lattice constant (Å)
c = 10.0  # vacuum thickness (Å)
theta = np.radians(60)  # 60° angle for hexagonal cell

# Create unit cell vectors for hexagonal lattice
cell = [
    [a, 0, 0],
    [a * np.cos(theta), a * np.sin(theta), 0],
    [0, 0, c]
]

# Atomic positions (Mo at center, S at top/bottom)
positions = [
    [0, 0, 0],  # Mo
    [0, 0, 0.2],  # S (top)
    [0, 0, -0.2]  # S (bottom)
]

# Create atoms
atoms = Atoms(
    symbols=['Mo', 'S', 'S'],
    positions=positions,
    cell=cell,
    pbc=[1, 1, 1]  # periodic in x,y but not z
)

# Print cell dimensions
print("Cell size (Å):")
print(f"x: {atoms.cell[0][0]:.2f}")
print(f"y: {atoms.cell[1][1]:.2f}")
print(f"z: {atoms.cell[2][2]:.2f}")
