from ase.build import bulk

a = 2.95
c = a * 1.59  # c/a = 1.59
ti = bulk('Ti', 'hcp', a=a, c=c)

print('Cell vectors (Å):')
print(ti.get_cell())
print('\nAtomic positions (Å):')
print(ti.get_positions())
