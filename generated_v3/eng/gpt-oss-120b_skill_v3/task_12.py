from ase.build import bulk

# Ti HCP bulk, a = 2.95 Å, c/a = 1.59
ti = bulk('Ti', 'hcp', a=2.95, c_over_a=1.59)

# Cell vectors (Å)
print('Cell vectors (Å):')
print(ti.get_cell())          # 3×3 array

# Atomic positions (fractional then Cartesian)
print('\nAtomic positions (fractional):')
print(ti.get_scaled_positions())

print('\nAtomic positions (Cartesian, Å):')
print(ti.get_positions())
