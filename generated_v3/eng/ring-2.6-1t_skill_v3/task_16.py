from ase.lattice.surface import bcc110
from ase import Atoms

# Build Fe BCC(110) slab: 2×2 in‑plane, 4 layers, 10 Å vacuum
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print(f'Number of atoms: {len(slab)}')
print('Cell matrix (Å):')
print(slab.get_cell())

# (optional) also show lengths & angles
lengths, angles = slab.get_cell_lengths_and_angles()[:3], slab.get_cell_lengths_and_angles()[3:]
print(f'Cell lengths (a,b,c) = {lengths} Å')
print(f'Cell angles (α,β,γ)   = {angles} °')
