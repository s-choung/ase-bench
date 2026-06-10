from ase.build import bulk
ti = bulk('Ti', 'HCP', a=2.95, kind='tiHCP', cubic=False)
print(ti.cell)
print(ti.get_positions())
