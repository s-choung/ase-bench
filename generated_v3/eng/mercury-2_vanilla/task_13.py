from ase.build import bulk

# Create Si diamond bulk with lattice constant 5.43 Å
si = bulk('Si', 'diamond', a=5.43)

# Expand to 3×3×3 supercell
si_super = si * (3, 3, 3)

# Output
print(len(si_super))          # number of atoms
print(si_super.get_volume())  # cell volume in Å³
