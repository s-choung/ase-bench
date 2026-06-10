from ase.build import bulk

a = 2.95
c = 1.59 * a
ti = bulk('Ti', 'hcp', a=a, c=c)

print('Cell vectors:')
print(ti.get_cell())
print('Atomic positions (Cartesian):')
print(ti.get_positions())
