from ase.build import bulk

a = 2.95
c = 1.59 * a

ti = bulk('Ti', 'hcp', a=a, c=c)
print('Cell vectors:\n', ti.cell.array)
print('Atomic positions (fractional):\n', ti.get_scaled_positions())
