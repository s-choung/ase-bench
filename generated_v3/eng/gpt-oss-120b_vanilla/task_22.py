from ase.build import fcc111, molecule
import numpy as np

# Al(111) slab: 2x2 surface cell, 3 layers, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Identify top‑layer atoms
zmax = slab.positions[:, 2].max()
top_idx = np.where(np.isclose(slab.positions[:, 2], zmax, atol=1e-3))[0]

# Bridge site = midpoint of first two top atoms, raised 2.0 Å above surface
bridge = (slab.positions[top_idx[0]] + slab.positions[top_idx[1]]) / 2
bridge[2] = zmax + 2.0

# N2 molecule, bond aligned along surface normal (z)
n2 = molecule('N2')
n2.rotate('y', 90, center=(0, 0, 0))   # x → z
n2.translate(bridge)                  # place at bridge site

# Combine slab and molecule
system = slab + n2

print("Number of atoms:", len(system))
print("Atom types:", set(system.get_chemical_symbols()))
