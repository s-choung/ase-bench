from ase.build import bulk

ti_hcp = bulk('Ti', 'hcp', a=2.95, c=2.95 * 1.59)
print('Cell vectors:\n', ti_hcp.get_cell())
print('Atomic positions:\n', ti_hcp.get_positions())
