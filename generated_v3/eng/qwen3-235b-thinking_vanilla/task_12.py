from ase.build import bulk

ti = bulk('Ti', 'hcp', a=2.95, covera=1.59)
print(ti.get_cell())
print(ti.get_positions())
