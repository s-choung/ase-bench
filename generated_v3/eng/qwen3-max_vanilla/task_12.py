from ase import Atoms

a = 2.95
c = 1.59 * a

# HCP lattice vectors
cell = [[a, 0, 0],
        [-a/2, a * 3**0.5 / 2, 0],
        [0, 0, c]]

# Atomic positions for HCP (2 atoms per unit cell)
positions = [[0, 0, 0],
             [a/2, a/(2*3**0.5), c/2]]

# Create Ti HCP structure
ti_hcp = Atoms('Ti2', cell=cell, positions=positions, pbc=True)

print("Cell vectors:")
print(ti_hcp.get_cell())
print("Atomic positions:")
print(ti_hcp.get_positions())
